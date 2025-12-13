---
type: class
name: _Stream
module: tarfile
lineno: 330
tags:
  - python
  - class
---

# Class: _Stream

## Overview

Class that serves as an adapter between TarFile and
a stream-like object.  The stream-like object only
needs to have a read() or write() method that works with bytes,
and the method is accessed blockwise.
Use of gzip or bzip2 compression is possible.
A stream-like object could be for example: sys.stdin.buffer,
sys.stdout.buffer, a socket, a tape device etc.

_Stream is intended to be used only internally.

**Module:** [[Modules/tarfile|tarfile]]
**Line:** 330

## Methods

### Constructors
- [[Functions/__init___1725|__init__()]] (line 342)
- [[Functions/__del___1726|__del__()]] (line 413)

### Methods
- [[Functions/_init_write_gz_1727|_init_write_gz()]] (line 417)
- [[Functions/write_1728|write()]] (line 434)
- [[Functions/__write_1729|__write()]] (line 444)
- [[Functions/close_1730|close()]] (line 453)
- [[Functions/_init_read_gz_1731|_init_read_gz()]] (line 475)
- [[Functions/tell_1732|tell()]] (line 506)
- [[Functions/seek_1733|seek()]] (line 511)
- [[Functions/read_1734|read()]] (line 524)
- [[Functions/_read_1735|_read()]] (line 531)
- [[Functions/__read_1736|__read()]] (line 558)
