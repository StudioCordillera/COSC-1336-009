---
type: function
name: get_verified_chain
module: ssl
lineno: 888
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - accessor
  - accessor
---

# Function: get_verified_chain()

## Overview

Returns verified certificate chain provided by the other
end of the SSL channel as a list of DER-encoded bytes.

If certificate verification was disabled method acts the same as
``SSLSocket.get_unverified_chain``.

```python
def get_verified_chain(self)
```

**Module:** [[Modules/ssl|ssl]]
**Class:** [[Classes/SSLObject|SSLObject]]
**Type:** Method
**Line:** 888

## Categories

- [[Taxonomy/accessor|accessor]]
- [[Taxonomy/accessor|accessor]]
