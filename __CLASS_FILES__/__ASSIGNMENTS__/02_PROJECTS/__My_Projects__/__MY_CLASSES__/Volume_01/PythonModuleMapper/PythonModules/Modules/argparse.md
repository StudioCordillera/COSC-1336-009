---
type: module
name: argparse
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\argparse.py
is_package: False
analyzed_at: 2025-12-10T03:46:17.566220
tags:
  - python
  - module
---

# Module: argparse

## Overview

Command-line parsing library

This module is an optparse-inspired command-line parsing library that:

    - handles both optional and positional arguments
    - produces highly informative usage messages
    - supports parsers that dispatch to sub-parsers

The following is a simple usage example that sums integers from the
command-line and writes the result to a file::

    parser = argparse.ArgumentParser(
        description='sum the integers at the command line')
    parser.add_argument(
        'integers', metavar='int', nargs='+', type=int,
        help='an integer to be summed')
    parser.add_argument(
        '--log', default=sys.stdout, type=argparse.FileType('w'),
        help='the file where the sum should be written')
    args = parser.parse_args()
    args.log.write('%s' % sum(args.integers))
    args.log.close()

The module contains the following public classes:

    - ArgumentParser -- The main entry point for command-line parsing. As the
        example above shows, the add_argument() method is used to populate
        the parser with actions for optional and positional arguments. Then
        the parse_args() method is invoked to convert the args at the
        command-line into an object with attributes.

    - ArgumentError -- The exception raised by ArgumentParser objects when
        there are errors with the parser's actions. Errors raised while
        parsing the command-line are caught by ArgumentParser and emitted
        as command-line messages.

    - FileType -- A factory for defining types of files to be created. As the
        example above shows, instances of FileType are typically passed as
        the type= argument of add_argument() calls.

    - Action -- The base class for parser actions. Typically actions are
        selected by passing strings like 'store_true' or 'append_const' to
        the action= argument of add_argument(). However, for greater
        customization of ArgumentParser actions, subclasses of Action may
        be defined and passed as the action= argument.

    - HelpFormatter, RawDescriptionHelpFormatter, RawTextHelpFormatter,
        ArgumentDefaultsHelpFormatter -- Formatter classes which
        may be passed as the formatter_class= argument to the
        ArgumentParser constructor. HelpFormatter is the default,
        RawDescriptionHelpFormatter and RawTextHelpFormatter tell the parser
        not to change the formatting for help text, and
        ArgumentDefaultsHelpFormatter adds information about argument defaults
        to the help.

All other classes in this module are considered implementation details.
(Also note that HelpFormatter and RawDescriptionHelpFormatter are only
considered public as object names -- the API of the formatter objects is
still considered an implementation detail.)

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\argparse.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:17

## Dependencies

This module imports:
- [[Modules/textwrap|textwrap]]
- [[Modules/re|re]]
- [[Modules/os|os]]
- [[Modules/shutil|shutil]]
- [[Modules/copy|copy]]

## Used By

This module is imported by:
- [[Modules/webbrowser|webbrowser]]
- [[Modules/uuid|uuid]]
- [[Modules/doctest|doctest]]
- [[Modules/pdb|pdb]]
- [[Modules/trace|trace]]
- [[Modules/ensurepip|ensurepip]]
- [[Modules/venv|venv]]
- [[Modules/zipapp|zipapp]]
- [[Modules/inspect|inspect]]
- [[Modules/code|code]]
- [[Modules/ast|ast]]
- [[Modules/tokenize|tokenize]]
- [[Modules/py_compile|py_compile]]
- [[Modules/compileall|compileall]]
- [[Modules/dis|dis]]
- [[Modules/pickletools|pickletools]]

## Classes

- [[Classes/_AttributeHolder|_AttributeHolder]] (line 107)
- [[Classes/HelpFormatter|HelpFormatter]] (line 155)
- [[Classes/RawDescriptionHelpFormatter|RawDescriptionHelpFormatter]] (line 638)
- [[Classes/RawTextHelpFormatter|RawTextHelpFormatter]] (line 649)
- [[Classes/ArgumentDefaultsHelpFormatter|ArgumentDefaultsHelpFormatter]] (line 660)
- [[Classes/MetavarTypeHelpFormatter|MetavarTypeHelpFormatter]] (line 681)
- [[Classes/ArgumentError|ArgumentError]] (line 723)
- [[Classes/ArgumentTypeError|ArgumentTypeError]] (line 743)
- [[Classes/Action|Action]] (line 752)
- [[Classes/BooleanOptionalAction|BooleanOptionalAction]] (line 853)
- [[Classes/_StoreAction|_StoreAction]] (line 913)
- [[Classes/_StoreConstAction|_StoreConstAction]] (line 950)
- [[Classes/_StoreTrueAction|_StoreTrueAction]] (line 975)
- [[Classes/_StoreFalseAction|_StoreFalseAction]] (line 994)
- [[Classes/_AppendAction|_AppendAction]] (line 1013)
- [[Classes/_AppendConstAction|_AppendConstAction]] (line 1053)
- [[Classes/_CountAction|_CountAction]] (line 1082)
- [[Classes/_HelpAction|_HelpAction]] (line 1107)
- [[Classes/_VersionAction|_VersionAction]] (line 1128)
- [[Classes/_SubParsersAction|_SubParsersAction]] (line 1157)
- [[Classes/_ExtendAction|_ExtendAction]] (line 1267)
- [[Classes/FileType|FileType]] (line 1278)
- [[Classes/Namespace|Namespace]] (line 1333)
- [[Classes/_ActionsContainer|_ActionsContainer]] (line 1353)
- [[Classes/_ArgumentGroup|_ArgumentGroup]] (line 1671)
- [[Classes/_MutuallyExclusiveGroup|_MutuallyExclusiveGroup]] (line 1714)
- [[Classes/ArgumentParser|ArgumentParser]] (line 1743)

## Functions

- [[Functions/__2080|_()]] (line 627)
- [[Functions/ngettext_2081|ngettext()]] (line 631)
- [[Functions/_copy_items_2085|_copy_items()]] (line 138)
- [[Functions/_get_action_name_2118|_get_action_name()]] (line 700)
