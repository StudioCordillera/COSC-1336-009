---
type: function
name: compile_command
module: codeop
lineno: 84
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: compile_command()

## Overview

Compile a command and determine whether it is incomplete.

Arguments:

source -- the source string; may contain \n characters
filename -- optional filename from which source was read; default
            "<input>"
symbol -- optional grammar start symbol; "single" (default), "exec"
          or "eval"

Return value / exceptions raised:

- Return a code object if the command is complete and valid
- Return None if the command is incomplete
- Raise SyntaxError, ValueError or OverflowError if the command is a
  syntax error (OverflowError and ValueError can be produced by
  malformed literals).

```python
def compile_command(source, filename, symbol)
```

**Module:** [[Modules/codeop|codeop]]
**Type:** Module-level function
**Line:** 84
