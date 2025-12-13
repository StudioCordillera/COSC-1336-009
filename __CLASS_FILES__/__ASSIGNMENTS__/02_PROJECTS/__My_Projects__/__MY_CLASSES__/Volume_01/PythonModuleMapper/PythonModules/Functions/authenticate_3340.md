---
type: function
name: authenticate
module: imaplib
lineno: 429
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: authenticate()

## Overview

Authenticate command - requires response processing.

'mechanism' specifies which authentication mechanism is to
be used - it must appear in <instance>.capabilities in the
form AUTH=<mechanism>.

'authobject' must be a callable object:

        data = authobject(response)

It will be called to process server continuation responses; the
response argument it is passed will be a bytes.  It should return bytes
data that will be base64 encoded and sent to the server.  It should
return None if the client abort response '*' should be sent instead.

```python
def authenticate(self, mechanism, authobject)
```

**Module:** [[Modules/imaplib|imaplib]]
**Class:** [[Classes/IMAP4|IMAP4]]
**Type:** Method
**Line:** 429

## Categories

- [[Taxonomy/public_method|public_method]]
