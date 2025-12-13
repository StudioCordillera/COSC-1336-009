---
type: class
name: LogRecord
module: logging
lineno: 286
tags:
  - python
  - class
---

# Class: LogRecord

## Overview

A LogRecord instance represents an event being logged.

LogRecord instances are created every time something is logged. They
contain all the information pertinent to the event being logged. The
main information passed in is in msg and args, which are combined
using str(msg) % args to create the message field of the record. The
record also includes information such as when the record was created,
the source line where the logging call was made, and any exception
information to be logged.

**Module:** [[Modules/logging|logging]]
**Line:** 286

## Methods

### Constructors
- [[Functions/__init___2247|__init__()]] (line 298)

### Magic Methods
- [[Functions/__repr___2248|__repr__()]] (line 387)

### Methods
- [[Functions/getMessage_2249|getMessage()]] (line 391)
