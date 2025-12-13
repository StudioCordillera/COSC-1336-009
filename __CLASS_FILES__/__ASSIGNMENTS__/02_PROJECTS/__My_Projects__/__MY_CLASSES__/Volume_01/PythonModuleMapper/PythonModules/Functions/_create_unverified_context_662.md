---
type: function
name: _create_unverified_context
module: ssl
lineno: 730
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _create_unverified_context()

## Overview

Create a SSLContext object for Python stdlib modules

All Python stdlib modules shall use this function to create SSLContext
objects in order to keep common settings in one place. The configuration
is less restrict than create_default_context()'s to increase backward
compatibility.

```python
def _create_unverified_context(protocol)
```

**Module:** [[Modules/ssl|ssl]]
**Type:** Module-level function
**Line:** 730
