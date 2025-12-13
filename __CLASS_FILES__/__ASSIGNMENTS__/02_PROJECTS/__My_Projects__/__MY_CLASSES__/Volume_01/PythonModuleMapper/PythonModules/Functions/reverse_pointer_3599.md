---
type: function
name: reverse_pointer
module: ipaddress
lineno: 400
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: reverse_pointer()

## Overview

The name of the reverse DNS pointer for the IP address, e.g.:
>>> ipaddress.ip_address("127.0.0.1").reverse_pointer
'1.0.0.127.in-addr.arpa'
>>> ipaddress.ip_address("2001:db8::1").reverse_pointer
'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa'

```python
@property
def reverse_pointer(self)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Class:** [[Classes/_IPAddressBase|_IPAddressBase]]
**Type:** Method
**Line:** 400

## Categories

- [[Taxonomy/public_method|public_method]]
