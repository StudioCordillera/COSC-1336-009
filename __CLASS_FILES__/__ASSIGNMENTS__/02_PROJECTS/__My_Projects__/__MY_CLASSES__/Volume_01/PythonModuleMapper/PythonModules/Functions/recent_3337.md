---
type: function
name: recent
module: imaplib
lineno: 372
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: recent()

## Overview

Return most recent 'RECENT' responses if any exist,
else prompt server for an update using the 'NOOP' command.

(typ, [data]) = <instance>.recent()

'data' is None if no new messages,
else list of RECENT responses, most recent last.

```python
def recent(self)
```

**Module:** [[Modules/imaplib|imaplib]]
**Class:** [[Classes/IMAP4|IMAP4]]
**Type:** Method
**Line:** 372

## Categories

- [[Taxonomy/public_method|public_method]]
