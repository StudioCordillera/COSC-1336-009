---
type: module
name: compileall
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\compileall.py
is_package: False
analyzed_at: 2025-12-10T03:46:28.208870
tags:
  - python
  - module
---

# Module: compileall

## Overview

Module/script to byte-compile all .py files to .pyc files.

When called as a script with arguments, this compiles the directories
given as arguments recursively; the -l option prevents it from
recursing into directories.

Without arguments, it compiles all modules on sys.path, without
recursing into subdirectories.  (Even though it should do so for
packages -- for now, you'll have to deal with packages separately.)

See module py_compile for details of the actual byte-compilation.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\compileall.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:28

## Dependencies

This module imports:
- [[Modules/concurrent.futures|concurrent.futures]]
- [[Modules/filecmp|filecmp]]
- [[Modules/os|os]]
- [[Modules/re|re]]
- [[Modules/struct|struct]]
- [[Modules/sys|sys]]
- [[Modules/functools|functools]]
- [[Modules/pathlib|pathlib]]
- [[Modules/py_compile|py_compile]]
- [[Modules/multiprocessing|multiprocessing]]
- [[Modules/argparse|argparse]]

## Classes

- [[Classes/partial|partial]] (line 279)

## Functions

- [[Functions/_walk_dir_6157|_walk_dir()]] (line 25)
- [[Functions/compile_dir_6158|compile_dir()]] (line 48)
- [[Functions/compile_file_6159|compile_file()]] (line 132)
- [[Functions/compile_path_6160|compile_path()]] (line 281)
- [[Functions/main_6161|main()]] (line 315)
