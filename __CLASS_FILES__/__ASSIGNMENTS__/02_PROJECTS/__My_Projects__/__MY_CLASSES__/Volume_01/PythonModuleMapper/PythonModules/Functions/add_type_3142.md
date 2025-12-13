---
type: function
name: add_type
module: mimetypes
lineno: 86
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
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
def add_type(self, type, ext, strict)
```

**Module:** [[Modules/mimetypes|mimetypes]]
**Class:** [[Classes/MimeTypes|MimeTypes]]
**Type:** Method
**Line:** 86

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
