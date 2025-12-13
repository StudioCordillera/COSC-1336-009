---
type: class
name: redirect_stdout
module: contextlib
lineno: 411
tags:
  - python
  - class
---

# Class: redirect_stdout

## Overview

Context manager for temporarily redirecting stdout to another file.

# How to send help() to stderr
with redirect_stdout(sys.stderr):
    help(dir)

# How to write help() to a file
with open('help.txt', 'w') as f:
    with redirect_stdout(f):
        help(pow)

**Module:** [[Modules/contextlib|contextlib]]
**Line:** 411

## Inheritance

**Inherits from:**
- [[Classes/_RedirectStream|_RedirectStream]]
