---
type: module
name: pprint
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\pprint.py
is_package: False
analyzed_at: 2025-12-10T03:46:13.845044
tags:
  - python
  - module
---

# Module: pprint

## Overview

Support to pretty-print lists, tuples, & dictionaries recursively.

Very simple, but useful, especially in debugging data structures.

Classes
-------

PrettyPrinter()
    Handle pretty-printing operations onto a stream using a configured
    set of formatting parameters.

Functions
---------

pformat()
    Format a Python object into a pretty-printed representation.

pprint()
    Pretty-print a Python object to a stream [default is sys.stdout].

saferepr()
    Generate a 'standard' repr()-like value, but protect against recursive
    data structures.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\pprint.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:13

## Dependencies

This module imports:
- [[Modules/re|re]]
- [[Modules/types|types]]
- [[Modules/collections|collections]]

## Used By

This module is imported by:
- [[Modules/pickle|pickle]]
- [[Modules/pdb|pdb]]

## Classes

- [[Classes/_safe_key|_safe_key]] (line 80)
- [[Classes/PrettyPrinter|PrettyPrinter]] (line 106)

## Functions

- [[Functions/pprint_553|pprint()]] (line 48)
- [[Functions/pformat_554|pformat()]] (line 57)
- [[Functions/pp_555|pp()]] (line 64)
- [[Functions/saferepr_556|saferepr()]] (line 68)
- [[Functions/isreadable_557|isreadable()]] (line 72)
- [[Functions/isrecursive_558|isrecursive()]] (line 76)
- [[Functions/_safe_tuple_561|_safe_tuple()]] (line 102)
- [[Functions/_recursion_592|_recursion()]] (line 638)
- [[Functions/_wrap_bytes_repr_593|_wrap_bytes_repr()]] (line 643)
