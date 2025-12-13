---
type: function
name: _EndRecData
module: zipfile
lineno: 295
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _EndRecData()

## Overview

Return data from the "End of Central Directory" record, or None.

The data is a list of the nine items in the ZIP "End of central dir"
record followed by a tenth item, the file seek offset of this record.

```python
def _EndRecData(fpin)
```

**Module:** [[Modules/zipfile|zipfile]]
**Type:** Module-level function
**Line:** 295
