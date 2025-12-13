---
type: class
name: _TemporaryFileCloser
module: tempfile
lineno: 432
tags:
  - python
  - class
---

# Class: _TemporaryFileCloser

## Overview

A separate object allowing proper closing of a temporary file's
underlying file object, without adding a __del__ method to the
temporary file.

**Module:** [[Modules/tempfile|tempfile]]
**Line:** 432

## Methods

### Constructors
- [[Functions/__init___1214|__init__()]] (line 440)
- [[Functions/__del___1217|__del__()]] (line 471)

### Methods
- [[Functions/cleanup_1215|cleanup()]] (line 446)
- [[Functions/close_1216|close()]] (line 462)
