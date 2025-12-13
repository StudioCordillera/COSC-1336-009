---
type: function
name: __init__
module: pprint
lineno: 107
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: __init__()

## Overview

Handle pretty printing operations onto a stream using a set of
configured parameters.

indent
    Number of spaces to indent for each level of nesting.

width
    Attempted maximum number of columns in the output.

depth
    The maximum depth to print out nested structures.

stream
    The desired output stream.  If omitted (or false), the standard
    output stream available at construction will be used.

compact
    If true, several items will be combined in one line.

sort_dicts
    If true, dict keys are sorted.

underscore_numbers
    If true, digit groups are separated with underscores.

```python
def __init__(self, indent, width, depth, stream)
```

**Module:** [[Modules/pprint|pprint]]
**Class:** [[Classes/PrettyPrinter|PrettyPrinter]]
**Type:** Method
**Line:** 107
