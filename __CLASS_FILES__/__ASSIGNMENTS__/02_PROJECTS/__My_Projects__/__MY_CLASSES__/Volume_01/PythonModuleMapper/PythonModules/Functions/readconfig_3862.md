---
type: function
name: readconfig
module: turtle
lineno: 194
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: readconfig()

## Overview

Read config-files, change configuration-dict accordingly.

If there is a turtle.cfg file in the current working directory,
read it from there. If this contains an importconfig-value,
say 'myway', construct filename turtle_mayway.cfg else use
turtle.cfg and read it from the import-directory, where
turtle.py is located.
Update configuration dictionary first according to config-file,
in the import directory, then according to config-file in the
current working directory.
If no config-file is found, the default configuration is used.

```python
def readconfig(cfgdict)
```

**Module:** [[Modules/turtle|turtle]]
**Type:** Module-level function
**Line:** 194
