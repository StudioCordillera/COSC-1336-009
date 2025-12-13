---
type: function
name: tk_busy_configure
module: tkinter
lineno: 930
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: tk_busy_configure()

## Overview

Query or modify the busy configuration options.

The widget must have been previously made busy by
tk_busy_hold().  Options may have any of the values accepted by
tk_busy_hold().

Please note that the option database is referenced by the widget
name or class.  For example, if a Frame widget with name "frame"
is to be made busy, the busy cursor can be specified for it by
either call:

    w.option_add('*frame.busyCursor', 'gumby')
    w.option_add('*Frame.BusyCursor', 'gumby')

```python
def tk_busy_configure(self, cnf)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Misc|Misc]]
**Type:** Method
**Line:** 930

## Categories

- [[Taxonomy/public_method|public_method]]
