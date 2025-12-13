---
type: function
name: _mdiff
module: difflib
lineno: 1340
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _mdiff()

## Overview

Returns generator yielding marked up from/to side by side differences.

Arguments:
fromlines -- list of text lines to compared to tolines
tolines -- list of text lines to be compared to fromlines
context -- number of context lines to display on each side of difference,
           if None, all from/to text lines will be generated.
linejunk -- passed on to ndiff (see ndiff documentation)
charjunk -- passed on to ndiff (see ndiff documentation)

This function returns an iterator which returns a tuple:
(from line tuple, to line tuple, boolean flag)

from/to line tuple -- (line num, line text)
    line num -- integer or None (to indicate a context separation)
    line text -- original line text with following markers inserted:
        '\0+' -- marks start of added text
        '\0-' -- marks start of deleted text
        '\0^' -- marks start of changed text
        '\1' -- marks end of added/deleted/changed text

boolean flag -- None indicates context separation, True indicates
    either "from" or "to" line contains a change, otherwise False.

This function/iterator was originally developed to generate side by side
file difference for making HTML pages (see HtmlDiff class for example
usage).

Note, this function utilizes the ndiff function to generate the side by
side difference markup.  Optional ndiff arguments may be passed to this
function and they in turn will be passed to ndiff.

```python
def _mdiff(fromlines, tolines, context, linejunk, charjunk)
```

**Module:** [[Modules/difflib|difflib]]
**Type:** Module-level function
**Line:** 1340
