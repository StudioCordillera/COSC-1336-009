---
type: function
name: __setattr__
module: enum
lineno: 829
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - attribute_access
---

# Function: __setattr__()

## Overview

Block attempts to reassign Enum members.

A simple assignment to the class namespace only changes one of the
several possible ways to get an Enum member from the Enum class,
resulting in an inconsistent Enumeration.

```python
def __setattr__(cls, name, value)
```

**Module:** [[Modules/enum|enum]]
**Class:** [[Classes/EnumType|EnumType]]
**Type:** Method
**Line:** 829

## Categories

- [[Taxonomy/attribute_access|attribute_access]]
