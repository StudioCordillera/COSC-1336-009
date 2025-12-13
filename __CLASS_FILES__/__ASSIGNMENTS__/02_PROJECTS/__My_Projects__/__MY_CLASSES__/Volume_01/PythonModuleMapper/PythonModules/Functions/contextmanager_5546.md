---
type: function
name: contextmanager
module: contextlib
lineno: 276
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: contextmanager()

## Overview

@contextmanager decorator.

Typical usage:

    @contextmanager
    def some_generator(<arguments>):
        <setup>
        try:
            yield <value>
        finally:
            <cleanup>

This makes this:

    with some_generator(<arguments>) as <variable>:
        <body>

equivalent to this:

    <setup>
    try:
        <variable> = <value>
        <body>
    finally:
        <cleanup>

```python
def contextmanager(func)
```

**Module:** [[Modules/contextlib|contextlib]]
**Type:** Module-level function
**Line:** 276
