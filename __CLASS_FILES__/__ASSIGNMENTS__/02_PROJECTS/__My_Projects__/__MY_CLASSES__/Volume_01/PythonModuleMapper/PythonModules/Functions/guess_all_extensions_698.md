---
type: function
name: guess_all_extensions
module: mimetypes
lineno: 337
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: guess_all_extensions()

## Overview

Guess the extensions for a file based on its MIME type.

Return value is a list of strings giving the possible filename
extensions, including the leading dot ('.').  The extension is not
guaranteed to have been associated with any particular data
stream, but would be mapped to the MIME type `type' by
guess_type().  If no extension can be guessed for `type', None
is returned.

Optional `strict' argument when false adds a bunch of commonly found,
but non-standard types.

```python
def guess_all_extensions(type, strict)
```

**Module:** [[Modules/mimetypes|mimetypes]]
**Type:** Module-level function
**Line:** 337
