---
type: class
name: FileInput
module: fileinput
lineno: 171
tags:
  - python
  - class
---

# Class: FileInput

## Overview

FileInput([files[, inplace[, backup]]], *, mode=None, openhook=None)

Class FileInput is the implementation of the module; its methods
filename(), lineno(), fileline(), isfirstline(), isstdin(), fileno(),
nextfile() and close() correspond to the functions of the same name
in the module.
In addition it has a readline() method which returns the next
input line, and a __getitem__() method which implements the
sequence behavior. The sequence must be accessed in strictly
sequential order; random access and readline() cannot be mixed.

**Module:** [[Modules/fileinput|fileinput]]
**Line:** 171

## Methods

### Constructors
- [[Functions/__init___1127|__init__()]] (line 184)
- [[Functions/__del___1128|__del__()]] (line 231)

### Magic Methods
- [[Functions/__enter___1130|__enter__()]] (line 240)
- [[Functions/__exit___1131|__exit__()]] (line 243)
- [[Functions/__iter___1132|__iter__()]] (line 246)
- [[Functions/__next___1133|__next__()]] (line 249)

### Methods
- [[Functions/close_1129|close()]] (line 234)
- [[Functions/nextfile_1134|nextfile()]] (line 260)
- [[Functions/readline_1135|readline()]] (line 290)
- [[Functions/_readline_1136|_readline()]] (line 301)
- [[Functions/filename_1137|filename()]] (line 374)
- [[Functions/lineno_1138|lineno()]] (line 377)
- [[Functions/filelineno_1139|filelineno()]] (line 380)
- [[Functions/fileno_1140|fileno()]] (line 383)
- [[Functions/isfirstline_1141|isfirstline()]] (line 392)
- [[Functions/isstdin_1142|isstdin()]] (line 395)
