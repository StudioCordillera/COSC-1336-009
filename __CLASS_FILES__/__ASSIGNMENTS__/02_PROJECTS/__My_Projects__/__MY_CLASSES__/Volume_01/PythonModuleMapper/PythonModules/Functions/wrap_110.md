---
type: function
name: wrap
module: textwrap
lineno: 373
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: wrap()

## Overview

Wrap a single paragraph of text, returning a list of wrapped lines.

Reformat the single paragraph in 'text' so it fits in lines of no
more than 'width' columns, and return a list of wrapped lines.  By
default, tabs in 'text' are expanded with string.expandtabs(), and
all other whitespace characters (including newline) are converted to
space.  See TextWrapper class for available keyword args to customize
wrapping behaviour.

```python
def wrap(text, width)
```

**Module:** [[Modules/textwrap|textwrap]]
**Type:** Module-level function
**Line:** 373
