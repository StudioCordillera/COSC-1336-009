---
type: function
name: multimode
module: statistics
lineno: 788
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: multimode()

## Overview

Return a list of the most frequently occurring values.

Will return more than one result if there are multiple modes
or an empty list if *data* is empty.

>>> multimode('aabbbbbbbbcc')
['b']
>>> multimode('aabbbbccddddeeffffgg')
['b', 'd', 'f']
>>> multimode('')
[]

```python
def multimode(data)
```

**Module:** [[Modules/statistics|statistics]]
**Type:** Module-level function
**Line:** 788
