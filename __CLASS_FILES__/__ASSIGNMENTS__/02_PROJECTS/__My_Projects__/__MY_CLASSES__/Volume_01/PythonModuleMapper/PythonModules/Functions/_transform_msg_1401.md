---
type: function
name: _transform_msg
module: tokenize
lineno: 565
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _transform_msg()

## Overview

Transform error messages from the C tokenizer into the Python tokenize

The C tokenizer is more picky than the Python one, so we need to massage
the error messages a bit for backwards compatibility.

```python
def _transform_msg(msg)
```

**Module:** [[Modules/tokenize|tokenize]]
**Type:** Module-level function
**Line:** 565
