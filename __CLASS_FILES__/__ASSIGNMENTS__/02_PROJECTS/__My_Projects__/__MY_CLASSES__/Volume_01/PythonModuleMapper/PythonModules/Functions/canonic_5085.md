---
type: function
name: canonic
module: bdb
lineno: 43
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: canonic()

## Overview

Return canonical form of filename.

For real filenames, the canonical form is a case-normalized (on
case insensitive filesystems) absolute path.  'Filenames' with
angle brackets, such as "<stdin>", generated in interactive
mode, are returned unchanged.

```python
def canonic(self, filename)
```

**Module:** [[Modules/bdb|bdb]]
**Class:** [[Classes/Bdb|Bdb]]
**Type:** Method
**Line:** 43

## Categories

- [[Taxonomy/public_method|public_method]]
