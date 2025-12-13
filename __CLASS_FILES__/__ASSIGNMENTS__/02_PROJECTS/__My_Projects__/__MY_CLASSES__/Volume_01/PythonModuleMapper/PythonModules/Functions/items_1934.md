---
type: function
name: items
module: configparser
lineno: 862
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: items()

## Overview

Return a list of (name, value) tuples for each option in a section.

All % interpolations are expanded in the return values, based on the
defaults passed into the constructor, unless the optional argument
`raw` is true.  Additional substitutions may be provided using the
`vars` argument, which must be a dictionary whose contents overrides
any pre-existing defaults.

The section DEFAULT is special.

```python
def items(self, section, raw, vars)
```

**Module:** [[Modules/configparser|configparser]]
**Class:** [[Classes/RawConfigParser|RawConfigParser]]
**Type:** Method
**Line:** 862

## Categories

- [[Taxonomy/public_method|public_method]]
