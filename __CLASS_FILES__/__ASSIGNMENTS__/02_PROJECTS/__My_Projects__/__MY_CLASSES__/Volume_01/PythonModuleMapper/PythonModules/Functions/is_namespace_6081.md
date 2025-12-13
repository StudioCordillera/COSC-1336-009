---
type: function
name: is_namespace
module: symtable
lineno: 345
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - accessor
---

# Function: is_namespace()

## Overview

Returns *True* if name binding introduces new namespace.

If the name is used as the target of a function or class
statement, this will be true.

Note that a single name can be bound to multiple objects.  If
is_namespace() is true, the name may also be bound to other
objects, like an int or list, that does not introduce a new
namespace.

```python
def is_namespace(self)
```

**Module:** [[Modules/symtable|symtable]]
**Class:** [[Classes/Symbol|Symbol]]
**Type:** Method
**Line:** 345

## Categories

- [[Taxonomy/accessor|accessor]]
