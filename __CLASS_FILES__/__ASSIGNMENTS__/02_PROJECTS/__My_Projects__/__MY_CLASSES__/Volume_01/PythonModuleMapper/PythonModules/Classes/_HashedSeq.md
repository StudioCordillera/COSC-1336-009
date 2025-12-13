---
type: class
name: _HashedSeq
module: functools
lineno: 457
tags:
  - python
  - class
---

# Class: _HashedSeq

## Overview

This class guarantees that hash() will be called no more than once
per element.  This is important because the lru_cache() will hash
the key multiple times on a cache miss.

**Module:** [[Modules/functools|functools]]
**Line:** 457

## Methods

### Constructors
- [[Functions/__init___1037|__init__()]] (line 466)

### Magic Methods
- [[Functions/__hash___1038|__hash__()]] (line 470)
