---
type: class
name: Differ
module: difflib
lineno: 724
tags:
  - python
  - class
---

# Class: Differ

## Overview

Differ is a class for comparing sequences of lines of text, and
producing human-readable differences or deltas.  Differ uses
SequenceMatcher both to compare sequences of lines, and to compare
sequences of characters within similar (near-matching) lines.

Each line of a Differ delta begins with a two-letter code:

    '- '    line unique to sequence 1
    '+ '    line unique to sequence 2
    '  '    line common to both sequences
    '? '    line not present in either input sequence

Lines beginning with '? ' attempt to guide the eye to intraline
differences, and were not present in either input sequence.  These lines
can be confusing if the sequences contain tab characters.

Note that Differ makes no claim to produce a *minimal* diff.  To the
contrary, minimal diffs are often counter-intuitive, because they synch
up anywhere possible, sometimes accidental matches 100 pages apart.
Restricting synch points to contiguous matches preserves some notion of
locality, at the occasional cost of producing a longer diff.

Example: Comparing two texts.

First we set up the texts, sequences of individual single-line strings
ending with newlines (such sequences can also be obtained from the
`readlines()` method of file-like objects):

>>> text1 = '''  1. Beautiful is better than ugly.
...   2. Explicit is better than implicit.
...   3. Simple is better than complex.
...   4. Complex is better than complicated.
... '''.splitlines(keepends=True)
>>> len(text1)
4
>>> text1[0][-1]
'\n'
>>> text2 = '''  1. Beautiful is better than ugly.
...   3.   Simple is better than complex.
...   4. Complicated is better than complex.
...   5. Flat is better than nested.
... '''.splitlines(keepends=True)

Next we instantiate a Differ object:

>>> d = Differ()

Note that when instantiating a Differ object we may pass functions to
filter out line and character 'junk'.  See Differ.__init__ for details.

Finally, we compare the two:

>>> result = list(d.compare(text1, text2))

'result' is a list of strings, so let's pretty-print it:

>>> from pprint import pprint as _pprint
>>> _pprint(result)
['    1. Beautiful is better than ugly.\n',
 '-   2. Explicit is better than implicit.\n',
 '-   3. Simple is better than complex.\n',
 '+   3.   Simple is better than complex.\n',
 '?     ++\n',
 '-   4. Complex is better than complicated.\n',
 '?            ^                     ---- ^\n',
 '+   4. Complicated is better than complex.\n',
 '?           ++++ ^                      ^\n',
 '+   5. Flat is better than nested.\n']

As a single multi-line string it looks like this:

>>> print(''.join(result), end="")
    1. Beautiful is better than ugly.
-   2. Explicit is better than implicit.
-   3. Simple is better than complex.
+   3.   Simple is better than complex.
?     ++
-   4. Complex is better than complicated.
?            ^                     ---- ^
+   4. Complicated is better than complex.
?           ++++ ^                      ^
+   5. Flat is better than nested.

**Module:** [[Modules/difflib|difflib]]
**Line:** 724

## Methods

### Constructors
- [[Functions/__init___72|__init__()]] (line 810)

### Methods
- [[Functions/compare_73|compare()]] (line 833)
- [[Functions/_dump_74|_dump()]] (line 874)
- [[Functions/_plain_replace_75|_plain_replace()]] (line 879)
- [[Functions/_fancy_replace_76|_fancy_replace()]] (line 893)
- [[Functions/_fancy_helper_77|_fancy_helper()]] (line 987)
- [[Functions/_qformat_78|_qformat()]] (line 999)
