---
type: function
name: __call__
module: enum
lineno: 695
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: __call__()

## Overview

Either returns an existing member, or creates a new enum class.

This method is used both when an enum class is given a value to match
to an enumeration member (i.e. Color(3)) and for the functional API
(i.e. Color = Enum('Color', names='RED GREEN BLUE')).

The value lookup branch is chosen if the enum is final.

When used for the functional API:

`value` will be the name of the new class.

`names` should be either a string of white-space/comma delimited names
(values will start at `start`), or an iterator/mapping of name, value pairs.

`module` should be set to the module this class is being created in;
if it is not set, an attempt to find that module will be made, but if
it fails the class will not be picklable.

`qualname` should be set to the actual location this class can be found
at in its module; by default it is set to the global scope.  If this is
not correct, unpickling will fail in some circumstances.

`type`, if set, will be mixed in as the first base class.

```python
def __call__(cls, value, names)
```

**Module:** [[Modules/enum|enum]]
**Class:** [[Classes/EnumType|EnumType]]
**Type:** Method
**Line:** 695
