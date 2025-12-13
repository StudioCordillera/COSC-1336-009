---
type: class
name: FrameSummary
module: traceback
lineno: 276
tags:
  - python
  - class
---

# Class: FrameSummary

## Overview

Information about a single frame from a traceback.

- :attr:`filename` The filename for the frame.
- :attr:`lineno` The line within filename for the frame that was
  active when the frame was captured.
- :attr:`name` The name of the function or method that was executing
  when the frame was captured.
- :attr:`line` The text from the linecache module for the
  of code that was running when the frame was captured.
- :attr:`locals` Either None if locals were not supplied, or a dict
  mapping the name to the repr() of the variable.

**Module:** [[Modules/traceback|traceback]]
**Line:** 276

## Methods

### Constructors
- [[Functions/__init___5612|__init__()]] (line 293)

### Magic Methods
- [[Functions/__eq___5613|__eq__()]] (line 319)
- [[Functions/__getitem___5614|__getitem__()]] (line 329)
- [[Functions/__iter___5615|__iter__()]] (line 332)
- [[Functions/__repr___5616|__repr__()]] (line 335)
- [[Functions/__len___5617|__len__()]] (line 339)

### Methods
- [[Functions/_set_lines_5618|_set_lines()]] (line 342)
- [[Functions/_original_lines_5619|_original_lines()]] (line 358)
- [[Functions/_dedented_lines_5620|_dedented_lines()]] (line 364)
- [[Functions/line_5621|line()]] (line 372)
