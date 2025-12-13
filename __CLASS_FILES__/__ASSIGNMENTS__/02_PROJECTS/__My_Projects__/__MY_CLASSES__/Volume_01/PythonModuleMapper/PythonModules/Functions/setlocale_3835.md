---
type: function
name: setlocale
module: locale
lineno: 600
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: setlocale()

## Overview

Set the locale for the given category.  The locale can be
a string, an iterable of two strings (language code and encoding),
or None.

Iterables are converted to strings using the locale aliasing
engine.  Locale strings are passed directly to the C lib.

category may be given as one of the LC_* values.

```python
def setlocale(category, locale)
```

**Module:** [[Modules/locale|locale]]
**Type:** Module-level function
**Line:** 600
