---
type: function
name: showsyntaxerror
module: code
lineno: 98
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: showsyntaxerror()

## Overview

Display the syntax error that just occurred.

This doesn't display a stack trace because there isn't one.

If a filename is given, it is stuffed in the exception instead
of what was there before (because Python's parser always uses
"<string>" when reading from a string).

The output is written by self.write(), below.

```python
def showsyntaxerror(self, filename)
```

**Module:** [[Modules/code|code]]
**Class:** [[Classes/InteractiveInterpreter|InteractiveInterpreter]]
**Type:** Method
**Line:** 98

## Categories

- [[Taxonomy/public_method|public_method]]
