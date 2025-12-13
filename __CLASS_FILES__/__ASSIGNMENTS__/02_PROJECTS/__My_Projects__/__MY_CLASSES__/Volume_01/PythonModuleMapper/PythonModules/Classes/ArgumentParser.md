---
type: class
name: ArgumentParser
module: argparse
lineno: 1743
tags:
  - python
  - class
---

# Class: ArgumentParser

## Overview

Object for parsing command line strings into Python objects.

Keyword Arguments:
    - prog -- The name of the program (default:
        ``os.path.basename(sys.argv[0])``)
    - usage -- A usage message (default: auto-generated from arguments)
    - description -- A description of what the program does
    - epilog -- Text following the argument descriptions
    - parents -- Parsers whose arguments should be copied into this one
    - formatter_class -- HelpFormatter class for printing help messages
    - prefix_chars -- Characters that prefix optional arguments
    - fromfile_prefix_chars -- Characters that prefix files containing
        additional arguments
    - argument_default -- The default value for all arguments
    - conflict_handler -- String indicating how to handle conflicts
    - add_help -- Add a -h/-help option
    - allow_abbrev -- Allow long options to be abbreviated unambiguously
    - exit_on_error -- Determines whether or not ArgumentParser exits with
        error info when an error occurs

**Module:** [[Modules/argparse|argparse]]
**Line:** 1743

## Inheritance

**Inherits from:**
- [[Classes/_AttributeHolder|_AttributeHolder]]
- [[Classes/_ActionsContainer|_ActionsContainer]]

## Methods

### Constructors
- [[Functions/__init___2181|__init__()]] (line 1765)

### Methods
- [[Functions/_get_kwargs_2182|_get_kwargs()]] (line 1830)
- [[Functions/add_subparsers_2183|add_subparsers()]] (line 1845)
- [[Functions/_add_action_2184|_add_action()]] (line 1876)
- [[Functions/_get_optional_actions_2185|_get_optional_actions()]] (line 1883)
- [[Functions/_get_positional_actions_2186|_get_positional_actions()]] (line 1888)
- [[Functions/parse_args_2187|parse_args()]] (line 1897)
- [[Functions/parse_known_args_2188|parse_known_args()]] (line 1907)
- [[Functions/_parse_known_args2_2189|_parse_known_args2()]] (line 1910)
- [[Functions/_parse_known_args_2190|_parse_known_args()]] (line 1948)
- [[Functions/_read_args_from_files_2191|_read_args_from_files()]] (line 2255)
- [[Functions/convert_arg_line_to_args_2192|convert_arg_line_to_args()]] (line 2282)
- [[Functions/_match_argument_2193|_match_argument()]] (line 2285)
- [[Functions/_match_arguments_partial_2194|_match_arguments_partial()]] (line 2307)
- [[Functions/_parse_optional_2195|_parse_optional()]] (line 2324)
- [[Functions/_get_option_tuples_2196|_get_option_tuples()]] (line 2370)
- [[Functions/_get_nargs_pattern_2197|_get_nargs_pattern()]] (line 2414)
- [[Functions/parse_intermixed_args_2198|parse_intermixed_args()]] (line 2460)
- [[Functions/parse_known_intermixed_args_2199|parse_known_intermixed_args()]] (line 2470)
- [[Functions/_get_values_2200|_get_values()]] (line 2492)
- [[Functions/_get_value_2201|_get_value()]] (line 2543)
- [[Functions/_check_value_2202|_check_value()]] (line 2568)
- [[Functions/format_usage_2203|format_usage()]] (line 2584)
- [[Functions/format_help_2204|format_help()]] (line 2590)
- [[Functions/_get_formatter_2205|_get_formatter()]] (line 2613)
- [[Functions/print_usage_2206|print_usage()]] (line 2620)
- [[Functions/print_help_2207|print_help()]] (line 2625)
- [[Functions/_print_message_2208|_print_message()]] (line 2630)
- [[Functions/exit_2209|exit()]] (line 2642)
- [[Functions/error_2210|error()]] (line 2647)
- [[Functions/_warning_2211|_warning()]] (line 2660)
