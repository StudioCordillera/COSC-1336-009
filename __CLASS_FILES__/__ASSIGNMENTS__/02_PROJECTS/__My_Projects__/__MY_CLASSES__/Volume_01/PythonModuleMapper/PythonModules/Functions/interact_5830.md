---
type: function
name: interact
module: code
lineno: 205
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: interact()

## Overview

Closely emulate the interactive Python console.

The optional banner argument specifies the banner to print
before the first interaction; by default it prints a banner
similar to the one printed by the real Python interpreter,
followed by the current class name in parentheses (so as not
to confuse this with the real interpreter -- since it's so
close!).

The optional exitmsg argument specifies the exit message
printed when exiting. Pass the empty string to suppress
printing an exit message. If exitmsg is not given or None,
a default message is printed.

```python
def interact(self, banner, exitmsg)
```

**Module:** [[Modules/code|code]]
**Class:** [[Classes/InteractiveConsole|InteractiveConsole]]
**Type:** Method
**Line:** 205

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
