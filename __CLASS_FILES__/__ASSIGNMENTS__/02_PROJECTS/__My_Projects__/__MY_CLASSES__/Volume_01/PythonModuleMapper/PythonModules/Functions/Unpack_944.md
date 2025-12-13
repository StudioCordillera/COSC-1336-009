---
type: function
name: Unpack
module: typing
lineno: 1827
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: Unpack()

## Overview

Type unpack operator.

The type unpack operator takes the child types from some container type,
such as `tuple[int, str]` or a `TypeVarTuple`, and 'pulls them out'.

For example::

    # For some generic class `Foo`:
    Foo[Unpack[tuple[int, str]]]  # Equivalent to Foo[int, str]

    Ts = TypeVarTuple('Ts')
    # Specifies that `Bar` is generic in an arbitrary number of types.
    # (Think of `Ts` as a tuple of an arbitrary number of individual
    #  `TypeVar`s, which the `Unpack` is 'pulling out' directly into the
    #  `Generic[]`.)
    class Bar(Generic[Unpack[Ts]]): ...
    Bar[int]  # Valid
    Bar[int, str]  # Also valid

From Python 3.11, this can also be done using the `*` operator::

    Foo[*tuple[int, str]]
    class Bar(Generic[*Ts]): ...

And from Python 3.12, it can be done using built-in syntax for generics::

    Foo[*tuple[int, str]]
    class Bar[*Ts]: ...

The operator can also be used along with a `TypedDict` to annotate
`**kwargs` in a function signature::

    class Movie(TypedDict):
        name: str
        year: int

    # This function expects two keyword arguments - *name* of type `str` and
    # *year* of type `int`.
    def foo(**kwargs: Unpack[Movie]): ...

Note that there is only some runtime checking of this operator. Not
everything the runtime allows may be accepted by static type checkers.

For more information, see PEPs 646 and 692.

```python
@_SpecialForm
def Unpack(self, parameters)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 1827
