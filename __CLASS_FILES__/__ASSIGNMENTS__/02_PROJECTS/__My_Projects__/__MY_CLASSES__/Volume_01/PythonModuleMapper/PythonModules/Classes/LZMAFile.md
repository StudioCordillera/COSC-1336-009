---
type: class
name: LZMAFile
module: lzma
lineno: 38
tags:
  - python
  - class
---

# Class: LZMAFile

## Overview

A file object providing transparent LZMA (de)compression.

An LZMAFile can act as a wrapper for an existing file object, or
refer directly to a named file on disk.

Note that LZMAFile provides a *binary* file interface - data read
is returned as bytes, and data to be written must be given as bytes.

**Module:** [[Modules/lzma|lzma]]
**Line:** 38

## Methods

### Constructors
- [[Functions/__init___1603|__init__()]] (line 49)

### Methods
- [[Functions/close_1604|close()]] (line 134)
- [[Functions/closed_1605|closed()]] (line 158)
- [[Functions/name_1606|name()]] (line 163)
- [[Functions/mode_1607|mode()]] (line 168)
- [[Functions/fileno_1608|fileno()]] (line 171)
- [[Functions/seekable_1609|seekable()]] (line 176)
- [[Functions/readable_1610|readable()]] (line 180)
- [[Functions/writable_1611|writable()]] (line 185)
- [[Functions/peek_1612|peek()]] (line 190)
- [[Functions/read_1613|read()]] (line 201)
- [[Functions/read1_1614|read1()]] (line 210)
- [[Functions/readline_1615|readline()]] (line 222)
- [[Functions/write_1616|write()]] (line 232)
- [[Functions/seek_1617|seek()]] (line 253)
- [[Functions/tell_1618|tell()]] (line 271)
