---
type: module
name: pickletools
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\pickletools.py
is_package: False
analyzed_at: 2025-12-10T03:46:28.420370
tags:
  - python
  - module
---

# Module: pickletools

## Overview

"Executable documentation" for the pickle module.

Extensive comments about the pickle protocols and pickle-machine opcodes
can be found here.  Some functions meant for external use:

genops(pickle)
   Generate all the opcodes in a pickle, as (opcode, arg, position) triples.

dis(pickle, out=None, memo=None, indentlevel=4)
   Print a symbolic disassembly of a pickle.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\pickletools.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:28

## Dependencies

This module imports:
- [[Modules/re|re]]
- [[Modules/pickle|pickle]]
- [[Modules/sys|sys]]
- [[Modules/struct|struct]]
- [[Modules/io|io]]
- [[Modules/codecs|codecs]]
- [[Modules/doctest|doctest]]
- [[Modules/argparse|argparse]]

## Classes

- [[Classes/ArgumentDescriptor|ArgumentDescriptor]] (line 174)
- [[Classes/StackObject|StackObject]] (line 948)
- [[Classes/OpcodeInfo|OpcodeInfo]] (line 1093)
- [[Classes/_Example|_Example]] (line 2553)

## Functions

- [[Functions/read_uint1_6219|read_uint1()]] (line 212)
- [[Functions/read_uint2_6220|read_uint2()]] (line 231)
- [[Functions/read_int4_6221|read_int4()]] (line 252)
- [[Functions/read_uint4_6222|read_uint4()]] (line 273)
- [[Functions/read_uint8_6223|read_uint8()]] (line 294)
- [[Functions/read_stringnl_6224|read_stringnl()]] (line 315)
- [[Functions/read_stringnl_noescape_6225|read_stringnl_noescape()]] (line 372)
- [[Functions/read_stringnl_noescape_pair_6226|read_stringnl_noescape_pair()]] (line 386)
- [[Functions/read_string1_6227|read_string1()]] (line 409)
- [[Functions/read_string4_6228|read_string4()]] (line 438)
- [[Functions/read_bytes1_6229|read_bytes1()]] (line 472)
- [[Functions/read_bytes4_6230|read_bytes4()]] (line 500)
- [[Functions/read_bytes8_6231|read_bytes8()]] (line 534)
- [[Functions/read_bytearray8_6232|read_bytearray8()]] (line 569)
- [[Functions/read_unicodestringnl_6233|read_unicodestringnl()]] (line 603)
- [[Functions/read_unicodestring1_6234|read_unicodestring1()]] (line 629)
- [[Functions/read_unicodestring4_6235|read_unicodestring4()]] (line 668)
- [[Functions/read_unicodestring8_6236|read_unicodestring8()]] (line 709)
- [[Functions/read_decimalnl_short_6237|read_decimalnl_short()]] (line 750)
- [[Functions/read_decimalnl_long_6238|read_decimalnl_long()]] (line 772)
- [[Functions/read_floatnl_6239|read_floatnl()]] (line 813)
- [[Functions/read_float8_6240|read_float8()]] (line 835)
- [[Functions/decode_long_6241|decode_long()]] (line 379)
- [[Functions/read_long1_6242|read_long1()]] (line 873)
- [[Functions/read_long4_6243|read_long4()]] (line 905)
- [[Functions/assure_pickle_consistency_6247|assure_pickle_consistency()]] (line 2224)
- [[Functions/_genops_6248|_genops()]] (line 2268)
- [[Functions/genops_6249|genops()]] (line 2300)
- [[Functions/optimize_6250|optimize()]] (line 2328)
- [[Functions/dis_6251|dis()]] (line 2395)
- [[Functions/_test_6253|_test()]] (line 2845)
