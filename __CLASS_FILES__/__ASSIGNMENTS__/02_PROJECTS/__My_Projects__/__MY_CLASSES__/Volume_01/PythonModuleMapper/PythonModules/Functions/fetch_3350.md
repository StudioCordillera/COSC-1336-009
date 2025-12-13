---
type: function
name: fetch
module: imaplib
lineno: 546
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: fetch()

## Overview

Fetch (parts of) messages.

(typ, [data, ...]) = <instance>.fetch(message_set, message_parts)

'message_parts' should be a string of selected parts
enclosed in parentheses, eg: "(UID BODY[TEXT])".

'data' are tuples of message part envelope and data.

```python
def fetch(self, message_set, message_parts)
```

**Module:** [[Modules/imaplib|imaplib]]
**Class:** [[Classes/IMAP4|IMAP4]]
**Type:** Method
**Line:** 546

## Categories

- [[Taxonomy/public_method|public_method]]
