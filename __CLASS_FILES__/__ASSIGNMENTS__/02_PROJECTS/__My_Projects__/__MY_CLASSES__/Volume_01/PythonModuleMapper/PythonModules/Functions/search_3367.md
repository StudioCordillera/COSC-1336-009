---
type: function
name: search
module: imaplib
lineno: 729
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: search()

## Overview

Search mailbox for matching messages.

(typ, [data]) = <instance>.search(charset, criterion, ...)

'data' is space separated list of matching message numbers.
If UTF8 is enabled, charset MUST be None.

```python
def search(self, charset)
```

**Module:** [[Modules/imaplib|imaplib]]
**Class:** [[Classes/IMAP4|IMAP4]]
**Type:** Method
**Line:** 729

## Categories

- [[Taxonomy/public_method|public_method]]
