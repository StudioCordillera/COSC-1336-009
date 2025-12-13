---
type: function
name: gnu_getopt
module: getopt
lineno: 99
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: gnu_getopt()

## Overview

getopt(args, options[, long_options]) -> opts, args

This function works like getopt(), except that GNU style scanning
mode is used by default. This means that option and non-option
arguments may be intermixed. The getopt() function stops
processing options as soon as a non-option argument is
encountered.

If the first character of the option string is `+', or if the
environment variable POSIXLY_CORRECT is set, then option
processing stops as soon as a non-option argument is encountered.

```python
def gnu_getopt(args, shortopts, longopts)
```

**Module:** [[Modules/getopt|getopt]]
**Type:** Module-level function
**Line:** 99
