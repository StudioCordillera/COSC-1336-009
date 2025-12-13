---
type: function
name: get_examples
module: doctest
lineno: 705
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_examples()

## Overview

Extract all doctest examples from the given string, and return
them as a list of `Example` objects.  Line numbers are
0-based, because it's most common in doctests that nothing
interesting appears on the same line as opening triple-quote,
and so the first interesting line is called "line 1" then.

The optional argument `name` is a name identifying this
string, and is only used for error messages.

```python
def get_examples(self, string, name)
```

**Module:** [[Modules/doctest|doctest]]
**Class:** [[Classes/DocTestParser|DocTestParser]]
**Type:** Method
**Line:** 705

## Categories

- [[Taxonomy/accessor|accessor]]
