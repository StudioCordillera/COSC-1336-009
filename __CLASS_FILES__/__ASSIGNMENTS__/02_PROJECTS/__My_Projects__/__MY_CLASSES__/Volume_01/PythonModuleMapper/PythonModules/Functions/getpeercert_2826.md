---
type: function
name: getpeercert
module: ssl
lineno: 879
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: getpeercert()

## Overview

Returns a formatted version of the data in the certificate provided
by the other end of the SSL channel.

Return None if no certificate was provided, {} if a certificate was
provided, but not validated.

```python
def getpeercert(self, binary_form)
```

**Module:** [[Modules/ssl|ssl]]
**Class:** [[Classes/SSLObject|SSLObject]]
**Type:** Method
**Line:** 879

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
