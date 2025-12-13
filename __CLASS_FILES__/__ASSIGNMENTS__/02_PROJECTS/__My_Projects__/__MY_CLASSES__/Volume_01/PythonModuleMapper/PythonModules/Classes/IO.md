---
type: class
name: IO
module: typing
lineno: 3460
tags:
  - python
  - class
---

# Class: IO

## Overview

Generic base class for TextIO and BinaryIO.

This is an abstract, generic version of the return of open().

NOTE: This does not distinguish between the different possible
classes (text vs. binary, read vs. write vs. read/write,
append-only, unbuffered).  The TextIO and BinaryIO subclasses
below capture the distinctions between text vs. binary, which is
pervasive in the interface; however we currently do not offer a
way to track the other distinctions in the type system.

**Module:** [[Modules/typing|typing]]
**Line:** 3460

## Methods

### Magic Methods
- [[Functions/__enter___4832|__enter__()]] (line 3551)
- [[Functions/__exit___4833|__exit__()]] (line 3555)

### Methods
- [[Functions/mode_4814|mode()]] (line 3477)
- [[Functions/name_4815|name()]] (line 3482)
- [[Functions/close_4816|close()]] (line 3486)
- [[Functions/closed_4817|closed()]] (line 3491)
- [[Functions/fileno_4818|fileno()]] (line 3495)
- [[Functions/flush_4819|flush()]] (line 3499)
- [[Functions/isatty_4820|isatty()]] (line 3503)
- [[Functions/read_4821|read()]] (line 3507)
- [[Functions/readable_4822|readable()]] (line 3511)
- [[Functions/readline_4823|readline()]] (line 3515)
- [[Functions/readlines_4824|readlines()]] (line 3519)
- [[Functions/seek_4825|seek()]] (line 3523)
- [[Functions/seekable_4826|seekable()]] (line 3527)
- [[Functions/tell_4827|tell()]] (line 3531)
- [[Functions/truncate_4828|truncate()]] (line 3535)
- [[Functions/writable_4829|writable()]] (line 3539)
- [[Functions/write_4830|write()]] (line 3543)
- [[Functions/writelines_4831|writelines()]] (line 3547)
