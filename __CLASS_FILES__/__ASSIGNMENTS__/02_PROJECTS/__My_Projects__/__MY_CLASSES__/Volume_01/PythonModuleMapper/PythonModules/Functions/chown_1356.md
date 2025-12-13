---
type: function
name: chown
module: shutil
lineno: 1399
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: chown()

## Overview

Change owner user and group of the given path.

user and group can be the uid/gid or the user/group names, and in that case,
they are converted to their respective uid/gid.

If dir_fd is set, it should be an open file descriptor to the directory to
be used as the root of *path* if it is relative.

If follow_symlinks is set to False and the last element of the path is a
symbolic link, chown will modify the link itself and not the file being
referenced by the link.

```python
def chown(path, user, group)
```

**Module:** [[Modules/shutil|shutil]]
**Type:** Module-level function
**Line:** 1399
