---
type: function
name: getreply
module: smtplib
lineno: 380
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: getreply()

## Overview

Get a reply from the server.

Returns a tuple consisting of:

  - server response code (e.g. '250', or such, if all goes well)
    Note: returns -1 if it can't read response code.

  - server response string corresponding to response code (multiline
    responses are converted to a single, multiline string).

Raises SMTPServerDisconnected if end-of-file is reached.

```python
def getreply(self)
```

**Module:** [[Modules/smtplib|smtplib]]
**Class:** [[Classes/SMTP|SMTP]]
**Type:** Method
**Line:** 380

## Categories

- [[Taxonomy/public_method|public_method]]
