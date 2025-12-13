---
type: function
name: update
module: collections
lineno: 673
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: update()

## Overview

Like dict.update() but add counts instead of replacing them.

Source can be an iterable, a dictionary, or another Counter instance.

>>> c = Counter('which')
>>> c.update('witch')           # add elements from another iterable
>>> d = Counter('watch')
>>> c.update(d)                 # add elements from another counter
>>> c['h']                      # four 'h' in which, witch, and watch
4

```python
def update()
```

**Module:** [[Modules/collections|collections]]
**Class:** [[Classes/Counter|Counter]]
**Type:** Method
**Line:** 673

## Categories

- [[Taxonomy/public_method|public_method]]
