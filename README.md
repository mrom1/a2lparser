# Python A2L Parser

![Main Workflow](https://github.com/mrom1/a2lparser/actions/workflows/main.yml/badge.svg)
![PyPI Workflow](https://github.com/mrom1/a2lparser/actions/workflows/publish-to-pypi.yml/badge.svg)
![Build Workflow](https://github.com/mrom1/a2lparser/actions/workflows/build.yml/badge.svg)
![Flake8 Workflow](https://github.com/mrom1/a2lparser/actions/workflows/flake8.yml/badge.svg)
[![codecov](https://codecov.io/gh/mrom1/a2lparser/branch/main/graph/badge.svg?token=CZ74J83NO2)](https://codecov.io/gh/mrom1/a2lparser)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Overview

The Python A2L Parser is a tool designed for reading A2L files compliant with the [ASAM MCD-2 MC](https://www.asam.net/standards/detail/mcd-2-mc/) Data Model for ECU Measurement and Calibration. This parser, implemented in Python using [PLY](https://ply.readthedocs.io/en/latest/index.html), constructs an Abstract Syntax Tree (AST) from A2L files, allowing for structured data access and utility functions like searching.

This project supports ASAM MCD-2 MC Version 1.7.1 and focuses on parsing A2L grammar, not providing mapping capabilities. The module also includes functionality for converting parsed A2L files into simpler formats like XML, JSON, and YAML.

You can use this repository to interpret A2L files, build upon this functionality, or for educational purposes.

**Note:** This project is released under the GPL license with no warranty and is recommended for educational purposes. For professional solutions, consider exploring specialized tools such as the [MATLAB Vehicle Network Toolbox](https://www.mathworks.com/help/vnt/index.html) or the [Vector ASAP2 Toolset](https://www.vector.com/int/en/products/products-a-z/software/asap2-tool-set/).

## Installation

To install the A2L Parser, run:

```console
pip install -i https://test.pypi.org/simple/ a2lparser --extra-index-url https://pypi.org/simple/
```

## Usage as Module

```python
from a2lparser.a2lparser import A2LParser
from a2lparser.a2lparser_exception import A2LParserException

try:
    # Create Parser and parse files
    ast = A2LParser(quiet=True).parse_file(files="./data/test.a2l")

    # Dictionary access on abstract syntax tree
    module = ast["test.a2l"]["PROJECT"]["MODULE"]

    # Searches for all MEASUREMENT sections
    measurements = ast.find_sections("MEASUREMENT")
    print(measurements)

except A2LParserException as ex:
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
  --version             show program's version number and exit  ```
```
