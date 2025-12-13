---
type: function
name: _guess_quote_and_delimiter
module: csv
lineno: 273
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _guess_quote_and_delimiter()

## Overview

Looks for text enclosed between two identical quotes
(the probable quotechar) which are preceded and followed
by the same character (the probable delimiter).
For example:
                 ,'some text',
The quote with the most wins, same with the delimiter.
If there is no quotechar the delimiter can't be determined
this way.

```python
def _guess_quote_and_delimiter(self, data, delimiters)
```

**Module:** [[Modules/csv|csv]]
**Class:** [[Classes/Sniffer|Sniffer]]
**Type:** Method
**Line:** 273

## Categories

- [[Taxonomy/protected_method|protected_method]]
