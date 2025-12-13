---
type: function
name: _validate_value_types
module: configparser
lineno: 1203
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _validate_value_types()

## Overview

Raises a TypeError for non-string values.

The only legal non-string value if we allow valueless
options is None, so we need to check if the value is a
string if:
- we do not allow valueless options, or
- we allow valueless options but the value is not None

For compatibility reasons this method is not used in classic set()
for RawConfigParsers. It is invoked in every case for mapping protocol
access and in ConfigParser.set().

```python
def _validate_value_types(self)
```

**Module:** [[Modules/configparser|configparser]]
**Class:** [[Classes/RawConfigParser|RawConfigParser]]
**Type:** Method
**Line:** 1203

## Categories

- [[Taxonomy/protected_method|protected_method]]
