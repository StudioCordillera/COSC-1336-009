---
type: function
name: select
module: imaplib
lineno: 747
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: select()

## Overview

Select a mailbox.

Flush all untagged responses.

(typ, [data]) = <instance>.select(mailbox='INBOX', readonly=False)

'data' is count of messages in mailbox ('EXISTS' response).

Mandated responses are ('FLAGS', 'EXISTS', 'RECENT', 'UIDVALIDITY'), so
other responses should be obtained via <instance>.response('FLAGS') etc.

```python
def select(self, mailbox, readonly)
```

**Module:** [[Modules/imaplib|imaplib]]
**Class:** [[Classes/IMAP4|IMAP4]]
**Type:** Method
**Line:** 747

## Categories

- [[Taxonomy/public_method|public_method]]
