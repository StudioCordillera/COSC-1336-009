---
type: class
name: Breakpoint
module: bdb
lineno: 723
tags:
  - python
  - class
---

# Class: Breakpoint

## Overview

Breakpoint class.

Implements temporary breakpoints, ignore counts, disabling and
(re)-enabling, and conditionals.

Breakpoints are indexed by number through bpbynumber and by
the (file, line) tuple using bplist.  The former points to a
single instance of class Breakpoint.  The latter points to a
list of such instances since there may be more than one
breakpoint per line.

When creating a breakpoint, its associated filename should be
in canonical form.  If funcname is defined, a breakpoint hit will be
counted when the first line of that function is executed.  A
conditional breakpoint always counts a hit.

**Module:** [[Modules/bdb|bdb]]
**Line:** 723

## Methods

### Constructors
- [[Functions/__init___5135|__init__()]] (line 750)

### Magic Methods
- [[Functions/__str___5142|__str__()]] (line 838)

### Methods
- [[Functions/clearBreakpoints_5136|clearBreakpoints()]] (line 771)
- [[Functions/deleteMe_5137|deleteMe()]] (line 776)
- [[Functions/enable_5138|enable()]] (line 790)
- [[Functions/disable_5139|disable()]] (line 794)
- [[Functions/bpprint_5140|bpprint()]] (line 798)
- [[Functions/bpformat_5141|bpformat()]] (line 808)
