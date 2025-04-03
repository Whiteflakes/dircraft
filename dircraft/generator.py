import os
from pathlib import Path
from dircraft.parser import load_structure 

def create_structure(base_dir: Path, structure: dict):
    """
    Recursively create directories and files from the provided structure.
    """
    for name, content in structure.items():
        current_path = base_dir / name
        if isinstance(content, dict):
            current_path.mkdir(parents=True, exist_ok=True)
            create_structure(current_path, content)
        else:
            current_path.parent.mkdir(parents=True, exist_ok=True)
            with open(current_path, "w") as f:
                f.write(content)

def generate_structure(input_source: str, target_dir: Path):
    """
    Generate file structure based on the input_source into the target directory.
    The input_source can be a file path or a direct structure string.
    """
    structure = load_structure(input_source)
    create_structure(target_dir, structure)

    print("\nGenerated File Structure:")
    for root, dirs, files in os.walk(target_dir):
        level = root.replace(str(target_dir), "").count(os.sep)
        indent = " " * (level * 4)
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = " " * ((level + 1) * 4)
        for f in files:
            print(f"{sub_indent}{f}")
