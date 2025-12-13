---
type: function
name: get_server_certificate
module: ssl
lineno: 1506
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_server_certificate()

## Overview

Retrieve the certificate from the server at the specified address,
and return it as a PEM-encoded string.
If 'ca_certs' is specified, validate the server cert against it.
If 'ssl_version' is specified, use it in the connection attempt.
If 'timeout' is specified, use it in the connection attempt.

```python
def get_server_certificate(addr, ssl_version, ca_certs, timeout)
```

**Module:** [[Modules/ssl|ssl]]
**Type:** Module-level function
**Line:** 1506

## Categories

- [[Taxonomy/accessor|accessor]]
