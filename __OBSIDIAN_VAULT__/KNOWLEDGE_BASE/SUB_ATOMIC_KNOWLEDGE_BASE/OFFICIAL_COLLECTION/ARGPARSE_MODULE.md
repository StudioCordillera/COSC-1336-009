# ARGPARSE_MODULE

## Core Definition
**argparse** is Python's standard library module for parsing command-line arguments. It automatically generates help messages, handles both optional and positional arguments, supports subcommands, and validates user input with clear error messages.

**Tags**: #argparse #cli #command-line #arguments #parser #options

---

## COMPLETE ARGPARSE QUICK REFERENCE

### ARGPARSE METHODS - Target | Operation | Output

```python
# ═══════════════════════════════════════════════════════════════════════════
# ARGUMENTPARSER CREATION
# ═══════════════════════════════════════════════════════════════════════════
ArgumentParser()                                      # No args | Create basic parser | Returns ArgumentParser object
ArgumentParser(prog='name')                           # Program name | Set program name | Returns ArgumentParser object
ArgumentParser(usage='%(prog)s [options]')            # Usage string | Custom usage message | Returns ArgumentParser object
ArgumentParser(description='text')                    # Description | Add program description | Returns ArgumentParser object
ArgumentParser(epilog='text')                         # Epilog text | Add text after help | Returns ArgumentParser object
ArgumentParser(parents=[parser1, parser2])            # Parent parsers | Inherit arguments | Returns ArgumentParser object
ArgumentParser(formatter_class=class)                 # Formatter class | Customize help format | Returns ArgumentParser object
ArgumentParser(prefix_chars='-+')                     # Prefix chars | Set option prefixes | Returns ArgumentParser object
ArgumentParser(fromfile_prefix_chars='@')             # File prefix | Enable @file arguments | Returns ArgumentParser object
ArgumentParser(argument_default=None)                 # Default value | Global default for args | Returns ArgumentParser object
ArgumentParser(conflict_handler='error')              # Conflict mode | Handle option conflicts | Returns ArgumentParser object
ArgumentParser(add_help=True)                         # Boolean | Add -h/--help option | Returns ArgumentParser object
ArgumentParser(allow_abbrev=True)                     # Boolean | Allow option abbreviation | Returns ArgumentParser object
ArgumentParser(exit_on_error=True)                    # Boolean | Exit on parse error | Returns ArgumentParser object
ArgumentParser(suggest_on_error=False)                # Boolean (3.14+) | Suggest corrections | Returns ArgumentParser object
ArgumentParser(color=True)                            # Boolean (3.14+) | Colorize help output | Returns ArgumentParser object

# ═══════════════════════════════════════════════════════════════════════════
# ADDING ARGUMENTS
# ═══════════════════════════════════════════════════════════════════════════
parser.add_argument('name')                           # Positional | Add positional argument | Returns Action object
parser.add_argument('-f', '--foo')                    # Option flags | Add optional argument | Returns Action object
parser.add_argument('--foo', action='store')          # Action type | Store value (default) | Returns Action object
parser.add_argument('--foo', action='store_const')    # Action type | Store constant value | Returns Action object
parser.add_argument('--foo', action='store_true')     # Action type | Store True if present | Returns Action object
parser.add_argument('--foo', action='store_false')    # Action type | Store False if present | Returns Action object
parser.add_argument('--foo', action='append')         # Action type | Append to list | Returns Action object
parser.add_argument('--foo', action='append_const')   # Action type | Append constant to list | Returns Action object
parser.add_argument('--foo', action='extend')         # Action type (3.8+) | Extend list with values | Returns Action object
parser.add_argument('--foo', action='count')          # Action type | Count occurrences | Returns Action object
parser.add_argument('--foo', action='help')           # Action type | Show help and exit | Returns Action object
parser.add_argument('--foo', action='version')        # Action type | Show version and exit | Returns Action object
parser.add_argument('--foo', action=BooleanOptionalAction) # Action (3.9+) | Add --foo/--no-foo | Returns Action object
parser.add_argument('--foo', nargs=N)                 # Integer | Consume N arguments | Returns Action object
parser.add_argument('--foo', nargs='?')               # Nargs | 0 or 1 argument | Returns Action object
parser.add_argument('--foo', nargs='*')               # Nargs | 0 or more arguments | Returns Action object
parser.add_argument('--foo', nargs='+')               # Nargs | 1 or more arguments | Returns Action object
parser.add_argument('--foo', const='value')           # Constant | Value for store_const | Returns Action object
parser.add_argument('--foo', default='value')         # Default value | Value if arg absent | Returns Action object
parser.add_argument('--foo', type=int)                # Type converter | Convert to int | Returns Action object
parser.add_argument('--foo', choices=['a', 'b'])      # Choice list | Restrict to choices | Returns Action object
parser.add_argument('--foo', required=True)           # Boolean | Make option required | Returns Action object
parser.add_argument('--foo', help='help text')        # Help string | Add help description | Returns Action object
parser.add_argument('--foo', metavar='NAME')          # Metavar | Display name in help | Returns Action object
parser.add_argument('--foo', dest='variable')         # Destination | Attribute name | Returns Action object
parser.add_argument('--foo', deprecated=True)         # Boolean (3.13+) | Mark as deprecated | Returns Action object

# ═══════════════════════════════════════════════════════════════════════════
# PARSING ARGUMENTS
# ═══════════════════════════════════════════════════════════════════════════
parser.parse_args()                                   # No args | Parse sys.argv | Returns Namespace object
parser.parse_args(['arg1', 'arg2'])                   # Arg list | Parse custom args | Returns Namespace object
parser.parse_args(namespace=obj)                      # Namespace | Parse into existing object | Returns Namespace object
parser.parse_known_args()                             # No args | Parse known args only | Returns (Namespace, list) tuple
parser.parse_known_args(['arg1', 'arg2'])             # Arg list | Parse known from list | Returns (Namespace, list) tuple
parser.parse_intermixed_args()                        # No args (3.7+) | Parse intermixed args | Returns Namespace object
parser.parse_known_intermixed_args()                  # No args (3.7+) | Parse intermixed known | Returns (Namespace, list) tuple

# ═══════════════════════════════════════════════════════════════════════════
# SUBCOMMANDS
# ═══════════════════════════════════════════════════════════════════════════
parser.add_subparsers()                               # No args | Create subparser container | Returns SubParsersAction object
parser.add_subparsers(title='commands')               # Title | Set subparser section title | Returns SubParsersAction object
parser.add_subparsers(description='text')             # Description | Add subparser description | Returns SubParsersAction object
parser.add_subparsers(prog='name')                    # Program name | Set program name | Returns SubParsersAction object
parser.add_subparsers(parser_class=class)             # Parser class | Subparser class to use | Returns SubParsersAction object
parser.add_subparsers(action='store')                 # Action | Action type for subparser | Returns SubParsersAction object
parser.add_subparsers(dest='subcmd')                  # Destination | Attribute for subcommand | Returns SubParsersAction object
parser.add_subparsers(required=True)                  # Boolean (3.7+) | Require subcommand | Returns SubParsersAction object
parser.add_subparsers(help='help text')               # Help string | Help for subparsers | Returns SubParsersAction object
parser.add_subparsers(metavar='COMMAND')              # Metavar | Display name in help | Returns SubParsersAction object
subparsers.add_parser('name')                         # Command name | Create subcommand parser | Returns ArgumentParser object
subparsers.add_parser('name', aliases=['alias'])      # Aliases | Add command aliases | Returns ArgumentParser object
subparsers.add_parser('name', help='text')            # Help string | Help for subcommand | Returns ArgumentParser object
subparsers.add_parser('name', deprecated=True)        # Boolean (3.13+) | Mark subcommand deprecated | Returns ArgumentParser object

# ═══════════════════════════════════════════════════════════════════════════
# ARGUMENT GROUPS
# ═══════════════════════════════════════════════════════════════════════════
parser.add_argument_group('name')                     # Group name | Create argument group | Returns ArgumentGroup object
parser.add_argument_group('name', 'description')      # Name, desc | Create described group | Returns ArgumentGroup object
parser.add_argument_group(argument_default=None)      # Default | Set group default | Returns ArgumentGroup object
parser.add_argument_group(conflict_handler='error')   # Handler | Set conflict handler | Returns ArgumentGroup object
parser.add_mutually_exclusive_group()                 # No args | Create exclusive group | Returns MutuallyExclusiveGroup object
parser.add_mutually_exclusive_group(required=True)    # Boolean | Require one of group | Returns MutuallyExclusiveGroup object

# ═══════════════════════════════════════════════════════════════════════════
# PARSER DEFAULTS
# ═══════════════════════════════════════════════════════════════════════════
parser.set_defaults(**kwargs)                         # Key-value pairs | Set default attributes | Returns None
parser.get_default('dest')                            # Attribute name | Get default value | Returns default value

# ═══════════════════════════════════════════════════════════════════════════
# HELP AND USAGE
# ═══════════════════════════════════════════════════════════════════════════
parser.print_help()                                   # No args | Print full help | Prints to stdout
parser.print_help(file=sys.stderr)                    # File object | Print help to file | Prints to file
parser.print_usage()                                  # No args | Print usage line | Prints to stdout
parser.print_usage(file=sys.stderr)                   # File object | Print usage to file | Prints to file
parser.format_help()                                  # No args | Get help as string | Returns help string
parser.format_usage()                                 # No args | Get usage as string | Returns usage string

# ═══════════════════════════════════════════════════════════════════════════
# ERROR HANDLING
# ═══════════════════════════════════════════════════════════════════════════
parser.error('message')                               # Error message | Print error and exit | Exits with code 2
parser.exit(status=0, message='text')                 # Status, message | Exit program | Exits with status code

# ═══════════════════════════════════════════════════════════════════════════
# FILE ARGUMENT PARSING
# ═══════════════════════════════════════════════════════════════════════════
parser.convert_arg_line_to_args(line)                 # Line string | Parse file argument line | Returns list of arguments
FileType('r')                                         # File mode | Create file type for reading | Returns file object
FileType('w', encoding='utf-8')                       # Mode, encoding | Create file type for writing | Returns file object
FileType('rb')                                        # Binary mode | Create binary file type | Returns file object

# ═══════════════════════════════════════════════════════════════════════════
# CUSTOM ACTIONS
# ═══════════════════════════════════════════════════════════════════════════
parser.register('action', 'name', class)              # Type, name, class | Register custom action | Returns None
parser.register('type', 'name', callable)             # Type, name, function | Register custom type | Returns None
Action(option_strings, dest)                          # Strings, dest | Create custom action | Returns Action subclass
action.__call__(parser, namespace, values, option)    # Call args | Execute action | Modifies namespace
action.format_usage()                                 # No args | Format action usage | Returns usage string

# ═══════════════════════════════════════════════════════════════════════════
# NAMESPACE OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════
Namespace()                                           # No args | Create empty namespace | Returns Namespace object
Namespace(foo='bar', baz=42)                          # Key-values | Create initialized namespace | Returns Namespace object
vars(namespace)                                       # Namespace | Get dict view | Returns dict
namespace.attribute                                   # Attribute | Access parsed value | Returns value
setattr(namespace, 'name', value)                     # Name, value | Set attribute | Returns None
hasattr(namespace, 'name')                            # Attribute name | Check if exists | Returns True/False

# ═══════════════════════════════════════════════════════════════════════════
# FORMATTER CLASSES
# ═══════════════════════════════════════════════════════════════════════════
RawDescriptionHelpFormatter                           # Formatter class | Preserve description formatting | Class reference
RawTextHelpFormatter                                  # Formatter class | Preserve all text formatting | Class reference
ArgumentDefaultsHelpFormatter                         # Formatter class | Show default values in help | Class reference
MetavarTypeHelpFormatter                              # Formatter class | Use type as metavar | Class reference

# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════
argparse.SUPPRESS                                     # Constant | Suppress attribute creation | SUPPRESS constant
argparse.REMAINDER                                    # Constant | Collect remaining args | REMAINDER constant

# ═══════════════════════════════════════════════════════════════════════════
# EXCEPTIONS
# ═══════════════════════════════════════════════════════════════════════════
ArgumentError                                         # Exception | Argument configuration error | Exception class
ArgumentTypeError                                     # Exception | Type conversion error | Exception class
```

### COMMON OPERATION EXAMPLES

```python
import argparse

# Basic parser
parser = argparse.ArgumentParser(description='Process some data')

# Positional argument
parser.add_argument('filename')

# Optional argument with value
parser.add_argument('-o', '--output', help='output file')

# Flag (boolean)
parser.add_argument('-v', '--verbose', action='store_true')

# Integer argument
parser.add_argument('-c', '--count', type=int, default=1)

# Choice restriction
parser.add_argument('--format', choices=['json', 'xml', 'csv'])

# Multiple values
parser.add_argument('files', nargs='+')

# Parse arguments
args = parser.parse_args()

# Access values
print(args.filename)
print(args.verbose)
print(args.count)
```

---

## DETAILED ARGPARSE OPERATIONS

### 1. CREATING AN ARGUMENTPARSER

```python
import argparse

# Basic parser
parser = argparse.ArgumentParser()

# Parser with description
parser = argparse.ArgumentParser(
    description='A program that processes files',
    epilog='Thanks for using %(prog)s!'
)

# Custom program name
parser = argparse.ArgumentParser(prog='myapp')

# Custom usage message
parser = argparse.ArgumentParser(
    prog='myapp',
    usage='%(prog)s [options] input output'
)

# Inherit from parent parsers
parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--verbose', action='store_true')

parser = argparse.ArgumentParser(parents=[parent_parser])
# Now parser has --verbose argument inherited

# Custom formatter (preserve formatting)
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''
    Line 1
        Indented line 2
    Line 3
    '''
)

# Show defaults in help
parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

# Custom prefix characters (for Windows-style /options)
parser = argparse.ArgumentParser(prefix_chars='-/')
parser.add_argument('/o', '--output')  # Works with /o or --output

# Enable @file arguments
parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
# Can now use: python script.py @args.txt

# Don't exit on error (for testing or interactive use)
parser = argparse.ArgumentParser(exit_on_error=False)
try:
    args = parser.parse_args(['--invalid'])
except argparse.ArgumentError as e:
    print(f"Error: {e}")

# Enable suggestions for typos (Python 3.14+)
parser = argparse.ArgumentParser(suggest_on_error=True)
# If user types --ouput, suggests "did you mean --output?"

# Disable color in help (Python 3.14+)
parser = argparse.ArgumentParser(color=False)

# Disable abbreviation matching
parser = argparse.ArgumentParser(allow_abbrev=False)
parser.add_argument('--foobar')
parser.add_argument('--foobaz')
# Now --foo won't match (would be ambiguous)
```

### 2. ADDING POSITIONAL ARGUMENTS

```python
import argparse

parser = argparse.ArgumentParser()

# Simple positional argument
parser.add_argument('filename')
args = parser.parse_args(['input.txt'])
print(args.filename)  # → 'input.txt'

# Positional with type
parser.add_argument('count', type=int)
args = parser.parse_args(['42'])
print(args.count)  # → 42

# Positional with help
parser.add_argument('source', help='source file to process')

# Optional positional (with nargs='?')
parser.add_argument('output', nargs='?', default='stdout')
args = parser.parse_args([])
print(args.output)  # → 'stdout' (default)

# One or more positionals (nargs='+')
parser.add_argument('files', nargs='+')
args = parser.parse_args(['file1.txt', 'file2.txt', 'file3.txt'])
print(args.files)  # → ['file1.txt', 'file2.txt', 'file3.txt']

# Zero or more positionals (nargs='*')
parser.add_argument('files', nargs='*')
args = parser.parse_args([])
print(args.files)  # → []

# Exactly N arguments
parser.add_argument('dimensions', nargs=2, type=int)
args = parser.parse_args(['800', '600'])
print(args.dimensions)  # → [800, 600]

# Positional with choices
parser.add_argument('mode', choices=['fast', 'slow', 'auto'])
args = parser.parse_args(['fast'])
print(args.mode)  # → 'fast'

# Custom metavar for display
parser.add_argument('input', metavar='INPUT_FILE')
# Help shows: INPUT_FILE instead of input
```

### 3. ADDING OPTIONAL ARGUMENTS (FLAGS/OPTIONS)

```python
import argparse

parser = argparse.ArgumentParser()

# Short and long option
parser.add_argument('-o', '--output')
args = parser.parse_args(['-o', 'file.txt'])
print(args.output)  # → 'file.txt'

# Option with default value
parser.add_argument('-c', '--count', type=int, default=10)
args = parser.parse_args([])
print(args.count)  # → 10

# Required option (not recommended, but possible)
parser.add_argument('-i', '--input', required=True)
# Will error if not provided

# Boolean flag (store_true)
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args(['-v'])
print(args.verbose)  # → True

# Boolean flag (store_false)
parser.add_argument('-q', '--quiet', action='store_false', dest='verbose')
args = parser.parse_args(['-q'])
print(args.verbose)  # → False

# Counting flag (for verbosity levels)
parser.add_argument('-v', '--verbose', action='count', default=0)
args = parser.parse_args(['-vvv'])
print(args.verbose)  # → 3

# Append to list
parser.add_argument('-f', '--file', action='append')
args = parser.parse_args(['-f', 'a.txt', '-f', 'b.txt'])
print(args.file)  # → ['a.txt', 'b.txt']

# Extend list (Python 3.8+)
parser.add_argument('--files', action='extend', nargs='+')
args = parser.parse_args(['--files', 'a.txt', 'b.txt', '--files', 'c.txt'])
print(args.files)  # → ['a.txt', 'b.txt', 'c.txt']

# Store constant
parser.add_argument('--mode', action='store_const', const='debug')
args = parser.parse_args(['--mode'])
print(args.mode)  # → 'debug'

# BooleanOptionalAction (Python 3.9+)
parser.add_argument('--feature', action=argparse.BooleanOptionalAction)
args = parser.parse_args(['--feature'])
print(args.feature)  # → True
args = parser.parse_args(['--no-feature'])
print(args.feature)  # → False

# Version action
parser.add_argument('--version', action='version', version='%(prog)s 2.0')
# Running with --version prints "myprogram 2.0" and exits

# Deprecated argument (Python 3.13+)
parser.add_argument('--old-option', deprecated=True)
# Using it prints a warning
```

### 4. ARGUMENT TYPES AND VALIDATION

```python
import argparse
import pathlib

parser = argparse.ArgumentParser()

# Built-in types
parser.add_argument('--int', type=int)
parser.add_argument('--float', type=float)
parser.add_argument('--str', type=str)  # Default

# Pathlib.Path for file paths
parser.add_argument('--path', type=pathlib.Path)
args = parser.parse_args(['--path', '/tmp/file.txt'])
print(type(args.path))  # → <class 'pathlib.Path'>

# Choices validation
parser.add_argument('--format', choices=['json', 'xml', 'yaml'])
args = parser.parse_args(['--format', 'json'])
# parser.parse_args(['--format', 'txt'])  # Error: invalid choice

# Range validation (using choices with range)
parser.add_argument('--level', type=int, choices=range(1, 11))
args = parser.parse_args(['--level', '5'])  # OK
# parser.parse_args(['--level', '15'])  # Error: invalid choice

# Custom type function
def port_number(string):
    value = int(string)
    if not (1 <= value <= 65535):
        raise argparse.ArgumentTypeError(f"{value} is not a valid port")
    return value

parser.add_argument('--port', type=port_number)
args = parser.parse_args(['--port', '8080'])  # OK
# parser.parse_args(['--port', '99999'])  # Error

# FileType for file handles (deprecated but still used)
parser.add_argument('infile', type=argparse.FileType('r'))
parser.add_argument('outfile', type=argparse.FileType('w'))
args = parser.parse_args(['input.txt', 'output.txt'])
# args.infile is an open file object

# Accept stdin/stdout with '-'
parser.add_argument('input', type=argparse.FileType('r'))
args = parser.parse_args(['-'])  # Uses stdin

# Custom validation with action
class ValidateRange(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not (0 <= values <= 100):
            raise argparse.ArgumentError(self, "must be 0-100")
        setattr(namespace, self.dest, values)

parser.add_argument('--percent', type=int, action=ValidateRange)
```

### 5. NARGS (NUMBER OF ARGUMENTS)

```python
import argparse

parser = argparse.ArgumentParser()

# Exactly N arguments
parser.add_argument('--coords', nargs=2, type=float)
args = parser.parse_args(['--coords', '3.5', '7.2'])
print(args.coords)  # → [3.5, 7.2]

# Optional single argument (?)
parser.add_argument('--output', nargs='?', const='default.txt', default=None)
args = parser.parse_args([])
print(args.output)  # → None (not provided)
args = parser.parse_args(['--output'])
print(args.output)  # → 'default.txt' (flag without value)
args = parser.parse_args(['--output', 'file.txt'])
print(args.output)  # → 'file.txt' (flag with value)

# Zero or more arguments (*)
parser.add_argument('--extras', nargs='*')
args = parser.parse_args(['--extras'])
print(args.extras)  # → []
args = parser.parse_args(['--extras', 'a', 'b', 'c'])
print(args.extras)  # → ['a', 'b', 'c']

# One or more arguments (+)
parser.add_argument('files', nargs='+')
args = parser.parse_args(['file1.txt', 'file2.txt'])
print(args.files)  # → ['file1.txt', 'file2.txt']
# parser.parse_args([])  # Error: required

# REMAINDER (capture all remaining)
parser.add_argument('command')
parser.add_argument('args', nargs=argparse.REMAINDER)
args = parser.parse_args(['ls', '-la', '/tmp'])
print(args.command)  # → 'ls'
print(args.args)  # → ['-la', '/tmp']

# Practical example: optional input/output files
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                   default=sys.stdin)
parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                   default=sys.stdout)
```

### 6. SUBCOMMANDS (SUB-PARSERS)

```python
import argparse

# Create main parser
parser = argparse.ArgumentParser(prog='myapp')
parser.add_argument('--verbose', action='store_true')

# Add subparsers
subparsers = parser.add_subparsers(
    title='commands',
    description='available commands',
    dest='command',  # Stores which command was used
    required=True    # Require a subcommand (Python 3.7+)
)

# Create 'add' subcommand
add_parser = subparsers.add_parser('add', help='add a record')
add_parser.add_argument('name')
add_parser.add_argument('--age', type=int)

# Create 'delete' subcommand
del_parser = subparsers.add_parser('delete', help='delete a record')
del_parser.add_argument('id', type=int)

# Create 'list' subcommand with aliases
list_parser = subparsers.add_parser('list', aliases=['ls'], help='list records')
list_parser.add_argument('--format', choices=['table', 'json'])

# Parse
args = parser.parse_args(['add', 'John', '--age', '30'])
print(args.command)  # → 'add'
print(args.name)     # → 'John'
print(args.age)      # → 30

args = parser.parse_args(['ls', '--format', 'json'])
print(args.command)  # → 'list' (even though we used 'ls')

# Associating functions with subcommands
def add_func(args):
    print(f"Adding {args.name}, age {args.age}")

def delete_func(args):
    print(f"Deleting record {args.id}")

add_parser.set_defaults(func=add_func)
del_parser.set_defaults(func=delete_func)

args = parser.parse_args(['add', 'Jane', '--age', '25'])
args.func(args)  # → "Adding Jane, age 25"

# Deprecated subcommand (Python 3.13+)
old_parser = subparsers.add_parser('old-cmd', deprecated=True)
# Using it prints deprecation warning
```

### 7. ARGUMENT GROUPS

```python
import argparse

parser = argparse.ArgumentParser()

# Create groups for better organization
input_group = parser.add_argument_group('input options')
input_group.add_argument('-i', '--input', help='input file')
input_group.add_argument('--format', choices=['json', 'csv'])

output_group = parser.add_argument_group('output options')
output_group.add_argument('-o', '--output', help='output file')
output_group.add_argument('--compress', action='store_true')

# Mutually exclusive group
group = parser.add_mutually_exclusive_group()
group.add_argument('--verbose', action='store_true')
group.add_argument('--quiet', action='store_true')
# Can use --verbose OR --quiet, but not both

# Required mutually exclusive group
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--create', action='store_true')
group.add_argument('--delete', action='store_true')
# Must use either --create OR --delete

# Group with custom defaults
auth_group = parser.add_argument_group(
    'authentication',
    'authentication options'
)
auth_group.add_argument('--username')
auth_group.add_argument('--password')

# Nested groups (add exclusive to named group)
connection_group = parser.add_argument_group('connection options')
protocol_group = connection_group.add_mutually_exclusive_group()
protocol_group.add_argument('--http', action='store_true')
protocol_group.add_argument('--https', action='store_true')
```

### 8. PARSING AND NAMESPACE

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo')
parser.add_argument('--bar', type=int)
parser.add_argument('files', nargs='*')

# Parse sys.argv (default)
args = parser.parse_args()

# Parse custom argument list
args = parser.parse_args(['--foo', 'value', '--bar', '42', 'file.txt'])
print(args.foo)   # → 'value'
print(args.bar)   # → 42
print(args.files) # → ['file.txt']

# Access as dictionary
args_dict = vars(args)
print(args_dict)  # → {'foo': 'value', 'bar': 42, 'files': ['file.txt']}

# Parse into existing namespace
class Config:
    def __init__(self):
        self.foo = 'default'

config = Config()
parser.parse_args(['--bar', '99'], namespace=config)
print(config.foo)  # → 'default' (unchanged)
print(config.bar)  # → 99 (added)

# Parse known args (ignore unknown)
parser = argparse.ArgumentParser()
parser.add_argument('--foo')
args, unknown = parser.parse_known_args(['--foo', 'bar', '--unknown', 'baz'])
print(args.foo)  # → 'bar'
print(unknown)   # → ['--unknown', 'baz']

# Parse intermixed args (Python 3.7+)
parser = argparse.ArgumentParser()
parser.add_argument('--foo')
parser.add_argument('cmd')
parser.add_argument('rest', nargs='*')
args = parser.parse_intermixed_args(['cmd', 'a', '--foo', 'bar', 'b'])
print(args.cmd)   # → 'cmd'
print(args.foo)   # → 'bar'
print(args.rest)  # → ['a', 'b'] (collected positionals)

# Handle parse errors
parser = argparse.ArgumentParser(exit_on_error=False)
parser.add_argument('--num', type=int)
try:
    args = parser.parse_args(['--num', 'not-a-number'])
except argparse.ArgumentError as e:
    print(f"Parse error: {e}")
```

### 9. DEFAULTS AND SPECIAL VALUES

```python
import argparse

parser = argparse.ArgumentParser()

# Set parser-level defaults
parser.set_defaults(verbosity=0, color=True)
parser.add_argument('--verbose', dest='verbosity', action='count')

# Get default values
default_color = parser.get_default('color')
print(default_color)  # → True

# Argument-level defaults
parser.add_argument('--timeout', type=int, default=30)

# Default value interactions
parser = argparse.ArgumentParser()
parser.add_argument('--foo', default='parser_default')
parser.set_defaults(foo='set_default')  # Overwrites parser default
args = parser.parse_args([])
print(args.foo)  # → 'set_default' (last one wins)

# SUPPRESS - don't create attribute if not provided
parser = argparse.ArgumentParser()
parser.add_argument('--foo', default=argparse.SUPPRESS)
parser.add_argument('--bar', default='bar_default')
args = parser.parse_args([])
print(hasattr(args, 'foo'))  # → False (suppressed)
print(args.bar)              # → 'bar_default'

# Useful for overlaying config files
default_config = {'foo': 'config_value', 'bar': 'config_bar'}
parser = argparse.ArgumentParser()
parser.add_argument('--foo', default=argparse.SUPPRESS)
parser.add_argument('--bar', default=argparse.SUPPRESS)
args = parser.parse_args(['--foo', 'cli_value'])
# Merge: CLI args override config
final_config = {**default_config, **vars(args)}
print(final_config)  # → {'foo': 'cli_value', 'bar': 'config_bar'}

# Const vs default
parser = argparse.ArgumentParser()
parser.add_argument('--flag', nargs='?', const='const_val', default='default_val')
args = parser.parse_args([])
print(args.flag)  # → 'default_val' (nothing provided)
args = parser.parse_args(['--flag'])
print(args.flag)  # → 'const_val' (flag without value)
args = parser.parse_args(['--flag', 'explicit'])
print(args.flag)  # → 'explicit' (flag with value)
```

### 10. HELP AND USAGE CUSTOMIZATION

```python
import argparse

# Custom help text
parser = argparse.ArgumentParser(
    prog='myapp',
    description='A tool for processing data files',
    epilog='For more info, visit https://example.com',
    formatter_class=argparse.RawDescriptionHelpFormatter
)

# Disable help
parser = argparse.ArgumentParser(add_help=False)
# Now -h/--help won't be added automatically

# Custom help flags
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-?', '--help', action='help', help='show this help')

# Help with format specifiers
parser = argparse.ArgumentParser(prog='myapp')
parser.add_argument('--count', type=int, default=10,
                   help='number of items (default: %(default)s)')
parser.add_argument('--type', type=str, default='auto',
                   help='type to use, must be %(type)s')

# Hide argument from help
parser.add_argument('--secret', help=argparse.SUPPRESS)

# Print help programmatically
parser.print_help()

# Get help as string
help_text = parser.format_help()
print(help_text)

# Print just usage
parser.print_usage()

# Get usage as string
usage = parser.format_usage()

# Custom usage message
parser = argparse.ArgumentParser(
    usage='%(prog)s [--verbose] input output\n'
          '       %(prog)s --version'
)

# Multiple metavar for nargs
parser.add_argument('-c', '--coords', nargs=2, metavar=('X', 'Y'))
# Shows: -c X Y  instead of  -c COORDS COORDS

# Format help in different ways
# RawDescriptionHelpFormatter - preserve description whitespace
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''
    Instructions:
      1. First step
      2. Second step
    '''
)

# ArgumentDefaultsHelpFormatter - show defaults
parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument('--count', type=int, default=10)
# Help shows: --count COUNT  number of items (default: 10)

# MetavarTypeHelpFormatter - use type as metavar
parser = argparse.ArgumentParser(
    formatter_class=argparse.MetavarTypeHelpFormatter
)
parser.add_argument('--count', type=int)
# Help shows: --count int  instead of  --count COUNT
```

---

## PRACTICAL PROJECT PATTERNS

### Pattern 1: Simple CLI Tool
```python
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        description='File processor utility',
        epilog='Example: %(prog)s input.txt -o output.txt'
    )
    
    parser.add_argument('input', help='input file to process')
    parser.add_argument('-o', '--output', help='output file (default: stdout)')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='verbose output')
    parser.add_argument('--format', choices=['json', 'xml', 'csv'],
                       default='json', help='output format')
    
    args = parser.parse_args()
    
    # Use arguments
    if args.verbose:
        print(f"Processing {args.input}...")
    
    # Process file
    with open(args.input) as f:
        data = f.read()
    
    # Handle output
    output = sys.stdout if args.output is None else open(args.output, 'w')
    output.write(f"Formatted as {args.format}: {data}\n")
    if args.output:
        output.close()

if __name__ == '__main__':
    main()
```

### Pattern 2: Multi-Command Application
```python
import argparse

def cmd_create(args):
    print(f"Creating {args.name} of type {args.type}")

def cmd_delete(args):
    print(f"Deleting {args.name}")
    if args.force:
        print("Forcing deletion")

def cmd_list(args):
    print(f"Listing items (format: {args.format})")

def main():
    parser = argparse.ArgumentParser(prog='myapp')
    parser.add_argument('-v', '--verbose', action='count', default=0)
    
    subparsers = parser.add_subparsers(dest='command', required=True)
    
    # Create command
    create_parser = subparsers.add_parser('create', help='create item')
    create_parser.add_argument('name')
    create_parser.add_argument('--type', default='default')
    create_parser.set_defaults(func=cmd_create)
    
    # Delete command
    delete_parser = subparsers.add_parser('delete', help='delete item')
    delete_parser.add_argument('name')
    delete_parser.add_argument('-f', '--force', action='store_true')
    delete_parser.set_defaults(func=cmd_delete)
    
    # List command
    list_parser = subparsers.add_parser('list', aliases=['ls'], help='list items')
    list_parser.add_argument('--format', choices=['table', 'json'], default='table')
    list_parser.set_defaults(func=cmd_list)
    
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
```

### Pattern 3: Configuration File + CLI Override
```python
import argparse
import json
from pathlib import Path

def load_config(config_file):
    """Load configuration from file"""
    if config_file and Path(config_file).exists():
        with open(config_file) as f:
            return json.load(f)
    return {}

def main():
    # First pass: get config file
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument('-c', '--config', help='config file')
    pre_args, remaining = pre_parser.parse_known_args()
    
    # Load config
    config = load_config(pre_args.config)
    
    # Main parser with defaults from config
    parser = argparse.ArgumentParser(
        parents=[pre_parser],
        description='Tool with config file support'
    )
    
    parser.add_argument('--host', default=config.get('host', 'localhost'))
    parser.add_argument('--port', type=int, default=config.get('port', 8080))
    parser.add_argument('--timeout', type=int, default=config.get('timeout', 30))
    parser.add_argument('--verbose', action='store_true',
                       default=config.get('verbose', False))
    
    args = parser.parse_args(remaining)
    
    print(f"Connecting to {args.host}:{args.port}")
    print(f"Timeout: {args.timeout}s")
    if args.verbose:
        print("Verbose mode enabled")

if __name__ == '__main__':
    main()
```

### Pattern 4: Grouped Arguments with Validation
```python
import argparse
import sys

def validate_args(args):
    """Custom validation across multiple arguments"""
    if args.ssl and not args.cert:
        return "SSL enabled but no certificate provided"
    if args.parallel < 1 or args.parallel > 16:
        return "Parallel workers must be between 1 and 16"
    return None

def main():
    parser = argparse.ArgumentParser()
    
    # Connection group
    conn_group = parser.add_argument_group('connection options')
    conn_group.add_argument('--host', required=True)
    conn_group.add_argument('--port', type=int, default=443)
    conn_group.add_argument('--timeout', type=int, default=30)
    
    # Security group
    sec_group = parser.add_argument_group('security options')
    sec_group.add_argument('--ssl', action='store_true')
    sec_group.add_argument('--cert', help='SSL certificate file')
    sec_group.add_argument('--key', help='SSL key file')
    
    # Performance group
    perf_group = parser.add_argument_group('performance options')
    perf_group.add_argument('--parallel', type=int, default=4,
                           help='number of parallel workers')
    perf_group.add_argument('--buffer-size', type=int, default=8192,
                           help='buffer size in bytes')
    
    # Mutually exclusive output
    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument('--json', action='store_true')
    output_group.add_argument('--xml', action='store_true')
    
    args = parser.parse_args()
    
    # Validate
    error = validate_args(args)
    if error:
        parser.error(error)
    
    print(f"Connecting to {args.host}:{args.port}")

if __name__ == '__main__':
    main()
```

### Pattern 5: Custom Action for Complex Logic
```python
import argparse

class RangeAction(argparse.Action):
    """Custom action to parse range like 1-10"""
    def __call__(self, parser, namespace, values, option_string=None):
        if '-' in values:
            start, end = values.split('-')
            value_range = range(int(start), int(end) + 1)
        else:
            value_range = [int(values)]
        setattr(namespace, self.dest, list(value_range))

class KeyValueAction(argparse.Action):
    """Custom action to parse key=value pairs"""
    def __call__(self, parser, namespace, values, option_string=None):
        if not hasattr(namespace, self.dest) or getattr(namespace, self.dest) is None:
            setattr(namespace, self.dest, {})
        k, v = values.split('=', 1)
        getattr(namespace, self.dest)[k] = v

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--pages', action=RangeAction,
                       help='page range like 1-5')
    parser.add_argument('-D', '--define', action=KeyValueAction,
                       help='define variable (key=value)')
    
    args = parser.parse_args(['--pages', '1-3', '-D', 'mode=debug', '-D', 'level=5'])
    
    print(args.pages)   # → [1, 2, 3]
    print(args.define)  # → {'mode': 'debug', 'level': '5'}

if __name__ == '__main__':
    main()
```

### Pattern 6: Argument File Support
```python
import argparse

class CustomArgumentParser(argparse.ArgumentParser):
    """Parser with custom file parsing"""
    def convert_arg_line_to_args(self, arg_line):
        # Skip comments and empty lines
        arg_line = arg_line.strip()
        if not arg_line or arg_line.startswith('#'):
            return []
        # Split on spaces, handling quotes
        import shlex
        return shlex.split(arg_line)

def main():
    parser = CustomArgumentParser(
        fromfile_prefix_chars='@',
        description='Tool with argument file support'
    )
    
    parser.add_argument('--input')
    parser.add_argument('--output')
    parser.add_argument('--verbose', action='store_true')
    
    # Create args.txt:
    # --input input.txt
    # --output output.txt
    # --verbose
    
    # Then use: python script.py @args.txt
    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()
```

---

## COMMON ERRORS & SOLUTIONS

### Error 1: Positional Arguments After Optional
```python
# WRONG - positional after optional with nargs='*'
parser = argparse.ArgumentParser()
parser.add_argument('--files', nargs='*')
parser.add_argument('output')  # Ambiguous!

# RIGHT - use nargs='+' and careful ordering
parser = argparse.ArgumentParser()
parser.add_argument('files', nargs='+')
parser.add_argument('--output')  # Optional after positional
```

### Error 2: Type Conversion Errors
```python
# WRONG - no error handling
parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int)
# Crashes with poor message if non-integer provided

# RIGHT - custom type with validation
def port_type(string):
    try:
        port = int(string)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{string}' is not a valid integer")
    
    if not (1 <= port <= 65535):
        raise argparse.ArgumentTypeError(f"port must be 1-65535, got {port}")
    return port

parser.add_argument('--port', type=port_type)
```

### Error 3: Required Optional Arguments
```python
# WRONG - defeats purpose of "optional"
parser = argparse.ArgumentParser()
parser.add_argument('--required-option', required=True)

# RIGHT - use positional or rethink design
parser.add_argument('required_arg')  # Positional

# OR - use subcommands if it's context-dependent
subparser.add_argument('--option', required=True)  # OK in subparser
```

### Error 4: Mutually Exclusive with Required
```python
# WRONG - doesn't work as expected
group = parser.add_mutually_exclusive_group()
group.add_argument('--foo', required=True)  # Doesn't enforce mutual exclusion
group.add_argument('--bar', required=True)

# RIGHT - make the group required
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--foo', action='store_true')
group.add_argument('--bar', action='store_true')
```

### Error 5: Namespace Attribute Conflicts
```python
# WRONG - dest conflicts with Python keywords or methods
parser.add_argument('--class', dest='class')  # 'class' is a keyword

# RIGHT - use valid Python identifiers
parser.add_argument('--class', dest='class_name')
parser.add_argument('--type', dest='type_name')
```

### Error 6: Default Value Type Mismatch
```python
# WRONG - default doesn't match type
parser.add_argument('--count', type=int, default='ten')  # String default!

# RIGHT - match types
parser.add_argument('--count', type=int, default=10)
```

---

## PERFORMANCE TIPS

1. **Lazy Imports in Subcommands**
   ```python
   def cmd_heavy_operation(args):
       import expensive_module  # Import only when needed
       expensive_module.process(args)
   ```

2. **Use `exit_on_error=False` for Testing**
   ```python
   parser = argparse.ArgumentParser(exit_on_error=False)
   # Now you can catch ArgumentError instead of sys.exit
   ```

3. **Disable Abbreviations for Speed**
   ```python
   # Abbreviation checking can be slow with many options
   parser = argparse.ArgumentParser(allow_abbrev=False)
   ```

4. **Reuse Parent Parsers**
   ```python
   # Share common arguments across multiple parsers
   common = argparse.ArgumentParser(add_help=False)
   common.add_argument('--verbose', action='store_true')
   
   parser1 = argparse.ArgumentParser(parents=[common])
   parser2 = argparse.ArgumentParser(parents=[common])
   ```

5. **Avoid FileType for Large Projects**
   ```python
   # SLOW - opens files during parsing
   parser.add_argument('input', type=argparse.FileType('r'))
   
   # FAST - validate path, open later
   parser.add_argument('input', type=pathlib.Path)
   # Then open in your code when needed
   ```

---

## ADVANCED FEATURES

### Custom Formatters
```python
class CustomHelpFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings:
            return super()._format_action_invocation(action)
        # Custom formatting for options
        return ', '.join(action.option_strings)

parser = argparse.ArgumentParser(formatter_class=CustomHelpFormatter)
```

### Argument Prefixes
```python
# Windows-style /options
parser = argparse.ArgumentParser(prefix_chars='/-')
parser.add_argument('/o', '--output')
parser.add_argument('-v', '--verbose', action='store_true')
# Now both /o and -o work
```

### Registering Custom Types
```python
def hexadecimal(string):
    return int(string, 16)

parser.register('type', 'hex', hexadecimal)
parser.add_argument('--addr', type='hex')
args = parser.parse_args(['--addr', '0xFF'])
print(args.addr)  # → 255
```

### Intermixed Parsing
```python
# Collect options anywhere among positionals
parser = argparse.ArgumentParser()
parser.add_argument('--opt')
parser.add_argument('files', nargs='*')

# Standard parse_args
args = parser.parse_args(['file1', '--opt', 'value', 'file2'])
print(args.files)  # → ['file1'] (stops at first option)

# Intermixed
args = parser.parse_intermixed_args(['file1', '--opt', 'value', 'file2'])
print(args.files)  # → ['file1', 'file2'] (collects all positionals)
```

---

## WHEN TO USE ARGPARSE

### ✅ Use argparse When:
- **Building command-line tools** (scripts, utilities)
- **Need automatic help generation** (--help)
- **Want standard Unix conventions** (- for options)
- **Simple to moderate complexity** (most CLI tools)
- **Part of standard library** (no dependencies)
- **Need subcommands** (like git, pip)
- **Type conversion and validation** needed

### ❌ Consider Alternatives When:
- **Very complex CLI applications** (try Click, Typer)
- **Want automatic shell completion** (Click, argcomplete)
- **Need advanced features** (Click has more)
- **Interactive prompts** (Click, questionary)
- **Strict validation** (Click has better support)
- **Modern CLI UX** (Rich, Typer for better output)

---

## SUMMARY CHEAT SHEET

```python
import argparse

# Create parser
parser = argparse.ArgumentParser(description='My tool')

# Positional argument
parser.add_argument('file')

# Optional argument
parser.add_argument('-o', '--output')

# Flag (boolean)
parser.add_argument('-v', '--verbose', action='store_true')

# Type conversion
parser.add_argument('-n', '--number', type=int)

# Choices
parser.add_argument('--format', choices=['json', 'xml'])

# Multiple values
parser.add_argument('files', nargs='+')

# With default
parser.add_argument('--timeout', type=int, default=30)

# Required optional
parser.add_argument('--required', required=True)

# Parse
args = parser.parse_args()

# Access
print(args.file, args.verbose, args.number)

# Subcommands
subparsers = parser.add_subparsers(dest='command')
sub = subparsers.add_parser('subcmd')
sub.add_argument('--opt')

# Mutually exclusive
group = parser.add_mutually_exclusive_group()
group.add_argument('--opt1', action='store_true')
group.add_argument('--opt2', action='store_true')
```

---

## REFERENCES & RESOURCES

- **Official Documentation**: https://docs.python.org/3/library/argparse.html
- **Tutorial**: https://docs.python.org/3/howto/argparse.html
- **PEP 389**: argparse - New Command Line Parsing Module
- **Related Modules**: `sys.argv`, `getopt`, `optparse` (deprecated)
- **Modern Alternatives**: Click, Typer, Fire, Clize
- **Common Use Cases**: CLI tools, scripts, automation, DevOps tools
