---
type: function
name: set_debuglevel
module: ftplib
lineno: 172
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - mutator
---

# Function: set_debuglevel()

## Overview

Set the debugging level.
The required argument level means:
0: no debugging output (default)
1: print commands and responses but not body text etc.
2: also print raw lines read and sent before stripping CR/LF

```python
def set_debuglevel(self, level)
```

**Module:** [[Modules/ftplib|ftplib]]
**Class:** [[Classes/FTP|FTP]]
**Type:** Method
**Line:** 172

## Categories

- [[Taxonomy/mutator|mutator]]
