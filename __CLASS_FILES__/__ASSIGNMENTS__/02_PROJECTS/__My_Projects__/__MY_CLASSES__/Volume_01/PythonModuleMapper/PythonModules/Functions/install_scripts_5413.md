---
type: function
name: install_scripts
module: venv
lineno: 522
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: install_scripts()

## Overview

Install scripts into the created environment from a directory.

:param context: The information for the environment creation request
                being processed.
:param path:    Absolute pathname of a directory containing script.
                Scripts in the 'common' subdirectory of this directory,
                and those in the directory named for the platform
                being run on, are installed in the created environment.
                Placeholder variables are replaced with environment-
                specific values.

```python
def install_scripts(self, context, path)
```

**Module:** [[Modules/venv|venv]]
**Class:** [[Classes/EnvBuilder|EnvBuilder]]
**Type:** Method
**Line:** 522

## Categories

- [[Taxonomy/public_method|public_method]]
