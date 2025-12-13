---
type: module
name: mimetypes
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\mimetypes.py
is_package: False
analyzed_at: 2025-12-10T03:46:20.168529
tags:
  - python
  - module
---

# Module: mimetypes

## Overview

Guess the MIME type of a file.

This module defines two useful functions:

guess_type(url, strict=True) -- guess the MIME type and encoding of a URL.

guess_extension(type, strict=True) -- guess the extension for a given MIME type.

It also contains the following, for tuning the behavior:

Data:

knownfiles -- list of files to parse
inited -- flag set when init() has been called
suffix_map -- dictionary mapping suffixes to suffixes
encodings_map -- dictionary mapping suffixes to encodings
types_map -- dictionary mapping suffixes to types

Functions:

init([files]) -- parse a list of files, default knownfiles (on Windows, the
  default values are taken from the registry)
read_mime_types(file) -- parse one file, return a dictionary or None

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\mimetypes.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:20

## Dependencies

This module imports:
- [[Modules/os|os]]
- [[Modules/getopt|getopt]]

## Classes

- [[Classes/MimeTypes|MimeTypes]] (line 64)

## Functions

- [[Functions/guess_type_3152|guess_type()]] (line 304)
- [[Functions/guess_file_type_3153|guess_file_type()]] (line 327)
- [[Functions/guess_all_extensions_3154|guess_all_extensions()]] (line 337)
- [[Functions/guess_extension_3155|guess_extension()]] (line 354)
- [[Functions/add_type_3156|add_type()]] (line 370)
- [[Functions/init_3157|init()]] (line 387)
- [[Functions/read_mime_types_3158|read_mime_types()]] (line 415)
- [[Functions/_default_mime_types_3159|_default_mime_types()]] (line 426)
- [[Functions/_main_3160|_main()]] (line 632)
