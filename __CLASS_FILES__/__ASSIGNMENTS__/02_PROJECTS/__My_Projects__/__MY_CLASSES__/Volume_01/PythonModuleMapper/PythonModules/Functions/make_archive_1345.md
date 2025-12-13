---
type: function
name: make_archive
module: shutil
lineno: 1116
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: make_archive()

## Overview

Create an archive file (eg. zip or tar).

'base_name' is the name of the file to create, minus any format-specific
extension; 'format' is the archive format: one of "zip", "tar", "gztar",
"bztar", or "xztar".  Or any other registered format.

'root_dir' is a directory that will be the root directory of the
archive; ie. we typically chdir into 'root_dir' before creating the
archive.  'base_dir' is the directory where we start archiving from;
ie. 'base_dir' will be the common prefix of all files and
directories in the archive.  'root_dir' and 'base_dir' both default
to the current directory.  Returns the name of the archive file.

'owner' and 'group' are used when creating a tar archive. By default,
uses the current owner and group.

```python
def make_archive(base_name, format, root_dir, base_dir, verbose, dry_run, owner, group, logger)
```

**Module:** [[Modules/shutil|shutil]]
**Type:** Module-level function
**Line:** 1116
