---
type: function
name: ehlo_or_helo_if_needed
module: smtplib
lineno: 599
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: ehlo_or_helo_if_needed()

## Overview

Call self.ehlo() and/or self.helo() if needed.

If there has been no previous EHLO or HELO command this session, this
method tries ESMTP EHLO first.

This method may raise the following exceptions:

 SMTPHeloError            The server didn't reply properly to
                          the helo greeting.

```python
def ehlo_or_helo_if_needed(self)
```

**Module:** [[Modules/smtplib|smtplib]]
**Class:** [[Classes/SMTP|SMTP]]
**Type:** Method
**Line:** 599

## Categories

- [[Taxonomy/public_method|public_method]]
