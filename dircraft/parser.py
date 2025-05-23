import yaml
import re
import unicodedata
from pathlib import Path

def normalize_text(text):
    """Normalize Unicode text to prevent encoding issues."""
    return unicodedata.normalize("NFKD", text)

def load_structure_from_yaml(yaml_file: Path) -> dict:
    """
    Load the YAML file containing the file structure.
    """
    with open(yaml_file, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def parse_tree_line(line: str) -> (str, str):
    """
    Parse a single line from a tree structure.
    Expected format: "name [# optional content]"
    """
    if "#" in line:
        name, comment = line.split("#", 1)
        return name.strip(), normalize_text(comment.strip())
    return line.strip(), ""

def load_structure_from_tree(tree_file: Path) -> dict:
    """
    Parse a plain text file representing a tree structure (e.g., generated by the 'tree' command)
    and convert it into a nested dictionary.
    
    This version removes box-drawing characters and ignores header/footer lines.
    """
    structure = {}
    with open(tree_file, "r", encoding="utf-8") as f:
        lines = [normalize_text(line.rstrip()) for line in f if line.strip()]
    
    # Filter out common header/footer lines from 'tree' command output
    filtered_lines = []
    for line in lines:
        if line.startswith("Folder") or line.startswith("File(s)") or line.startswith("----"):
            continue
        filtered_lines.append(line)
    
    # Remove common box-drawing characters from each line
    cleaned_lines = []
    for line in filtered_lines:
        # Remove characters like '├', '└', '│', and '─'
        cleaned = re.sub(r"[├└│─]", "", line)
        cleaned_lines.append(cleaned)

    # Use a stack to build the hierarchy: each entry is (indent_level, current_dict)
    stack = [(-1, structure)]
    for line in cleaned_lines:
        # Determine the indent level (number of leading spaces)
        indent_level = len(line) - len(line.lstrip(" "))
        # Get the actual text (strip leading/trailing spaces)
        text = line.strip()
        if not text:
            continue
        name, comment = parse_tree_line(text)
        # Pop from the stack until we find a parent with a lower indent
        while stack and indent_level <= stack[-1][0]:
            stack.pop()
        parent_dict = stack[-1][1]
        # Check if this line represents a directory.
        # For our purposes, we assume that if the name does not contain a dot ('.'),
        # or if it explicitly ends with '/', it is a directory.
        if ("." not in name) or name.endswith("/"):
            # Use name without trailing slash if present.
            dir_name = name.rstrip("/")
            parent_dict[dir_name] = {}
            stack.append((indent_level, parent_dict[dir_name]))
        else:
            # It is a file; store the comment (or empty string) as file content.
            parent_dict[name] = comment
    return structure

def load_structure_from_direct_string(input_string: str) -> dict:
    """
    Parse a direct terminal input string.
    Expected format: 
      "path/to/file1:content1; path/to/file2:content2; dir/subdir/:"
    Multiple definitions are separated by semicolons.
    Directories are indicated by a trailing '/'.
    """
    structure = {}
    entries = input_string.split(";")
    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue
        if ":" in entry:
            path, content = entry.split(":", 1)
        else:
            path, content = entry, ""
        parts = [p.strip() for p in path.split("/") if p.strip()]
        current_dict = structure
        for i, part in enumerate(parts):
            if i == len(parts) - 1:
                # If the original path ends with a '/', then it is a directory.
                if path.endswith("/"):
                    current_dict.setdefault(part, {})
                else:
                    current_dict[part] = content.strip()
            else:
                current_dict = current_dict.setdefault(part, {})
    return structure

def load_structure(input_source: str) -> dict:
    """
    Automatically detect the input type based on input_source.
    - If input_source is an existing file path with extension .yaml or .yml, use YAML.
    - If it has extension .txt, use the tree parser.
    - Otherwise, assume it is a direct structure string.
    """
    path = Path(input_source)
    if path.exists():
        if path.suffix in [".yaml", ".yml"]:
            return load_structure_from_yaml(path)
        elif path.suffix == ".txt":
            return load_structure_from_tree(path)
        else:
            # Fallback: treat as a text file with a tree structure.
            return load_structure_from_tree(path)
    else:
        return load_structure_from_direct_string(input_source)
