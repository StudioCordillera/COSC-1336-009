---
type: function
name: final
module: typing
lineno: 2754
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: final()

## Overview

Decorator to indicate final methods and final classes.

Use this decorator to indicate to type checkers that the decorated
method cannot be overridden, and decorated class cannot be subclassed.

For example::

    class Base:
        @final
        def done(self) -> None:
            ...
    class Sub(Base):
        def done(self) -> None:  # Error reported by type checker
            ...

    @final
    class Leaf:
        ...
    class Other(Leaf):  # Error reported by type checker
        ...

There is no runtime checking of these properties. The decorator
attempts to set the ``__final__`` attribute to ``True`` on the decorated
object to allow runtime introspection.

```python
def final(f)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 2754
