---
type: module
name: getopt
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\getopt.py
is_package: False
analyzed_at: 2025-12-10T03:46:17.815164
tags:
  - python
  - module
---

# Module: getopt

## Overview

Parser for command line options.

This module helps scripts to parse the command line arguments in
sys.argv.  It supports the same conventions as the Unix getopt()
function (including the special meanings of arguments of the form `-'
and `--').  Long options similar to those supported by GNU software
may be used as well via an optional third argument.  This module
provides two functions and an exception:

getopt() -- Parse command line options
gnu_getopt() -- Like getopt(), but allow option and non-option arguments
to be intermixed.
GetoptError -- exception (class) raised with 'opt' attribute, which is the
option involved with the exception.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\getopt.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:17

## Dependencies

This module imports:
- [[Modules/os|os]]

## Used By

This module is imported by:
- [[Modules/mimetypes|mimetypes]]
- [[Modules/base64|base64]]
- [[Modules/quopri|quopri]]
- [[Modules/imaplib|imaplib]]
- [[Modules/pydoc|pydoc]]
- [[Modules/timeit|timeit]]
- [[Modules/modulefinder|modulefinder]]
- [[Modules/tabnanny|tabnanny]]

## Classes

- [[Classes/GetoptError|GetoptError]] (line 43)

## Functions

- [[Functions/__2212|_()]] (line 41)
- [[Functions/getopt_2215|getopt()]] (line 56)
- [[Functions/gnu_getopt_2216|gnu_getopt()]] (line 99)
- [[Functions/do_longs_2217|do_longs()]] (line 149)
- [[Functions/long_has_args_2218|long_has_args()]] (line 171)
- [[Functions/do_shorts_2219|do_shorts()]] (line 192)
- [[Functions/short_has_arg_2220|short_has_arg()]] (line 207)
