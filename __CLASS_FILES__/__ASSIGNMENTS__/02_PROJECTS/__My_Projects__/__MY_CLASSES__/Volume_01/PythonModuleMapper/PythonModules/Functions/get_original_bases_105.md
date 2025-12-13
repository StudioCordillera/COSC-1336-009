---
type: function
name: get_original_bases
module: types
lineno: 148
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_original_bases()

## Overview

Return the class's "original" bases prior to modification by `__mro_entries__`.

Examples::

    from typing import TypeVar, Generic, NamedTuple, TypedDict

    T = TypeVar("T")
    class Foo(Generic[T]): ...
    class Bar(Foo[int], float): ...
    class Baz(list[str]): ...
    Eggs = NamedTuple("Eggs", [("a", int), ("b", str)])
    Spam = TypedDict("Spam", {"a": int, "b": str})

    assert get_original_bases(Bar) == (Foo[int], float)
    assert get_original_bases(Baz) == (list[str],)
    assert get_original_bases(Eggs) == (NamedTuple,)
    assert get_original_bases(Spam) == (TypedDict,)
    assert get_original_bases(int) == (object,)

```python
def get_original_bases()
```

**Module:** [[Modules/types|types]]
**Type:** Module-level function
**Line:** 148

## Categories

- [[Taxonomy/accessor|accessor]]
