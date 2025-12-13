---
type: function
name: _create_
module: enum
lineno: 842
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _create_()

## Overview

Convenience method to create a new Enum class.

`names` can be:

* A string containing member names, separated either with spaces or
  commas.  Values are incremented by 1 from `start`.
* An iterable of member names.  Values are incremented by 1 from `start`.
* An iterable of (member name, value) pairs.
* A mapping of member name -> value pairs.

```python
def _create_(cls, class_name, names)
```

**Module:** [[Modules/enum|enum]]
**Class:** [[Classes/EnumType|EnumType]]
**Type:** Method
**Line:** 842

## Categories

- [[Taxonomy/protected_method|protected_method]]
