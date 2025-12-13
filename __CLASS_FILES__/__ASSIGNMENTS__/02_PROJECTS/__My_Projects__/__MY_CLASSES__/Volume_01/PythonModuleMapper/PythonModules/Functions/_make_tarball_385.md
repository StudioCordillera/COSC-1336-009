---
type: function
name: _make_tarball
module: shutil
lineno: 930
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _make_tarball()

## Overview

Create a (possibly compressed) tar file from all the files under
'base_dir'.

'compress' must be "gzip" (the default), "bzip2", "xz", or None.

'owner' and 'group' can be used to define an owner and a group for the
archive that is being built. If not provided, the current owner and group
will be used.

The output tar file will be named 'base_name' +  ".tar", possibly plus
the appropriate compression extension (".gz", ".bz2", or ".xz").

Returns the output filename.

```python
def _make_tarball(base_name, base_dir, compress, verbose, dry_run, owner, group, logger, root_dir)
```

**Module:** [[Modules/shutil|shutil]]
**Type:** Module-level function
**Line:** 930
