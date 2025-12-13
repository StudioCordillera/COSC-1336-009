---
type: function
name: paneconfigure
module: tkinter
lineno: 4873
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: paneconfigure()

## Overview

Query or modify the management options for window.

If no option is specified, returns a list describing all
of the available options for pathName.  If option is
specified with no value, then the command returns a list
describing the one named option (this list will be identical
to the corresponding sublist of the value returned if no
option is specified). If one or more option-value pairs are
specified, then the command modifies the given widget
option(s) to have the given value(s); in this case the
command returns an empty string. The following options
are supported:

after window
    Insert the window after the window specified. window
    should be the name of a window already managed by pathName.
before window
    Insert the window before the window specified. window
    should be the name of a window already managed by pathName.
height size
    Specify a height for the window. The height will be the
    outer dimension of the window including its border, if
    any. If size is an empty string, or if -height is not
    specified, then the height requested internally by the
    window will be used initially; the height may later be
    adjusted by the movement of sashes in the panedwindow.
    Size may be any value accepted by Tk_GetPixels.
minsize n
    Specifies that the size of the window cannot be made
    less than n. This constraint only affects the size of
    the widget in the paned dimension -- the x dimension
    for horizontal panedwindows, the y dimension for
    vertical panedwindows. May be any value accepted by
    Tk_GetPixels.
padx n
    Specifies a non-negative value indicating how much
    extra space to leave on each side of the window in
    the X-direction. The value may have any of the forms
    accepted by Tk_GetPixels.
pady n
    Specifies a non-negative value indicating how much
    extra space to leave on each side of the window in
    the Y-direction. The value may have any of the forms
    accepted by Tk_GetPixels.
sticky style
    If a window's pane is larger than the requested
    dimensions of the window, this option may be used
    to position (or stretch) the window within its pane.
    Style is a string that contains zero or more of the
    characters n, s, e or w. The string can optionally
    contains spaces or commas, but they are ignored. Each
    letter refers to a side (north, south, east, or west)
    that the window will "stick" to. If both n and s
    (or e and w) are specified, the window will be
    stretched to fill the entire height (or width) of
    its cavity.
width size
    Specify a width for the window. The width will be
    the outer dimension of the window including its
    border, if any. If size is an empty string, or
    if -width is not specified, then the width requested
    internally by the window will be used initially; the
    width may later be adjusted by the movement of sashes
    in the panedwindow. Size may be any value accepted by
    Tk_GetPixels.

```python
def paneconfigure(self, tagOrId, cnf)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/PanedWindow|PanedWindow]]
**Type:** Method
**Line:** 4873

## Categories

- [[Taxonomy/public_method|public_method]]
