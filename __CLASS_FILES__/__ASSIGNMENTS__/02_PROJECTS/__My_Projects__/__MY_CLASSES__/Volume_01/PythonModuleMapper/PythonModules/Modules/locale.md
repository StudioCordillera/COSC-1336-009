---
type: module
name: locale
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\locale.py
is_package: False
analyzed_at: 2025-12-10T03:46:22.318066
tags:
  - python
  - module
---

# Module: locale

## Overview

Locale support module.

The module provides low-level access to the C lib's locale APIs and adds high
level number formatting APIs as well as a locale aliasing engine to complement
these.

The aliasing engine includes support for many commonly used locale names and
maps them to values suitable for passing to the C lib's setlocale() function. It
also includes default encodings for all supported locale names.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\locale.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:22

## Dependencies

This module imports:
- [[Modules/re|re]]
- [[Modules/os|os]]
- [[Modules/functools|functools]]

## Functions

- [[Functions/_strcoll_3832|_strcoll()]] (line 33)
- [[Functions/_strxfrm_3833|_strxfrm()]] (line 39)
- [[Functions/localeconv_3834|localeconv()]] (line 109)
- [[Functions/setlocale_3835|setlocale()]] (line 600)
- [[Functions/_grouping_intervals_3836|_grouping_intervals()]] (line 122)
- [[Functions/_group_3837|_group()]] (line 138)
- [[Functions/_strip_padding_3838|_strip_padding()]] (line 169)
- [[Functions/_format_3839|_format()]] (line 183)
- [[Functions/_localize_3840|_localize()]] (line 193)
- [[Functions/format_string_3841|format_string()]] (line 213)
- [[Functions/currency_3842|currency()]] (line 250)
- [[Functions/str_3843|str()]] (line 297)
- [[Functions/delocalize_3844|delocalize()]] (line 301)
- [[Functions/localize_3845|localize()]] (line 317)
- [[Functions/atof_3846|atof()]] (line 321)
- [[Functions/atoi_3847|atoi()]] (line 325)
- [[Functions/_test_3848|_test()]] (line 329)
- [[Functions/_replace_encoding_3849|_replace_encoding()]] (line 347)
- [[Functions/_append_modifier_3850|_append_modifier()]] (line 370)
- [[Functions/normalize_3851|normalize()]] (line 381)
- [[Functions/_parse_localename_3852|_parse_localename()]] (line 464)
- [[Functions/_build_localename_3853|_build_localename()]] (line 498)
- [[Functions/getdefaultlocale_3854|getdefaultlocale()]] (line 519)
- [[Functions/_getdefaultlocale_3855|_getdefaultlocale()]] (line 552)
- [[Functions/getlocale_3856|getlocale()]] (line 582)
- [[Functions/getencoding_3857|getencoding()]] (line 623)
- [[Functions/getpreferredencoding_3858|getpreferredencoding()]] (line 642)
- [[Functions/_print_locale_3859|_print_locale()]] (line 1717)
