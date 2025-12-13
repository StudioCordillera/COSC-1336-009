---
type: function
name: run_docstring_examples
module: doctest
lineno: 2210
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: run_docstring_examples()

## Overview

Test examples in the given object's docstring (`f`), using `globs`
as globals.  Optional argument `name` is used in failure messages.
If the optional argument `verbose` is true, then generate output
even if there are no failures.

`compileflags` gives the set of flags that should be used by the
Python compiler when running the examples.  If not specified, then
it will default to the set of future-import flags that apply to
`globs`.

Optional keyword arg `optionflags` specifies options for the
testing and output.  See the documentation for `testmod` for more
information.

```python
def run_docstring_examples(f, globs, verbose, name, compileflags, optionflags)
```

**Module:** [[Modules/doctest|doctest]]
**Type:** Module-level function
**Line:** 2210
