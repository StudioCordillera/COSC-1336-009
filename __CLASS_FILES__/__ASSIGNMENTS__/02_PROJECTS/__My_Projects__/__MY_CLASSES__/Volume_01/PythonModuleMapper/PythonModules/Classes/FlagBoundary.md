---
type: class
name: FlagBoundary
module: enum
lineno: 1398
tags:
  - python
  - class
---

# Class: FlagBoundary

## Overview

control how out of range values are handled
"strict" -> error is raised             [default for Flag]
"conform" -> extra bits are discarded
"eject" -> lose flag status
"keep" -> keep flag status and all bits [default for IntFlag]

**Module:** [[Modules/enum|enum]]
**Line:** 1398

## Inheritance

**Inherits from:**
- [[Classes/StrEnum|StrEnum]]
