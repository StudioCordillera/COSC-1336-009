---
type: function
name: detect_encoding
module: tokenize
lineno: 358
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: detect_encoding()

## Overview

The detect_encoding() function is used to detect the encoding that should
be used to decode a Python source file.  It requires one argument, readline,
in the same way as the tokenize() generator.

It will call readline a maximum of twice, and return the encoding used
(as a string) and a list of any lines (left as bytes) it has read in.

It detects the encoding from the presence of a utf-8 bom or an encoding
cookie as specified in pep-0263.  If both a bom and a cookie are present,
but disagree, a SyntaxError will be raised.  If the encoding cookie is an
invalid charset, raise a SyntaxError.  Note that if a utf-8 bom is found,
'utf-8-sig' is returned.

If no encoding is specified, then the default of 'utf-8' will be returned.

```python
def detect_encoding(readline)
```

**Module:** [[Modules/tokenize|tokenize]]
**Type:** Module-level function
**Line:** 358
