---
type: function
name: wrapper
module: curses
lineno: 63
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: wrapper()

## Overview

Wrapper function that initializes curses and calls another function,
restoring normal keyboard/screen behavior on error.
The callable object 'func' is then passed the main window 'stdscr'
as its first argument, followed by any other arguments passed to
wrapper().

```python
def wrapper()
```

**Module:** [[Modules/curses|curses]]
**Type:** Module-level function
**Line:** 63
