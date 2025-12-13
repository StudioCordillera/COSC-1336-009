---
type: function
name: untokenize
module: tokenize
lineno: 326
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: untokenize()

## Overview

Transform tokens back into Python source code.
It returns a bytes object, encoded using the ENCODING
token, which is the first token sequence output by tokenize.

Each element returned by the iterable must be a token sequence
with at least two elements, a token number and token value.  If
only two tokens are passed, the resulting output is poor.

The result is guaranteed to tokenize back to match the input so
that the conversion is lossless and round-trips are assured.
The guarantee applies only to the token type and token string as
the spacing between tokens (column positions) may change.

```python
def untokenize(iterable)
```

**Module:** [[Modules/tokenize|tokenize]]
**Type:** Module-level function
**Line:** 326
