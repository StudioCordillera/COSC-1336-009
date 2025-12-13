---
type: module
name: gzip
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\gzip.py
is_package: False
analyzed_at: 2025-12-10T03:46:16.110895
tags:
  - python
  - module
---

# Module: gzip

## Overview

Functions that read and write gzipped files.

The user of the file doesn't have to worry about the compression,
but random access is not allowed.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\gzip.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:16

## Dependencies

This module imports:
- [[Modules/zlib|zlib]]
- [[Modules/struct|struct]]
- [[Modules/weakref|weakref]]

## Used By

This module is imported by:
- [[Modules/tarfile|tarfile]]

## Classes

- [[Classes/_PaddedFile|_PaddedFile]] (line 83)
- [[Classes/BadGzipFile|BadGzipFile]] (line 125)
- [[Classes/_WriteBufferStream|_WriteBufferStream]] (line 129)
- [[Classes/GzipFile|GzipFile]] (line 147)
- [[Classes/_GzipReader|_GzipReader]] (line 502)

## Functions

- [[Functions/open_1537|open()]] (line 33)
- [[Functions/write32u_1538|write32u()]] (line 78)
- [[Functions/_read_exact_1570|_read_exact()]] (line 449)
- [[Functions/_read_gzip_header_1571|_read_gzip_header()]] (line 465)
- [[Functions/compress_1578|compress()]] (line 600)
- [[Functions/decompress_1579|decompress()]] (line 617)
- [[Functions/main_1580|main()]] (line 642)
