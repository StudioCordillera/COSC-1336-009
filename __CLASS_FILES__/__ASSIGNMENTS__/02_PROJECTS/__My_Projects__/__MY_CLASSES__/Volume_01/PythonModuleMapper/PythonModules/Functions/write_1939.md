---
type: function
name: write
module: configparser
lineno: 936
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: write()

## Overview

Write an .ini-format representation of the configuration state.

If `space_around_delimiters` is True (the default), delimiters
between keys and values are surrounded by spaces.

Please note that comments in the original configuration file are not
preserved when writing the configuration back.

```python
def write(self, fp, space_around_delimiters)
```

**Module:** [[Modules/configparser|configparser]]
**Class:** [[Classes/RawConfigParser|RawConfigParser]]
**Type:** Method
**Line:** 936

## Categories

- [[Taxonomy/public_method|public_method]]
