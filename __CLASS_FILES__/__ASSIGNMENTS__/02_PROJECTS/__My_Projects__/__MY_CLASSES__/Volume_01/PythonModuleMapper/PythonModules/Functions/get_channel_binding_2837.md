---
type: function
name: get_channel_binding
module: ssl
lineno: 957
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - accessor
  - accessor
---

# Function: get_channel_binding()

## Overview

Get channel binding data for current connection.  Raise ValueError
if the requested `cb_type` is not supported.  Return bytes of the data
or None if the data is not available (e.g. before the handshake).

```python
def get_channel_binding(self, cb_type)
```

**Module:** [[Modules/ssl|ssl]]
**Class:** [[Classes/SSLObject|SSLObject]]
**Type:** Method
**Line:** 957

## Categories

- [[Taxonomy/accessor|accessor]]
- [[Taxonomy/accessor|accessor]]
