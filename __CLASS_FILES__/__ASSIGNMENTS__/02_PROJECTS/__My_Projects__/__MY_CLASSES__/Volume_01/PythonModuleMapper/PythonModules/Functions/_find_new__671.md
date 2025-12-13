---
type: function
name: _find_new_
module: enum
lineno: 1015
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _find_new_()

## Overview

Returns the __new__ to be used for creating the enum members.

classdict: the class dictionary given to __new__
member_type: the data type whose __new__ will be used by default
first_enum: enumeration to check for an overriding __new__

```python
@classmethod
def _find_new_(mcls, classdict, member_type, first_enum)
```

**Module:** [[Modules/enum|enum]]
**Class:** [[Classes/EnumType|EnumType]]
**Type:** Method
**Line:** 1015

## Categories

- [[Taxonomy/protected_method|protected_method]]
