---
type: function
name: register_archive_format
module: shutil
lineno: 1092
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: register_archive_format()

## Overview

Registers an archive format.

name is the name of the format. function is the callable that will be
used to create archives. If provided, extra_args is a sequence of
(name, value) tuples that will be passed as arguments to the callable.
description can be provided to describe the format, and will be returned
by the get_archive_formats() function.

```python
def register_archive_format(name, function, extra_args, description)
```

**Module:** [[Modules/shutil|shutil]]
**Type:** Module-level function
**Line:** 1092
