---
type: class
name: Pdb
module: pdb
lineno: 306
tags:
  - python
  - class
---

# Class: Pdb

## Overview

**Module:** [[Modules/pdb|pdb]]
**Line:** 306

## Inheritance

**Inherits from:**
- [[Classes/Bdb|Bdb]]
- [[Classes/Cmd|Cmd]]

## Methods

### Constructors
- [[Functions/__init___5174|__init__()]] (line 315)

### Methods
- [[Functions/sigint_handler_5175|sigint_handler()]] (line 368)
- [[Functions/reset_5176|reset()]] (line 375)
- [[Functions/forget_5177|forget()]] (line 379)
- [[Functions/setup_5178|setup()]] (line 389)
- [[Functions/user_call_5179|user_call()]] (line 425)
- [[Functions/user_line_5180|user_line()]] (line 434)
- [[Functions/bp_commands_5181|bp_commands()]] (line 452)
- [[Functions/user_return_5182|user_return()]] (line 476)
- [[Functions/user_exception_5183|user_exception()]] (line 485)
- [[Functions/_cmdloop_5184|_cmdloop()]] (line 505)
- [[Functions/_validate_file_mtime_5185|_validate_file_mtime()]] (line 517)
- [[Functions/_show_display_5186|_show_display()]] (line 533)
- [[Functions/_get_tb_and_exceptions_5187|_get_tb_and_exceptions()]] (line 547)
- [[Functions/_hold_exceptions_5188|_hold_exceptions()]] (line 584)
- [[Functions/interaction_5189|interaction()]] (line 604)
- [[Functions/displayhook_5190|displayhook()]] (line 631)
- [[Functions/_disable_command_completion_5191|_disable_command_completion()]] (line 640)
- [[Functions/_exec_in_closure_5192|_exec_in_closure()]] (line 649)
- [[Functions/default_5193|default()]] (line 733)
- [[Functions/_replace_convenience_variables_5194|_replace_convenience_variables()]] (line 781)
- [[Functions/precmd_5195|precmd()]] (line 814)
- [[Functions/onecmd_5196|onecmd()]] (line 852)
- [[Functions/handle_command_def_5197|handle_command_def()]] (line 869)
- [[Functions/message_5198|message()]] (line 897)
- [[Functions/error_5199|error()]] (line 900)
- [[Functions/set_convenience_variable_5200|set_convenience_variable()]] (line 905)
- [[Functions/completenames_5201|completenames()]] (line 913)
- [[Functions/_complete_location_5202|_complete_location()]] (line 928)
- [[Functions/_complete_bpnumber_5203|_complete_bpnumber()]] (line 947)
- [[Functions/_complete_expression_5204|_complete_expression()]] (line 954)
- [[Functions/completedefault_5205|completedefault()]] (line 983)
- [[Functions/_pdbcmd_print_frame_status_5206|_pdbcmd_print_frame_status()]] (line 1000)
- [[Functions/do_commands_5207|do_commands()]] (line 1008)
- [[Functions/do_break_5208|do_break()]] (line 1093)
- [[Functions/defaultFile_5209|defaultFile()]] (line 1190)
- [[Functions/do_tbreak_5210|do_tbreak()]] (line 1202)
- [[Functions/lineinfo_5211|lineinfo()]] (line 1212)
- [[Functions/checkline_5212|checkline()]] (line 1245)
- [[Functions/do_enable_5213|do_enable()]] (line 1267)
- [[Functions/do_disable_5214|do_disable()]] (line 1285)
- [[Functions/do_condition_5215|do_condition()]] (line 1306)
- [[Functions/do_ignore_5216|do_ignore()]] (line 1337)
- [[Functions/do_clear_5217|do_clear()]] (line 1381)
- [[Functions/do_where_5218|do_where()]] (line 1433)
- [[Functions/_select_frame_5219|_select_frame()]] (line 1447)
- [[Functions/do_exceptions_5220|do_exceptions()]] (line 1456)
- [[Functions/do_up_5221|do_up()]] (line 1503)
- [[Functions/do_down_5222|do_down()]] (line 1524)
- [[Functions/do_until_5223|do_until()]] (line 1545)
- [[Functions/do_step_5224|do_step()]] (line 1570)
- [[Functions/do_next_5225|do_next()]] (line 1584)
- [[Functions/do_run_5226|do_run()]] (line 1597)
- [[Functions/do_return_5227|do_return()]] (line 1619)
- [[Functions/do_continue_5228|do_continue()]] (line 1631)
- [[Functions/do_jump_5229|do_jump()]] (line 1653)
- [[Functions/do_debug_5230|do_debug()]] (line 1683)
- [[Functions/do_quit_5231|do_quit()]] (line 1706)
- [[Functions/do_EOF_5232|do_EOF()]] (line 1718)
- [[Functions/do_args_5233|do_args()]] (line 1728)
- [[Functions/do_retval_5234|do_retval()]] (line 1749)
- [[Functions/_getval_5235|_getval()]] (line 1763)
- [[Functions/_getval_except_5236|_getval_except()]] (line 1770)
- [[Functions/_error_exc_5237|_error_exc()]] (line 1779)
- [[Functions/_msg_val_func_5238|_msg_val_func()]] (line 1783)
- [[Functions/_safe_repr_5239|_safe_repr()]] (line 1793)
- [[Functions/do_p_5240|do_p()]] (line 1799)
- [[Functions/do_pp_5241|do_pp()]] (line 1806)
- [[Functions/do_list_5242|do_list()]] (line 1817)
- [[Functions/do_longlist_5243|do_longlist()]] (line 1874)
- [[Functions/do_source_5244|do_source()]] (line 1892)
- [[Functions/_print_lines_5245|_print_lines()]] (line 1910)
- [[Functions/do_whatis_5246|do_whatis()]] (line 1931)
- [[Functions/do_display_5247|do_display()]] (line 1967)
- [[Functions/do_undisplay_5248|do_undisplay()]] (line 1992)
- [[Functions/complete_undisplay_5249|complete_undisplay()]] (line 2007)
- [[Functions/do_interact_5250|do_interact()]] (line 2011)
- [[Functions/do_alias_5251|do_alias()]] (line 2022)
- [[Functions/do_unalias_5252|do_unalias()]] (line 2072)
- [[Functions/complete_unalias_5253|complete_unalias()]] (line 2084)
- [[Functions/print_stack_trace_5254|print_stack_trace()]] (line 2099)
- [[Functions/print_stack_entry_5255|print_stack_entry()]] (line 2106)
- [[Functions/do_help_5256|do_help()]] (line 2117)
- [[Functions/help_exec_5257|help_exec()]] (line 2147)
- [[Functions/help_pdb_5258|help_pdb()]] (line 2163)
- [[Functions/lookupmodule_5259|lookupmodule()]] (line 2168)
- [[Functions/_run_5260|_run()]] (line 2198)
- [[Functions/_format_exc_5261|_format_exc()]] (line 2222)
- [[Functions/_compile_error_message_5262|_compile_error_message()]] (line 2225)
- [[Functions/_getsourcelines_5263|_getsourcelines()]] (line 2233)
- [[Functions/_help_message_from_doc_5264|_help_message_from_doc()]] (line 2243)
- [[Functions/_print_invalid_arg_5265|_print_invalid_arg()]] (line 2265)
