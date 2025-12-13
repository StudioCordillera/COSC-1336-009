---
type: function
name: asynccontextmanager
module: contextlib
lineno: 309
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: asynccontextmanager()

## Overview

@asynccontextmanager decorator.

Typical usage:

    @asynccontextmanager
    async def some_async_generator(<arguments>):
        <setup>
        try:
            yield <value>
        finally:
            <cleanup>

This makes this:

    async with some_async_generator(<arguments>) as <variable>:
        <body>

equivalent to this:

    <setup>
    try:
        <variable> = <value>
        <body>
    finally:
        <cleanup>

```python
def asynccontextmanager(func)
```

**Module:** [[Modules/contextlib|contextlib]]
**Type:** Module-level function
**Line:** 309
