---
type: module
name: re
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\re\__init__.py
is_package: True
analyzed_at: 2025-12-10T03:46:12.479506
tags:
  - python
  - module
---

# Module: re

## Overview

Support for regular expressions (RE).

This module provides regular expression matching operations similar to
those found in Perl.  It supports both 8-bit and Unicode strings; both
the pattern and the strings being processed can contain null bytes and
characters outside the US ASCII range.

Regular expressions can contain both special and ordinary characters.
Most ordinary characters, like "A", "a", or "0", are the simplest
regular expressions; they simply match themselves.  You can
concatenate ordinary characters, so last matches the string 'last'.

The special characters are:
    "."      Matches any character except a newline.
    "^"      Matches the start of the string.
    "$"      Matches the end of the string or just before the newline at
             the end of the string.
    "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
             Greedy means that it will match as many repetitions as possible.
    "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
    "?"      Matches 0 or 1 (greedy) of the preceding RE.
    *?,+?,?? Non-greedy versions of the previous three special characters.
    {m,n}    Matches from m to n repetitions of the preceding RE.
    {m,n}?   Non-greedy version of the above.
    "\\"     Either escapes special characters or signals a special sequence.
    []       Indicates a set of characters.
             A "^" as the first character indicates a complementing set.
    "|"      A|B, creates an RE that will match either A or B.
    (...)    Matches the RE inside the parentheses.
             The contents can be retrieved or matched later in the string.
    (?aiLmsux) The letters set the corresponding flags defined below.
    (?:...)  Non-grouping version of regular parentheses.
    (?P<name>...) The substring matched by the group is accessible by name.
    (?P=name)     Matches the text matched earlier by the group named name.
    (?#...)  A comment; ignored.
    (?=...)  Matches if ... matches next, but doesn't consume the string.
    (?!...)  Matches if ... doesn't match next.
    (?<=...) Matches if preceded by ... (must be fixed length).
    (?<!...) Matches if not preceded by ... (must be fixed length).
    (?(id/name)yes|no) Matches yes pattern if the group with id/name matched,
                       the (optional) no pattern otherwise.

The special sequences consist of "\\" and a character from the list
below.  If the ordinary character is not on the list, then the
resulting RE will match the second character.
    \number  Matches the contents of the group of the same number.
    \A       Matches only at the start of the string.
    \Z       Matches only at the end of the string.
    \b       Matches the empty string, but only at the start or end of a word.
    \B       Matches the empty string, but not at the start or end of a word.
    \d       Matches any decimal digit; equivalent to the set [0-9] in
             bytes patterns or string patterns with the ASCII flag.
             In string patterns without the ASCII flag, it will match the whole
             range of Unicode digits.
    \D       Matches any non-digit character; equivalent to [^\d].
    \s       Matches any whitespace character; equivalent to [ \t\n\r\f\v] in
             bytes patterns or string patterns with the ASCII flag.
             In string patterns without the ASCII flag, it will match the whole
             range of Unicode whitespace characters.
    \S       Matches any non-whitespace character; equivalent to [^\s].
    \w       Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]
             in bytes patterns or string patterns with the ASCII flag.
             In string patterns without the ASCII flag, it will match the
             range of Unicode alphanumeric characters (letters plus digits
             plus underscore).
             With LOCALE, it will match the set [0-9_] plus characters defined
             as letters for the current locale.
    \W       Matches the complement of \w.
    \\       Matches a literal backslash.

This module exports the following functions:
    match     Match a regular expression pattern to the beginning of a string.
    fullmatch Match a regular expression pattern to all of a string.
    search    Search a string for the presence of a pattern.
    sub       Substitute occurrences of a pattern found in a string.
    subn      Same as sub, but also return the number of substitutions made.
    split     Split a string by the occurrences of a pattern.
    findall   Find all occurrences of a pattern in a string.
    finditer  Return an iterator yielding a Match object for each match.
    compile   Compile a pattern into a Pattern object.
    purge     Clear the regular expression cache.
    escape    Backslash all non-alphanumerics in a string.

Each function other than purge and escape can take an optional 'flags' argument
consisting of one or more of the following module constants, joined by "|".
A, L, and U are mutually exclusive.
    A  ASCII       For string patterns, make \w, \W, \b, \B, \d, \D
                   match the corresponding ASCII character categories
                   (rather than the whole Unicode categories, which is the
                   default).
                   For bytes patterns, this flag is the only available
                   behaviour and needn't be specified.
    I  IGNORECASE  Perform case-insensitive matching.
    L  LOCALE      Make \w, \W, \b, \B, dependent on the current locale.
    M  MULTILINE   "^" matches the beginning of lines (after a newline)
                   as well as the string.
                   "$" matches the end of lines (before a newline) as well
                   as the end of the string.
    S  DOTALL      "." matches any character at all, including the newline.
    X  VERBOSE     Ignore whitespace and comments for nicer looking RE's.
    U  UNICODE     For compatibility only. Ignored for string patterns (it
                   is the default), and forbidden for bytes patterns.

This module also defines exception 'PatternError', aliased to 'error' for
backward compatibility.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\re\__init__.py`
**Type:** Package
**Analyzed:** 2025-12-10 03:46:12

## Used By

This module is imported by:
- [[Modules/difflib|difflib]]
- [[Modules/textwrap|textwrap]]
- [[Modules/pprint|pprint]]
- [[Modules/fractions|fractions]]
- [[Modules/glob|glob]]
- [[Modules/fnmatch|fnmatch]]
- [[Modules/pickle|pickle]]
- [[Modules/tarfile|tarfile]]
- [[Modules/csv|csv]]
- [[Modules/configparser|configparser]]
- [[Modules/plistlib|plistlib]]
- [[Modules/argparse|argparse]]
- [[Modules/logging|logging]]
- [[Modules/platform|platform]]
- [[Modules/base64|base64]]
- [[Modules/html|html]]
- [[Modules/ftplib|ftplib]]
- [[Modules/poplib|poplib]]
- [[Modules/imaplib|imaplib]]
- [[Modules/smtplib|smtplib]]
- [[Modules/ipaddress|ipaddress]]
- [[Modules/gettext|gettext]]
- [[Modules/locale|locale]]
- [[Modules/turtle|turtle]]
- [[Modules/shlex|shlex]]
- [[Modules/tkinter|tkinter]]
- [[Modules/typing|typing]]
- [[Modules/pydoc|pydoc]]
- [[Modules/doctest|doctest]]
- [[Modules/pdb|pdb]]
- [[Modules/sysconfig|sysconfig]]
- [[Modules/warnings|warnings]]
- [[Modules/dataclasses|dataclasses]]
- [[Modules/inspect|inspect]]
- [[Modules/pkgutil|pkgutil]]
- [[Modules/ast|ast]]
- [[Modules/tokenize|tokenize]]
- [[Modules/compileall|compileall]]
- [[Modules/pickletools|pickletools]]

## Classes

- [[Classes/RegexFlag|RegexFlag]] (line 144)
- [[Classes/_ZeroSentinel|_ZeroSentinel]] (line 179)
- [[Classes/Scanner|Scanner]] (line 391)

## Functions

- [[Functions/match_39|match()]] (line 164)
- [[Functions/fullmatch_40|fullmatch()]] (line 169)
- [[Functions/search_41|search()]] (line 174)
- [[Functions/sub_42|sub()]] (line 183)
- [[Functions/subn_43|subn()]] (line 211)
- [[Functions/split_44|split()]] (line 241)
- [[Functions/findall_45|findall()]] (line 270)
- [[Functions/finditer_46|finditer()]] (line 280)
- [[Functions/compile_47|compile()]] (line 287)
- [[Functions/purge_48|purge()]] (line 291)
- [[Functions/escape_49|escape()]] (line 305)
- [[Functions/_compile_50|_compile()]] (line 330)
- [[Functions/_compile_template_51|_compile_template()]] (line 375)
- [[Functions/_pickle_52|_pickle()]] (line 383)
