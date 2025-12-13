---
type: class
name: NewType
module: typing
lineno: 3390
tags:
  - python
  - class
---

# Class: NewType

## Overview

NewType creates simple unique types with almost zero runtime overhead.

NewType(name, tp) is considered a subtype of tp
by static type checkers. At runtime, NewType(name, tp) returns
a dummy callable that simply returns its argument.

Usage::

    UserId = NewType('UserId', int)

    def name_by_id(user_id: UserId) -> str:
        ...

    UserId('user')          # Fails type check

    name_by_id(42)          # Fails type check
    name_by_id(UserId(42))  # OK

    num = UserId(5) + 1     # type: int

**Module:** [[Modules/typing|typing]]
**Line:** 3390

## Methods

### Constructors
- [[Functions/__init___4808|__init__()]] (line 3414)

### Magic Methods
- [[Functions/__mro_entries___4809|__mro_entries__()]] (line 3424)
- [[Functions/__repr___4810|__repr__()]] (line 3439)
- [[Functions/__reduce___4811|__reduce__()]] (line 3442)
- [[Functions/__or___4812|__or__()]] (line 3445)
- [[Functions/__ror___4813|__ror__()]] (line 3448)
