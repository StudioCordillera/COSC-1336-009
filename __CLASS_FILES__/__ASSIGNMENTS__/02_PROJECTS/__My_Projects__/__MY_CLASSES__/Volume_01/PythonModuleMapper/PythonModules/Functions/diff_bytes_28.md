---
type: function
name: diff_bytes
module: difflib
lineno: 1273
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: diff_bytes()

## Overview

Compare `a` and `b`, two sequences of lines represented as bytes rather
than str. This is a wrapper for `dfunc`, which is typically either
unified_diff() or context_diff(). Inputs are losslessly converted to
strings so that `dfunc` only has to worry about strings, and encoded
back to bytes on return. This is necessary to compare files with
unknown or inconsistent encoding. All other inputs (except `n`) must be
bytes rather than str.

```python
def diff_bytes(dfunc, a, b, fromfile, tofile, fromfiledate, tofiledate, n, lineterm)
```

**Module:** [[Modules/difflib|difflib]]
**Type:** Module-level function
**Line:** 1273
