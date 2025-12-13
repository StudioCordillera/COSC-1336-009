---
type: function
name: guess_extension
module: mimetypes
lineno: 203
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: guess_extension()

## Overview

Guess the extension for a file based on its MIME type.

Return value is a string giving a filename extension,
including the leading dot ('.').  The extension is not
guaranteed to have been associated with any particular data
stream, but would be mapped to the MIME type `type' by
guess_type().  If no extension can be guessed for `type', None
is returned.

Optional `strict' argument when false adds a bunch of commonly found,
but non-standard types.

```python
def guess_extension(self, type, strict)
```

**Module:** [[Modules/mimetypes|mimetypes]]
**Class:** [[Classes/MimeTypes|MimeTypes]]
**Type:** Method
**Line:** 203

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
