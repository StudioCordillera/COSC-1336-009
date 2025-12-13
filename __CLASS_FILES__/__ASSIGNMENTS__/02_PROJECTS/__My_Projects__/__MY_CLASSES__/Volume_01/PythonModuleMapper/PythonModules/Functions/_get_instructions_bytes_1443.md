---
type: function
name: _get_instructions_bytes
module: dis
lineno: 705
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: _get_instructions_bytes()

## Overview

Iterate over the instructions in a bytecode string.

Generates a sequence of Instruction namedtuples giving the details of each
opcode.

```python
def _get_instructions_bytes(code, linestarts, line_offset, co_positions, original_code, arg_resolver)
```

**Module:** [[Modules/dis|dis]]
**Type:** Module-level function
**Line:** 705

## Categories

- [[Taxonomy/accessor|accessor]]
