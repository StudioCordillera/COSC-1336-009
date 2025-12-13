---
type: function
name: expunge
module: imaplib
lineno: 532
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: expunge()

## Overview

Permanently remove deleted items from selected mailbox.

Generates 'EXPUNGE' response for each deleted message.

(typ, [data]) = <instance>.expunge()

'data' is list of 'EXPUNGE'd message numbers in order received.

```python
def expunge(self)
```

**Module:** [[Modules/imaplib|imaplib]]
**Class:** [[Classes/IMAP4|IMAP4]]
**Type:** Method
**Line:** 532

## Categories

- [[Taxonomy/public_method|public_method]]
