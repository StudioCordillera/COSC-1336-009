---
type: function
name: compile_path
module: compileall
lineno: 281
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: compile_path()

## Overview

Byte-compile all module on sys.path.

Arguments (all optional):

skip_curdir: if true, skip current directory (default True)
maxlevels:   max recursion level (default 0)
force: as for compile_dir() (default False)
quiet: as for compile_dir() (default 0)
legacy: as for compile_dir() (default False)
optimize: as for compile_dir() (default -1)
invalidation_mode: as for compiler_dir()

```python
def compile_path(skip_curdir, maxlevels, force, quiet, legacy, optimize, invalidation_mode)
```

**Module:** [[Modules/compileall|compileall]]
**Type:** Module-level function
**Line:** 281
