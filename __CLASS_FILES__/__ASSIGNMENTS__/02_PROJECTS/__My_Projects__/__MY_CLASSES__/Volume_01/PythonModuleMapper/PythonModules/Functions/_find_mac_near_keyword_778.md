---
type: function
name: _find_mac_near_keyword
module: uuid
lineno: 413
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _find_mac_near_keyword()

## Overview

Searches a command's output for a MAC address near a keyword.

Each line of words in the output is case-insensitively searched for
any of the given keywords.  Upon a match, get_word_index is invoked
to pick a word from the line, given the index of the match.  For
example, lambda i: 0 would get the first word on the line, while
lambda i: i - 1 would get the word preceding the keyword.

```python
def _find_mac_near_keyword(command, args, keywords, get_word_index)
```

**Module:** [[Modules/uuid|uuid]]
**Type:** Module-level function
**Line:** 413
