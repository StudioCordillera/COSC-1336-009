---
type: function
name: _start_server
module: pydoc
lineno: 2292
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _start_server()

## Overview

Start an HTTP server thread on a specific port.

Start an HTML/text server thread, so HTML or text documents can be
browsed dynamically and interactively with a web browser.  Example use:

    >>> import time
    >>> import pydoc

    Define a URL handler.  To determine what the client is asking
    for, check the URL and content_type.

    Then get or generate some text or HTML code and return it.

    >>> def my_url_handler(url, content_type):
    ...     text = 'the URL sent was: (%s, %s)' % (url, content_type)
    ...     return text

    Start server thread on port 0.
    If you use port 0, the server will pick a random port number.
    You can then use serverthread.port to get the port number.

    >>> port = 0
    >>> serverthread = pydoc._start_server(my_url_handler, port)

    Check that the server is really started.  If it is, open browser
    and get first page.  Use serverthread.url as the starting page.

    >>> if serverthread.serving:
    ...    import webbrowser

    The next two lines are commented out so a browser doesn't open if
    doctest is run on this module.

    #...    webbrowser.open(serverthread.url)
    #True

    Let the server do its thing. We just need to monitor its status.
    Use time.sleep so the loop doesn't hog the CPU.

    >>> starttime = time.monotonic()
    >>> timeout = 1                    #seconds

    This is a short timeout for testing purposes.

    >>> while serverthread.serving:
    ...     time.sleep(.01)
    ...     if serverthread.serving and time.monotonic() - starttime > timeout:
    ...          serverthread.stop()
    ...          break

    Print any errors that may have occurred.

    >>> print(serverthread.error)
    None

```python
def _start_server(urlhandler, hostname, port)
```

**Module:** [[Modules/pydoc|pydoc]]
**Type:** Module-level function
**Line:** 2292
