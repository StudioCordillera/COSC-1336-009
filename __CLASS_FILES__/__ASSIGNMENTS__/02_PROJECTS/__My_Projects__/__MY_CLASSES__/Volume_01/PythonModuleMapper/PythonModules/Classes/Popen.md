---
type: class
name: Popen
module: subprocess
lineno: 759
tags:
  - python
  - class
---

# Class: Popen

## Overview

Execute a child program in a new process.

For a complete description of the arguments see the Python documentation.

Arguments:
  args: A string, or a sequence of program arguments.

  bufsize: supplied as the buffering argument to the open() function when
      creating the stdin/stdout/stderr pipe file objects

  executable: A replacement program to execute.

  stdin, stdout and stderr: These specify the executed programs' standard
      input, standard output and standard error file handles, respectively.

  preexec_fn: (POSIX only) An object to be called in the child process
      just before the child is executed.

  close_fds: Controls closing or inheriting of file descriptors.

  shell: If true, the command will be executed through the shell.

  cwd: Sets the current directory before the child is executed.

  env: Defines the environment variables for the new process.

  text: If true, decode stdin, stdout and stderr using the given encoding
      (if set) or the system default otherwise.

  universal_newlines: Alias of text, provided for backwards compatibility.

  startupinfo and creationflags (Windows only)

  restore_signals (POSIX only)

  start_new_session (POSIX only)

  process_group (POSIX only)

  group (POSIX only)

  extra_groups (POSIX only)

  user (POSIX only)

  umask (POSIX only)

  pass_fds (POSIX only)

  encoding and errors: Text mode encoding and error handling to use for
      file objects stdin, stdout and stderr.

Attributes:
    stdin, stdout, stderr, pid, returncode

**Module:** [[Modules/subprocess|subprocess]]
**Line:** 759

## Methods

### Constructors
- [[Functions/__init___2638|__init__()]] (line 817)
- [[Functions/__del___2644|__del__()]] (line 1133)

### Magic Methods
- [[Functions/__repr___2639|__repr__()]] (line 1077)
- [[Functions/__enter___2642|__enter__()]] (line 1102)
- [[Functions/__exit___2643|__exit__()]] (line 1105)

### Methods
- [[Functions/universal_newlines_2640|universal_newlines()]] (line 1095)
- [[Functions/_translate_newlines_2641|_translate_newlines()]] (line 1098)
- [[Functions/_get_devnull_2645|_get_devnull()]] (line 1148)
- [[Functions/_stdin_write_2646|_stdin_write()]] (line 1153)
- [[Functions/communicate_2647|communicate()]] (line 1178)
- [[Functions/poll_2648|poll()]] (line 1249)
- [[Functions/_remaining_time_2649|_remaining_time()]] (line 1255)
- [[Functions/_check_timeout_2650|_check_timeout()]] (line 1263)
- [[Functions/wait_2651|wait()]] (line 1275)
- [[Functions/_close_pipe_fds_2652|_close_pipe_fds()]] (line 1298)
- [[Functions/_on_error_fd_closer_2653|_on_error_fd_closer()]] (line 1328)
- [[Functions/_get_handles_2654|_get_handles()]] (line 1704)
- [[Functions/_make_inheritable_2655|_make_inheritable()]] (line 1430)
- [[Functions/_filter_handle_list_2656|_filter_handle_list()]] (line 1439)
- [[Functions/_execute_child_2657|_execute_child()]] (line 1808)
- [[Functions/_internal_poll_2658|_internal_poll()]] (line 1987)
- [[Functions/_wait_2659|_wait()]] (line 2034)
- [[Functions/_readerthread_2660|_readerthread()]] (line 1614)
- [[Functions/_communicate_2661|_communicate()]] (line 2075)
- [[Functions/send_signal_2662|send_signal()]] (line 2192)
- [[Functions/terminate_2663|terminate()]] (line 2224)
- [[Functions/_posix_spawn_2664|_posix_spawn()]] (line 1768)
- [[Functions/_handle_exitstatus_2665|_handle_exitstatus()]] (line 1978)
- [[Functions/_try_wait_2666|_try_wait()]] (line 2021)
- [[Functions/_save_input_2667|_save_input()]] (line 2180)
- [[Functions/kill_2668|kill()]] (line 2229)
