---
type: function
name: getfullargspec
module: inspect
lineno: 1331
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getfullargspec()

## Overview

Get the names and default values of a callable object's parameters.

A tuple of seven things is returned:
(args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations).
'args' is a list of the parameter names.
'varargs' and 'varkw' are the names of the * and ** parameters or None.
'defaults' is an n-tuple of the default values of the last n parameters.
'kwonlyargs' is a list of keyword-only parameter names.
'kwonlydefaults' is a dictionary mapping names from kwonlyargs to defaults.
'annotations' is a dictionary mapping parameter names to annotations.

Notable differences from inspect.signature():
  - the "self" parameter is always reported, even for bound methods
  - wrapper chains defined by __wrapped__ *not* unwrapped automatically

```python
def getfullargspec(func)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 1331
