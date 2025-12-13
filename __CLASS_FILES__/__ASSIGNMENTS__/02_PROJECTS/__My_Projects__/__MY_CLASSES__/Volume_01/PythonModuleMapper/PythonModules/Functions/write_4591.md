---
type: function
name: write
module: tkinter
lineno: 4454
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: write()

## Overview

Writes image data from the image to a file named FILENAME.

The FORMAT option specifies the name of the image file format
handler to be used to write the data to the file.  If this option
is not given, the format is guessed from the file extension.

The FROM_COORDS option specifies a rectangular region of the image
to be written to the image file.  It must be a tuple or a list of 1
to 4 integers (x1, y1, x2, y2).  If only x1 and y1 are specified,
the region extends from (x1,y1) to the bottom-right corner of the
image.  If all four coordinates are given, they specify diagonally
opposite corners of the rectangular region.  The default, if this
option is not given, is the whole image.

If BACKGROUND is specified, the data will not contain any
transparency information.  In all transparent pixels the color will
be replaced by the specified color.

If GRAYSCALE is true, the data will not contain color information.
All pixel data will be transformed into grayscale.

```python
def write(self, filename, format, from_coords)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/PhotoImage|PhotoImage]]
**Type:** Method
**Line:** 4454

## Categories

- [[Taxonomy/public_method|public_method]]
