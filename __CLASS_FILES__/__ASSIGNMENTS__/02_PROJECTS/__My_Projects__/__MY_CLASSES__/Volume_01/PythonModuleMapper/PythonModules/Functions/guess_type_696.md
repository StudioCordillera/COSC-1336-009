---
type: function
name: guess_type
module: mimetypes
lineno: 304
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: guess_type()

## Overview

Guess the type of a file based on its URL.

Return value is a tuple (type, encoding) where type is None if the
type can't be guessed (no or unknown suffix) or a string of the
form type/subtype, usable for a MIME Content-type header; and
encoding is None for no encoding or the name of the program used
to encode (e.g. compress or gzip).  The mappings are table
driven.  Encoding suffixes are case sensitive; type suffixes are
first tried case sensitive, then case insensitive.

The suffixes .tgz, .taz and .tz (case sensitive!) are all mapped
to ".tar.gz".  (This is table-driven too, using the dictionary
suffix_map).

Optional `strict' argument when false adds a bunch of commonly found, but
non-standard types.

```python
def guess_type(url, strict)
```

**Module:** [[Modules/mimetypes|mimetypes]]
**Type:** Module-level function
**Line:** 304
