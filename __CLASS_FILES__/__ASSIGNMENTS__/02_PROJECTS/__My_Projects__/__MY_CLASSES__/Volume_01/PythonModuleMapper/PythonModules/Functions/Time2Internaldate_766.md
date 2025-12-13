---
type: function
name: Time2Internaldate
module: imaplib
lineno: 1496
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: Time2Internaldate()

## Overview

Convert date_time to IMAP4 INTERNALDATE representation.

Return string in form: '"DD-Mmm-YYYY HH:MM:SS +HHMM"'.  The
date_time argument can be a number (int or float) representing
seconds since epoch (as returned by time.time()), a 9-tuple
representing local time, an instance of time.struct_time (as
returned by time.localtime()), an aware datetime instance or a
double-quoted string.  In the last case, it is assumed to already
be in the correct format.

```python
def Time2Internaldate(date_time)
```

**Module:** [[Modules/imaplib|imaplib]]
**Type:** Module-level function
**Line:** 1496
