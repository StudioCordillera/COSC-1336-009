---
type: class
name: property
module: enum
lineno: 186
tags:
  - python
  - class
---

# Class: property

## Overview

This is a descriptor, used to define attributes that act differently
when accessed through an enum member and through an enum class.
Instance access is the same as property(), but access to an attribute
through the enum class will instead look in the class' _member_map_ for
a corresponding enum member.

**Module:** [[Modules/enum|enum]]
**Line:** 186

## Inheritance

**Inherits from:**
- [[Classes/DynamicClassAttribute|DynamicClassAttribute]]

## Methods

### Magic Methods
- [[Functions/__get___641|__get__()]] (line 199)
- [[Functions/__set___642|__set__()]] (line 224)
- [[Functions/__delete___643|__delete__()]] (line 231)
- [[Functions/__set_name___644|__set_name__()]] (line 238)
