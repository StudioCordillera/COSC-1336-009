---
type: function
name: _get_revised_path
module: pydoc
lineno: 2721
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: _get_revised_path()

## Overview

Ensures current directory is on returned path, and argv0 directory is not

Exception: argv0 dir is left alone if it's also pydoc's directory.

Returns a new path entry list, or None if no adjustment is needed.

```python
def _get_revised_path(given_path, argv0)
```

**Module:** [[Modules/pydoc|pydoc]]
**Type:** Module-level function
**Line:** 2721

## Categories

- [[Taxonomy/accessor|accessor]]
