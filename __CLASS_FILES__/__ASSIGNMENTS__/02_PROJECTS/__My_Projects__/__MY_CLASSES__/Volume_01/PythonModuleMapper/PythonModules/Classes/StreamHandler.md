---
type: class
name: StreamHandler
module: logging
lineno: 1111
tags:
  - python
  - class
---

# Class: StreamHandler

## Overview

A handler class which writes logging records, appropriately formatted,
to a stream. Note that this class does not close the stream, as
sys.stdout or sys.stderr may be used.

**Module:** [[Modules/logging|logging]]
**Line:** 1111

## Inheritance

**Inherits from:**
- [[Classes/Handler|Handler]]

**Subclasses:**
- [[Classes/FileHandler|FileHandler]]
- [[Classes/_StderrHandler|_StderrHandler]]

## Methods

### Constructors
- [[Functions/__init___2301|__init__()]] (line 1120)

### Magic Methods
- [[Functions/__repr___2305|__repr__()]] (line 1178)

### Methods
- [[Functions/flush_2302|flush()]] (line 1131)
- [[Functions/emit_2303|emit()]] (line 1139)
- [[Functions/setStream_2304|setStream()]] (line 1161)
