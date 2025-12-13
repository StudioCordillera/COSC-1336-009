---
type: function
name: post_setup
module: venv
lineno: 464
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: post_setup()

## Overview

Hook for post-setup modification of the venv. Subclasses may install
additional packages or scripts here, add activation shell scripts, etc.

:param context: The information for the environment creation request
                being processed.

```python
def post_setup(self, context)
```

**Module:** [[Modules/venv|venv]]
**Class:** [[Classes/EnvBuilder|EnvBuilder]]
**Type:** Method
**Line:** 464

## Categories

- [[Taxonomy/public_method|public_method]]
