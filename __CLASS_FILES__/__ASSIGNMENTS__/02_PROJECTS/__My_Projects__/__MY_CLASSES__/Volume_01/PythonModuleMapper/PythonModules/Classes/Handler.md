---
type: class
name: Handler
module: logging
lineno: 922
tags:
  - python
  - class
---

# Class: Handler

## Overview

Handler instances dispatch logging events to specific destinations.

The base handler class. Acts as a placeholder which defines the Handler
interface. Handlers can optionally use Formatter instances to format
records as desired. By default, no formatter is specified; in this case,
the 'raw' message as determined by record.message is logged.

**Module:** [[Modules/logging|logging]]
**Line:** 922

## Inheritance

**Inherits from:**
- [[Classes/Filterer|Filterer]]

**Subclasses:**
- [[Classes/StreamHandler|StreamHandler]]
- [[Classes/NullHandler|NullHandler]]

## Methods

### Constructors
- [[Functions/__init___2285|__init__()]] (line 931)

### Magic Methods
- [[Functions/__repr___2300|__repr__()]] (line 1107)

### Methods
- [[Functions/get_name_2286|get_name()]] (line 945)
- [[Functions/set_name_2287|set_name()]] (line 948)
- [[Functions/createLock_2288|createLock()]] (line 958)
- [[Functions/_at_fork_reinit_2289|_at_fork_reinit()]] (line 965)
- [[Functions/acquire_2290|acquire()]] (line 968)
- [[Functions/release_2291|release()]] (line 975)
- [[Functions/setLevel_2292|setLevel()]] (line 982)
- [[Functions/format_2293|format()]] (line 988)
- [[Functions/emit_2294|emit()]] (line 1001)
- [[Functions/handle_2295|handle()]] (line 1011)
- [[Functions/setFormatter_2296|setFormatter()]] (line 1030)
- [[Functions/flush_2297|flush()]] (line 1036)
- [[Functions/close_2298|close()]] (line 1045)
- [[Functions/handleError_2299|handleError()]] (line 1060)
