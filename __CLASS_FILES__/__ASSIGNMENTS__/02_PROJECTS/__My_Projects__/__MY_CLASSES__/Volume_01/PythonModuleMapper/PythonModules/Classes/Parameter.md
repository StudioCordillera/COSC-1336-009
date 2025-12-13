---
type: class
name: Parameter
module: inspect
lineno: 2722
tags:
  - python
  - class
---

# Class: Parameter

## Overview

Represents a parameter in a function signature.

Has the following public attributes:

* name : str
    The name of the parameter as a string.
* default : object
    The default value for the parameter if specified.  If the
    parameter has no default value, this attribute is set to
    `Parameter.empty`.
* annotation
    The annotation for the parameter if specified.  If the
    parameter has no annotation, this attribute is set to
    `Parameter.empty`.
* kind : str
    Describes how argument values are bound to the parameter.
    Possible values: `Parameter.POSITIONAL_ONLY`,
    `Parameter.POSITIONAL_OR_KEYWORD`, `Parameter.VAR_POSITIONAL`,
    `Parameter.KEYWORD_ONLY`, `Parameter.VAR_KEYWORD`.

**Module:** [[Modules/inspect|inspect]]
**Line:** 2722

## Methods

### Constructors
- [[Functions/__init___5778|__init__()]] (line 2754)

### Magic Methods
- [[Functions/__reduce___5779|__reduce__()]] (line 2797)
- [[Functions/__setstate___5780|__setstate__()]] (line 2803)
- [[Functions/__str___5786|__str__()]] (line 2841)
- [[Functions/__repr___5787|__repr__()]] (line 2865)
- [[Functions/__hash___5788|__hash__()]] (line 2868)
- [[Functions/__eq___5789|__eq__()]] (line 2871)

### Methods
- [[Functions/name_5781|name()]] (line 2808)
- [[Functions/default_5782|default()]] (line 2812)
- [[Functions/annotation_5783|annotation()]] (line 2816)
- [[Functions/kind_5784|kind()]] (line 2820)
- [[Functions/replace_5785|replace()]] (line 2823)
