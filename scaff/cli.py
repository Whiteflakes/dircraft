import click
from pathlib import Path
from scaff.generator import generate_from_yaml

@click.command()
@click.argument("yaml_file", type=click.Path(exists=True))
@click.argument("target_dir", type=click.Path())
def main(yaml_file, target_dir):
    """
    Generate a file structure from YAML_FILE into TARGET_DIR.
    """
    yaml_path = Path(yaml_file)
    target_path = Path(target_dir)
    generate_from_yaml(yaml_path, target_path)
    click.echo(f"File structure generated in {target_path}")

if __name__ == "__main__":
    main()
