---
type: class
name: Signature
module: inspect
lineno: 3012
tags:
  - python
  - class
---

# Class: Signature

## Overview

A Signature object represents the overall signature of a function.
It stores a Parameter object for each parameter accepted by the
function, as well as information specific to the function itself.

A Signature object has the following public attributes and methods:

* parameters : OrderedDict
    An ordered mapping of parameters' names to the corresponding
    Parameter objects (keyword-only arguments are in the same order
    as listed in `code.co_varnames`).
* return_annotation : object
    The annotation for the return type of the function if specified.
    If the function has no annotation for its return type, this
    attribute is set to `Signature.empty`.
* bind(*args, **kwargs) -> BoundArguments
    Creates a mapping from positional and keyword arguments to
    parameters.
* bind_partial(*args, **kwargs) -> BoundArguments
    Creates a partial mapping from positional and keyword arguments
    to parameters (simulating 'functools.partial' behavior.)

**Module:** [[Modules/inspect|inspect]]
**Line:** 3012

## Methods

### Constructors
- [[Functions/__init___5799|__init__()]] (line 3042)

### Magic Methods
- [[Functions/__hash___5805|__hash__()]] (line 3136)
- [[Functions/__eq___5806|__eq__()]] (line 3141)
- [[Functions/__reduce___5810|__reduce__()]] (line 3304)
- [[Functions/__setstate___5811|__setstate__()]] (line 3309)
- [[Functions/__repr___5812|__repr__()]] (line 3312)
- [[Functions/__str___5813|__str__()]] (line 3315)

### Methods
- [[Functions/from_callable_5800|from_callable()]] (line 3095)
- [[Functions/parameters_5801|parameters()]] (line 3103)
- [[Functions/return_annotation_5802|return_annotation()]] (line 3107)
- [[Functions/replace_5803|replace()]] (line 3110)
- [[Functions/_hash_basis_5804|_hash_basis()]] (line 3127)
- [[Functions/_bind_5807|_bind()]] (line 3148)
- [[Functions/bind_5808|bind()]] (line 3290)
- [[Functions/bind_partial_5809|bind_partial()]] (line 3297)
- [[Functions/format_5814|format()]] (line 3318)
