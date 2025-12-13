---
type: function
name: parseline
module: cmd
lineno: 180
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: parseline()

## Overview

Parse the line into a command name and a string containing
the arguments.  Returns a tuple containing (command, args, line).
'command' and 'args' may be None if the line couldn't be parsed.

```python
def parseline(self, line)
```

**Module:** [[Modules/cmd|cmd]]
**Class:** [[Classes/Cmd|Cmd]]
**Type:** Method
**Line:** 180

## Categories

- [[Taxonomy/public_method|public_method]]
