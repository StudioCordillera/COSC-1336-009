---
type: module
name: pdb
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\pdb.py
is_package: False
analyzed_at: 2025-12-10T03:46:25.029727
tags:
  - python
  - module
---

# Module: pdb

## Overview

The Python Debugger Pdb
=======================

To use the debugger in its simplest form:

        >>> import pdb
        >>> pdb.run('<a statement>')

The debugger's prompt is '(Pdb) '.  This will stop in the first
function call in <a statement>.

Alternatively, if a statement terminated with an unhandled exception,
you can use pdb's post-mortem facility to inspect the contents of the
traceback:

        >>> <a statement>
        <exception traceback>
        >>> import pdb
        >>> pdb.pm()

The commands recognized by the debugger are listed in the next
section.  Most can be abbreviated as indicated; e.g., h(elp) means
that 'help' can be typed as 'h' or 'help' (but not as 'he' or 'hel',
nor as 'H' or 'Help' or 'HELP').  Optional arguments are enclosed in
square brackets.  Alternatives in the command syntax are separated
by a vertical bar (|).

A blank line repeats the previous command literally, except for
'list', where it lists the next 11 lines.

Commands that the debugger doesn't recognize are assumed to be Python
statements and are executed in the context of the program being
debugged.  Python statements can also be prefixed with an exclamation
point ('!').  This is a powerful way to inspect the program being
debugged; it is even possible to change variables or call functions.
When an exception occurs in such a statement, the exception name is
printed but the debugger's state is not changed.

The debugger supports aliases, which can save typing.  And aliases can
have parameters (see the alias help entry) which allows one a certain
level of adaptability to the context under examination.

Multiple commands may be entered on a single line, separated by the
pair ';;'.  No intelligence is applied to separating the commands; the
input is split at the first ';;', even if it is in the middle of a
quoted string.

If a file ".pdbrc" exists in your home directory or in the current
directory, it is read in and executed as if it had been typed at the
debugger prompt.  This is particularly useful for aliases.  If both
files exist, the one in the home directory is read first and aliases
defined there can be overridden by the local file.  This behavior can be
disabled by passing the "readrc=False" argument to the Pdb constructor.

Aside from aliases, the debugger is not directly programmable; but it
is implemented as a class from which you can derive your own debugger
class, which you can make as fancy as you like.


Debugger commands
=================

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\pdb.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:25

## Dependencies

This module imports:
- [[Modules/bdb|bdb]]
- [[Modules/pprint|pprint]]
- [[Modules/io|io]]
- [[Modules/types|types]]
- [[Modules/pydoc|pydoc]]
- [[Modules/argparse|argparse]]
- [[Modules/textwrap|textwrap]]
- [[Modules/cmd|cmd]]
- [[Modules/itertools|itertools]]
- [[Modules/signal|signal]]
- [[Modules/glob|glob]]
- [[Modules/linecache|linecache]]
- [[Modules/re|re]]
- [[Modules/os|os]]
- [[Modules/shlex|shlex]]
- [[Modules/pdb|pdb]]

## Used By

This module is imported by:
- [[Modules/pdb|pdb]]

## Classes

- [[Classes/Restart|Restart]] (line 97)
- [[Classes/_rstr|_rstr]] (line 162)
- [[Classes/_ExecutableTarget|_ExecutableTarget]] (line 168)
- [[Classes/_ScriptTarget|_ScriptTarget]] (line 174)
- [[Classes/_ModuleTarget|_ModuleTarget]] (line 213)
- [[Classes/_ZipTarget|_ZipTarget]] (line 250)
- [[Classes/_PdbInteractiveConsole|_PdbInteractiveConsole]] (line 288)
- [[Classes/Pdb|Pdb]] (line 306)

## Functions

- [[Functions/contextmanager_5152|contextmanager()]] (line 276)
- [[Functions/find_first_executable_line_5153|find_first_executable_line()]] (line 105)
- [[Functions/find_function_5154|find_function()]] (line 122)
- [[Functions/lasti2lineno_5155|lasti2lineno()]] (line 153)
- [[Functions/run_5266|run()]] (line 2298)
- [[Functions/runeval_5267|runeval()]] (line 2313)
- [[Functions/runctx_5268|runctx()]] (line 2322)
- [[Functions/runcall_5269|runcall()]] (line 2326)
- [[Functions/set_trace_5270|set_trace()]] (line 2336)
- [[Functions/post_mortem_5271|post_mortem()]] (line 2351)
- [[Functions/_post_mortem_5272|_post_mortem()]] (line 2365)
- [[Functions/pm_5273|pm()]] (line 2384)
- [[Functions/test_5274|test()]] (line 2393)
- [[Functions/help_5275|help()]] (line 2397)
- [[Functions/main_5276|main()]] (line 2415)
