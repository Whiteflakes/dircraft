import click
from pathlib import Path
from dircraft.generator import generate_structure

@click.command()
@click.argument("input_source", type=click.STRING)
@click.argument("target_dir", type=click.Path())
def main(input_source, target_dir):
    """
    Generate a file structure from INPUT_SOURCE into TARGET_DIR.

    INPUT_SOURCE can be a path to a YAML, TXT, or a direct structure string.
    """
    target_path = Path(target_dir)
    generate_structure(input_source, target_path)
    click.echo(f"\n✅ File structure successfully generated in: {target_path}\n")

if __name__ == "__main__":
    main()
