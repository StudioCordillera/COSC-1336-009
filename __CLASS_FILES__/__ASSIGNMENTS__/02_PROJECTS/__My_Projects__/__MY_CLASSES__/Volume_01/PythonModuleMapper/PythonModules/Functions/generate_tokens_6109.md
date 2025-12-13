---
type: function
name: generate_tokens
module: tokenize
lineno: 494
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: generate_tokens()

## Overview

Tokenize a source reading Python code as unicode strings.

This has the same API as tokenize(), except that it expects the *readline*
callable to return str objects instead of bytes.

```python
def generate_tokens(readline)
```

**Module:** [[Modules/tokenize|tokenize]]
**Type:** Module-level function
**Line:** 494
