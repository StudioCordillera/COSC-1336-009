---
type: function
name: get_doctest
module: doctest
lineno: 693
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_doctest()

## Overview

Extract all doctest examples from the given string, and
collect them into a `DocTest` object.

`globs`, `name`, `filename`, and `lineno` are attributes for
the new `DocTest` object.  See the documentation for `DocTest`
for more information.

```python
def get_doctest(self, string, globs, name, filename, lineno)
```

**Module:** [[Modules/doctest|doctest]]
**Class:** [[Classes/DocTestParser|DocTestParser]]
**Type:** Method
**Line:** 693

## Categories

- [[Taxonomy/accessor|accessor]]
