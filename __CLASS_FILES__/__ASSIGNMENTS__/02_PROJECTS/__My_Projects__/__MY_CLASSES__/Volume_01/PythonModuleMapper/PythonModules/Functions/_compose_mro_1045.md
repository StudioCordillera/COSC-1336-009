---
type: function
name: _compose_mro
module: functools
lineno: 758
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _compose_mro()

## Overview

Calculates the method resolution order for a given class *cls*.

Includes relevant abstract base classes (with their respective bases) from
the *types* iterable. Uses a modified C3 linearization algorithm.

```python
def _compose_mro(cls, types)
```

**Module:** [[Modules/functools|functools]]
**Type:** Module-level function
**Line:** 758
