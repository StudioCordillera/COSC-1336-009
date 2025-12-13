---
type: class
name: TarInfo
module: tarfile
lineno: 869
tags:
  - python
  - class
---

# Class: TarInfo

## Overview

Informational class which holds the details about an
archive member given by a tar header block.
TarInfo objects are returned by TarFile.getmember(),
TarFile.getmembers() and TarFile.gettarinfo() and are
usually created internally.

**Module:** [[Modules/tarfile|tarfile]]
**Line:** 869

## Methods

### Constructors
- [[Functions/__init___1763|__init__()]] (line 904)

### Magic Methods
- [[Functions/__repr___1767|__repr__()]] (line 964)

### Methods
- [[Functions/tarfile_1764|tarfile()]] (line 938)
- [[Functions/path_1765|path()]] (line 952)
- [[Functions/linkpath_1766|linkpath()]] (line 961)
- [[Functions/replace_1768|replace()]] (line 967)
- [[Functions/get_info_1769|get_info()]] (line 995)
- [[Functions/tobuf_1770|tobuf()]] (line 1023)
- [[Functions/create_ustar_header_1771|create_ustar_header()]] (line 1040)
- [[Functions/create_gnu_header_1772|create_gnu_header()]] (line 1053)
- [[Functions/create_pax_header_1773|create_pax_header()]] (line 1067)
- [[Functions/create_pax_global_header_1774|create_pax_global_header()]] (line 1126)
- [[Functions/_posix_split_name_1775|_posix_split_name()]] (line 1131)
- [[Functions/_create_header_1776|_create_header()]] (line 1148)
- [[Functions/_create_payload_1777|_create_payload()]] (line 1190)
- [[Functions/_create_gnu_long_header_1778|_create_gnu_long_header()]] (line 1200)
- [[Functions/_create_pax_generic_header_1779|_create_pax_generic_header()]] (line 1217)
- [[Functions/frombuf_1780|frombuf()]] (line 1268)
- [[Functions/fromtarfile_1781|fromtarfile()]] (line 1331)
- [[Functions/_proc_member_1782|_proc_member()]] (line 1351)
- [[Functions/_proc_builtin_1783|_proc_builtin()]] (line 1364)
- [[Functions/_proc_gnulong_1784|_proc_gnulong()]] (line 1386)
- [[Functions/_proc_sparse_1785|_proc_sparse()]] (line 1413)
- [[Functions/_proc_pax_1786|_proc_pax()]] (line 1441)
- [[Functions/_proc_gnusparse_00_1787|_proc_gnusparse_00()]] (line 1562)
- [[Functions/_proc_gnusparse_01_1788|_proc_gnusparse_01()]] (line 1582)
- [[Functions/_proc_gnusparse_10_1789|_proc_gnusparse_10()]] (line 1588)
- [[Functions/_apply_pax_info_1790|_apply_pax_info()]] (line 1604)
- [[Functions/_decode_pax_field_1791|_decode_pax_field()]] (line 1627)
- [[Functions/_block_1792|_block()]] (line 1635)
- [[Functions/isreg_1793|isreg()]] (line 1644)
- [[Functions/isfile_1794|isfile()]] (line 1648)
- [[Functions/isdir_1795|isdir()]] (line 1652)
- [[Functions/issym_1796|issym()]] (line 1656)
- [[Functions/islnk_1797|islnk()]] (line 1660)
- [[Functions/ischr_1798|ischr()]] (line 1664)
- [[Functions/isblk_1799|isblk()]] (line 1668)
- [[Functions/isfifo_1800|isfifo()]] (line 1672)
- [[Functions/issparse_1801|issparse()]] (line 1676)
- [[Functions/isdev_1802|isdev()]] (line 1679)
