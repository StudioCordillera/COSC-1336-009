---
type: function
name: place_configure
module: tkinter
lineno: 2626
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: place_configure()

## Overview

Place a widget in the parent widget. Use as options:
in=master - master relative to which the widget is placed
in_=master - see 'in' option description
x=amount - locate anchor of this widget at position x of master
y=amount - locate anchor of this widget at position y of master
relx=amount - locate anchor of this widget between 0.0 and 1.0
              relative to width of master (1.0 is right edge)
rely=amount - locate anchor of this widget between 0.0 and 1.0
              relative to height of master (1.0 is bottom edge)
anchor=NSEW (or subset) - position anchor according to given direction
width=amount - width of this widget in pixel
height=amount - height of this widget in pixel
relwidth=amount - width of this widget between 0.0 and 1.0
                  relative to width of master (1.0 is the same width
                  as the master)
relheight=amount - height of this widget between 0.0 and 1.0
                   relative to height of master (1.0 is the same
                   height as the master)
bordermode="inside" or "outside" - whether to take border width of
                                   master widget into account

```python
def place_configure(self, cnf)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Place|Place]]
**Type:** Method
**Line:** 2626

## Categories

- [[Taxonomy/public_method|public_method]]
