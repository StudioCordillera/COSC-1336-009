---
type: function
name: xatom
module: imaplib
lineno: 931
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: xatom()

## Overview

Allow simple extension commands
        notified by server in CAPABILITY response.

Assumes command is legal in current state.

(typ, [data]) = <instance>.xatom(name, arg, ...)

Returns response appropriate to extension command `name'.

```python
def xatom(self, name)
```

**Module:** [[Modules/imaplib|imaplib]]
**Class:** [[Classes/IMAP4|IMAP4]]
**Type:** Method
**Line:** 931

## Categories

- [[Taxonomy/public_method|public_method]]
