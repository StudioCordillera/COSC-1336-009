---
type: function
name: handle
module: logging
lineno: 1011
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
  - public_method
---

# Function: handle()

## Overview

Conditionally emit the specified logging record.

Emission depends on filters which may have been added to the handler.
Wrap the actual emission of the record with acquisition/release of
the I/O thread lock.

Returns an instance of the log record that was emitted
if it passed all filters, otherwise a false value is returned.

```python
def handle(self, record)
```

**Module:** [[Modules/logging|logging]]
**Class:** [[Classes/Handler|Handler]]
**Type:** Method
**Line:** 1011

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
