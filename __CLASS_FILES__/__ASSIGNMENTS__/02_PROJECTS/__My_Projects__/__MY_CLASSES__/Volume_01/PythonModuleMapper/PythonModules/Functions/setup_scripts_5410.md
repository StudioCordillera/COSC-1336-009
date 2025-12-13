---
type: function
name: setup_scripts
module: venv
lineno: 449
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: setup_scripts()

## Overview

Set up scripts into the created environment from a directory.

This method installs the default scripts into the environment
being created. You can prevent the default installation by overriding
this method if you really need to, or if you need to specify
a different location for the scripts to install. By default, the
'scripts' directory in the venv package is used as the source of
scripts to install.

```python
def setup_scripts(self, context)
```

**Module:** [[Modules/venv|venv]]
**Class:** [[Classes/EnvBuilder|EnvBuilder]]
**Type:** Method
**Line:** 449

## Categories

- [[Taxonomy/public_method|public_method]]
