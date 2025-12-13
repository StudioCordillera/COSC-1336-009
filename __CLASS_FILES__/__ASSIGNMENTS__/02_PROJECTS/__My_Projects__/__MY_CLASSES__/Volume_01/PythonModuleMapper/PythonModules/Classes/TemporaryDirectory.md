---
type: class
name: TemporaryDirectory
module: tempfile
lineno: 864
tags:
  - python
  - class
---

# Class: TemporaryDirectory

## Overview

Create and return a temporary directory.  This has the same
behavior as mkdtemp but can be used as a context manager.  For
example:

    with TemporaryDirectory() as tmpdir:
        ...

Upon exiting the context, the directory and everything contained
in it are removed (unless delete=False is passed or an exception
is raised during cleanup and ignore_cleanup_errors is not True).

Optional Arguments:
    suffix - A str suffix for the directory name.  (see mkdtemp)
    prefix - A str prefix for the directory name.  (see mkdtemp)
    dir - A directory to create this temp dir in.  (see mkdtemp)
    ignore_cleanup_errors - False; ignore exceptions during cleanup?
    delete - True; whether the directory is automatically deleted.

**Module:** [[Modules/tempfile|tempfile]]
**Line:** 864

## Methods

### Constructors
- [[Functions/__init___1258|__init__()]] (line 884)

### Magic Methods
- [[Functions/__repr___1261|__repr__()]] (line 942)
- [[Functions/__enter___1262|__enter__()]] (line 945)
- [[Functions/__exit___1263|__exit__()]] (line 948)

### Methods
- [[Functions/_rmtree_1259|_rmtree()]] (line 895)
- [[Functions/_cleanup_1260|_cleanup()]] (line 937)
- [[Functions/cleanup_1264|cleanup()]] (line 952)
