---
type: function
name: add_type
module: mimetypes
lineno: 370
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: add_type()

## Overview

Add a mapping between a type and an extension.

When the extension is already known, the new
type will replace the old one. When the type
is already known the extension will be added
to the list of known extensions.

If strict is true, information will be added to
list of standard types, else to the list of non-standard
types.

```python
def add_type(type, ext, strict)
```

**Module:** [[Modules/mimetypes|mimetypes]]
**Type:** Module-level function
**Line:** 370
