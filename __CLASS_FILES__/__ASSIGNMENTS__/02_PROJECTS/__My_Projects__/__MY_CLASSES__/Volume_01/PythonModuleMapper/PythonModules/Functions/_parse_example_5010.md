---
type: function
name: _parse_example
module: doctest
lineno: 719
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _parse_example()

## Overview

Given a regular expression match from `_EXAMPLE_RE` (`m`),
return a pair `(source, want)`, where `source` is the matched
example's source code (with prompts and indentation stripped);
and `want` is the example's expected output (with indentation
stripped).

`name` is the string's name, and `lineno` is the line number
where the example starts; both are used for error messages.

```python
def _parse_example(self, m, name, lineno)
```

**Module:** [[Modules/doctest|doctest]]
**Class:** [[Classes/DocTestParser|DocTestParser]]
**Type:** Method
**Line:** 719

## Categories

- [[Taxonomy/protected_method|protected_method]]
