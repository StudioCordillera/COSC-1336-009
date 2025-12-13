---
type: class
name: TracebackException
module: traceback
lineno: 997
tags:
  - python
  - class
---

# Class: TracebackException

## Overview

An exception ready for rendering.

The traceback module captures enough attributes from the original exception
to this intermediary form to ensure that no references are held, while
still being able to fully print or format it.

max_group_width and max_group_depth control the formatting of exception
groups. The depth refers to the nesting level of the group, and the width
refers to the size of a single exception group's exceptions array. The
formatted output is truncated when either limit is exceeded.

Use `from_exception` to create TracebackException instances from exception
objects, or the constructor to create TracebackException instances from
individual components.

- :attr:`__cause__` A TracebackException of the original *__cause__*.
- :attr:`__context__` A TracebackException of the original *__context__*.
- :attr:`exceptions` For exception groups - a list of TracebackException
  instances for the nested *exceptions*.  ``None`` for other exceptions.
- :attr:`__suppress_context__` The *__suppress_context__* value from the
  original exception.
- :attr:`stack` A `StackSummary` representing the traceback.
- :attr:`exc_type` (deprecated) The class of the original traceback.
- :attr:`exc_type_str` String display of exc_type
- :attr:`filename` For syntax errors - the filename where the error
  occurred.
- :attr:`lineno` For syntax errors - the linenumber where the error
  occurred.
- :attr:`end_lineno` For syntax errors - the end linenumber where the error
  occurred. Can be `None` if not present.
- :attr:`text` For syntax errors - the text where the error
  occurred.
- :attr:`offset` For syntax errors - the offset into the text where the
  error occurred.
- :attr:`end_offset` For syntax errors - the end offset into the text where
  the error occurred. Can be `None` if not present.
- :attr:`msg` For syntax errors - the compiler error message.

**Module:** [[Modules/traceback|traceback]]
**Line:** 997

## Methods

### Constructors
- [[Functions/__init___5638|__init__()]] (line 1037)

### Magic Methods
- [[Functions/__eq___5643|__eq__()]] (line 1210)
- [[Functions/__str___5644|__str__()]] (line 1215)

### Methods
- [[Functions/from_exception_5639|from_exception()]] (line 1183)
- [[Functions/exc_type_5640|exc_type()]] (line 1188)
- [[Functions/exc_type_str_5641|exc_type_str()]] (line 1194)
- [[Functions/_load_lines_5642|_load_lines()]] (line 1205)
- [[Functions/format_exception_only_5645|format_exception_only()]] (line 1218)
- [[Functions/_format_syntax_error_5646|_format_syntax_error()]] (line 1272)
- [[Functions/format_5647|format()]] (line 1363)
- [[Functions/print_5648|print()]] (line 1464)
