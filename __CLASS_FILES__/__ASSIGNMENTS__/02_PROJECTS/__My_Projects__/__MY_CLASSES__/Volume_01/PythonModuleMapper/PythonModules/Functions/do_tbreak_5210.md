---
type: function
name: do_tbreak
module: pdb
lineno: 1202
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: do_tbreak()

## Overview

tbreak [ ([filename:]lineno | function) [, condition] ]

Same arguments as break, but sets a temporary breakpoint: it
is automatically deleted when first hit.

```python
def do_tbreak(self, arg)
```

**Module:** [[Modules/pdb|pdb]]
**Class:** [[Classes/Pdb|Pdb]]
**Type:** Method
**Line:** 1202

## Categories

- [[Taxonomy/public_method|public_method]]
