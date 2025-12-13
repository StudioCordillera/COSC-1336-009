---
type: function
name: makeLogRecord
module: logging
lineno: 425
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: makeLogRecord()

## Overview

Make a LogRecord whose attributes are defined by the specified dictionary,
This function is useful for converting a logging event received over
a socket connection (which is sent as a dictionary) into a LogRecord
instance.

```python
def makeLogRecord(dict)
```

**Module:** [[Modules/logging|logging]]
**Type:** Module-level function
**Line:** 425
