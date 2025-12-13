---
type: function
name: getdefaultlocale
module: locale
lineno: 519
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getdefaultlocale()

## Overview

Tries to determine the default locale settings and returns
them as tuple (language code, encoding).

According to POSIX, a program which has not called
setlocale(LC_ALL, "") runs using the portable 'C' locale.
Calling setlocale(LC_ALL, "") lets it use the default locale as
defined by the LANG variable. Since we don't want to interfere
with the current locale setting we thus emulate the behavior
in the way described above.

To maintain compatibility with other platforms, not only the
LANG variable is tested, but a list of variables given as
envvars parameter. The first found to be defined will be
used. envvars defaults to the search path used in GNU gettext;
it must always contain the variable name 'LANG'.

Except for the code 'C', the language code corresponds to RFC
1766.  code and encoding can be None in case the values cannot
be determined.

```python
def getdefaultlocale(envvars)
```

**Module:** [[Modules/locale|locale]]
**Type:** Module-level function
**Line:** 519
