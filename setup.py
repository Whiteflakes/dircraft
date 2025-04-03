from setuptools import setup, find_packages

setup(
    name="dircraft",
    version="0.1.0",
    author="Whiteflakes",
    author_email="whiteflakesdev@gmail.com",
    description="A tool to generate project directory structures from specifications.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Whiteflakes/dircraft", 
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pyyaml",
        "click",
    ],
    entry_points={
        "console_scripts": [
            "dircraft = dircraft.cli:main",
            "dircraft-gui = dircraft.gui:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
