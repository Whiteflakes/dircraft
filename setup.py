from setuptools import setup, find_packages

setup(
    name="scaff",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyYAML",
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "scaff = scaff.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    author="Whiteflakes",
    description="A tool to generate file structures from YAML configurations.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  
)
