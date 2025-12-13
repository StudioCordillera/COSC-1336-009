---
type: class
name: PyCompileError
module: py_compile
lineno: 18
tags:
  - python
  - class
---

# Class: PyCompileError

## Overview

Exception raised when an error occurs while attempting to
compile the file.

To raise this exception, use

    raise PyCompileError(exc_type,exc_value,file[,msg])

where

    exc_type:   exception type to be used in error message
                type name can be accesses as class variable
                'exc_type_name'

    exc_value:  exception value to be used in error message
                can be accesses as class variable 'exc_value'

    file:       name of file being compiled to be used in error message
                can be accesses as class variable 'file'

    msg:        string message to be written as error message
                If no value is given, a default exception message will be
                given, consistent with 'standard' py_compile output.
                message (or default) can be accesses as class variable
                'msg'

**Module:** [[Modules/py_compile|py_compile]]
**Line:** 18

## Methods

### Constructors
- [[Functions/__init___6146|__init__()]] (line 46)

### Magic Methods
- [[Functions/__str___6147|__str__()]] (line 62)
