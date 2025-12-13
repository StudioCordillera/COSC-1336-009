---
type: function
name: normalize
module: locale
lineno: 381
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: normalize()

## Overview

Returns a normalized locale code for the given locale
name.

The returned locale code is formatted for use with
setlocale().

If normalization fails, the original name is returned
unchanged.

If the given encoding is not known, the function defaults to
the default encoding for the locale code just like setlocale()
does.

```python
def normalize(localename)
```

**Module:** [[Modules/locale|locale]]
**Type:** Module-level function
**Line:** 381
