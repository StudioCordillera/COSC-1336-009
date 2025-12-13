---
type: function
name: compile_dir
module: compileall
lineno: 48
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: compile_dir()

## Overview

Byte-compile all modules in the given directory tree.

Arguments (only dir is required):

dir:       the directory to byte-compile
maxlevels: maximum recursion level (default `sys.getrecursionlimit()`)
ddir:      the directory that will be prepended to the path to the
           file as it is compiled into each byte-code file.
force:     if True, force compilation, even if timestamps are up-to-date
quiet:     full output with False or 0, errors only with 1,
           no output with 2
legacy:    if True, produce legacy pyc paths instead of PEP 3147 paths
optimize:  int or list of optimization levels or -1 for level of
           the interpreter. Multiple levels leads to multiple compiled
           files each with one optimization level.
workers:   maximum number of parallel workers
invalidation_mode: how the up-to-dateness of the pyc will be checked
stripdir:  part of path to left-strip from source file path
prependdir: path to prepend to beginning of original file path, applied
           after stripdir
limit_sl_dest: ignore symlinks if they are pointing outside of
               the defined path
hardlink_dupes: hardlink duplicated pyc files

```python
def compile_dir(dir, maxlevels, ddir, force, rx, quiet, legacy, optimize, workers, invalidation_mode)
```

**Module:** [[Modules/compileall|compileall]]
**Type:** Module-level function
**Line:** 48
