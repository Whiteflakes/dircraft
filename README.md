# dircraft

dircraft is a versatile Python package that automatically generates a project folder structure with files based on an input specification. It supports input in various formats – a YAML file, a plain text tree structure, or even direct terminal input – to create the corresponding directories and files.

## Features

- **Multi-format Input:**  
  - **YAML Files:** Define your folder structure with nested dictionaries.
  - **Tree/Text Files:** Provide a tree-like text representation of the desired structure.
  - **Direct Terminal Input:** Paste a file structure directly via command-line parameters.
- **Customizable File Contents:**  
  Include file content in the input definition. If no content is provided, empty files are created.
- **Recursive Directory Creation:**  
  Automatically creates nested directories and files.
- **Command Line Interface (CLI):**  
  Easy-to-use CLI using Click.
- **Extendable and Modular:**  
  Designed to be extended with additional input formats or templating engines.

## Installation

Clone the repository and install it using pip:

```bash
git clone https://github.com/yourusername/dircraft.git
cd dircraft
pip install -e .
```

Alternatively, you can install it directly from PyPI (if published):

```bash
pip install dircraft
```

## Usage

dircraftoldGen provides a CLI tool called `dircraft` that you can use to generate your project structure.

### Using a YAML File

Create a YAML file (e.g., `structure.yaml`) that defines your file structure. For example:

```yaml
modal_decomposition:
  data:
    train: {}
    val: {}
    test: {}
  models:
    vgg16_modified.py: "# TODO: VGG16 model implementation"
    pnorm_layer.py: "# TODO: Custom normalization layer"
  scripts:
    train.py: "# TODO: Training script"
    evaluate.py: "# TODO: Evaluation script"
    infer.py: "# TODO: Inference script"
  utils:
    data_loader.py: "# TODO: Data loader implementation"
    visualize.py: "# TODO: Visualization functions"
    losses.py: "# TODO: Custom loss functions"
  config:
    config.yaml: |
      learning_rate: 1e-4
      batch_size: 64
  main.py: "# Main entry point"
  README.md: "# Project documentation"
  requirements.txt: "torch\nnumpy\n..."
```

Then run:

```bash
dircraft structure.yaml /path/to/target/directory
```

### Using a Tree/Text File

If you have a tree-like structure defined in a text file (e.g., `structure.txt`), the file might look like:

```
modal_decomposition/
├── data/
│   ├── train/
│   ├── val/
│   └── test/
├── models/
│   ├── vgg16_modified.py # TODO: VGG16 model implementation
│   └── pnorm_layer.py    # TODO: Custom normalization layer
├── scripts/
│   ├── train.py    # TODO: Training script
│   ├── evaluate.py # TODO: Evaluation script
│   └── infer.py    # TODO: Inference script
├── utils/
│   ├── data_loader.py   # TODO: Data loader implementation
│   ├── visualize.py     # TODO: Visualization functions
│   └── losses.py        # TODO: Custom loss functions
├── config/
│   └── config.yaml      # learning_rate: 1e-4, batch_size: 64
├── main.py     # Main entry point
├── README.md   # Project documentation
└── requirements.txt  # torch, numpy, ...
```

dircraft can be extended to parse such tree-like formats. (For now, the basic version uses YAML but check out our roadmap for future support.)

### Direct Terminal Input

You can also pass a file structure definition directly as a command-line argument. For example:

```bash
dircraft --structure "modal_decomposition/main.py:# Main entry point; modal_decomposition/README.md:# Documentation" /path/to/target/directory
```

In this mode, separate multiple file definitions with a semicolon (`;`) and use a colon (`:`) to separate the file path from its content.

> **Note:** The direct terminal input is ideal for small structures and quick tests.

<!-- ## Advanced Configuration

The configuration file (`config.yaml`) under the `config` directory can be used to adjust package behavior and default settings, such as:
- Default file extension handling.
- Parsing preferences for text-based tree structures.
- Logging levels for the generation process.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request. Check our [CONTRIBUTING.md](CONTRIBUTING.md) file for more details. -->

## Roadmap

- **Enhanced Input Parsers:**  
  Support for more input formats (e.g., JSON, indented text trees).
- **Templating Support:**  
  Integration with Jinja2 for templated file contents.
- **GUI Frontend:**  
  A simple web interface to define and preview the project structure before generation.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please open an issue.

