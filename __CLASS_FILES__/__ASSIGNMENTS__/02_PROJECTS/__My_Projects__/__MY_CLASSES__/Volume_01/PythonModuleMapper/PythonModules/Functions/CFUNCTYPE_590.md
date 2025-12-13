---
type: function
name: CFUNCTYPE
module: ctypes
lineno: 73
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: CFUNCTYPE()

## Overview

CFUNCTYPE(restype, *argtypes,
             use_errno=False, use_last_error=False) -> function prototype.

restype: the result type
argtypes: a sequence specifying the argument types

The function prototype can be called in different ways to create a
callable object:

prototype(integer address) -> foreign function
prototype(callable) -> create and return a C callable function from callable
prototype(integer index, method name[, paramflags]) -> foreign function calling a COM method
prototype((ordinal number, dll object)[, paramflags]) -> foreign function exported by ordinal
prototype((function name, dll object)[, paramflags]) -> foreign function exported by name

```python
def CFUNCTYPE(restype)
```

**Module:** [[Modules/ctypes|ctypes]]
**Type:** Module-level function
**Line:** 73
