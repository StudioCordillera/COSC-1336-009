---
type: class
name: Instruction
module: dis
lineno: 351
tags:
  - python
  - class
---

# Class: Instruction

## Overview

Details for a bytecode operation.

Defined fields:
  opname - human readable name for operation
  opcode - numeric code for operation
  arg - numeric argument to operation (if any), otherwise None
  argval - resolved arg value (if known), otherwise same as arg
  argrepr - human readable description of operation argument
  offset - start index of operation within bytecode sequence
  start_offset - start index of operation within bytecode sequence including extended args if present;
                 otherwise equal to Instruction.offset
  starts_line - True if this opcode starts a source line, otherwise False
  line_number - source line number associated with this opcode (if any), otherwise None
  label - A label if this instruction is a jump target, otherwise None
  positions - Optional dis.Positions object holding the span of source code
              covered by this instruction
  cache_info - information about the format and content of the instruction's cache
                 entries (if any)

**Module:** [[Modules/dis|dis]]
**Line:** 351

## Methods

### Magic Methods
- [[Functions/__str___6182|__str__()]] (line 416)

### Methods
- [[Functions/oparg_6175|oparg()]] (line 373)
- [[Functions/baseopcode_6176|baseopcode()]] (line 378)
- [[Functions/baseopname_6177|baseopname()]] (line 386)
- [[Functions/cache_offset_6178|cache_offset()]] (line 394)
- [[Functions/end_offset_6179|end_offset()]] (line 399)
- [[Functions/jump_target_6180|jump_target()]] (line 404)
- [[Functions/is_jump_target_6181|is_jump_target()]] (line 412)
