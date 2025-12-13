---
type: module
name: difflib
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\difflib.py
is_package: False
analyzed_at: 2025-12-10T03:46:12.539435
tags:
  - python
  - module
---

# Module: difflib

## Overview

Module difflib -- helpers for computing deltas between objects.

Function get_close_matches(word, possibilities, n=3, cutoff=0.6):
    Use SequenceMatcher to return list of the best "good enough" matches.

Function context_diff(a, b):
    For two lists of strings, return a delta in context diff format.

Function ndiff(a, b):
    Return a delta: the difference between `a` and `b` (lists of strings).

Function restore(delta, which):
    Return one of the two sequences that generated an ndiff delta.

Function unified_diff(a, b):
    For two lists of strings, return a delta in unified diff format.

Class SequenceMatcher:
    A flexible class for comparing pairs of sequences of any type.

Class Differ:
    For producing human-readable deltas from sequences of lines of text.

Class HtmlDiff:
    For producing HTML side by side comparison with change highlights.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\difflib.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:12

## Dependencies

This module imports:
- [[Modules/re|re]]
- [[Modules/difflib|difflib]]

## Used By

This module is imported by:
- [[Modules/difflib|difflib]]
- [[Modules/doctest|doctest]]

## Classes

- [[Classes/SequenceMatcher|SequenceMatcher]] (line 44)
- [[Classes/Differ|Differ]] (line 724)
- [[Classes/HtmlDiff|HtmlDiff]] (line 1666)

## Functions

- [[Functions/_nlargest_55|_nlargest()]] (line 523)
- [[Functions/_namedtuple_56|_namedtuple()]] (line 358)
- [[Functions/_calculate_ratio_57|_calculate_ratio()]] (line 39)
- [[Functions/get_close_matches_70|get_close_matches()]] (line 666)
- [[Functions/_keep_original_ws_71|_keep_original_ws()]] (line 715)
- [[Functions/IS_LINE_JUNK_79|IS_LINE_JUNK()]] (line 1045)
- [[Functions/IS_CHARACTER_JUNK_80|IS_CHARACTER_JUNK()]] (line 1061)
- [[Functions/_format_range_unified_81|_format_range_unified()]] (line 1084)
- [[Functions/unified_diff_82|unified_diff()]] (line 1095)
- [[Functions/_format_range_context_83|_format_range_context()]] (line 1168)
- [[Functions/context_diff_84|context_diff()]] (line 1180)
- [[Functions/_check_types_85|_check_types()]] (line 1256)
- [[Functions/diff_bytes_86|diff_bytes()]] (line 1273)
- [[Functions/ndiff_87|ndiff()]] (line 1303)
- [[Functions/_mdiff_88|_mdiff()]] (line 1340)
- [[Functions/restore_99|restore()]] (line 2019)
- [[Functions/_test_100|_test()]] (line 2051)
