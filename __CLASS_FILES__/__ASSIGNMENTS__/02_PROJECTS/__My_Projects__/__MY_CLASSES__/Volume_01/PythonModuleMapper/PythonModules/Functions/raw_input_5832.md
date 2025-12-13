---
type: function
name: raw_input
module: code
lineno: 319
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: raw_input()

## Overview

Write a prompt and read a line.

The returned line does not include the trailing newline.
When the user enters the EOF key sequence, EOFError is raised.

The base implementation uses the built-in function
input(); a subclass may replace this with a different
implementation.

```python
def raw_input(self, prompt)
```

**Module:** [[Modules/code|code]]
**Class:** [[Classes/InteractiveConsole|InteractiveConsole]]
**Type:** Method
**Line:** 319

## Categories

- [[Taxonomy/public_method|public_method]]
