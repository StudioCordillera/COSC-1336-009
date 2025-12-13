---
type: class
name: BsdDbShelf
module: shelve
lineno: 175
tags:
  - python
  - class
---

# Class: BsdDbShelf

## Overview

Shelf implementation using the "BSD" db interface.

This adds methods first(), next(), previous(), last() and
set_location() that have no counterpart in [g]dbm databases.

The actual database must be opened using one of the "bsddb"
modules "open" routines (i.e. bsddb.hashopen, bsddb.btopen or
bsddb.rnopen) and passed to the constructor.

See the module's __doc__ string for an overview of the interface.

**Module:** [[Modules/shelve|shelve]]
**Line:** 175

## Inheritance

**Inherits from:**
- [[Classes/Shelf|Shelf]]

## Methods

### Constructors
- [[Functions/__init___1521|__init__()]] (line 188)

### Methods
- [[Functions/set_location_1522|set_location()]] (line 192)
- [[Functions/next_1523|next()]] (line 197)
- [[Functions/previous_1524|previous()]] (line 202)
- [[Functions/first_1525|first()]] (line 207)
- [[Functions/last_1526|last()]] (line 212)
