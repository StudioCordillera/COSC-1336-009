---
type: function
name: connect
module: smtplib
lineno: 315
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: connect()

## Overview

Connect to a host on a given port.

If the hostname ends with a colon (`:') followed by a number, and
there is no port specified, that suffix will be stripped off and the
number interpreted as the port number to use.

Note: This method is automatically invoked by __init__, if a host is
specified during instantiation.

```python
def connect(self, host, port, source_address)
```

**Module:** [[Modules/smtplib|smtplib]]
**Class:** [[Classes/SMTP|SMTP]]
**Type:** Method
**Line:** 315

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
