---
type: function
name: list2cmdline
module: subprocess
lineno: 582
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: list2cmdline()

## Overview

Translate a sequence of arguments into a command line
string, using the same rules as the MS C runtime:

1) Arguments are delimited by white space, which is either a
   space or a tab.

2) A string surrounded by double quotation marks is
   interpreted as a single argument, regardless of white space
   contained within.  A quoted string can be embedded in an
   argument.

3) A double quotation mark preceded by a backslash is
   interpreted as a literal double quotation mark.

4) Backslashes are interpreted literally, unless they
   immediately precede a double quotation mark.

5) If backslashes immediately precede a double quotation mark,
   every pair of backslashes is interpreted as a literal
   backslash.  If the number of backslashes is odd, the last
   backslash escapes the next double quotation mark as
   described in rule 3.

```python
def list2cmdline(seq)
```

**Module:** [[Modules/subprocess|subprocess]]
**Type:** Module-level function
**Line:** 582
