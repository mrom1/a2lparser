# Python A2L Parser

![Main Workflow](https://github.com/mrom1/a2lparser/actions/workflows/main.yml/badge.svg)
![PyPI Workflow](https://github.com/mrom1/a2lparser/actions/workflows/publish-to-pypi.yml/badge.svg)
![Build Workflow](https://github.com/mrom1/a2lparser/actions/workflows/build.yml/badge.svg)
![Flake8 Workflow](https://github.com/mrom1/a2lparser/actions/workflows/flake8.yml/badge.svg)
[![codecov](https://codecov.io/gh/mrom1/a2lparser/branch/main/graph/badge.svg?token=CZ74J83NO2)](https://codecov.io/gh/mrom1/a2lparser)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Overview

The Python A2L Parser is a tool designed to parse A2L files compliant with the [ASAM MCD-2 MC](https://www.asam.net/standards/detail/mcd-2-mc/) Data Model for ECU Measurement and Calibration. Implemented in Python using [PLY](https://ply.readthedocs.io/en/latest/index.html), it constructs an Abstract Syntax Tree (AST) from A2L files, enabling structured data access and utility functions such as searching. All resources used in development are sourced from publicly available information, including the [ASAM Wiki](https://www.asam.net/standards/detail/mcd-2-mc/wiki/).

The parser supports ASAM MCD-2 MC Version 1.7.1 and is focused on parsing A2L grammar without providing mapping capabilities. Additionally, the module includes functionality for converting parsed A2L files into simpler formats like XML, JSON, and YAML.

This repository can be used for interpreting or validating A2L files, extending its functionality, or for educational purposes.

**Note:** Released under the GPL license with no warranty, this project is recommended for educational use. For professional solutions, consider specialized tools such as the [MATLAB Vehicle Network Toolbox](https://www.mathworks.com/help/vnt/index.html) or the [Vector ASAP2 Toolset](https://www.vector.com/int/en/products/products-a-z/software/asap2-tool-set/).

## Installation

To install the A2L Parser, run:

**Note:** Until I fix some more minor issues and create a release version, a TestPyPi version is uploaded which you can use:

```console
pip install -i https://test.pypi.org/simple/ a2lparser --extra-index-url https://pypi.org/simple/
```

## Usage as Module

```python
from a2lparser.a2lparser import A2LParser
from a2lparser.a2lparser_exception import A2LParserException

try:
    # Create a parser and parse files.
    # Allows multiple files to be passed with wildcards.
    # Will only print errors, no information like progressbar.
    # Returns a dictionary.
    ast_dict = A2LParser(log_level="INFO").parse_file("./testfiles/test_*.a2l")

    # The dictionary holds the AbstractSyntaxTree object under the file name key.
    ast = ast_dict["test_1.a2l"]

    # Dictionary access on the abstract syntax tree.
    # Returns a Python dictionary.
    project = ast["PROJECT"]
    module = project["MODULE"]
    print(f"Project {project['Name']} with module: {module['Name']}"

    # Searches for all MEASUREMENT sections.
    # find_section returns an AbstractSyntaxTree
    measurements = ast.find_sections("MEASUREMENT")

    # All found MEASUREMENT sections are under the "MEASUREMENT" key
    measurements_list = measurements["MEASUREMENT"]

    print(f"Found {len(measurements_list)} MEASUREMENT sections.")

except A2LParserException as ex:
    # Catching A2LParserException:
    # Generally occurs when a fatal error in parsing is encountered,
    # or if the generated AST is empty (i.e., no data could be parsed).
    print(ex)
```

## Usage from CLI

```console
❯ a2lparser --help
usage: a2lparser [-h] [-x] [-j] [-y] [--output-dir [PATH]] [--prompt] [--quiet] [--no-optimize] [--no-validation]
                 [--gen-ast [CONFIG]] [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [--version]
                 [file]

positional arguments:
  file                  A2L files to parse

options:
  -h, --help            show this help message and exit
  -x, --xml             Converts an A2L file to a XML output file
  -j, --json            Converts an A2L file to a JSON output file
  -y, --yaml            Converts an A2L file to a YAML output file
  --output-dir [PATH]   Output directory for converted files
  --prompt              Enables CLI prompt after parsing
  --quiet               Disables console output
  --no-optimize         Disables optimization mode
  --no-validation       Disables possible A2L validation warnings
  --gen-ast [CONFIG]    Generates python file containing AST node classes
  --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
  --version             show program's version number and exit
```
