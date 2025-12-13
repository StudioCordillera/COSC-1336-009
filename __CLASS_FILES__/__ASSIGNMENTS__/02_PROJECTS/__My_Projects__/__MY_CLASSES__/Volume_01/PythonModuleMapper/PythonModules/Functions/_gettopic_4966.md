---
type: function
name: _gettopic
module: pydoc
lineno: 2155
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _gettopic()

## Overview

Return unbuffered tuple of (topic, xrefs).

If an error occurs here, the exception is caught and displayed by
the url handler.

This function duplicates the showtopic method but returns its
result directly so it can be formatted for display in an html page.

```python
def _gettopic(self, topic, more_xrefs)
```

**Module:** [[Modules/pydoc|pydoc]]
**Class:** [[Classes/Helper|Helper]]
**Type:** Method
**Line:** 2155

## Categories

- [[Taxonomy/protected_method|protected_method]]
