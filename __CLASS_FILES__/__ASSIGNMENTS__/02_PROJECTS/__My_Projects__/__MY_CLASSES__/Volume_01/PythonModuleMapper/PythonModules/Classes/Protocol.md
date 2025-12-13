---
type: class
name: Protocol
module: typing
lineno: 2162
tags:
  - python
  - class
---

# Class: Protocol

## Overview

Base class for protocol classes.

Protocol classes are defined as::

    class Proto(Protocol):
        def meth(self) -> int:
            ...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

    class C:
        def meth(self) -> int:
            return 0

    def func(x: Proto) -> int:
        return x.meth()

    func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

    class GenProto[T](Protocol):
        def meth(self) -> T:
            ...

**Module:** [[Modules/typing|typing]]
**Line:** 2162

## Inheritance

**Subclasses:**
- [[Classes/SupportsInt|SupportsInt]]
- [[Classes/SupportsFloat|SupportsFloat]]
- [[Classes/SupportsComplex|SupportsComplex]]
- [[Classes/SupportsBytes|SupportsBytes]]
- [[Classes/SupportsIndex|SupportsIndex]]
- [[Classes/SupportsAbs|SupportsAbs]]
- [[Classes/SupportsRound|SupportsRound]]
- [[Classes/_IdentityCallable|_IdentityCallable]]

## Methods

### Magic Methods
- [[Functions/__init_subclass___4764|__init_subclass__()]] (line 2199)
