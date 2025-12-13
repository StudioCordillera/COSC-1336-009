---
type: function
name: TypeGuard
module: typing
lineno: 891
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: TypeGuard()

## Overview

Special typing construct for marking user-defined type predicate functions.

``TypeGuard`` can be used to annotate the return type of a user-defined
type predicate function.  ``TypeGuard`` only accepts a single type argument.
At runtime, functions marked this way should return a boolean.

``TypeGuard`` aims to benefit *type narrowing* -- a technique used by static
type checkers to determine a more precise type of an expression within a
program's code flow.  Usually type narrowing is done by analyzing
conditional code flow and applying the narrowing to a block of code.  The
conditional expression here is sometimes referred to as a "type predicate".

Sometimes it would be convenient to use a user-defined boolean function
as a type predicate.  Such a function should use ``TypeGuard[...]`` or
``TypeIs[...]`` as its return type to alert static type checkers to
this intention. ``TypeGuard`` should be used over ``TypeIs`` when narrowing
from an incompatible type (e.g., ``list[object]`` to ``list[int]``) or when
the function does not return ``True`` for all instances of the narrowed type.

Using  ``-> TypeGuard[NarrowedType]`` tells the static type checker that
for a given function:

1. The return value is a boolean.
2. If the return value is ``True``, the type of its argument
   is ``NarrowedType``.

For example::

     def is_str_list(val: list[object]) -> TypeGuard[list[str]]:
         '''Determines whether all objects in the list are strings'''
         return all(isinstance(x, str) for x in val)

     def func1(val: list[object]):
         if is_str_list(val):
             # Type of ``val`` is narrowed to ``list[str]``.
             print(" ".join(val))
         else:
             # Type of ``val`` remains as ``list[object]``.
             print("Not a list of strings!")

Strict type narrowing is not enforced -- ``TypeB`` need not be a narrower
form of ``TypeA`` (it can even be a wider form) and this may lead to
type-unsafe results.  The main reason is to allow for things like
narrowing ``list[object]`` to ``list[str]`` even though the latter is not
a subtype of the former, since ``list`` is invariant.  The responsibility of
writing type-safe type predicates is left to the user.

``TypeGuard`` also works with type variables.  For more information, see
PEP 647 (User-Defined Type Guards).

```python
@_SpecialForm
def TypeGuard(self, parameters)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 891
