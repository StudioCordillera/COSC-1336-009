---
type: function
name: cert_time_to_seconds
module: ssl
lineno: 1450
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: cert_time_to_seconds()

## Overview

Return the time in seconds since the Epoch, given the timestring
representing the "notBefore" or "notAfter" date from a certificate
in ``"%b %d %H:%M:%S %Y %Z"`` strptime format (C locale).

"notBefore" or "notAfter" dates must use UTC (RFC 5280).

Month is one of: Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
UTC should be specified as GMT (see ASN1_TIME_print())

```python
def cert_time_to_seconds(cert_time)
```

**Module:** [[Modules/ssl|ssl]]
**Type:** Module-level function
**Line:** 1450
