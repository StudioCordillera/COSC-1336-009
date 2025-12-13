---
type: class
name: FileType
module: argparse
lineno: 1278
tags:
  - python
  - class
---

# Class: FileType

## Overview

Factory for creating file object types

Instances of FileType are typically passed as type= arguments to the
ArgumentParser add_argument() method.

Keyword Arguments:
    - mode -- A string indicating how the file is to be opened. Accepts the
        same values as the builtin open() function.
    - bufsize -- The file's desired buffer size. Accepts the same values as
        the builtin open() function.
    - encoding -- The file's encoding. Accepts the same values as the
        builtin open() function.
    - errors -- A string indicating how encoding and decoding errors are to
        be handled. Accepts the same value as the builtin open() function.

**Module:** [[Modules/argparse|argparse]]
**Line:** 1278

## Methods

### Constructors
- [[Functions/__init___2149|__init__()]] (line 1295)

### Magic Methods
- [[Functions/__call___2150|__call__()]] (line 1301)
- [[Functions/__repr___2151|__repr__()]] (line 1321)
