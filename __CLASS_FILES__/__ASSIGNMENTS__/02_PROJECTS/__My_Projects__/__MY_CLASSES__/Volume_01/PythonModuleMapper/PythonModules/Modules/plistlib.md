---
type: module
name: plistlib
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\plistlib.py
is_package: False
analyzed_at: 2025-12-10T03:46:17.279260
tags:
  - python
  - module
---

# Module: plistlib

## Overview

plistlib.py -- a tool to generate and parse MacOSX .plist files.

The property list (.plist) file format is a simple XML pickle supporting
basic object types, like dictionaries, lists, numbers and strings.
Usually the top level object is a dictionary.

To write out a plist file, use the dump(value, file)
function. 'value' is the top level object, 'file' is
a (writable) file object.

To parse a plist from a file, use the load(file) function,
with a (readable) file object as the only argument. It
returns the top level object (again, usually a dictionary).

To work with plist data in bytes objects, you can use loads()
and dumps().

Values can be strings, integers, floats, booleans, tuples, lists,
dictionaries (but only with string keys), Data, bytes, bytearray, or
datetime.datetime objects.

Generate Plist example:

    import datetime
    import plistlib

    pl = dict(
        aString = "Doodah",
        aList = ["A", "B", 12, 32.1, [1, 2, 3]],
        aFloat = 0.1,
        anInt = 728,
        aDict = dict(
            anotherString = "<hello & hi there!>",
            aThirdString = "M\xe4ssig, Ma\xdf",
            aTrueValue = True,
            aFalseValue = False,
        ),
        someData = b"<binary gunk>",
        someMoreData = b"<lots of binary gunk>" * 10,
        aDate = datetime.datetime.now()
    )
    print(plistlib.dumps(pl).decode())

Parse Plist example:

    import plistlib

    plist = b'''<plist version="1.0">
    <dict>
        <key>foo</key>
        <string>bar</string>
    </dict>
    </plist>'''
    pl = plistlib.loads(plist)
    print(pl["foo"])

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\plistlib.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:17

## Dependencies

This module imports:
- [[Modules/datetime|datetime]]
- [[Modules/re|re]]
- [[Modules/struct|struct]]
- [[Modules/enum|enum]]
- [[Modules/codecs|codecs]]
- [[Modules/itertools|itertools]]

## Used By

This module is imported by:
- [[Modules/platform|platform]]

## Classes

- [[Classes/UID|UID]] (line 77)
- [[Classes/_PlistParser|_PlistParser]] (line 177)
- [[Classes/_DumbXMLWriter|_DumbXMLWriter]] (line 289)
- [[Classes/_PlistWriter|_PlistWriter]] (line 327)
- [[Classes/InvalidFileException|InvalidFileException]] (line 456)
- [[Classes/_BinaryPlistParser|_BinaryPlistParser]] (line 464)
- [[Classes/_BinaryPlistWriter|_BinaryPlistWriter]] (line 644)

## Functions

- [[Functions/_encode_base64_1999|_encode_base64()]] (line 121)
- [[Functions/_decode_base64_2000|_decode_base64()]] (line 130)
- [[Functions/_date_from_string_2001|_date_from_string()]] (line 143)
- [[Functions/_date_to_string_2002|_date_to_string()]] (line 157)
- [[Functions/_escape_2003|_escape()]] (line 165)
- [[Functions/_is_fmt_xml_2035|_is_fmt_xml()]] (line 423)
- [[Functions/_count_to_size_2043|_count_to_size()]] (line 629)
- [[Functions/_is_fmt_binary_2050|_is_fmt_binary()]] (line 862)
- [[Functions/load_2051|load()]] (line 884)
- [[Functions/loads_2052|loads()]] (line 906)
- [[Functions/dump_2053|dump()]] (line 919)
- [[Functions/dumps_2054|dumps()]] (line 932)
