---
type: function
name: iscode
module: inspect
lineno: 509
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: iscode()

## Overview

Return true if the object is a code object.

Code objects provide these attributes:
    co_argcount         number of arguments (not including *, ** args
                        or keyword only arguments)
    co_code             string of raw compiled bytecode
    co_cellvars         tuple of names of cell variables
    co_consts           tuple of constants used in the bytecode
    co_filename         name of file in which this code object was created
    co_firstlineno      number of first line in Python source code
    co_flags            bitmap: 1=optimized | 2=newlocals | 4=*arg | 8=**arg
                        | 16=nested | 32=generator | 64=nofree | 128=coroutine
                        | 256=iterable_coroutine | 512=async_generator
    co_freevars         tuple of names of free variables
    co_posonlyargcount  number of positional only arguments
    co_kwonlyargcount   number of keyword only arguments (not including ** arg)
    co_lnotab           encoded mapping of line numbers to bytecode indices
    co_name             name with which this code object was defined
    co_names            tuple of names other than arguments and function locals
    co_nlocals          number of local variables
    co_stacksize        virtual machine stack space required
    co_varnames         tuple of names of arguments and local variables

```python
def iscode(object)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 509
