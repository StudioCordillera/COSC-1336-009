---
type: class
name: BasicInterpolation
module: configparser
lineno: 396
tags:
  - python
  - class
---

# Class: BasicInterpolation

## Overview

Interpolation as implemented in the classic ConfigParser.

The option values can contain format strings which refer to other values in
the same section, or values in the special default section.

For example:

    something: %(dir)s/whatever

would resolve the "%(dir)s" to the value of dir.  All reference
expansions are done late, on demand. If a user needs to use a bare % in
a configuration file, she can escape it by writing %%. Other % usage
is considered a user error and raises `InterpolationSyntaxError`.

**Module:** [[Modules/configparser|configparser]]
**Line:** 396

## Inheritance

**Inherits from:**
- [[Classes/Interpolation|Interpolation]]

## Methods

### Methods
- [[Functions/before_get_1905|before_get()]] (line 413)
- [[Functions/before_set_1906|before_set()]] (line 418)
- [[Functions/_interpolate_some_1907|_interpolate_some()]] (line 426)
