---
type: function
name: get_config_vars
module: sysconfig
lineno: 541
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_config_vars()

## Overview

With no arguments, return a dictionary of all configuration
variables relevant for the current platform.

On Unix, this means every variable defined in Python's installed Makefile;
On Windows it's a much smaller set.

With arguments, return a list of values that result from looking up
each argument in the configuration variable dictionary.

```python
def get_config_vars()
```

**Module:** [[Modules/sysconfig|sysconfig]]
**Type:** Module-level function
**Line:** 541

## Categories

- [[Taxonomy/accessor|accessor]]
