---
type: module
name: tkinter
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\tkinter\__init__.py
is_package: True
analyzed_at: 2025-12-10T03:46:22.984337
tags:
  - python
  - module
---

# Module: tkinter

## Overview

Wrapper functions for Tcl/Tk.

Tkinter provides classes which allow the display, positioning and
control of widgets. Toplevel widgets are Tk and Toplevel. Other
widgets are Frame, Label, Entry, Text, Canvas, Button, Radiobutton,
Checkbutton, Scale, Listbox, Scrollbar, OptionMenu, Spinbox
LabelFrame and PanedWindow.

Properties of the widgets are specified with keyword arguments.
Keyword arguments have the same name as the corresponding resource
under Tk.

Widgets are positioned with one of the geometry managers Place, Pack
or Grid. These managers can be called with methods place, pack, grid
available in every Widget.

Actions are bound to events by resources (e.g. keyword argument
command) or with the method bind.

Example (Hello, World):
import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\tkinter\__init__.py`
**Type:** Package
**Analyzed:** 2025-12-10 03:46:22

## Dependencies

This module imports:
- [[Modules/re|re]]
- [[Modules/os|os]]
- [[Modules/enum|enum]]
- [[Modules/types|types]]
- [[Modules/collections|collections]]

## Classes

- [[Classes/_VersionInfoType|_VersionInfoType]] (line 151)
- [[Classes/EventType|EventType]] (line 175)
- [[Classes/Event|Event]] (line 217)
- [[Classes/Variable|Variable]] (line 371)
- [[Classes/StringVar|StringVar]] (line 551)
- [[Classes/IntVar|IntVar]] (line 575)
- [[Classes/DoubleVar|DoubleVar]] (line 600)
- [[Classes/BooleanVar|BooleanVar]] (line 621)
- [[Classes/Misc|Misc]] (line 671)
- [[Classes/CallWrapper|CallWrapper]] (line 2053)
- [[Classes/XView|XView]] (line 2075)
- [[Classes/YView|YView]] (line 2096)
- [[Classes/Wm|Wm]] (line 2117)
- [[Classes/Tk|Tk]] (line 2434)
- [[Classes/Pack|Pack]] (line 2575)
- [[Classes/Place|Place]] (line 2621)
- [[Classes/Grid|Grid]] (line 2672)
- [[Classes/BaseWidget|BaseWidget]] (line 2727)
- [[Classes/Widget|Widget]] (line 2792)
- [[Classes/Toplevel|Toplevel]] (line 2800)
- [[Classes/Button|Button]] (line 2830)
- [[Classes/Canvas|Canvas]] (line 2877)
- [[Classes/Checkbutton|Checkbutton]] (line 3187)
- [[Classes/Entry|Entry]] (line 3236)
- [[Classes/Frame|Frame]] (line 3322)
- [[Classes/Label|Label]] (line 3342)
- [[Classes/Listbox|Listbox]] (line 3366)
- [[Classes/Menu|Menu]] (line 3482)
- [[Classes/Menubutton|Menubutton]] (line 3611)
- [[Classes/Message|Message]] (line 3618)
- [[Classes/Radiobutton|Radiobutton]] (line 3625)
- [[Classes/Scale|Scale]] (line 3658)
- [[Classes/Scrollbar|Scrollbar]] (line 3697)
- [[Classes/Text|Text]] (line 3747)
- [[Classes/_setit|_setit]] (line 4164)
- [[Classes/OptionMenu|OptionMenu]] (line 4178)
- [[Classes/Image|Image]] (line 4217)
- [[Classes/PhotoImage|PhotoImage]] (line 4279)
- [[Classes/BitmapImage|BitmapImage]] (line 4542)
- [[Classes/Spinbox|Spinbox]] (line 4562)
- [[Classes/LabelFrame|LabelFrame]] (line 4740)
- [[Classes/PanedWindow|PanedWindow]] (line 4764)

## Functions

- [[Functions/_join_4110|_join()]] (line 58)
- [[Functions/_stringify_4111|_stringify()]] (line 63)
- [[Functions/_flatten_4112|_flatten()]] (line 91)
- [[Functions/_cnfmerge_4113|_cnfmerge()]] (line 106)
- [[Functions/_splitdict_4114|_splitdict()]] (line 128)
- [[Functions/_parse_version_4116|_parse_version()]] (line 159)
- [[Functions/NoDefaultRoot_4118|NoDefaultRoot()]] (line 303)
- [[Functions/_get_default_root_4119|_get_default_root()]] (line 317)
- [[Functions/_get_temp_root_4120|_get_temp_root()]] (line 329)
- [[Functions/_destroy_temp_root_4121|_destroy_temp_root()]] (line 346)
- [[Functions/_tkerror_4122|_tkerror()]] (line 354)
- [[Functions/_exit_4123|_exit()]] (line 359)
- [[Functions/mainloop_4146|mainloop()]] (line 651)
- [[Functions/getboolean_4147|getboolean()]] (line 661)
- [[Functions/_print_command_4350|_print_command()]] (line 2549)
- [[Functions/Tcl_4351|Tcl()]] (line 2571)
- [[Functions/image_names_4596|image_names()]] (line 4552)
- [[Functions/image_types_4597|image_types()]] (line 4557)
- [[Functions/_test_4634|_test()]] (line 4958)
