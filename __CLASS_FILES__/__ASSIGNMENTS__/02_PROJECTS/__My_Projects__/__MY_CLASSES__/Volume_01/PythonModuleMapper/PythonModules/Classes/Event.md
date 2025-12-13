---
type: class
name: Event
module: tkinter
lineno: 217
tags:
  - python
  - class
---

# Class: Event

## Overview

Container for the properties of an event.

Instances of this type are generated if one of the following events occurs:

KeyPress, KeyRelease - for keyboard events
ButtonPress, ButtonRelease, Motion, Enter, Leave, MouseWheel - for mouse events
Visibility, Unmap, Map, Expose, FocusIn, FocusOut, Circulate,
Colormap, Gravity, Reparent, Property, Destroy, Activate,
Deactivate - for window events.

If a callback function for one of these events is registered
using bind, bind_all, bind_class, or tag_bind, the callback is
called with an Event as first argument. It will have the
following attributes (in braces are the event types for which
the attribute is valid):

    serial - serial number of event
num - mouse button pressed (ButtonPress, ButtonRelease)
focus - whether the window has the focus (Enter, Leave)
height - height of the exposed window (Configure, Expose)
width - width of the exposed window (Configure, Expose)
keycode - keycode of the pressed key (KeyPress, KeyRelease)
state - state of the event as a number (ButtonPress, ButtonRelease,
                        Enter, KeyPress, KeyRelease,
                        Leave, Motion)
state - state as a string (Visibility)
time - when the event occurred
x - x-position of the mouse
y - y-position of the mouse
x_root - x-position of the mouse on the screen
         (ButtonPress, ButtonRelease, KeyPress, KeyRelease, Motion)
y_root - y-position of the mouse on the screen
         (ButtonPress, ButtonRelease, KeyPress, KeyRelease, Motion)
char - pressed character (KeyPress, KeyRelease)
send_event - see X/Windows documentation
keysym - keysym of the event as a string (KeyPress, KeyRelease)
keysym_num - keysym of the event as a number (KeyPress, KeyRelease)
type - type of the event as a number
widget - widget in which the event occurred
delta - delta of wheel movement (MouseWheel)

**Module:** [[Modules/tkinter|tkinter]]
**Line:** 217

## Methods

### Magic Methods
- [[Functions/__repr___4117|__repr__()]] (line 260)
