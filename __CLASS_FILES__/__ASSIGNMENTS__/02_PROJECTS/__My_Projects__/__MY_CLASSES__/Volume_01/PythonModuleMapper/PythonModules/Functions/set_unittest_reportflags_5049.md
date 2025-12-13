---
type: function
name: set_unittest_reportflags
module: doctest
lineno: 2239
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - mutator
---

# Function: set_unittest_reportflags()

## Overview

Sets the unittest option flags.

The old flag is returned so that a runner could restore the old
value if it wished to:

  >>> import doctest
  >>> old = doctest._unittest_reportflags
  >>> doctest.set_unittest_reportflags(REPORT_NDIFF |
  ...                          REPORT_ONLY_FIRST_FAILURE) == old
  True

  >>> doctest._unittest_reportflags == (REPORT_NDIFF |
  ...                                   REPORT_ONLY_FIRST_FAILURE)
  True

Only reporting flags can be set:

  >>> doctest.set_unittest_reportflags(ELLIPSIS)
  Traceback (most recent call last):
  ...
  ValueError: ('Only reporting flags allowed', 8)

  >>> doctest.set_unittest_reportflags(old) == (REPORT_NDIFF |
  ...                                   REPORT_ONLY_FIRST_FAILURE)
  True

```python
def set_unittest_reportflags(flags)
```

**Module:** [[Modules/doctest|doctest]]
**Type:** Module-level function
**Line:** 2239

## Categories

- [[Taxonomy/mutator|mutator]]
