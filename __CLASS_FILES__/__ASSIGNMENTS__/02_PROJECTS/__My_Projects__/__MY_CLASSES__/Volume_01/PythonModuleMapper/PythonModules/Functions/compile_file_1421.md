---
type: function
name: compile_file
module: compileall
lineno: 132
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: compile_file()

## Overview

Byte-compile one file.

Arguments (only fullname is required):

fullname:  the file to byte-compile
ddir:      if given, the directory name compiled in to the
           byte-code file.
force:     if True, force compilation, even if timestamps are up-to-date
quiet:     full output with False or 0, errors only with 1,
           no output with 2
legacy:    if True, produce legacy pyc paths instead of PEP 3147 paths
optimize:  int or list of optimization levels or -1 for level of
           the interpreter. Multiple levels leads to multiple compiled
           files each with one optimization level.
invalidation_mode: how the up-to-dateness of the pyc will be checked
stripdir:  part of path to left-strip from source file path
prependdir: path to prepend to beginning of original file path, applied
           after stripdir
limit_sl_dest: ignore symlinks if they are pointing outside of
               the defined path.
hardlink_dupes: hardlink duplicated pyc files

```python
def compile_file(fullname, ddir, force, rx, quiet, legacy, optimize, invalidation_mode)
```

**Module:** [[Modules/compileall|compileall]]
**Type:** Module-level function
**Line:** 132
