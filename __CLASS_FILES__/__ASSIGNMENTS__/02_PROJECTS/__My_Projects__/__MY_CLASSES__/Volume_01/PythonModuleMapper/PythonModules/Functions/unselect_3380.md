---
type: function
name: unselect
module: imaplib
lineno: 915
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: unselect()

## Overview

Free server's resources associated with the selected mailbox
and returns the server to the authenticated state.
This command performs the same actions as CLOSE, except
that no messages are permanently removed from the currently
selected mailbox.

(typ, [data]) = <instance>.unselect()

```python
def unselect(self)
```

**Module:** [[Modules/imaplib|imaplib]]
**Class:** [[Classes/IMAP4|IMAP4]]
**Type:** Method
**Line:** 915

## Categories

- [[Taxonomy/public_method|public_method]]
