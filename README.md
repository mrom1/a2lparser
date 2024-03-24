# Python A2L Parser

![main_workflow](https://github.com/mrom1/a2lparser/actions/workflows/main.yml/badge.svg)
![build_workflow](https://github.com/mrom1/a2lparser/actions/workflows/build.yml/badge.svg)
![flake8_workflow](https://github.com/mrom1/a2lparser/actions/workflows/flake8.yml/badge.svg)
[![codecov](https://codecov.io/gh/mrom1/a2lparser/branch/main/graph/badge.svg?token=CZ74J83NO2)](https://codecov.io/gh/mrom1/a2lparser)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This A2L Parser, implemented in Python using [PLY](https://ply.readthedocs.io/en/latest/index.html), serves the purpose of reading A2L files according to the [ASAM MCD-2 MC](https://www.asam.net/standards/detail/mcd-2-mc/) Data Model for ECU Measurement and Calibration Standard. All resources utilized in developing this project are derived from publicly available information, such as the [ASAM Wiki](https://www.asam.net/standards/detail/mcd-2-mc/wiki/).

This Python module enables the parsing of A2L files into an Abstract Syntax Tree with dictionary access in Python. Moreover, it provides functionality to convert the parsed A2L file into simpler formats, currently supporting XML, JSON, or YAML conversions. It's important to note that this project focuses solely on parsing the A2L grammar and does not provide mapping capabilities. It has been entirely rewritten from the original codebase and now fully supports ASAM MCD-2 MC Version 1.7.1.

Released under the GPL license with no warranty, it is recommended primarily for educational purposes. For professional solutions, consider exploring specialized companies in this domain, such as the [MATLAB Vehicle Network Toolbox](https://www.mathworks.com/help/vnt/index.html) or the [Vector ASAP2 Toolset](https://www.vector.com/int/en/products/products-a-z/software/asap2-tool-set/).

## Installation

```console
pip install a2lparser
```

## Usage from CLI

```console
❯ a2lparser --help
usage: a2lparser [-h] [-x] [-j] [-y] [--no-prompt] [--no-optimize] [--no-validation] [--output-dir [OUTPUT_DIR]]
                 [--gen-ast [GEN_AST]] [--version]
                 [filename]

positional arguments:
  filename              A2L file(s) to parse

options:
  -h, --help            show this help message and exit
  -x, --xml             Converts an A2L file to a XML output file
  -j, --json            Converts an A2L file to a JSON output file
  -y, --yaml            Converts an A2L file to a YAML output file
  --no-prompt           Disables CLI prompt after parsing
  --no-validation       Disables possible A2L validation warnings
  --output-dir [OUTPUT_DIR]
                        Output directory for converted files
  --gen-ast [GEN_AST]   Generates python file containing AST node classes
  --version             show program's version number and exit
  ```

## Usage as Module

```python
from a2lparser.a2l.parser import Parser

try:
    # Create Parser and parse files
    ast = Parser().parse_files(files="./data/test.a2l")

    # Dictionary access on abstract syntax tree
    module = ast["test.a2l"]["PROJECT"]["MODULE"]

    # Searches for all MEASUREMENT sections
    measurements = ast.find_sections("MEASUREMENT")
    print(measurements)

except Exception as ex:
    print(ex)
```
