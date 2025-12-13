---
type: module
name: fnmatch
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\fnmatch.py
is_package: False
analyzed_at: 2025-12-10T03:46:15.509130
tags:
  - python
  - module
---

# Module: fnmatch

## Overview

Filename matching with shell patterns.

fnmatch(FILENAME, PATTERN) matches according to the local convention.
fnmatchcase(FILENAME, PATTERN) always takes case in account.

The functions operate by translating the pattern into a regular
expression.  They cache the compiled regular expressions for speed.

The function translate(PATTERN) returns a regular expression
corresponding to PATTERN.  (It does not compile it.)

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\fnmatch.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:15

## Dependencies

This module imports:
- [[Modules/re|re]]
- [[Modules/functools|functools]]

## Used By

This module is imported by:
- [[Modules/shutil|shutil]]
- [[Modules/bdb|bdb]]
- [[Modules/tracemalloc|tracemalloc]]

## Functions

- [[Functions/fnmatch_1297|fnmatch()]] (line 19)
- [[Functions/_compile_pattern_1298|_compile_pattern()]] (line 39)
- [[Functions/filter_1299|filter()]] (line 48)
- [[Functions/fnmatchcase_1300|fnmatchcase()]] (line 64)
- [[Functions/translate_1301|translate()]] (line 74)
- [[Functions/_translate_1302|_translate()]] (line 85)
- [[Functions/_join_translated_parts_1303|_join_translated_parts()]] (line 157)
