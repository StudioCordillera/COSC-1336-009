---
type: function
name: TypeIs
module: typing
lineno: 947
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: TypeIs()

## Overview

Special typing construct for marking user-defined type predicate functions.

``TypeIs`` can be used to annotate the return type of a user-defined
type predicate function.  ``TypeIs`` only accepts a single type argument.
At runtime, functions marked this way should return a boolean and accept
at least one argument.

``TypeIs`` aims to benefit *type narrowing* -- a technique used by static
type checkers to determine a more precise type of an expression within a
program's code flow.  Usually type narrowing is done by analyzing
conditional code flow and applying the narrowing to a block of code.  The
conditional expression here is sometimes referred to as a "type predicate".

Sometimes it would be convenient to use a user-defined boolean function
as a type predicate.  Such a function should use ``TypeIs[...]`` or
``TypeGuard[...]`` as its return type to alert static type checkers to
this intention.  ``TypeIs`` usually has more intuitive behavior than
``TypeGuard``, but it cannot be used when the input and output types
are incompatible (e.g., ``list[object]`` to ``list[int]``) or when the
function does not return ``True`` for all instances of the narrowed type.

Using  ``-> TypeIs[NarrowedType]`` tells the static type checker that for
a given function:

1. The return value is a boolean.
2. If the return value is ``True``, the type of its argument
   is the intersection of the argument's original type and
   ``NarrowedType``.
3. If the return value is ``False``, the type of its argument
   is narrowed to exclude ``NarrowedType``.

For example::

    from typing import assert_type, final, TypeIs

    class Parent: pass
    class Child(Parent): pass
    @final
    class Unrelated: pass

    def is_parent(val: object) -> TypeIs[Parent]:
        return isinstance(val, Parent)

    def run(arg: Child | Unrelated):
        if is_parent(arg):
            # Type of ``arg`` is narrowed to the intersection
            # of ``Parent`` and ``Child``, which is equivalent to
            # ``Child``.
            assert_type(arg, Child)
        else:
            # Type of ``arg`` is narrowed to exclude ``Parent``,
            # so only ``Unrelated`` is left.
            assert_type(arg, Unrelated)

The type inside ``TypeIs`` must be consistent with the type of the
function's argument; if it is not, static type checkers will raise
an error.  An incorrectly written ``TypeIs`` function can lead to
unsound behavior in the type system; it is the user's responsibility
to write such functions in a type-safe manner.

``TypeIs`` also works with type variables.  For more information, see
PEP 742 (Narrowing types with ``TypeIs``).

```python
@_SpecialForm
def TypeIs(self, parameters)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 947
