---
type: class
name: dircmp
module: filecmp
lineno: 88
tags:
  - python
  - class
---

# Class: dircmp

## Overview

A class that manages the comparison of 2 directories.

dircmp(a, b, ignore=None, hide=None, *, shallow=True)
  A and B are directories.
  IGNORE is a list of names to ignore,
    defaults to DEFAULT_IGNORES.
  HIDE is a list of names to hide,
    defaults to [os.curdir, os.pardir].
  SHALLOW specifies whether to just check the stat signature (do not read
    the files).
    defaults to True.

High level usage:
  x = dircmp(dir1, dir2)
  x.report() -> prints a report on the differences between dir1 and dir2
   or
  x.report_partial_closure() -> prints report on differences between dir1
        and dir2, and reports on common immediate subdirectories.
  x.report_full_closure() -> like report_partial_closure,
        but fully recursive.

Attributes:
 left_list, right_list: The files in dir1 and dir2,
    filtered by hide and ignore.
 common: a list of names in both dir1 and dir2.
 left_only, right_only: names only in dir1, dir2.
 common_dirs: subdirectories in both dir1 and dir2.
 common_files: files in both dir1 and dir2.
 common_funny: names in both dir1 and dir2 where the type differs between
    dir1 and dir2, or the name is not stat-able.
 same_files: list of identical files.
 diff_files: list of filenames which differ.
 funny_files: list of files which could not be compared.
 subdirs: a dictionary of dircmp instances (or MyDirCmp instances if this
   object is of type MyDirCmp, a subclass of dircmp), keyed by names
   in common_dirs.
 

**Module:** [[Modules/filecmp|filecmp]]
**Line:** 88

## Methods

### Constructors
- [[Functions/__init___1150|__init__()]] (line 127)

### Magic Methods
- [[Functions/__getattr___1160|__getattr__()]] (line 256)

### Methods
- [[Functions/phase0_1151|phase0()]] (line 140)
- [[Functions/phase1_1152|phase1()]] (line 148)
- [[Functions/phase2_1153|phase2()]] (line 155)
- [[Functions/phase3_1154|phase3()]] (line 192)
- [[Functions/phase4_1155|phase4()]] (line 196)
- [[Functions/phase4_closure_1156|phase4_closure()]] (line 208)
- [[Functions/report_1157|report()]] (line 213)
- [[Functions/report_partial_closure_1158|report_partial_closure()]] (line 238)
- [[Functions/report_full_closure_1159|report_full_closure()]] (line 244)
