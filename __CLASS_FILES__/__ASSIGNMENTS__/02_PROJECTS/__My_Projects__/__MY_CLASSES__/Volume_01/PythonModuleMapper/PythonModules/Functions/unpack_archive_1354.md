---
type: function
name: unpack_archive
module: shutil
lineno: 1314
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: unpack_archive()

## Overview

Unpack an archive.

`filename` is the name of the archive.

`extract_dir` is the name of the target directory, where the archive
is unpacked. If not provided, the current working directory is used.

`format` is the archive format: one of "zip", "tar", "gztar", "bztar",
or "xztar".  Or any other registered format.  If not provided,
unpack_archive will use the filename extension and see if an unpacker
was registered for that extension.

In case none is found, a ValueError is raised.

If `filter` is given, it is passed to the underlying
extraction function.

```python
def unpack_archive(filename, extract_dir, format)
```

**Module:** [[Modules/shutil|shutil]]
**Type:** Module-level function
**Line:** 1314
