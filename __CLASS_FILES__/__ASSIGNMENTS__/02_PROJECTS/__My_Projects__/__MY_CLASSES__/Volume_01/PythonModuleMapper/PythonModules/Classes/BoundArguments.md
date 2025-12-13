---
type: class
name: BoundArguments
module: inspect
lineno: 2882
tags:
  - python
  - class
---

# Class: BoundArguments

## Overview

Result of `Signature.bind` call.  Holds the mapping of arguments
to the function's parameters.

Has the following public attributes:

* arguments : dict
    An ordered mutable mapping of parameters' names to arguments' values.
    Does not contain arguments' default values.
* signature : Signature
    The Signature object that created this instance.
* args : tuple
    Tuple of positional arguments values.
* kwargs : dict
    Dict of keyword arguments values.

**Module:** [[Modules/inspect|inspect]]
**Line:** 2882

## Methods

### Constructors
- [[Functions/__init___5790|__init__()]] (line 2901)

### Magic Methods
- [[Functions/__eq___5795|__eq__()]] (line 2990)
- [[Functions/__setstate___5796|__setstate__()]] (line 2998)
- [[Functions/__getstate___5797|__getstate__()]] (line 3002)
- [[Functions/__repr___5798|__repr__()]] (line 3005)

### Methods
- [[Functions/signature_5791|signature()]] (line 2906)
- [[Functions/args_5792|args()]] (line 2910)
- [[Functions/kwargs_5793|kwargs()]] (line 2933)
- [[Functions/apply_defaults_5794|apply_defaults()]] (line 2962)
