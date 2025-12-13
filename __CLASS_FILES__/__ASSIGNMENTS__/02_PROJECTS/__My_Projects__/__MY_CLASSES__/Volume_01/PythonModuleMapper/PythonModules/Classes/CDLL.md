---
type: class
name: CDLL
module: ctypes
lineno: 322
tags:
  - python
  - class
---

# Class: CDLL

## Overview

An instance of this class represents a loaded dll/shared
library, exporting functions using the standard C calling
convention (named 'cdecl' on Windows).

The exported functions can be accessed as attributes, or by
indexing with the function name.  Examples:

<obj>.qsort -> callable object
<obj>['qsort'] -> callable object

Calling the functions releases the Python GIL during the call and
reacquires it afterwards.

**Module:** [[Modules/ctypes|ctypes]]
**Line:** 322

## Inheritance

**Subclasses:**
- [[Classes/PyDLL|PyDLL]]
- [[Classes/WinDLL|WinDLL]]
- [[Classes/OleDLL|OleDLL]]

## Methods

### Constructors
- [[Functions/__init___2461|__init__()]] (line 343)

### Magic Methods
- [[Functions/__repr___2462|__repr__()]] (line 394)
- [[Functions/__getattr___2463|__getattr__()]] (line 400)
- [[Functions/__getitem___2464|__getitem__()]] (line 407)
