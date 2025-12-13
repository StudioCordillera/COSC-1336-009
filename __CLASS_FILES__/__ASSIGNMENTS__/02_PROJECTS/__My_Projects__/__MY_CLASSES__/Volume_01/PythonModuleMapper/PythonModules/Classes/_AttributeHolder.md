---
type: class
name: _AttributeHolder
module: argparse
lineno: 107
tags:
  - python
  - class
---

# Class: _AttributeHolder

## Overview

Abstract base class that provides __repr__.

The __repr__ method returns a string in the format::
    ClassName(attr=name, attr=name, ...)
The attributes are determined either by a class-level attribute,
'_kwarg_names', or by inspecting the instance __dict__.

**Module:** [[Modules/argparse|argparse]]
**Line:** 107

## Inheritance

**Subclasses:**
- [[Classes/Action|Action]]
- [[Classes/Namespace|Namespace]]
- [[Classes/ArgumentParser|ArgumentParser]]

## Methods

### Magic Methods
- [[Functions/__repr___2082|__repr__()]] (line 116)

### Methods
- [[Functions/_get_kwargs_2083|_get_kwargs()]] (line 131)
- [[Functions/_get_args_2084|_get_args()]] (line 134)
