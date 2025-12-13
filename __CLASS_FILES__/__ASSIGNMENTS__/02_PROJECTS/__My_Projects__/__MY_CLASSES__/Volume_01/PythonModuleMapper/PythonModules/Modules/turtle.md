---
type: module
name: turtle
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\turtle.py
is_package: False
analyzed_at: 2025-12-10T03:46:22.384470
tags:
  - python
  - module
---

# Module: turtle

## Overview

Turtle graphics is a popular way for introducing programming to
kids. It was part of the original Logo programming language developed
by Wally Feurzig and Seymour Papert in 1966.

Imagine a robotic turtle starting at (0, 0) in the x-y plane. After an ``import turtle``, give it
the command turtle.forward(15), and it moves (on-screen!) 15 pixels in
the direction it is facing, drawing a line as it moves. Give it the
command turtle.right(25), and it rotates in-place 25 degrees clockwise.

By combining together these and similar commands, intricate shapes and
pictures can easily be drawn.

----- turtle.py

This module is an extended reimplementation of turtle.py from the
Python standard distribution up to Python 2.5. (See: https://www.python.org)

It tries to keep the merits of turtle.py and to be (nearly) 100%
compatible with it. This means in the first place to enable the
learning programmer to use all the commands, classes and methods
interactively when using the module from within IDLE run with
the -n switch.

Roughly it has the following features added:

- Better animation of the turtle movements, especially of turning the
  turtle. So the turtles can more easily be used as a visual feedback
  instrument by the (beginning) programmer.

- Different turtle shapes, gif-images as turtle shapes, user defined
  and user controllable turtle shapes, among them compound
  (multicolored) shapes. Turtle shapes can be stretched and tilted, which
  makes turtles very versatile geometrical objects.

- Fine control over turtle movement and screen updates via delay(),
  and enhanced tracer() and speed() methods.

- Aliases for the most commonly used commands, like fd for forward etc.,
  following the early Logo traditions. This reduces the boring work of
  typing long sequences of commands, which often occur in a natural way
  when kids try to program fancy pictures on their first encounter with
  turtle graphics.

- Turtles now have an undo()-method with configurable undo-buffer.

- Some simple commands/methods for creating event driven programs
  (mouse-, key-, timer-events). Especially useful for programming games.

- A scrollable Canvas class. The default scrollable Canvas can be
  extended interactively as needed while playing around with the turtle(s).

- A TurtleScreen class with methods controlling background color or
  background image, window and canvas size and other properties of the
  TurtleScreen.

- There is a method, setworldcoordinates(), to install a user defined
  coordinate-system for the TurtleScreen.

- The implementation uses a 2-vector class named Vec2D, derived from tuple.
  This class is public, so it can be imported by the application programmer,
  which makes certain types of computations very natural and compact.

- Appearance of the TurtleScreen and the Turtles at startup/import can be
  configured by means of a turtle.cfg configuration file.
  The default configuration mimics the appearance of the old turtle module.

- If configured appropriately the module reads in docstrings from a docstring
  dictionary in some different language, supplied separately  and replaces
  the English ones by those read in. There is a utility function
  write_docstringdict() to write a dictionary with the original (English)
  docstrings to disc, so it can serve as a template for translations.

Behind the scenes there are some features included with possible
extensions in mind. These will be commented and documented elsewhere.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\turtle.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:22

## Dependencies

This module imports:
- [[Modules/math|math]]
- [[Modules/re|re]]
- [[Modules/types|types]]
- [[Modules/time|time]]
- [[Modules/copy|copy]]

## Classes

- [[Classes/Vec2D|Vec2D]] (line 230)
- [[Classes/ScrolledCanvas|ScrolledCanvas]] (line 324)
- [[Classes/_Root|_Root]] (line 426)
- [[Classes/TurtleScreenBase|TurtleScreenBase]] (line 453)
- [[Classes/Terminator|Terminator]] (line 847)
- [[Classes/TurtleGraphicsError|TurtleGraphicsError]] (line 856)
- [[Classes/Shape|Shape]] (line 861)
- [[Classes/Tbuffer|Tbuffer]] (line 908)
- [[Classes/TurtleScreen|TurtleScreen]] (line 946)
- [[Classes/TNavigator|TNavigator]] (line 1501)
- [[Classes/TPen|TPen]] (line 2019)
- [[Classes/_TurtleImage|_TurtleImage]] (line 2488)
- [[Classes/RawTurtle|RawTurtle]] (line 2519)
- [[Classes/_Screen|_Screen]] (line 3702)
- [[Classes/Turtle|Turtle]] (line 3830)

## Functions

- [[Functions/deepcopy_3860|deepcopy()]] (line 119)
- [[Functions/config_dict_3861|config_dict()]] (line 165)
- [[Functions/readconfig_3862|readconfig()]] (line 194)
- [[Functions/__methodDict_3873|__methodDict()]] (line 283)
- [[Functions/__methods_3874|__methods()]] (line 293)
- [[Functions/__forwardmethods_3875|__forwardmethods()]] (line 303)
- [[Functions/Screen_4060|Screen()]] (line 3694)
- [[Functions/write_docstringdict_4068|write_docstringdict()]] (line 3852)
- [[Functions/read_docstrings_4069|read_docstrings()]] (line 3886)
- [[Functions/getmethparlist_4070|getmethparlist()]] (line 3915)
- [[Functions/_turtle_docrevise_4071|_turtle_docrevise()]] (line 3951)
- [[Functions/_screen_docrevise_4072|_screen_docrevise()]] (line 3963)
- [[Functions/_make_global_funcs_4073|_make_global_funcs()]] (line 3995)
- [[Functions/switchpen_4074|switchpen()]] (line 4016)
- [[Functions/demo1_4075|demo1()]] (line 4022)
- [[Functions/demo2_4076|demo2()]] (line 4075)
