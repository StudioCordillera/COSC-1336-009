---
type: class
name: SpooledTemporaryFile
module: tempfile
lineno: 685
tags:
  - python
  - class
---

# Class: SpooledTemporaryFile

## Overview

Temporary file wrapper, specialized to switch from BytesIO
or StringIO to a real file when it exceeds a certain size or
when a fileno is needed.

**Module:** [[Modules/tempfile|tempfile]]
**Line:** 685

## Methods

### Constructors
- [[Functions/__init___1226|__init__()]] (line 692)
- [[Functions/__del___1232|__del__()]] (line 750)

### Magic Methods
- [[Functions/__enter___1229|__enter__()]] (line 738)
- [[Functions/__exit___1230|__exit__()]] (line 743)
- [[Functions/__iter___1231|__iter__()]] (line 747)

### Methods
- [[Functions/_check_1227|_check()]] (line 711)
- [[Functions/rollover_1228|rollover()]] (line 717)
- [[Functions/close_1233|close()]] (line 760)
- [[Functions/closed_1234|closed()]] (line 764)
- [[Functions/encoding_1235|encoding()]] (line 768)
- [[Functions/errors_1236|errors()]] (line 772)
- [[Functions/fileno_1237|fileno()]] (line 775)
- [[Functions/flush_1238|flush()]] (line 779)
- [[Functions/isatty_1239|isatty()]] (line 782)
- [[Functions/mode_1240|mode()]] (line 786)
- [[Functions/name_1241|name()]] (line 793)
- [[Functions/newlines_1242|newlines()]] (line 800)
- [[Functions/readable_1243|readable()]] (line 803)
- [[Functions/read_1244|read()]] (line 806)
- [[Functions/read1_1245|read1()]] (line 809)
- [[Functions/readinto_1246|readinto()]] (line 812)
- [[Functions/readinto1_1247|readinto1()]] (line 815)
- [[Functions/readline_1248|readline()]] (line 818)
- [[Functions/readlines_1249|readlines()]] (line 821)
- [[Functions/seekable_1250|seekable()]] (line 824)
- [[Functions/seek_1251|seek()]] (line 827)
- [[Functions/tell_1252|tell()]] (line 830)
- [[Functions/truncate_1253|truncate()]] (line 833)
- [[Functions/writable_1254|writable()]] (line 841)
- [[Functions/write_1255|write()]] (line 844)
- [[Functions/writelines_1256|writelines()]] (line 850)
- [[Functions/detach_1257|detach()]] (line 860)
