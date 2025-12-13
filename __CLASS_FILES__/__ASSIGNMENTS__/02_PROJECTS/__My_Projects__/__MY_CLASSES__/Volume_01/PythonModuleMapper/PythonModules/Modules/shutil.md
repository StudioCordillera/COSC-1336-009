---
type: module
name: shutil
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\shutil.py
is_package: False
analyzed_at: 2025-12-10T03:46:15.572186
tags:
  - python
  - module
---

# Module: shutil

## Overview

Utility functions for copying and archiving files and directory trees.

XXX The functions here don't copy the resource fork or other metadata on Mac.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\shutil.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:15

## Dependencies

This module imports:
- [[Modules/fnmatch|fnmatch]]
- [[Modules/stat|stat]]
- [[Modules/collections|collections]]

## Used By

This module is imported by:
- [[Modules/zipfile|zipfile]]
- [[Modules/tarfile|tarfile]]
- [[Modules/argparse|argparse]]
- [[Modules/webbrowser|webbrowser]]
- [[Modules/uuid|uuid]]
- [[Modules/ensurepip|ensurepip]]
- [[Modules/venv|venv]]
- [[Modules/zipapp|zipapp]]

## Classes

- [[Classes/Error|Error]] (line 67)
- [[Classes/SameFileError|SameFileError]] (line 70)
- [[Classes/SpecialFileError|SpecialFileError]] (line 73)
- [[Classes/ExecError|ExecError]] (line 77)
- [[Classes/ReadError|ReadError]] (line 80)
- [[Classes/RegistryError|RegistryError]] (line 83)
- [[Classes/_GiveupOnFastCopy|_GiveupOnFastCopy]] (line 87)

## Functions

- [[Functions/_fastcopy_fcopyfile_1314|_fastcopy_fcopyfile()]] (line 92)
- [[Functions/_fastcopy_sendfile_1315|_fastcopy_sendfile()]] (line 112)
- [[Functions/_copyfileobj_readinto_1316|_copyfileobj_readinto()]] (line 176)
- [[Functions/copyfileobj_1317|copyfileobj()]] (line 196)
- [[Functions/_samefile_1318|_samefile()]] (line 206)
- [[Functions/_stat_1319|_stat()]] (line 224)
- [[Functions/_islink_1320|_islink()]] (line 227)
- [[Functions/copyfile_1321|copyfile()]] (line 230)
- [[Functions/copymode_1322|copymode()]] (line 294)
- [[Functions/_copyxattr_1323|_copyxattr()]] (line 345)
- [[Functions/copystat_1324|copystat()]] (line 348)
- [[Functions/copy_1325|copy()]] (line 414)
- [[Functions/copy2_1326|copy2()]] (line 432)
- [[Functions/ignore_patterns_1327|ignore_patterns()]] (line 472)
- [[Functions/_copytree_1328|_copytree()]] (line 484)
- [[Functions/copytree_1329|copytree()]] (line 550)
- [[Functions/_rmtree_islink_1330|_rmtree_islink()]] (line 604)
- [[Functions/_rmtree_unsafe_1331|_rmtree_unsafe()]] (line 608)
- [[Functions/_rmtree_safe_fd_1332|_rmtree_safe_fd()]] (line 638)
- [[Functions/rmtree_1333|rmtree()]] (line 714)
- [[Functions/_basename_1334|_basename()]] (line 796)
- [[Functions/move_1335|move()]] (line 814)
- [[Functions/_destinsrc_1336|_destinsrc()]] (line 880)
- [[Functions/_is_immutable_1337|_is_immutable()]] (line 889)
- [[Functions/_get_gid_1338|_get_gid()]] (line 894)
- [[Functions/_get_uid_1339|_get_uid()]] (line 912)
- [[Functions/_make_tarball_1340|_make_tarball()]] (line 930)
- [[Functions/_make_zipfile_1341|_make_zipfile()]] (line 1000)
- [[Functions/get_archive_formats_1342|get_archive_formats()]] (line 1082)
- [[Functions/register_archive_format_1343|register_archive_format()]] (line 1092)
- [[Functions/unregister_archive_format_1344|unregister_archive_format()]] (line 1113)
- [[Functions/make_archive_1345|make_archive()]] (line 1116)
- [[Functions/get_unpack_formats_1346|get_unpack_formats()]] (line 1180)
- [[Functions/_check_unpack_options_1347|_check_unpack_options()]] (line 1191)
- [[Functions/register_unpack_format_1348|register_unpack_format()]] (line 1209)
- [[Functions/unregister_unpack_format_1349|unregister_unpack_format()]] (line 1231)
- [[Functions/_ensure_directory_1350|_ensure_directory()]] (line 1235)
- [[Functions/_unpack_zipfile_1351|_unpack_zipfile()]] (line 1241)
- [[Functions/_unpack_tarfile_1352|_unpack_tarfile()]] (line 1271)
- [[Functions/_find_unpack_format_1353|_find_unpack_format()]] (line 1307)
- [[Functions/unpack_archive_1354|unpack_archive()]] (line 1314)
- [[Functions/disk_usage_1355|disk_usage()]] (line 1388)
- [[Functions/chown_1356|chown()]] (line 1399)
- [[Functions/get_terminal_size_1357|get_terminal_size()]] (line 1439)
- [[Functions/_access_check_1358|_access_check()]] (line 1488)
- [[Functions/_win_path_needs_curdir_1359|_win_path_needs_curdir()]] (line 1493)
- [[Functions/which_1360|which()]] (line 1503)
