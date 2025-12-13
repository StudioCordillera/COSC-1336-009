---
type: function
name: wm_attributes
module: tkinter
lineno: 2133
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: wm_attributes()

## Overview

Return or sets platform specific attributes.

When called with a single argument return_python_dict=True,
return a dict of the platform specific attributes and their values.
When called without arguments or with a single argument
return_python_dict=False, return a tuple containing intermixed
attribute names with the minus prefix and their values.

When called with a single string value, return the value for the
specific option.  When called with keyword arguments, set the
corresponding attributes.

```python
def wm_attributes(self)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Wm|Wm]]
**Type:** Method
**Line:** 2133

## Categories

- [[Taxonomy/public_method|public_method]]
