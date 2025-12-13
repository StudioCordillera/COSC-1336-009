---
type: function
name: format_string
module: locale
lineno: 213
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: format_string()

## Overview

Formats a string in the same way that the % formatting would use,
but takes the current locale into account.

Grouping is applied if the third parameter is true.
Conversion uses monetary thousands separator and grouping strings if
forth parameter monetary is true.

```python
def format_string(f, val, grouping, monetary)
```

**Module:** [[Modules/locale|locale]]
**Type:** Module-level function
**Line:** 213
