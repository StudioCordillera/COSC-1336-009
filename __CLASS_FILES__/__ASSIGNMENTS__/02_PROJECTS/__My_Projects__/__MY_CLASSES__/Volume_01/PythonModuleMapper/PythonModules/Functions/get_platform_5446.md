---
type: function
name: get_platform
module: sysconfig
lineno: 590
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_platform()

## Overview

Return a string that identifies the current platform.

This is used mainly to distinguish platform-specific build directories and
platform-specific built distributions.  Typically includes the OS name and
version and the architecture (as supplied by 'os.uname()'), although the
exact information included depends on the OS; on Linux, the kernel version
isn't particularly important.

Examples of returned values:
   linux-i586
   linux-alpha (?)
   solaris-2.6-sun4u

Windows will return one of:
   win-amd64 (64-bit Windows on AMD64 (aka x86_64, Intel64, EM64T, etc)
   win-arm64 (64-bit Windows on ARM64 (aka AArch64)
   win32 (all others - specifically, sys.platform is returned)

For other non-POSIX platforms, currently just returns 'sys.platform'.

```python
def get_platform()
```

**Module:** [[Modules/sysconfig|sysconfig]]
**Type:** Module-level function
**Line:** 590

## Categories

- [[Taxonomy/accessor|accessor]]
