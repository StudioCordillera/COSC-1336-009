---
type: function
name: wm_iconphoto
module: tkinter
lineno: 2293
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: wm_iconphoto()

## Overview

Sets the titlebar icon for this window based on the named photo
images passed through args. If default is True, this is applied to
all future created toplevels as well.

The data in the images is taken as a snapshot at the time of
invocation. If the images are later changed, this is not reflected
to the titlebar icons. Multiple images are accepted to allow
different images sizes to be provided. The window manager may scale
provided icons to an appropriate size.

On Windows, the images are packed into a Windows icon structure.
This will override an icon specified to wm_iconbitmap, and vice
versa.

On X, the images are arranged into the _NET_WM_ICON X property,
which most modern window managers support. An icon specified by
wm_iconbitmap may exist simultaneously.

On Macintosh, this currently does nothing.

```python
def wm_iconphoto(self, default)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Wm|Wm]]
**Type:** Method
**Line:** 2293

## Categories

- [[Taxonomy/public_method|public_method]]
