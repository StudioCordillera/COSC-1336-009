---
type: function
name: getlocale
module: locale
lineno: 582
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getlocale()

## Overview

Returns the current setting for the given locale category as
tuple (language code, encoding).

category may be one of the LC_* value except LC_ALL. It
defaults to LC_CTYPE.

Except for the code 'C', the language code corresponds to RFC
1766.  code and encoding can be None in case the values cannot
be determined.

```python
def getlocale(category)
```

**Module:** [[Modules/locale|locale]]
**Type:** Module-level function
**Line:** 582
