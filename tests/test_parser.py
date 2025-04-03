import os
import tempfile
from pathlib import Path
import yaml

from dircraft.parser import (
    normalize_text,
    load_structure_from_yaml,
    load_structure_from_tree,
    load_structure_from_direct_string,
    load_structure,
)

def test_normalize_text():
    # Test that normalization converts weird characters properly.
    text = "â”œâ”€â”€"
    normalized = normalize_text(text)
    # We expect the normalized version to be different (or at least valid UTF-8)
    assert isinstance(normalized, str)
    assert normalized != text

def test_load_structure_from_yaml(tmp_path):
    # Create a temporary YAML file
    data = {
        "folder": {
            "file.txt": "Hello World"
        }
    }
    yaml_file = tmp_path / "structure.yaml"
    with open(yaml_file, "w", encoding="utf-8") as f:
        yaml.dump(data, f)
    
    structure = load_structure_from_yaml(yaml_file)
    assert structure == data

def test_load_structure_from_direct_string():
    input_string = "folder/file.txt:Hello World; folder/subfolder/:"
    structure = load_structure_from_direct_string(input_string)
    # Check that the structure has a folder, a file, and a subfolder.
    assert "folder" in structure
    assert structure["folder"].get("file.txt") == "Hello World"
    assert isinstance(structure["folder"].get("subfolder"), dict)

def test_load_structure_from_tree(tmp_path):
    # Create a temporary tree file that simulates a simple tree.
    tree_content = """
folder/
    file.txt # Hello World
    subfolder/
    """
    tree_file = tmp_path / "structure.txt"
    with open(tree_file, "w", encoding="utf-8") as f:
        f.write(tree_content)
    
    structure = load_structure_from_tree(tree_file)
    # We expect 'folder' to be a key in the structure.
    assert "folder" in structure
    # And inside folder, 'file.txt' should have content "Hello World"
    # 'subfolder' should be an empty dict.
    folder = structure["folder"]
    assert folder.get("file.txt") == "Hello World"
    assert isinstance(folder.get("subfolder"), dict)

def test_load_structure_auto(tmp_path):
    # Test auto detection for YAML
    data = {"a": {"b.txt": "Test"}}
    yaml_file = tmp_path / "structure.yaml"
    with open(yaml_file, "w", encoding="utf-8") as f:
        yaml.dump(data, f)
    structure = load_structure(str(yaml_file))
    assert structure == data

    # Test auto detection for direct string
    input_string = "a/b.txt:Test"
    structure = load_structure(input_string)
    assert "a" in structure
    assert structure["a"].get("b.txt") == "Test"
