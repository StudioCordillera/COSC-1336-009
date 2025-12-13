---
type: function
name: shorten
module: textwrap
lineno: 398
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: shorten()

## Overview

Collapse and truncate the given text to fit in the given width.

The text first has its whitespace collapsed.  If it then fits in
the *width*, it is returned as is.  Otherwise, as many words
as possible are joined and then the placeholder is appended::

    >>> textwrap.shorten("Hello  world!", width=12)
    'Hello world!'
    >>> textwrap.shorten("Hello  world!", width=11)
    'Hello [...]'

```python
def shorten(text, width)
```

**Module:** [[Modules/textwrap|textwrap]]
**Type:** Module-level function
**Line:** 398
