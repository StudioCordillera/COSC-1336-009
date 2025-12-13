---
type: function
name: _get_default_tempdir
module: tempfile
lineno: 183
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: _get_default_tempdir()

## Overview

Calculate the default directory to use for temporary files.
This routine should be called exactly once.

We determine whether or not a candidate temp dir is usable by
trying to create and write to a file in that directory.  If this
is successful, the test file is deleted.  To prevent denial of
service, the name of the test file must be randomized.

```python
def _get_default_tempdir()
```

**Module:** [[Modules/tempfile|tempfile]]
**Type:** Module-level function
**Line:** 183

## Categories

- [[Taxonomy/accessor|accessor]]
