# Python A2L Parser

An A2L file is a description file that defines the implementation of an ECU (electrical control unit).

It is a formatted text file containing measurement definitions, computation methods, events and various configuration information. An A2L file allows a XCP master to communicate with a XCP slave through a XCP connection. It is used for acquiring and stimulating data and to perform other functions.

Oftentimes one only needs measurements from specific addresses, or specific computation methods, or a simple way to parse large datasets over multiple files.

This parser enables the possibility to parse a A2L file into a abstract syntax tree, which can be accessed or modified in memory, or additionally export it to the simpler format XML.


***Important: Currently only supports Python 2!***

## Basic Usage
To parse a A2L file and generate the corresponding XML file use this command:
```
python a2lparser.py [file.a2l] --xml
```
You can also glob multiple files together. For example if you have a directory ``a2l_files`` containing A2L files ending on ``*.a2l`` you can use this to convert all of them at once.
```
python a2lparser.py a2l_files/*.a2l --xml
```
If you wish to just generate the abstract syntax tree and manipulate or read the data in memory without generating a XML file, you could do something like this:
```python
from a2l.parser import Parser
from a2l.config.config import Config

# Create your parsing configuration
cfg = Config()

# Parse file into abstract syntax tree
p = Parser(config=cfg)
ast = p.parseFile(fileName="path/to/your/file.a2l")
if p.config.validateAST(ast):
	print("AST is valid!")
```
To run all of the unit tests invoke the parser with the ``--testcases`` argument like this:
```
python a2lparser.py --testcases
```
This is especially useful if you start to change the configuration file or add / update your own rules.


## How to use your own configuration

The `A2L_ASAM.cfg` file is specified for the use of the ASAM MCD-2 MC Version 1.61

If you need to support different keywords or parameters you should update this file\
and generate a new abstract syntax tree skeleton by using this command:
```
python a2lparser.py --gen-ast [your_config_file.cfg]
```

### Config file syntax

The config generator expects a specific file format. Every line is a defined A2L Keyword, or user defined reference and then a colon followed by the parameters for this object.

The Basic structure is as follows: 
```
A2L_KEYWORD : ([?]Parametername_Simple[*|**], ...)
```

| Symbols | Explanation 
| :--------------: | :--------- |
| #        | Declares the line as a comment
| ?        | Defines the parameter as optional 
| *        | Parameter is a reference to another object (A2L keyword) with more than one parameter |
| **       | References to a list of Objects (A2L keywords) |
|(nothing) | Simple attribut without reference (String, Int etc.)   |

For example the A2L keyword ``USER_RIGHTS`` is defined like this:
```c
## User Rights definitions
USER_RIGHTS : (UserLevelId, ?OptionalParams*)
USER_RIGHTS_OPT : (?Read_Only, ?Ref_Group**)

## Simple objects referenced by User Rights
READ_ONLY : (Boolean)
REF_GROUP : (Identifier)
```
Which could parse a A2L ``USER_RIGHTS`` section as this:
```c
/begin USER_RIGHTS calibration_engineers /* Required: User Level ID */
	/begin REF_GROUP group_1			 /* Ref Group: Identifier   */
	/end REF_GROUP
	/begin REF_GROUP group_2			 /* Ref Group: Identifier   */
	/end REF_GROUP
	READ_ONLY							 /* Read Only: Boolean		*/
/end USER_RIGHTS
```


### Changing the config file
Let's say you want to parse a A2L file which which uses a optional ``VERSION`` tag for their computation method.

```c
// Example_A2L_file.a2l

/begin COMPU_METHOD     TMPCON1 /* name */
                        "conversion method for engine temperature"
                        TAB_NOINTP /* convers_type */
                        "%4.2" /* display format */
                        "°C" /* physical unit */
    COMPU_TAB_REF       MOTEMP1
    VERSION             "BG5.0815" /* This parameter is not expected */
    							   /* in 'normal' ASAM MCD version */
/end COMPU_METHOD
```

So we change the ``COMPU_METHOD_OPT`` line in the config file like this: 
```c
## Pre-defined version identifier
VERSION : (VersoinIdentifier)

## This is the original definition according to the ASAM MCD-2 MC Version 1.61
COMPU_METHOD : (Name, LongIdentifier, ConversionType, Format, Unit, ?OptionalParams*)
COMPU_METHOD_OPT : (?Coeffs*, ?Coeffs_Linear*, ?Compu_Tab_Ref, ?Formula*, ?Ref_Unit, ?Status_String_Ref)

## Adding a version identifier to COMPU_METHOD_OPT
COMPU_METHOD : (Name, LongIdentifier, ConversionType, Format, Unit, ?OptionalParams*)
COMPU_METHOD_OPT : (?Version, ?Coeffs*, ?Coeffs_Linear*, ?Compu_Tab_Ref, ?Formula*, ?Ref_Unit, ?Status_String_Ref)
```

### How to use custom parsing rules
If you want to use your own parsing rules, for example a new ``VERSION`` tag for the ``COMPU_METHOD`` description as mentioned above, you can update the rules in the ``a2l/a2l_yacc.py`` file like this:

Original rule:

```python
# Original parsing rule
def p_COMPU_METHOD_opt_params(self, p):
        """
        compu_method_opt    : compu_tab_ref
                            | ref_unit
                            | status_string_ref

        """
        node = self.__get_or_create_AST_Node(A2l_ast.Compu_Method_Opt)
        self.__add_AST_Node_Param(NodeClass = node,
                                  AstNodeNames = [A2l_ast.Compu_Tab_Ref,
                                                  A2l_ast.Ref_Unit,
                                                  A2l_ast.Status_String_Ref],
                                  Param = p[1])

        p[0] = node
```
Updated rule:
```python
# Updated parsing rule
def p_COMPU_METHOD_opt_params(self, p):
        """
        compu_method_opt    : version
                            | compu_tab_ref
                            | ref_unit
                            | status_string_ref

        """
        node = self.__get_or_create_AST_Node(A2l_ast.Compu_Method_Opt)
        self.__add_AST_Node_Param(NodeClass = node,
                                 AstNodeNames = [A2l_ast.Version,
                                                 A2l_ast.Compu_Tab_Ref,
                                                 A2l_ast.Ref_Unit,
                                                 A2l_ast.Status_String_Ref],
                                 Param = p[1])

        p[0] = node
```

## ToDo
- [ ] Update to Python 3
- [ ] Reach 100% test coverage
