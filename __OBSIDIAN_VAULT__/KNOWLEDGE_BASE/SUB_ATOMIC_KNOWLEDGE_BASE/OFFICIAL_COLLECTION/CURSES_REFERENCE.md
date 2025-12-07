# CURSES_REFERENCE

## Core Definition
**Curses** is Python's interface to the curses library for creating terminal-based user interfaces with character-cell displays. Provides portable advanced terminal handling for text-based applications, menus, forms, and interactive programs.

**Tags**: #curses #terminal #tui #cli #ncurses #text-ui #menu #window

---

## COMPLETE CURSES QUICK REFERENCE

### CURSES FUNCTIONS & METHODS - Target | Operation | Output

```python
# ═══════════════════════════════════════════════════════════════════════════
# INITIALIZATION & CLEANUP
# ═══════════════════════════════════════════════════════════════════════════
curses.initscr()                     # None | Initialize curses library | Returns stdscr window object
curses.endwin()                      # None | De-initialize curses | Returns None, restores terminal
curses.wrapper(func, *args, **kwargs) # Function | Safe curses initialization | Calls func with stdscr, handles cleanup
curses.isendwin()                    # None | Check if endwin() called | Returns True/False

# ═══════════════════════════════════════════════════════════════════════════
# WINDOW CREATION & MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
curses.newwin(nlines, ncols)         # Dimensions | Create new window | Returns window object
curses.newwin(nlines, ncols, begin_y, begin_x) # Dims + position | Create positioned window | Returns window object
curses.newpad(nlines, ncols)         # Dimensions | Create pad (large virtual window) | Returns pad object
window.subwin(begin_y, begin_x)      # Position | Create subwindow | Returns subwindow object
window.subwin(nlines, ncols, begin_y, begin_x) # Full spec | Create sized subwindow | Returns subwindow object
window.derwin(begin_y, begin_x)      # Relative position | Create derived window | Returns window object
window.derwin(nlines, ncols, begin_y, begin_x) # Full relative spec | Create sized derived window | Returns window object
window.subpad(begin_y, begin_x)      # Position | Create sub-pad | Returns pad object
window.subpad(nlines, ncols, begin_y, begin_x) # Full spec | Create sized sub-pad | Returns pad object

# ═══════════════════════════════════════════════════════════════════════════
# TEXT OUTPUT - ADDING CHARACTERS & STRINGS
# ═══════════════════════════════════════════════════════════════════════════
window.addch(ch)                     # Window | Add char at cursor | Returns None
window.addch(ch, attr)               # Window | Add char with attributes | Returns None
window.addch(y, x, ch)               # Window | Add char at position | Returns None
window.addch(y, x, ch, attr)         # Window | Add char at pos with attr | Returns None
window.addstr(str)                   # Window | Add string at cursor | Returns None
window.addstr(str, attr)             # Window | Add string with attributes | Returns None
window.addstr(y, x, str)             # Window | Add string at position | Returns None
window.addstr(y, x, str, attr)       # Window | Add string at pos with attr | Returns None
window.addnstr(str, n)               # Window | Add max n chars | Returns None
window.addnstr(str, n, attr)         # Window | Add max n chars with attr | Returns None
window.addnstr(y, x, str, n)         # Window | Add max n chars at position | Returns None
window.addnstr(y, x, str, n, attr)   # Window | Add max n chars at pos with attr | Returns None
window.insch(ch)                     # Window | Insert char at cursor | Returns None, shifts right
window.insch(ch, attr)               # Window | Insert char with attributes | Returns None
window.insch(y, x, ch)               # Window | Insert char at position | Returns None
window.insch(y, x, ch, attr)         # Window | Insert char at pos with attr | Returns None
window.insstr(str)                   # Window | Insert string at cursor | Returns None, shifts right
window.insstr(str, attr)             # Window | Insert string with attributes | Returns None
window.insstr(y, x, str)             # Window | Insert string at position | Returns None
window.insstr(y, x, str, attr)       # Window | Insert string at pos with attr | Returns None
window.insnstr(str, n)               # Window | Insert max n chars | Returns None
window.insnstr(str, n, attr)         # Window | Insert max n chars with attr | Returns None
window.insnstr(y, x, str, n)         # Window | Insert max n chars at position | Returns None
window.insnstr(y, x, str, n, attr)   # Window | Insert max n chars at pos with attr | Returns None
window.echochar(ch)                  # Window | Add char and refresh | Returns None, immediate display
window.echochar(ch, attr)            # Window | Add char with attr and refresh | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# TEXT INPUT - READING CHARACTERS & STRINGS
# ═══════════════════════════════════════════════════════════════════════════
window.getch()                       # Window | Get character (blocking) | Returns int keycode
window.getch(y, x)                   # Window | Get char at position | Returns int keycode
window.get_wch()                     # Window | Get wide character | Returns char/int (Python 3.3+)
window.get_wch(y, x)                 # Window | Get wide char at position | Returns char/int
window.getkey()                      # Window | Get key as string | Returns string key name
window.getkey(y, x)                  # Window | Get key string at position | Returns string key name
window.getstr()                      # Window | Get string from user | Returns bytes object (max 2047 chars)
window.getstr(n)                     # Window | Get string max n chars | Returns bytes object
window.getstr(y, x)                  # Window | Get string at position | Returns bytes object
window.getstr(y, x, n)               # Window | Get string at pos max n chars | Returns bytes object
curses.ungetch(ch)                   # Int/char | Push char back to input | Returns None
curses.unget_wch(ch)                 # Int/char | Push wide char back | Returns None (Python 3.3+)

# ═══════════════════════════════════════════════════════════════════════════
# CURSOR MANIPULATION
# ═══════════════════════════════════════════════════════════════════════════
window.move(new_y, new_x)            # Window | Move cursor to position | Returns None
window.getyx()                       # Window | Get cursor position | Returns (y, x) tuple
curses.curs_set(visibility)          # Int (0/1/2) | Set cursor visibility | Returns previous state or raises
curses.getsyx()                      # None | Get virtual screen cursor | Returns (y, x) or (-1, -1)
curses.setsyx(y, x)                  # Coordinates | Set virtual screen cursor | Returns None
window.leaveok(flag)                 # Bool | Leave cursor where it is | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# WINDOW INFORMATION & GEOMETRY
# ═══════════════════════════════════════════════════════════════════════════
window.getmaxyx()                    # Window | Get window dimensions | Returns (lines, cols) tuple
window.getbegyx()                    # Window | Get window start position | Returns (y, x) tuple
window.getparyx()                    # Window | Get parent-relative position | Returns (y, x) or (-1, -1)
curses.LINES                         # Module constant | Terminal height | Int (after initscr)
curses.COLS                          # Module constant | Terminal width | Int (after initscr)
curses.update_lines_cols()           # None | Update LINES/COLS after resize | Returns None
window.enclose(y, x)                 # Coordinates | Test if point in window | Returns True/False

# ═══════════════════════════════════════════════════════════════════════════
# SCREEN REFRESH & UPDATE
# ═══════════════════════════════════════════════════════════════════════════
window.refresh()                     # Window | Update screen from window | Returns None
window.noutrefresh()                 # Window | Mark for refresh (no update) | Returns None
curses.doupdate()                    # None | Update physical screen | Returns None (call after noutrefresh)
window.redrawwin()                   # Window | Mark entire window for redraw | Returns None
window.redrawln(beg, num)            # Window | Mark lines for redraw | Returns None
window.touchwin()                    # Window | Mark all lines changed | Returns None
window.touchline(start, count)       # Window | Mark lines as changed | Returns None
window.touchline(start, count, changed) # Window | Mark/unmark lines changed | Returns None
window.untouchwin()                  # Window | Mark all lines unchanged | Returns None
window.is_wintouched()               # Window | Check if window modified | Returns True/False
window.is_linetouched(line)          # Window | Check if line modified | Returns True/False

# ═══════════════════════════════════════════════════════════════════════════
# CLEARING & ERASING
# ═══════════════════════════════════════════════════════════════════════════
window.clear()                       # Window | Clear and mark for full repaint | Returns None
window.erase()                       # Window | Clear window | Returns None
window.clrtobot()                    # Window | Clear from cursor to bottom | Returns None
window.clrtoeol()                    # Window | Clear from cursor to end of line | Returns None
window.delch()                       # Window | Delete char at cursor | Returns None
window.delch(y, x)                   # Window | Delete char at position | Returns None
window.deleteln()                    # Window | Delete current line | Returns None, lines move up
window.insertln()                    # Window | Insert blank line | Returns None, lines move down
window.insdelln(nlines)              # Window | Insert/delete lines | Returns None (negative = delete)

# ═══════════════════════════════════════════════════════════════════════════
# ATTRIBUTES & COLORS
# ═══════════════════════════════════════════════════════════════════════════
curses.start_color()                 # None | Initialize color support | Returns None (call after initscr)
curses.init_pair(pair_number, fg, bg) # Color nums | Define color pair | Returns None (pair 1-255)
curses.color_pair(pair_number)       # Int | Get color pair attribute | Returns attribute value
curses.pair_number(attr)             # Attribute | Extract pair number from attr | Returns int
curses.init_color(color_num, r, g, b) # Color + RGB | Redefine color | Returns None (0-1000 RGB)
curses.color_content(color_number)   # Int | Get RGB values | Returns (r, g, b) tuple (0-1000)
curses.pair_content(pair_number)     # Int | Get pair colors | Returns (fg, bg) tuple
curses.has_colors()                  # None | Check color support | Returns True/False
curses.can_change_color()            # None | Check if colors changeable | Returns True/False
curses.use_default_colors()          # None | Enable default terminal colors | Returns None
curses.assume_default_colors(fg, bg) # Colors | Set default color pair 0 | Returns None (Python 3.14+)

# Attribute Manipulation
window.attron(attr)                  # Window | Turn on attributes | Returns None
window.attroff(attr)                 # Window | Turn off attributes | Returns None
window.attrset(attr)                 # Window | Set attributes | Returns None
window.standout()                    # Window | Turn on standout mode | Returns None
window.standend()                    # Window | Turn off standout mode | Returns None
window.chgat(attr)                   # Window | Change attrs from cursor to EOL | Returns None
window.chgat(num, attr)              # Window | Change num chars attributes | Returns None
window.chgat(y, x, attr)             # Window | Change attrs from position to EOL | Returns None
window.chgat(y, x, num, attr)        # Window | Change num chars at position | Returns None

# Background
window.bkgd(ch)                      # Window | Set background char | Returns None
window.bkgd(ch, attr)                # Window | Set background char + attr | Returns None
window.bkgdset(ch)                   # Window | Set background property | Returns None
window.bkgdset(ch, attr)             # Window | Set background char + attr property | Returns None
window.getbkgd()                     # Window | Get background char/attr | Returns int

# ═══════════════════════════════════════════════════════════════════════════
# BORDERS & LINES
# ═══════════════════════════════════════════════════════════════════════════
window.border()                      # Window | Draw border with defaults | Returns None
window.border(ls, rs, ts, bs, tl, tr, bl, br) # Window | Draw custom border | Returns None
window.box()                         # Window | Draw box with defaults | Returns None
window.box(vertch, horch)            # Window | Draw box with custom chars | Returns None
window.hline(ch, n)                  # Window | Draw horizontal line | Returns None
window.hline(y, x, ch, n)            # Window | Draw hline at position | Returns None
window.vline(ch, n)                  # Window | Draw vertical line | Returns None
window.vline(y, x, ch, n)            # Window | Draw vline at position | Returns None
window.vline(y, x, ch, n, attr)      # Window | Draw vline with attributes | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# INPUT/OUTPUT MODES
# ═══════════════════════════════════════════════════════════════════════════
curses.cbreak()                      # None | Enable cbreak mode (no buffering) | Returns None
curses.nocbreak()                    # None | Disable cbreak mode | Returns None
curses.raw()                         # None | Enable raw mode (no signal processing) | Returns None
curses.noraw()                       # None | Disable raw mode | Returns None
curses.echo()                        # None | Enable echo of input | Returns None
curses.noecho()                      # None | Disable echo of input | Returns None
curses.nl()                          # None | Enable newline translation | Returns None
curses.nonl()                        # None | Disable newline translation | Returns None
window.keypad(flag)                  # Bool | Enable/disable special keys | Returns None
window.nodelay(flag)                 # Bool | Make getch() non-blocking | Returns None
window.timeout(delay)                # Int (ms) | Set input timeout | Returns None (-1=blocking, 0=non-blocking)
window.notimeout(flag)               # Bool | Enable/disable escape timeout | Returns None
curses.halfdelay(tenths)             # Int (0-255) | Half-delay mode | Returns None (tenths of seconds)
curses.meta(flag)                    # Bool | Enable 8-bit input | Returns None
window.idlok(flag)                   # Bool | Enable hardware line editing | Returns None
window.idcok(flag)                   # Bool | Enable hardware insert/delete char | Returns None
window.immedok(flag)                 # Bool | Auto-refresh on change | Returns None
window.scrollok(flag)                # Bool | Enable scrolling | Returns None
window.setscrreg(top, bottom)        # Window | Set scrolling region | Returns None
window.clearok(flag)                 # Bool | Force clear on next refresh | Returns None
window.syncok(flag)                  # Bool | Auto-call syncup on changes | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# SCROLLING
# ═══════════════════════════════════════════════════════════════════════════
window.scroll()                      # Window | Scroll up 1 line | Returns None
window.scroll(lines)                 # Window | Scroll up/down n lines | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# WINDOW POSITIONING & RESIZING
# ═══════════════════════════════════════════════════════════════════════════
window.mvwin(new_y, new_x)           # Window | Move window to position | Returns None
window.mvderwin(y, x)                # Window | Move within parent | Returns None
window.resize(nlines, ncols)         # Window | Resize window | Returns None
curses.resize_term(nlines, ncols)    # Terminal dims | Resize term and windows | Returns None
curses.resizeterm(nlines, ncols)     # Terminal dims | Resize with bookkeeping | Returns None
curses.is_term_resized(nlines, ncols) # Dimensions | Check if resize needed | Returns True/False

# ═══════════════════════════════════════════════════════════════════════════
# OVERLAYING & COPYING
# ═══════════════════════════════════════════════════════════════════════════
window.overlay(destwin)              # Window | Non-destructive copy | Returns None
window.overlay(destwin, sminrow, smincol, dminrow, dmincol, dmaxrow, dmaxcol) # Window | Copy region non-destructive | Returns None
window.overwrite(destwin)            # Window | Destructive copy | Returns None
window.overwrite(destwin, sminrow, smincol, dminrow, dmincol, dmaxrow, dmaxcol) # Window | Copy region destructive | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# WINDOW SYNCHRONIZATION
# ═══════════════════════════════════════════════════════════════════════════
window.syncup()                      # Window | Touch ancestors | Returns None
window.syncdown()                    # Window | Touch from ancestors | Returns None
window.cursyncup()                   # Window | Update cursor in ancestors | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# PAD-SPECIFIC METHODS
# ═══════════════════════════════════════════════════════════════════════════
pad.refresh(pminrow, pmincol, sminrow, smincol, smaxrow, smaxcol) # Pad | Display pad region on screen | Returns None
pad.noutrefresh(pminrow, pmincol, sminrow, smincol, smaxrow, smaxcol) # Pad | Mark pad region for refresh | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# READING FROM WINDOW
# ═══════════════════════════════════════════════════════════════════════════
window.inch()                        # Window | Get char at cursor | Returns int (char + attrs)
window.inch(y, x)                    # Window | Get char at position | Returns int (char + attrs)
window.instr()                       # Window | Get string from cursor | Returns bytes (max 2047)
window.instr(n)                      # Window | Get n chars from cursor | Returns bytes
window.instr(y, x)                   # Window | Get string from position | Returns bytes
window.instr(y, x, n)                # Window | Get n chars from position | Returns bytes

# ═══════════════════════════════════════════════════════════════════════════
# MOUSE SUPPORT
# ═══════════════════════════════════════════════════════════════════════════
curses.mousemask(mousemask)          # Bitmask | Set mouse events to report | Returns (availmask, oldmask)
curses.getmouse()                    # None | Get mouse event | Returns (id, x, y, z, bstate) tuple
curses.ungetmouse(id, x, y, z, bstate) # Event data | Push mouse event back | Returns None
curses.mouseinterval(interval)       # Int (ms) | Set click interval | Returns previous interval

# ═══════════════════════════════════════════════════════════════════════════
# TERMINAL CONTROL
# ═══════════════════════════════════════════════════════════════════════════
curses.beep()                        # None | Emit beep sound | Returns None
curses.flash()                       # None | Flash screen | Returns None
curses.flushinp()                    # None | Flush input buffer | Returns None
curses.napms(ms)                     # Int (ms) | Sleep milliseconds | Returns None
curses.delay_output(ms)              # Int (ms) | Delay output | Returns None
curses.baudrate()                    # None | Get terminal baud rate | Returns int
curses.erasechar()                   # None | Get erase character | Returns bytes object
curses.killchar()                    # None | Get line kill character | Returns bytes object
curses.termname()                    # None | Get terminal name | Returns bytes (TERM value)
curses.longname()                    # None | Get terminal description | Returns bytes (max 128 chars)
curses.termattrs()                   # None | Get supported attributes | Returns int bitmask

# ═══════════════════════════════════════════════════════════════════════════
# TERMINAL STATE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
curses.def_prog_mode()               # None | Save current terminal mode | Returns None
curses.def_shell_mode()              # None | Save shell mode | Returns None
curses.reset_prog_mode()             # None | Restore program mode | Returns None
curses.reset_shell_mode()            # None | Restore shell mode | Returns None
curses.savetty()                     # None | Save terminal state | Returns None
curses.resetty()                     # None | Restore terminal state | Returns None
curses.filter()                      # None | Restrict to one line | Returns None (call before initscr)

# ═══════════════════════════════════════════════════════════════════════════
# TERMINFO DATABASE ACCESS
# ═══════════════════════════════════════════════════════════════════════════
curses.setupterm(term, fd)           # Terminal info | Initialize terminfo | Returns None
curses.tigetflag(capname)            # String | Get boolean capability | Returns int (-1/0/1)
curses.tigetnum(capname)             # String | Get numeric capability | Returns int
curses.tigetstr(capname)             # String | Get string capability | Returns bytes or None
curses.tparm(str, *args)             # Parameterized string | Format terminfo string | Returns bytes
curses.putp(str)                     # Bytes | Output terminfo capability | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# ENVIRONMENT & CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════
curses.use_env(flag)                 # Bool | Use LINES/COLUMNS env vars | Returns None (call before initscr)
curses.typeahead(fd)                 # File descriptor | Set typeahead checking | Returns None
curses.qiflush()                     # None | Flush on interrupt | Returns None
curses.qiflush(flag)                 # Bool | Set flush on interrupt | Returns None
curses.noqiflush()                   # None | Don't flush on interrupt | Returns None
curses.get_escdelay()                # None | Get escape delay | Returns int (ms)
curses.set_escdelay(ms)              # Int (ms) | Set escape delay | Returns None
curses.get_tabsize()                 # None | Get tab size | Returns int
curses.set_tabsize(size)             # Int | Set tab size | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# KEY NAME UTILITIES
# ═══════════════════════════════════════════════════════════════════════════
curses.keyname(k)                    # Int | Get key name | Returns bytes object
curses.has_key(ch)                   # Int | Check if key recognized | Returns True/False
curses.unctrl(ch)                    # Int/char | Get printable representation | Returns bytes object

# ═══════════════════════════════════════════════════════════════════════════
# WINDOW SAVE/RESTORE
# ═══════════════════════════════════════════════════════════════════════════
window.putwin(file)                  # Window + file object | Save window to file | Returns None
curses.getwin(file)                  # File object | Restore window from file | Returns window object

# ═══════════════════════════════════════════════════════════════════════════
# WINDOW ENCODING
# ═══════════════════════════════════════════════════════════════════════════
window.encoding                      # Window attribute | Get/set encoding | String (locale default)

# ═══════════════════════════════════════════════════════════════════════════
# CAPABILITY CHECKS
# ═══════════════════════════════════════════════════════════════════════════
curses.has_ic()                      # None | Check insert/delete char support | Returns True/False
curses.has_il()                      # None | Check insert/delete line support | Returns True/False
curses.has_extended_color_support()  # None | Check extended color support | Returns True/False (Python 3.10+)

# ═══════════════════════════════════════════════════════════════════════════
# TEXTPAD MODULE - TEXT EDITING WIDGET
# ═══════════════════════════════════════════════════════════════════════════
from curses import textpad
textpad.Textbox(win)                 # Window | Create text editor widget | Returns Textbox object
textbox.edit()                       # Textbox | Enter edit mode | Returns window contents as string
textbox.edit(validator)              # Textbox + validator func | Edit with validation | Returns string
textbox.do_command(ch)               # Textbox + keystroke | Process edit command | Returns None
textbox.gather()                     # Textbox | Get window contents | Returns string
textbox.stripspaces                  # Textbox attribute | Strip trailing blanks | Bool (default True)
textpad.rectangle(win, uly, ulx, lry, lrx) # Window + coords | Draw rectangle | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS - ATTRIBUTES
# ═══════════════════════════════════════════════════════════════════════════
curses.A_NORMAL                      # Normal display (no attributes)
curses.A_STANDOUT                    # Best highlighting mode
curses.A_UNDERLINE                   # Underlining
curses.A_REVERSE                     # Reverse video
curses.A_BLINK                       # Blinking
curses.A_DIM                         # Half bright
curses.A_BOLD                        # Extra bright or bold
curses.A_ALTCHARSET                  # Alternate character set
curses.A_INVIS                       # Invisible or blank
curses.A_PROTECT                     # Protected mode
curses.A_HORIZONTAL                  # Horizontal highlight
curses.A_LEFT                        # Left highlight
curses.A_LOW                         # Low highlight
curses.A_RIGHT                       # Right highlight
curses.A_TOP                         # Top highlight
curses.A_VERTICAL                    # Vertical highlight
curses.A_ITALIC                      # Italic mode (Python 3.7+)

# Attribute Extraction Masks
curses.A_ATTRIBUTES                  # Bit-mask to extract attributes
curses.A_CHARTEXT                    # Bit-mask to extract character
curses.A_COLOR                       # Bit-mask to extract color pair

# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS - COLORS
# ═══════════════════════════════════════════════════════════════════════════
curses.COLOR_BLACK                   # Black color
curses.COLOR_RED                     # Red color
curses.COLOR_GREEN                   # Green color
curses.COLOR_YELLOW                  # Yellow color
curses.COLOR_BLUE                    # Blue color
curses.COLOR_MAGENTA                 # Magenta color
curses.COLOR_CYAN                    # Cyan color
curses.COLOR_WHITE                   # White color
curses.COLORS                        # Max colors available (after start_color)
curses.COLOR_PAIRS                   # Max color pairs available (after start_color)

# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS - KEYS (Partial List - 100+ Key Constants)
# ═══════════════════════════════════════════════════════════════════════════
curses.KEY_MIN                       # Minimum key value
curses.KEY_MAX                       # Maximum key value
curses.KEY_BREAK                     # Break key
curses.KEY_DOWN                      # Down arrow
curses.KEY_UP                        # Up arrow
curses.KEY_LEFT                      # Left arrow
curses.KEY_RIGHT                     # Right arrow
curses.KEY_HOME                      # Home key
curses.KEY_END                       # End key
curses.KEY_BACKSPACE                 # Backspace
curses.KEY_F0 to KEY_F63             # Function keys F0-F63
curses.KEY_NPAGE                     # Next page (Page Down)
curses.KEY_PPAGE                     # Previous page (Page Up)
curses.KEY_ENTER                     # Enter key
curses.KEY_IC                        # Insert char
curses.KEY_DC                        # Delete char
curses.KEY_DL                        # Delete line
curses.KEY_IL                        # Insert line
curses.KEY_CLEAR                     # Clear screen
curses.KEY_EOS                       # Clear to end of screen
curses.KEY_EOL                       # Clear to end of line
curses.KEY_SF                        # Scroll forward
curses.KEY_SR                        # Scroll backward
curses.KEY_RESIZE                    # Terminal resize event
curses.KEY_MOUSE                     # Mouse event occurred
curses.KEY_BTAB                      # Back tab
# ... (90+ more key constants available)

# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS - ACS (ALTERNATE CHARACTER SET) - Box Drawing
# ═══════════════════════════════════════════════════════════════════════════
curses.ACS_ULCORNER                  # Upper left corner
curses.ACS_LLCORNER                  # Lower left corner
curses.ACS_URCORNER                  # Upper right corner
curses.ACS_LRCORNER                  # Lower right corner
curses.ACS_LTEE                      # Left tee
curses.ACS_RTEE                      # Right tee
curses.ACS_BTEE                      # Bottom tee
curses.ACS_TTEE                      # Top tee
curses.ACS_HLINE                     # Horizontal line
curses.ACS_VLINE                     # Vertical line
curses.ACS_PLUS                      # Plus sign (crossover)
curses.ACS_BLOCK                     # Solid block
curses.ACS_DIAMOND                   # Diamond
curses.ACS_CKBOARD                   # Checker board (stipple)
curses.ACS_DEGREE                    # Degree symbol
curses.ACS_PLMINUS                   # Plus/minus sign
curses.ACS_BULLET                    # Bullet
curses.ACS_LARROW                    # Left arrow
curses.ACS_RARROW                    # Right arrow
curses.ACS_DARROW                    # Down arrow
curses.ACS_UARROW                    # Up arrow
curses.ACS_BOARD                     # Board of squares
curses.ACS_LANTERN                   # Lantern symbol
curses.ACS_S1                        # Scan line 1
curses.ACS_S9                        # Scan line 9
curses.ACS_LEQUAL                    # Less than or equal
curses.ACS_GEQUAL                    # Greater than or equal
curses.ACS_PI                        # Pi symbol
curses.ACS_NEQUAL                    # Not equal
curses.ACS_STERLING                  # Pound sterling symbol
# ... (40+ ACS constants for box drawing)

# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS - MOUSE BUTTONS
# ═══════════════════════════════════════════════════════════════════════════
curses.BUTTONn_PRESSED               # Button n pressed (n=1-5)
curses.BUTTONn_RELEASED              # Button n released
curses.BUTTONn_CLICKED               # Button n clicked
curses.BUTTONn_DOUBLE_CLICKED        # Button n double-clicked
curses.BUTTONn_TRIPLE_CLICKED        # Button n triple-clicked
curses.BUTTON_SHIFT                  # Shift held during button event
curses.BUTTON_CTRL                   # Ctrl held during button event
curses.BUTTON_ALT                    # Alt held during button event

# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS - RETURN VALUES
# ═══════════════════════════════════════════════════════════════════════════
curses.OK                            # Success return value
curses.ERR                           # Error return value

# ═══════════════════════════════════════════════════════════════════════════
# VERSION INFO
# ═══════════════════════════════════════════════════════════════════════════
curses.version                       # Curses module version (bytes)
curses.ncurses_version               # Ncurses version tuple (major, minor, patch)
```

---

## COMMON CURSES PATTERNS & EXAMPLES

### Basic Curses Application Template
```python
import curses

def main(stdscr):
    # Clear screen
    stdscr.clear()
    
    # Get dimensions
    height, width = stdscr.getmaxyx()
    
    # Display centered text
    message = "Hello, Curses!"
    x = width // 2 - len(message) // 2
    y = height // 2
    stdscr.addstr(y, x, message, curses.A_BOLD)
    
    # Refresh screen
    stdscr.refresh()
    
    # Wait for keypress
    stdscr.getch()

# Safe initialization and cleanup
curses.wrapper(main)
```

### Menu System
```python
import curses

def print_menu(stdscr, selected_idx, menu_items):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    
    for idx, item in enumerate(menu_items):
        x = w // 2 - len(item) // 2
        y = h // 2 - len(menu_items) // 2 + idx
        
        if idx == selected_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, item)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, item)
    
    stdscr.refresh()

def main(stdscr):
    # Initialize colors
    curses.curs_set(0)  # Hide cursor
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    
    menu_items = ["Option 1", "Option 2", "Option 3", "Exit"]
    current_idx = 0
    
    while True:
        print_menu(stdscr, current_idx, menu_items)
        key = stdscr.getch()
        
        if key == curses.KEY_UP and current_idx > 0:
            current_idx -= 1
        elif key == curses.KEY_DOWN and current_idx < len(menu_items) - 1:
            current_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_idx == len(menu_items) - 1:
                break
            else:
                stdscr.clear()
                stdscr.addstr(0, 0, f"You selected: {menu_items[current_idx]}")
                stdscr.refresh()
                stdscr.getch()

curses.wrapper(main)
```

### Windowed Application with Borders
```python
import curses

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    
    # Create windows
    h, w = stdscr.getmaxyx()
    header = curses.newwin(3, w, 0, 0)
    content = curses.newwin(h-6, w, 3, 0)
    footer = curses.newwin(3, w, h-3, 0)
    
    # Draw borders
    header.box()
    content.box()
    footer.box()
    
    # Add content
    header.addstr(1, 2, "My Application", curses.A_BOLD)
    content.addstr(1, 2, "Main content area")
    footer.addstr(1, 2, "Press 'q' to quit")
    
    # Refresh all windows
    header.refresh()
    content.refresh()
    footer.refresh()
    
    # Main loop
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

curses.wrapper(main)
```

### Color Usage
```python
import curses

def main(stdscr):
    # Start color support
    curses.start_color()
    
    # Define color pairs (pair_number, fg, bg)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    # Display colored text
    stdscr.addstr(0, 0, "Red text", curses.color_pair(1))
    stdscr.addstr(1, 0, "Green text", curses.color_pair(2))
    stdscr.addstr(2, 0, "Yellow text", curses.color_pair(3))
    stdscr.addstr(3, 0, "Blue text", curses.color_pair(4))
    
    # Combine with attributes
    stdscr.addstr(5, 0, "Bold Red", curses.color_pair(1) | curses.A_BOLD)
    stdscr.addstr(6, 0, "Underline Green", curses.color_pair(2) | curses.A_UNDERLINE)
    
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
```

### Text Input with Textbox
```python
import curses
from curses import textpad

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Enter your name:")
    stdscr.refresh()
    
    # Create input window
    input_win = curses.newwin(1, 30, 2, 0)
    input_win.box()
    
    # Create textbox for editing
    textbox = textpad.Textbox(input_win)
    
    # Draw rectangle around input
    textpad.rectangle(stdscr, 1, 0, 3, 31)
    stdscr.refresh()
    
    # Edit and get result
    textbox.edit()
    result = textbox.gather().strip()
    
    stdscr.addstr(5, 0, f"Hello, {result}!")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
```

### Mouse Handling
```python
import curses

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    
    # Enable mouse events
    curses.mousemask(curses.ALL_MOUSE_EVENTS)
    
    stdscr.addstr(0, 0, "Click anywhere (press 'q' to quit)")
    stdscr.refresh()
    
    while True:
        key = stdscr.getch()
        
        if key == ord('q'):
            break
        elif key == curses.KEY_MOUSE:
            _, x, y, z, bstate = curses.getmouse()
            
            if bstate & curses.BUTTON1_CLICKED:
                stdscr.addstr(2, 0, f"Left click at ({x}, {y})   ")
            elif bstate & curses.BUTTON3_CLICKED:
                stdscr.addstr(3, 0, f"Right click at ({x}, {y})  ")
            
            stdscr.refresh()

curses.wrapper(main)
```

### Pad (Large Virtual Window)
```python
import curses

def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    
    # Create large pad (100x100)
    pad = curses.newpad(100, 100)
    
    # Fill pad with content
    for y in range(100):
        for x in range(100):
            pad.addstr(y, x, str((y * 100 + x) % 10))
    
    # Display portion of pad
    h, w = stdscr.getmaxyx()
    pad_y, pad_x = 0, 0
    
    stdscr.addstr(0, 0, "Arrow keys to scroll, 'q' to quit")
    stdscr.refresh()
    
    while True:
        # Refresh pad (show portion)
        pad.refresh(pad_y, pad_x, 2, 0, h-1, w-1)
        
        key = stdscr.getch()
        
        if key == ord('q'):
            break
        elif key == curses.KEY_UP and pad_y > 0:
            pad_y -= 1
        elif key == curses.KEY_DOWN and pad_y < 100 - h + 2:
            pad_y += 1
        elif key == curses.KEY_LEFT and pad_x > 0:
            pad_x -= 1
        elif key == curses.KEY_RIGHT and pad_x < 100 - w:
            pad_x += 1

curses.wrapper(main)
```

### Progress Bar
```python
import curses
import time

def draw_progress(win, progress, width=40):
    win.clear()
    win.box()
    
    filled = int(width * progress)
    bar = "█" * filled + "░" * (width - filled)
    percent = int(progress * 100)
    
    h, w = win.getmaxyx()
    win.addstr(h//2, 2, bar)
    win.addstr(h//2 + 1, w//2 - 3, f"{percent}%")
    win.refresh()

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    
    h, w = stdscr.getmaxyx()
    progress_win = curses.newwin(5, 46, h//2 - 2, w//2 - 23)
    
    for i in range(101):
        draw_progress(progress_win, i / 100)
        time.sleep(0.05)
    
    stdscr.addstr(h-2, w//2 - 10, "Press any key to exit")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
```

---

## IMPORTANT CONCEPTS

### Screen Coordinates
- Origin (0,0) is top-left corner
- Y-axis goes down, X-axis goes right
- Format: `(y, x)` not `(x, y)`

### Window vs Screen
- **stdscr**: Main screen window (full terminal)
- **Window**: Rectangular area that can overlap
- **Pad**: Large virtual window (scrollable viewport)
- **Subwindow**: Shares memory with parent window

### Refresh Strategy
- Use `noutrefresh()` + `doupdate()` for multiple windows (faster)
- Use `refresh()` for single window updates
- Changes not visible until refresh called

### Input Modes
- **Cooked**: Line buffering (default terminal behavior)
- **Cbreak**: Character-by-character, special chars work
- **Raw**: Character-by-character, no special chars
- **Echo/Noecho**: Control input visibility

### Color Pairs
- Must call `start_color()` first
- Pairs numbered 1-255 (pair 0 is special)
- Combine with `|` operator: `color_pair(1) | A_BOLD`

### Attributes
- Can be combined with OR operator: `A_BOLD | A_UNDERLINE`
- Applied to text display (not stored in window)
- Background attributes affect all writes

### Error Handling
- Curses raises `curses.error` exception
- Writing outside window boundaries raises error
- Always use `curses.wrapper()` for safe cleanup

---

## TEXTBOX EDIT KEYS

```
Control-A    Move to beginning of line
Control-B    Cursor left
Control-D    Delete character under cursor
Control-E    Move to end of line
Control-F    Cursor right
Control-G    Terminate (return contents)
Control-H    Delete character backward (backspace)
Control-J    Terminate if 1 line, else newline
Control-K    Delete to end of line
Control-L    Refresh screen
Control-N    Cursor down
Control-O    Insert blank line
Control-P    Cursor up

Arrow keys work as expected (if keypad enabled)
```

---

## TERMINAL REQUIREMENTS

- **Unix/Linux/BSD**: ncurses library required
- **Windows**: windows-curses package (pip install windows-curses)
- **Not supported**: Android, iOS, WASM platforms
- **Terminal**: Must support character-cell display

---

## BEST PRACTICES

1. **Always use `curses.wrapper()`** - Ensures cleanup on exit
2. **Call `stdscr.keypad(True)`** - Enable arrow keys and function keys
3. **Use `curses.curs_set(0)`** - Hide cursor for cleaner UI
4. **Check `has_colors()`** before using color
5. **Use `noutrefresh()` + `doupdate()`** for multiple windows
6. **Handle `curses.error`** exceptions appropriately
7. **Test window bounds** before writing
8. **Use constants** instead of magic numbers (KEY_UP vs 259)
9. **Save/restore** terminal state when temporarily leaving curses
10. **Clear screen** before first draw to avoid artifacts

---

## RELATED MODULES

```python
curses              # Main module
curses.ascii        # ASCII character utilities
curses.panel        # Panel stack extension (depth management)
curses.textpad      # Text editing widget
```

---

## EXTERNAL RESOURCES

- **Python Curses HOWTO**: https://docs.python.org/3/howto/curses.html
- **Ncurses Programming Guide**: https://tldp.org/HOWTO/NCURSES-Programming-HOWTO/
- **Curses Man Pages**: https://man7.org/linux/man-pages/man3/ncurses.3x.html

---

**Version**: Python 3.11+ | ncurses 6.1+  
**Last Updated**: December 2025  
**Platform**: Unix/Linux/BSD (Windows with windows-curses)
