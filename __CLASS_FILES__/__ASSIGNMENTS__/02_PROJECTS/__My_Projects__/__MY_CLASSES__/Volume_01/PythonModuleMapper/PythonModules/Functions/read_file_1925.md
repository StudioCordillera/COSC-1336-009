---
type: function
name: read_file
module: configparser
lineno: 745
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: read_file()

## Overview

Like read() but the argument must be a file-like object.

The `f` argument must be iterable, returning one line at a time.
Optional second argument is the `source` specifying the name of the
file being read. If not given, it is taken from f.name. If `f` has no
`name` attribute, `<???>` is used.

```python
def read_file(self, f, source)
```

**Module:** [[Modules/configparser|configparser]]
**Class:** [[Classes/RawConfigParser|RawConfigParser]]
**Type:** Method
**Line:** 745

## Categories

- [[Taxonomy/public_method|public_method]]
