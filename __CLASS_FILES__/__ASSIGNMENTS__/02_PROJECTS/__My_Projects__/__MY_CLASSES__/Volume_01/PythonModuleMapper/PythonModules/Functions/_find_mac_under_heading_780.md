---
type: function
name: _find_mac_under_heading
module: uuid
lineno: 476
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _find_mac_under_heading()

## Overview

Looks for a MAC address under a heading in a command's output.

The first line of words in the output is searched for the given
heading. Words at the same word index as the heading in subsequent
lines are then examined to see if they look like MAC addresses.

```python
def _find_mac_under_heading(command, args, heading)
```

**Module:** [[Modules/uuid|uuid]]
**Type:** Module-level function
**Line:** 476
