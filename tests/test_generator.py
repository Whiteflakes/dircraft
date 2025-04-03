import os
import tempfile
from pathlib import Path
import shutil

from dircraft.generator import create_structure

def test_create_structure(tmp_path):
    # Create a sample structure as a dict.
    sample_structure = {
        "folder": {
            "file.txt": "Hello World",
            "subfolder": {
                "inner.txt": "Inner Content"
            }
        },
        "readme.md": "This is a readme."
    }
    # Create the structure in a temporary directory
    target_dir = tmp_path / "output"
    target_dir.mkdir()
    create_structure(target_dir, sample_structure)

    # Check that folder exists
    folder_path = target_dir / "folder"
    assert folder_path.is_dir()

    # Check that file.txt exists and has correct content
    file_path = folder_path / "file.txt"
    assert file_path.is_file()
    with open(file_path, "r") as f:
        content = f.read()
    assert content == "Hello World"

    # Check inner subfolder and file
    inner_file = folder_path / "subfolder" / "inner.txt"
    assert inner_file.is_file()
    with open(inner_file, "r") as f:
        inner_content = f.read()
    assert inner_content == "Inner Content"

    # Check readme.md
    readme = target_dir / "readme.md"
    assert readme.is_file()
    with open(readme, "r") as f:
        readme_content = f.read()
    assert readme_content == "This is a readme."
