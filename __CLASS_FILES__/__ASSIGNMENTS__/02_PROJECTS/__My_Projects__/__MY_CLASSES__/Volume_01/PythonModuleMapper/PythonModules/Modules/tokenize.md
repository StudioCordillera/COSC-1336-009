---
type: module
name: tokenize
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\tokenize.py
is_package: False
analyzed_at: 2025-12-10T03:46:27.884387
tags:
  - python
  - module
---

# Module: tokenize

## Overview

Tokenization help for Python programs.

tokenize(readline) is a generator that breaks a stream of bytes into
Python tokens.  It decodes the bytes according to PEP-0263 for
determining source file encoding.

It accepts a readline-like method which is called repeatedly to get the
next line of input (or b"" for EOF).  It generates 5-tuples with these
members:

    the token type (see token.py)
    the token (a string)
    the starting (row, column) indices of the token (a 2-tuple of ints)
    the ending (row, column) indices of the token (a 2-tuple of ints)
    the original line (string)

It is designed to match the working of the Python tokenizer exactly, except
that it produces COMMENT tokens for comments and gives type OP for all
operators.  Additionally, all token lists start with an ENCODING token
which tells you which encoding was used to decode the bytes stream.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\tokenize.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:27

## Dependencies

This module imports:
- [[Modules/token|token]]
- [[Modules/re|re]]
- [[Modules/sys|sys]]
- [[Modules/functools|functools]]
- [[Modules/io|io]]
- [[Modules/codecs|codecs]]
- [[Modules/itertools|itertools]]
- [[Modules/builtins|builtins]]
- [[Modules/collections|collections]]
- [[Modules/argparse|argparse]]

## Used By

This module is imported by:
- [[Modules/tabnanny|tabnanny]]

## Classes

- [[Classes/TokenInfo|TokenInfo]] (line 47)
- [[Classes/TokenError|TokenError]] (line 162)
- [[Classes/Untokenizer|Untokenizer]] (line 165)

## Functions

- [[Functions/ISTERMINAL_6088|ISTERMINAL()]] (line 134)
- [[Functions/ISNONTERMINAL_6089|ISNONTERMINAL()]] (line 137)
- [[Functions/ISEOF_6090|ISEOF()]] (line 140)
- [[Functions/group_6093|group()]] (line 60)
- [[Functions/any_6094|any()]] (line 61)
- [[Functions/maybe_6095|maybe()]] (line 62)
- [[Functions/_all_string_prefixes_6096|_all_string_prefixes()]] (line 85)
- [[Functions/_compile_6097|_compile()]] (line 101)
- [[Functions/untokenize_6104|untokenize()]] (line 326)
- [[Functions/_get_normal_name_6105|_get_normal_name()]] (line 347)
- [[Functions/detect_encoding_6106|detect_encoding()]] (line 358)
- [[Functions/open_6107|open()]] (line 451)
- [[Functions/tokenize_6108|tokenize()]] (line 466)
- [[Functions/generate_tokens_6109|generate_tokens()]] (line 494)
- [[Functions/main_6110|main()]] (line 502)
- [[Functions/_transform_msg_6111|_transform_msg()]] (line 565)
- [[Functions/_generate_tokens_from_c_tokenizer_6112|_generate_tokens_from_c_tokenizer()]] (line 575)
