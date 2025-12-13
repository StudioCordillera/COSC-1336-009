---
type: function
name: runsource
module: code
lineno: 40
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: runsource()

## Overview

Compile and run some source in the interpreter.

Arguments are as for compile_command().

One of several things can happen:

1) The input is incorrect; compile_command() raised an
exception (SyntaxError or OverflowError).  A syntax traceback
will be printed by calling the showsyntaxerror() method.

2) The input is incomplete, and more input is required;
compile_command() returned None.  Nothing happens.

3) The input is complete; compile_command() returned a code
object.  The code is executed by calling self.runcode() (which
also handles run-time exceptions, except for SystemExit).

The return value is True in case 2, False in the other cases (unless
an exception is raised).  The return value can be used to
decide whether to use sys.ps1 or sys.ps2 to prompt the next
line.

```python
def runsource(self, source, filename, symbol)
```

**Module:** [[Modules/code|code]]
**Class:** [[Classes/InteractiveInterpreter|InteractiveInterpreter]]
**Type:** Method
**Line:** 40

## Categories

- [[Taxonomy/public_method|public_method]]
