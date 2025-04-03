# dircraft

`dircraft` is a powerful Python package that automatically generates a project folder structure based on an input specification. It supports multiple formats – YAML, plain text, JSON (if added), or direct terminal input – to create the corresponding directories and files.

## Features

- **Multi-format Input:**
  - **YAML Files:** Define your folder structure with nested dictionaries.
  - **Tree/Text Files:** Provide a tree-like text representation.
  - **Direct Terminal Input:** Paste a file structure via CLI arguments.
- **Customizable File Contents:**  
  If no content is provided, empty files are created.
- **Recursive Directory Creation:**  
  Automatically creates nested directories and files.
- **Command Line Interface (CLI):**  
  Easily generate projects from the command line.
- **Extendable and Modular:**  
  Future support for GUI-based customization.

## Installation

Install `dircraft` directly from PyPI:

```bash
pip install dircraft
```

Or, install from source:

```bash
git clone https://github.com/whiteflakes/dircraft.git
cd dircraft
pip install -e .
```

## Usage

### **Using a YAML File**
Create a `structure.yaml` file:

```yaml
project_name:
  src:
    main.py: "# Main entry point"
    utils.py: "# Helper functions"
  data:
    raw: {}
    processed: {}
  tests:
    test_main.py: "# Unit tests"
  README.md: "# Documentation"
  requirements.txt: "numpy\nmatplotlib"
```

Then run:

```bash
dircraft structure.yaml /path/to/target/directory
```
> Usage of ```dircraft-gui``` on CLI is recommended for better experience.

### **Using a Tree/Text File**
Define your project in `structure.txt`:

```
project_name/
├── src/
│   ├── main.py        # Main entry point
│   └── utils.py       # Helper functions
├── data/
│   ├── raw/
│   ├── processed/
├── tests/
│   └── test_main.py   # Unit tests
├── README.md         # Documentation
└── requirements.txt  # Dependencies
```

Then run:

```bash
dircraft structure.txt /path/to/target/directory
```
> Usage of ```dircraft-gui``` on CLI is recommended for better experience.

### **Direct Terminal Input**
Generate a simple project structure from the command line:

```bash
dircraft --structure "project/src/main.py:# Main entry; project/README.md:# Docs" /target/directory
```

> **Note:** Separate multiple file definitions with `;` and use `:` to specify content.


---

## **Roadmap**
- **Enhanced Input Parsers:** JSON, Markdown-based input support.
- **Templating Support:** Jinja2 templates for dynamic project structures.
- **GUI Frontend:** A web-based tool to define structures visually.

## **License**
MIT License – see [LICENSE](LICENSE).

## **Contact**
For questions or suggestions, please open an issue on [GitHub](https://github.com/yourusername/dircraft).

