---
type: function
name: trace_dispatch
module: bdb
lineno: 73
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: trace_dispatch()

## Overview

Dispatch a trace function for debugged frames based on the event.

This function is installed as the trace function for debugged
frames. Its return value is the new trace function, which is
usually itself. The default implementation decides how to
dispatch a frame, depending on the type of event (passed in as a
string) that is about to be executed.

The event can be one of the following:
    line: A new line of code is going to be executed.
    call: A function is about to be called or another code block
          is entered.
    return: A function or other code block is about to return.
    exception: An exception has occurred.
    c_call: A C function is about to be called.
    c_return: A C function has returned.
    c_exception: A C function has raised an exception.

For the Python events, specialized functions (see the dispatch_*()
methods) are called.  For the C events, no action is taken.

The arg parameter depends on the previous event.

```python
def trace_dispatch(self, frame, event, arg)
```

**Module:** [[Modules/bdb|bdb]]
**Class:** [[Classes/Bdb|Bdb]]
**Type:** Method
**Line:** 73

## Categories

- [[Taxonomy/public_method|public_method]]
