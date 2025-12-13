---
type: class
name: Bdb
module: bdb
lineno: 18
tags:
  - python
  - class
---

# Class: Bdb

## Overview

Generic Python debugger base class.

This class takes care of details of the trace facility;
a derived class should implement user interaction.
The standard debugger class (pdb.Pdb) is an example.

The optional skip argument must be an iterable of glob-style
module name patterns.  The debugger will not step into frames
that originate in a module that matches one of these patterns.
Whether a frame is considered to originate in a certain module
is determined by the __name__ in the frame globals.

**Module:** [[Modules/bdb|bdb]]
**Line:** 18

## Inheritance

**Subclasses:**
- [[Classes/Tdb|Tdb]]
- [[Classes/Pdb|Pdb]]

## Methods

### Constructors
- [[Functions/__init___5084|__init__()]] (line 32)

### Methods
- [[Functions/canonic_5085|canonic()]] (line 43)
- [[Functions/reset_5086|reset()]] (line 60)
- [[Functions/set_enterframe_5087|set_enterframe()]] (line 68)
- [[Functions/trace_dispatch_5088|trace_dispatch()]] (line 73)
- [[Functions/dispatch_line_5089|dispatch_line()]] (line 120)
- [[Functions/dispatch_call_5090|dispatch_call()]] (line 132)
- [[Functions/dispatch_return_5091|dispatch_return()]] (line 154)
- [[Functions/dispatch_exception_5092|dispatch_exception()]] (line 181)
- [[Functions/dispatch_opcode_5093|dispatch_opcode()]] (line 208)
- [[Functions/is_skipped_module_5094|is_skipped_module()]] (line 223)
- [[Functions/stop_here_5095|stop_here()]] (line 232)
- [[Functions/break_here_5096|break_here()]] (line 247)
- [[Functions/do_clear_5097|do_clear()]] (line 274)
- [[Functions/break_anywhere_5098|break_anywhere()]] (line 281)
- [[Functions/user_call_5099|user_call()]] (line 289)
- [[Functions/user_line_5100|user_line()]] (line 293)
- [[Functions/user_return_5101|user_return()]] (line 297)
- [[Functions/user_exception_5102|user_exception()]] (line 301)
- [[Functions/user_opcode_5103|user_opcode()]] (line 305)
- [[Functions/_set_trace_opcodes_5104|_set_trace_opcodes()]] (line 309)
- [[Functions/_set_stopinfo_5105|_set_stopinfo()]] (line 319)
- [[Functions/_set_caller_tracefunc_5106|_set_caller_tracefunc()]] (line 334)
- [[Functions/set_until_5107|set_until()]] (line 347)
- [[Functions/set_step_5108|set_step()]] (line 355)
- [[Functions/set_stepinstr_5109|set_stepinstr()]] (line 359)
- [[Functions/set_next_5110|set_next()]] (line 363)
- [[Functions/set_return_5111|set_return()]] (line 367)
- [[Functions/set_trace_5112|set_trace()]] (line 374)
- [[Functions/set_continue_5113|set_continue()]] (line 393)
- [[Functions/set_quit_5114|set_quit()]] (line 411)
- [[Functions/_add_to_breaks_5115|_add_to_breaks()]] (line 428)
- [[Functions/set_break_5116|set_break()]] (line 434)
- [[Functions/_load_breaks_5117|_load_breaks()]] (line 458)
- [[Functions/_prune_breaks_5118|_prune_breaks()]] (line 469)
- [[Functions/clear_break_5119|clear_break()]] (line 482)
- [[Functions/clear_bpbynumber_5120|clear_bpbynumber()]] (line 499)
- [[Functions/clear_all_file_breaks_5121|clear_all_file_breaks()]] (line 512)
- [[Functions/clear_all_breaks_5122|clear_all_breaks()]] (line 527)
- [[Functions/get_bpbynumber_5123|get_bpbynumber()]] (line 540)
- [[Functions/get_break_5124|get_break()]] (line 560)
- [[Functions/get_breaks_5125|get_breaks()]] (line 566)
- [[Functions/get_file_breaks_5126|get_file_breaks()]] (line 576)
- [[Functions/get_all_breaks_5127|get_all_breaks()]] (line 587)
- [[Functions/get_stack_5128|get_stack()]] (line 594)
- [[Functions/format_stack_entry_5129|format_stack_entry()]] (line 617)
- [[Functions/run_5130|run()]] (line 651)
- [[Functions/runeval_5131|runeval()]] (line 673)
- [[Functions/runctx_5132|runctx()]] (line 693)
- [[Functions/runcall_5133|runcall()]] (line 700)
