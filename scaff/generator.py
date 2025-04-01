import os
from pathlib import Path
import yaml

def create_structure(base_dir: Path, structure: dict):
    """
    Recursively create directories and files from the provided structure.
    """
    for name, content in structure.items():
        current_path = base_dir / name
        if isinstance(content, dict):
            # Create a directory
            current_path.mkdir(parents=True, exist_ok=True)
            # Recursively create structure in sub-directory
            create_structure(current_path, content)
        else:
            # Content is assumed to be a string (file content)
            # Create parent directories if they don't exist
            current_path.parent.mkdir(parents=True, exist_ok=True)
            with open(current_path, "w") as f:
                f.write(content)

def load_structure(yaml_file: Path) -> dict:
    """
    Load the YAML file containing the file structure.
    """
    with open(yaml_file, "r") as f:
        structure = yaml.safe_load(f)
    return structure

def generate_from_yaml(yaml_file: Path, target_dir: Path):
    """
    Generate file structure based on the YAML file into the target directory.
    """
    structure = load_structure(yaml_file)
    create_structure(target_dir, structure)
