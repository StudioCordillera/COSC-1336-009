---
type: function
name: starttls
module: smtplib
lineno: 752
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: starttls()

## Overview

Puts the connection to the SMTP server into TLS mode.

If there has been no previous EHLO or HELO command this session, this
method tries ESMTP EHLO first.

If the server supports TLS, this will encrypt the rest of the SMTP
session. If you provide the context parameter,
the identity of the SMTP server and client can be checked. This,
however, depends on whether the socket module really checks the
certificates.

This method may raise the following exceptions:

 SMTPHeloError            The server didn't reply properly to
                          the helo greeting.

```python
def starttls(self)
```

**Module:** [[Modules/smtplib|smtplib]]
**Class:** [[Classes/SMTP|SMTP]]
**Type:** Method
**Line:** 752

## Categories

- [[Taxonomy/public_method|public_method]]
