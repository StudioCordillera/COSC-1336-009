---
type: function
name: _same_path
module: venv
lineno: 112
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _same_path()

## Overview

Check whether two paths appear the same.

Whether they refer to the same file is irrelevant; we're testing for
whether a human reader would look at the path string and easily tell
that they're the same file.

```python
@classmethod
def _same_path(cls, path1, path2)
```

**Module:** [[Modules/venv|venv]]
**Class:** [[Classes/EnvBuilder|EnvBuilder]]
**Type:** Method
**Line:** 112

## Categories

- [[Taxonomy/protected_method|protected_method]]
