---
type: module
name: platform
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\platform.py
is_package: False
analyzed_at: 2025-12-10T03:46:18.279439
tags:
  - python
  - module
---

# Module: platform

## Overview

This module tries to retrieve as much platform-identifying data as
possible. It makes this information available via function APIs.

If called from the command line, it prints the platform
information concatenated as single string to stdout. The output
format is usable as part of a filename.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\platform.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:18

## Dependencies

This module imports:
- [[Modules/re|re]]
- [[Modules/os|os]]
- [[Modules/functools|functools]]
- [[Modules/itertools|itertools]]
- [[Modules/plistlib|plistlib]]
- [[Modules/struct|struct]]
- [[Modules/collections|collections]]

## Used By

This module is imported by:
- [[Modules/uuid|uuid]]
- [[Modules/pydoc|pydoc]]

## Classes

- [[Classes/_Processor|_Processor]] (line 865)
- [[Classes/uname_result|uname_result]] (line 921)

## Functions

- [[Functions/_comparable_version_2398|_comparable_version()]] (line 145)
- [[Functions/libc_ver_2399|libc_ver()]] (line 161)
- [[Functions/_norm_version_2400|_norm_version()]] (line 241)
- [[Functions/_syscmd_ver_2401|_syscmd_ver()]] (line 266)
- [[Functions/_wmi_query_2402|_wmi_query()]] (line 321)
- [[Functions/win32_is_iot_2403|win32_is_iot()]] (line 370)
- [[Functions/win32_edition_2404|win32_edition()]] (line 373)
- [[Functions/_win32_ver_2405|_win32_ver()]] (line 388)
- [[Functions/win32_ver_2406|win32_ver()]] (line 447)
- [[Functions/_mac_ver_xml_2407|_mac_ver_xml()]] (line 460)
- [[Functions/mac_ver_2408|mac_ver()]] (line 482)
- [[Functions/ios_ver_2409|ios_ver()]] (line 509)
- [[Functions/_java_getprop_2410|_java_getprop()]] (line 525)
- [[Functions/java_ver_2411|java_ver()]] (line 536)
- [[Functions/android_ver_2412|android_ver()]] (line 575)
- [[Functions/system_alias_2413|system_alias()]] (line 614)
- [[Functions/_platform_2414|_platform()]] (line 656)
- [[Functions/_node_2415|_node()]] (line 688)
- [[Functions/_follow_symlinks_2416|_follow_symlinks()]] (line 703)
- [[Functions/_syscmd_file_2417|_syscmd_file()]] (line 715)
- [[Functions/architecture_2418|architecture()]] (line 759)
- [[Functions/_get_machine_win32_2419|_get_machine_win32()]] (line 837)
- [[Functions/_unknown_as_blank_2425|_unknown_as_blank()]] (line 915)
- [[Functions/uname_2432|uname()]] (line 968)
- [[Functions/system_2433|system()]] (line 1066)
- [[Functions/node_2434|node()]] (line 1075)
- [[Functions/release_2435|release()]] (line 1085)
- [[Functions/version_2436|version()]] (line 1094)
- [[Functions/machine_2437|machine()]] (line 1103)
- [[Functions/processor_2438|processor()]] (line 1112)
- [[Functions/_sys_version_2439|_sys_version()]] (line 1128)
- [[Functions/python_implementation_2440|python_implementation()]] (line 1232)
- [[Functions/python_version_2441|python_version()]] (line 1244)
- [[Functions/python_version_tuple_2442|python_version_tuple()]] (line 1254)
- [[Functions/python_branch_2443|python_branch()]] (line 1265)
- [[Functions/python_revision_2444|python_revision()]] (line 1279)
- [[Functions/python_build_2445|python_build()]] (line 1292)
- [[Functions/python_compiler_2446|python_compiler()]] (line 1300)
- [[Functions/platform_2447|platform()]] (line 1312)
- [[Functions/_parse_os_release_2448|_parse_os_release()]] (line 1397)
- [[Functions/freedesktop_os_release_2449|freedesktop_os_release()]] (line 1424)
