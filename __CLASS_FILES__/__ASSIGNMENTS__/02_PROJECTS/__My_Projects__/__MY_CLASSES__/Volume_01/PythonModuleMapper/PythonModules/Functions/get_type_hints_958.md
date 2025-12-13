---
type: function
name: get_type_hints
module: typing
lineno: 2403
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_type_hints()

## Overview

Return type hints for an object.

This is often the same as obj.__annotations__, but it handles
forward references encoded as string literals and recursively replaces all
'Annotated[T, ...]' with 'T' (unless 'include_extras=True').

The argument may be a module, class, method, or function. The annotations
are returned as a dictionary. For classes, annotations include also
inherited members.

TypeError is raised if the argument is not of a type that can contain
annotations, and an empty dictionary is returned if no annotations are
present.

BEWARE -- the behavior of globalns and localns is counterintuitive
(unless you are familiar with how eval() and exec() work).  The
search order is locals first, then globals.

- If no dict arguments are passed, an attempt is made to use the
  globals from obj (or the respective module's globals for classes),
  and these are also used as the locals.  If the object does not appear
  to have globals, an empty dictionary is used.  For classes, the search
  order is globals first then locals.

- If one dict argument is passed, it is used for both globals and
  locals.

- If two dict arguments are passed, they specify globals and
  locals, respectively.

```python
def get_type_hints(obj, globalns, localns, include_extras)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 2403

## Categories

- [[Taxonomy/accessor|accessor]]
