---
type: class
name: deprecated
module: warnings
lineno: 518
tags:
  - python
  - class
---

# Class: deprecated

## Overview

Indicate that a class, function or overload is deprecated.

When this decorator is applied to an object, the type checker
will generate a diagnostic on usage of the deprecated object.

Usage:

    @deprecated("Use B instead")
    class A:
        pass

    @deprecated("Use g instead")
    def f():
        pass

    @overload
    @deprecated("int support is deprecated")
    def g(x: int) -> int: ...
    @overload
    def g(x: str) -> int: ...

The warning specified by *category* will be emitted at runtime
on use of deprecated objects. For functions, that happens on calls;
for classes, on instantiation and on creation of subclasses.
If the *category* is ``None``, no warning is emitted at runtime.
The *stacklevel* determines where the
warning is emitted. If it is ``1`` (the default), the warning
is emitted at the direct caller of the deprecated object; if it
is higher, it is emitted further up the stack.
Static type checker behavior is not affected by the *category*
and *stacklevel* arguments.

The deprecation message passed to the decorator is saved in the
``__deprecated__`` attribute on the decorated object.
If applied to an overload, the decorator
must be after the ``@overload`` decorator for the attribute to
exist on the overload as returned by ``get_overloads()``.

See PEP 702 for details.

**Module:** [[Modules/warnings|warnings]]
**Line:** 518

## Methods

### Constructors
- [[Functions/__init___5476|__init__()]] (line 560)

### Magic Methods
- [[Functions/__call___5477|__call__()]] (line 576)
