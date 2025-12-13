---
type: function
name: guess_type
module: mimetypes
lineno: 105
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: guess_type()

## Overview

Guess the type of a file which is either a URL or a path-like object.

Return value is a tuple (type, encoding) where type is None if
the type can't be guessed (no or unknown suffix) or a string
of the form type/subtype, usable for a MIME Content-type
header; and encoding is None for no encoding or the name of
the program used to encode (e.g. compress or gzip).  The
mappings are table driven.  Encoding suffixes are case
sensitive; type suffixes are first tried case sensitive, then
case insensitive.

The suffixes .tgz, .taz and .tz (case sensitive!) are all
mapped to '.tar.gz'.  (This is table-driven too, using the
dictionary suffix_map.)

Optional `strict' argument when False adds a bunch of commonly found,
but non-standard types.

```python
def guess_type(self, url, strict)
```

**Module:** [[Modules/mimetypes|mimetypes]]
**Class:** [[Classes/MimeTypes|MimeTypes]]
**Type:** Method
**Line:** 105

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
