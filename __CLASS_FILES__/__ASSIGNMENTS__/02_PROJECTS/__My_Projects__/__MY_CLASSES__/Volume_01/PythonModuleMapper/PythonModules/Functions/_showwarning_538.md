---
type: function
name: _showwarning
module: logging
lineno: 2303
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _showwarning()

## Overview

Implementation of showwarnings which redirects to logging, which will first
check to see if the file parameter is None. If a file is specified, it will
delegate to the original warnings implementation of showwarning. Otherwise,
it will call warnings.formatwarning and will log the resulting string to a
warnings logger named "py.warnings" with level logging.WARNING.

```python
def _showwarning(message, category, filename, lineno, file, line)
```

**Module:** [[Modules/logging|logging]]
**Type:** Module-level function
**Line:** 2303
