---
type: function
name: read_dict
module: configparser
lineno: 765
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: read_dict()

## Overview

Read configuration from a dictionary.

Keys are section names, values are dictionaries with keys and values
that should be present in the section. If the used dictionary type
preserves order, sections and their keys will be added in order.

All types held in the dictionary are converted to strings during
reading, including section names, option names and keys.

Optional second argument is the `source` specifying the name of the
dictionary being read.

```python
def read_dict(self, dictionary, source)
```

**Module:** [[Modules/configparser|configparser]]
**Class:** [[Classes/RawConfigParser|RawConfigParser]]
**Type:** Method
**Line:** 765

## Categories

- [[Taxonomy/public_method|public_method]]
