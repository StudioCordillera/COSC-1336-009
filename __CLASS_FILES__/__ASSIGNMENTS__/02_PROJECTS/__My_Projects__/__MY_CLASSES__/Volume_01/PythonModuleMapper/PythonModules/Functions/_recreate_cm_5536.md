---
type: function
name: _recreate_cm
module: contextlib
lineno: 69
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
  - protected_method
  - protected_method
---

# Function: _recreate_cm()

## Overview

Return a recreated instance of self.

Allows an otherwise one-shot context manager like
_GeneratorContextManager to support use as
a decorator via implicit recreation.

This is a private interface just for _GeneratorContextManager.
See issue #11647 for details.

```python
def _recreate_cm(self)
```

**Module:** [[Modules/contextlib|contextlib]]
**Class:** [[Classes/ContextDecorator|ContextDecorator]]
**Type:** Method
**Line:** 69

## Categories

- [[Taxonomy/protected_method|protected_method]]
- [[Taxonomy/protected_method|protected_method]]
- [[Taxonomy/protected_method|protected_method]]
