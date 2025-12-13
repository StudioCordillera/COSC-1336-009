---
type: function
name: subn
module: re
lineno: 211
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: subn()

## Overview

Return a 2-tuple containing (new_string, number).
new_string is the string obtained by replacing the leftmost
non-overlapping occurrences of the pattern in the source
string by the replacement repl.  number is the number of
substitutions that were made. repl can be either a string or a
callable; if a string, backslash escapes in it are processed.
If it is a callable, it's passed the Match object and must
return a replacement string to be used.

```python
def subn(pattern, repl, string)
```

**Module:** [[Modules/re|re]]
**Type:** Module-level function
**Line:** 211
