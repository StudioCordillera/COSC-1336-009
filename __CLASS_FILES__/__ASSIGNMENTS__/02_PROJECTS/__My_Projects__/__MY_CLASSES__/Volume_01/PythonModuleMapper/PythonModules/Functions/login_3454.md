---
type: function
name: login
module: smtplib
lineno: 686
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: login()

## Overview

Log in on an SMTP server that requires authentication.

The arguments are:
    - user:         The user name to authenticate with.
    - password:     The password for the authentication.

Keyword arguments:
    - initial_response_ok: Allow sending the RFC 4954 initial-response
      to the AUTH command, if the authentication methods supports it.

If there has been no previous EHLO or HELO command this session, this
method tries ESMTP EHLO first.

This method will return normally if the authentication was successful.

This method may raise the following exceptions:

 SMTPHeloError            The server didn't reply properly to
                          the helo greeting.
 SMTPAuthenticationError  The server didn't accept the username/
                          password combination.
 SMTPNotSupportedError    The AUTH command is not supported by the
                          server.
 SMTPException            No suitable authentication method was
                          found.

```python
def login(self, user, password)
```

**Module:** [[Modules/smtplib|smtplib]]
**Class:** [[Classes/SMTP|SMTP]]
**Type:** Method
**Line:** 686

## Categories

- [[Taxonomy/public_method|public_method]]
