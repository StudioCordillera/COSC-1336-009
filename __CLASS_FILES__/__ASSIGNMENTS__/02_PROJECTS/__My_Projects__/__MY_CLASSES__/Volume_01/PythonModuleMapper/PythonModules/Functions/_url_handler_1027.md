---
type: function
name: _url_handler
module: pydoc
lineno: 2445
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _url_handler()

## Overview

The pydoc url handler for use with the pydoc server.

If the content_type is 'text/css', the _pydoc.css style
sheet is read and returned if it exits.

If the content_type is 'text/html', then the result of
get_html_page(url) is returned.

```python
def _url_handler(url, content_type)
```

**Module:** [[Modules/pydoc|pydoc]]
**Type:** Module-level function
**Line:** 2445
