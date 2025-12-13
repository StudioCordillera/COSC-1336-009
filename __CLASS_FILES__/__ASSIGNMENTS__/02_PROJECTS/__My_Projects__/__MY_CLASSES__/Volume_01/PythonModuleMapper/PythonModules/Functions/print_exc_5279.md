---
type: function
name: print_exc
module: timeit
lineno: 139
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: print_exc()

## Overview

Helper to print a traceback from the timed code.

Typical use:

    t = Timer(...)       # outside the try/except
    try:
        t.timeit(...)    # or t.repeat(...)
    except:
        t.print_exc()

The advantage over the standard traceback is that source lines
in the compiled template will be displayed.

The optional file argument directs where the traceback is
sent; it defaults to sys.stderr.

```python
def print_exc(self, file)
```

**Module:** [[Modules/timeit|timeit]]
**Class:** [[Classes/Timer|Timer]]
**Type:** Method
**Line:** 139

## Categories

- [[Taxonomy/public_method|public_method]]
