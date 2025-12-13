---
type: class
name: DocTest
module: doctest
lineno: 529
tags:
  - python
  - class
---

# Class: DocTest

## Overview

A collection of doctest examples that should be run in a single
namespace.  Each `DocTest` defines the following attributes:

  - examples: the list of examples.

  - globs: The namespace (aka globals) that the examples should
    be run in.

  - name: A name identifying the DocTest (typically, the name of
    the object whose docstring this DocTest was extracted from).

  - filename: The name of the file that this DocTest was extracted
    from, or `None` if the filename is unknown.

  - lineno: The line number within filename where this DocTest
    begins, or `None` if the line number is unavailable.  This
    line number is zero-based, with respect to the beginning of
    the file.

  - docstring: The string that the examples were extracted from,
    or `None` if the string is unavailable.

**Module:** [[Modules/doctest|doctest]]
**Line:** 529

## Methods

### Constructors
- [[Functions/__init___5002|__init__()]] (line 553)

### Magic Methods
- [[Functions/__repr___5003|__repr__()]] (line 567)
- [[Functions/__eq___5004|__eq__()]] (line 578)
- [[Functions/__hash___5005|__hash__()]] (line 589)
- [[Functions/__lt___5006|__lt__()]] (line 593)
