---
type: function
name: get_instructions
module: dis
lineno: 606
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_instructions()

## Overview

Iterator for the opcodes in methods, functions or code

Generates a series of Instruction named tuples giving the details of
each operations in the supplied code.

If *first_line* is not None, it indicates the line number that should
be reported for the first source line in the disassembled code.
Otherwise, the source line information (if any) is taken directly from
the disassembled code object.

```python
def get_instructions(x)
```

**Module:** [[Modules/dis|dis]]
**Type:** Module-level function
**Line:** 606

## Categories

- [[Taxonomy/accessor|accessor]]
