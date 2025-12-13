---
type: class
name: ZipFile
module: zipfile
lineno: 1302
tags:
  - python
  - class
---

# Class: ZipFile

## Overview

Class with methods to open, read, write, close, list zip files.

z = ZipFile(file, mode="r", compression=ZIP_STORED, allowZip64=True,
            compresslevel=None)

file: Either the path to the file, or a file-like object.
      If it is a path, the file will be opened and closed by ZipFile.
mode: The mode can be either read 'r', write 'w', exclusive create 'x',
      or append 'a'.
compression: ZIP_STORED (no compression), ZIP_DEFLATED (requires zlib),
             ZIP_BZIP2 (requires bz2) or ZIP_LZMA (requires lzma).
allowZip64: if True ZipFile will create files with ZIP64 extensions when
            needed, otherwise it will raise an exception when this would
            be necessary.
compresslevel: None (default for the given compression type) or an integer
               specifying the level to pass to the compressor.
               When using ZIP_STORED or ZIP_LZMA this keyword has no effect.
               When using ZIP_DEFLATED integers 0 through 9 are accepted.
               When using ZIP_BZIP2 integers 1 through 9 are accepted.

**Module:** [[Modules/zipfile|zipfile]]
**Line:** 1302

## Inheritance

**Subclasses:**
- [[Classes/PyZipFile|PyZipFile]]

## Methods

### Constructors
- [[Functions/__init___1683|__init__()]] (line 1328)
- [[Functions/__del___1706|__del__()]] (line 1986)

### Magic Methods
- [[Functions/__enter___1684|__enter__()]] (line 1424)
- [[Functions/__exit___1685|__exit__()]] (line 1427)
- [[Functions/__repr___1686|__repr__()]] (line 1430)

### Methods
- [[Functions/_RealGetContents_1687|_RealGetContents()]] (line 1444)
- [[Functions/namelist_1688|namelist()]] (line 1529)
- [[Functions/infolist_1689|infolist()]] (line 1533)
- [[Functions/printdir_1690|printdir()]] (line 1538)
- [[Functions/testzip_1691|testzip()]] (line 1547)
- [[Functions/getinfo_1692|getinfo()]] (line 1563)
- [[Functions/setpassword_1693|setpassword()]] (line 1572)
- [[Functions/comment_1694|comment()]] (line 1587)
- [[Functions/read_1695|read()]] (line 1599)
- [[Functions/open_1696|open()]] (line 1605)
- [[Functions/_open_to_write_1697|_open_to_write()]] (line 1716)
- [[Functions/extract_1698|extract()]] (line 1758)
- [[Functions/extractall_1699|extractall()]] (line 1772)
- [[Functions/_sanitize_windows_name_1700|_sanitize_windows_name()]] (line 1791)
- [[Functions/_extract_member_1701|_extract_member()]] (line 1805)
- [[Functions/_writecheck_1702|_writecheck()]] (line 1854)
- [[Functions/write_1703|write()]] (line 1877)
- [[Functions/writestr_1704|writestr()]] (line 1910)
- [[Functions/mkdir_1705|mkdir()]] (line 1951)
- [[Functions/close_1707|close()]] (line 1990)
- [[Functions/_write_end_record_1708|_write_end_record()]] (line 2012)
- [[Functions/_fpclose_1709|_fpclose()]] (line 2106)
