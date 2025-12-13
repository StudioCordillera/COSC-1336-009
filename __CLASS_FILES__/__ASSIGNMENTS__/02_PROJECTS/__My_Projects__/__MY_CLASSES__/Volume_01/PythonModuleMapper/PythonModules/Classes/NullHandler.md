---
type: class
name: NullHandler
module: logging
lineno: 2277
tags:
  - python
  - class
---

# Class: NullHandler

## Overview

This handler does nothing. It's intended to be used to avoid the
"No handlers could be found for logger XXX" one-off warning. This is
important for library code, which may contain code to log events. If a user
of the library does not configure logging, the one-off warning might be
produced; to avoid this, the library developer simply needs to instantiate
a NullHandler and add it to the top-level logger of the library module or
package.

**Module:** [[Modules/logging|logging]]
**Line:** 2277

## Inheritance

**Inherits from:**
- [[Classes/Handler|Handler]]

## Methods

### Methods
- [[Functions/handle_2384|handle()]] (line 2287)
- [[Functions/emit_2385|emit()]] (line 2290)
- [[Functions/createLock_2386|createLock()]] (line 2293)
- [[Functions/_at_fork_reinit_2387|_at_fork_reinit()]] (line 2296)
