---
type: function
name: guess_all_extensions
module: mimetypes
lineno: 184
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: guess_all_extensions()

## Overview

Guess the extensions for a file based on its MIME type.

Return value is a list of strings giving the possible filename
extensions, including the leading dot ('.').  The extension is not
guaranteed to have been associated with any particular data stream,
but would be mapped to the MIME type `type' by guess_type().

Optional `strict' argument when false adds a bunch of commonly found,
but non-standard types.

```python
def guess_all_extensions(self, type, strict)
```

**Module:** [[Modules/mimetypes|mimetypes]]
**Class:** [[Classes/MimeTypes|MimeTypes]]
**Type:** Method
**Line:** 184

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
