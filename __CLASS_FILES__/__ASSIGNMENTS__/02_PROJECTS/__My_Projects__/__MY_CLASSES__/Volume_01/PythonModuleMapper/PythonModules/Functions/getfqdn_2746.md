---
type: function
name: getfqdn
module: socket
lineno: 793
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getfqdn()

## Overview

Get fully qualified domain name from name.

An empty argument is interpreted as meaning the local host.

First the hostname returned by gethostbyaddr() is checked, then
possibly existing aliases. In case no FQDN is available and `name`
was given, it is returned unchanged. If `name` was empty, '0.0.0.0' or '::',
hostname from gethostname() is returned.

```python
def getfqdn(name)
```

**Module:** [[Modules/socket|socket]]
**Type:** Module-level function
**Line:** 793
