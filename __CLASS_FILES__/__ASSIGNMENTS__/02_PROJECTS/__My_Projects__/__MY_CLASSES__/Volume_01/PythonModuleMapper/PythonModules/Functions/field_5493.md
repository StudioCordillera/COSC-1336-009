---
type: function
name: field
module: dataclasses
lineno: 383
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: field()

## Overview

Return an object to identify dataclass fields.

default is the default value of the field.  default_factory is a
0-argument function called to initialize a field's value.  If init
is true, the field will be a parameter to the class's __init__()
function.  If repr is true, the field will be included in the
object's repr().  If hash is true, the field will be included in the
object's hash().  If compare is true, the field will be used in
comparison functions.  metadata, if specified, must be a mapping
which is stored but not otherwise examined by dataclass.  If kw_only
is true, the field will become a keyword-only parameter to
__init__().

It is an error to specify both default and default_factory.

```python
def field()
```

**Module:** [[Modules/dataclasses|dataclasses]]
**Type:** Module-level function
**Line:** 383
