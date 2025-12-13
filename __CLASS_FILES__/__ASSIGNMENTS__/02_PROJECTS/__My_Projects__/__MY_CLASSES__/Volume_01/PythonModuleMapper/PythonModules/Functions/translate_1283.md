---
type: function
name: translate
module: glob
lineno: 267
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: translate()

## Overview

Translate a pathname with shell wildcards to a regular expression.

If `recursive` is true, the pattern segment '**' will match any number of
path segments.

If `include_hidden` is true, wildcards can match path segments beginning
with a dot ('.').

If a sequence of separator characters is given to `seps`, they will be
used to split the pattern into segments and match path separators. If not
given, os.path.sep and os.path.altsep (where available) are used.

```python
def translate(pat)
```

**Module:** [[Modules/glob|glob]]
**Type:** Module-level function
**Line:** 267
