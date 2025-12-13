---
type: function
name: tokenize
module: tokenize
lineno: 466
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: tokenize()

## Overview

The tokenize() generator requires one argument, readline, which
must be a callable object which provides the same interface as the
readline() method of built-in file objects.  Each call to the function
should return one line of input as bytes.  Alternatively, readline
can be a callable function terminating with StopIteration:
    readline = open(myfile, 'rb').__next__  # Example of alternate readline

The generator produces 5-tuples with these members: the token type; the
token string; a 2-tuple (srow, scol) of ints specifying the row and
column where the token begins in the source; a 2-tuple (erow, ecol) of
ints specifying the row and column where the token ends in the source;
and the line on which the token was found.  The line passed is the
physical line.

The first token sequence will always be an ENCODING token
which tells you which encoding was used to decode the bytes stream.

```python
def tokenize(readline)
```

**Module:** [[Modules/tokenize|tokenize]]
**Type:** Module-level function
**Line:** 466
