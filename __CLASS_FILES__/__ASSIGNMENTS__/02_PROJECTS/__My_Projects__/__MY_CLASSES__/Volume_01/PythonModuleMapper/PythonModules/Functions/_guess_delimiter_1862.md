---
type: function
name: _guess_delimiter
module: csv
lineno: 349
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _guess_delimiter()

## Overview

The delimiter /should/ occur the same number of times on
each row. However, due to malformed data, it may not. We don't want
an all or nothing approach, so we allow for small variations in this
number.
  1) build a table of the frequency of each character on every line.
  2) build a table of frequencies of this frequency (meta-frequency?),
     e.g.  'x occurred 5 times in 10 rows, 6 times in 1000 rows,
     7 times in 2 rows'
  3) use the mode of the meta-frequency to determine the /expected/
     frequency for that character
  4) find out how often the character actually meets that goal
  5) the character that best meets its goal is the delimiter
For performance reasons, the data is evaluated in chunks, so it can
try and evaluate the smallest portion of the data possible, evaluating
additional chunks as necessary.

```python
def _guess_delimiter(self, data, delimiters)
```

**Module:** [[Modules/csv|csv]]
**Class:** [[Classes/Sniffer|Sniffer]]
**Type:** Method
**Line:** 349

## Categories

- [[Taxonomy/protected_method|protected_method]]
