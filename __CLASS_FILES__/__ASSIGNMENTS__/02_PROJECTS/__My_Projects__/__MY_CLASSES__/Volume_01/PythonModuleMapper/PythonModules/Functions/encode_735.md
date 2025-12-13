---
type: function
name: encode
module: quopri
lineno: 44
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: encode()

## Overview

Read 'input', apply quoted-printable encoding, and write to 'output'.

'input' and 'output' are binary file objects. The 'quotetabs' flag
indicates whether embedded tabs and spaces should be quoted. Note that
line-ending tabs and spaces are always encoded, as per RFC 1521.
The 'header' flag indicates whether we are encoding spaces as _ as per RFC
1522.

```python
def encode(input, output, quotetabs, header)
```

**Module:** [[Modules/quopri|quopri]]
**Type:** Module-level function
**Line:** 44
