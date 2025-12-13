---
type: function
name: runtime_checkable
module: typing
lineno: 2329
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: runtime_checkable()

## Overview

Mark a protocol class as a runtime protocol.

Such protocol can be used with isinstance() and issubclass().
Raise TypeError if applied to a non-protocol class.
This allows a simple-minded structural check very similar to
one trick ponies in collections.abc such as Iterable.

For example::

    @runtime_checkable
    class Closable(Protocol):
        def close(self): ...

    assert isinstance(open('/some/file'), Closable)

Warning: this will check only the presence of the required methods,
not their type signatures!

```python
def runtime_checkable(cls)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 2329
