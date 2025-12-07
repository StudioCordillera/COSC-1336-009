# TKINTER_MENU_REFERENCE

## Core Definition
**Tkinter** is Python's standard GUI (Graphical User Interface) library providing a Python interface to the Tcl/Tk GUI toolkit. It enables creation of windows, widgets, menus, dialogs, and event-driven applications with a rich set of UI components.

**Tags**: #tkinter #gui #menu #widgets #ui #tcl-tk #interface #events

---

## COMPLETE TKINTER MENU & GUI QUICK REFERENCE

### CORE CLASSES & INITIALIZATION

```python
# ═══════════════════════════════════════════════════════════════════════════
# MAIN WINDOW & APPLICATION SETUP
# ═══════════════════════════════════════════════════════════════════════════
tkinter.Tk()                          # None | Create root window | Returns Tk instance (main window)
tkinter.Tcl()                         # None | Create Tcl interpreter only | Returns Tcl instance (no GUI)
root.mainloop()                       # Tk instance | Start event loop | Blocks until window closed
root.quit()                           # Tk instance | Exit mainloop | Returns control to program
root.destroy()                        # Tk instance | Destroy window & widgets | Closes application
root.title(string)                    # Tk instance | Set window title | Returns None
root.geometry("WxH+X+Y")              # Tk instance | Set size & position | Returns None
root.resizable(width, height)         # Tk instance | Enable/disable resize | Returns None
root.minsize(width, height)           # Tk instance | Set minimum size | Returns None
root.maxsize(width, height)           # Tk instance | Set maximum size | Returns None
root.iconbitmap(path)                 # Tk instance | Set window icon | Returns None
root.attributes('-alpha', value)      # Tk instance | Set transparency (0.0-1.0) | Returns None
root.withdraw()                       # Tk instance | Hide window | Returns None
root.deiconify()                      # Tk instance | Show hidden window | Returns None
root.state('zoomed')                  # Tk instance | Maximize window | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# MENU WIDGET - PRIMARY FOCUS
# ═══════════════════════════════════════════════════════════════════════════
tkinter.Menu(parent)                  # Widget | Create menu | Returns Menu instance
Menu(parent, tearoff=0)               # Widget | Create menu without tearoff | Returns Menu instance
Menu(parent, bg='color')              # Widget | Create menu with background | Returns Menu instance
Menu(parent, font=('family', size))   # Widget | Create menu with font | Returns Menu instance

# Menu Item Addition
menu.add_command(label, command)      # Menu | Add clickable item | Returns None
menu.add_separator()                  # Menu | Add divider line | Returns None
menu.add_checkbutton(label, variable) # Menu | Add checkbox item | Returns None
menu.add_radiobutton(label, variable) # Menu | Add radio button item | Returns None
menu.add_cascade(label, menu)         # Menu | Add submenu | Returns None

# Menu Configuration
menu.entryconfig(index, option=value) # Menu | Configure menu item | Returns None
menu.delete(index)                    # Menu | Delete menu item | Returns None
menu.delete(start, end)               # Menu | Delete range of items | Returns None
menu.insert_command(index, label, command) # Menu | Insert item at position | Returns None
menu.insert_separator(index)          # Menu | Insert separator at position | Returns None
menu.post(x, y)                       # Menu | Display menu at coordinates | Returns None
menu.unpost()                         # Menu | Hide menu | Returns None
menu.invoke(index)                    # Menu | Execute menu item command | Returns result

# Menu Attachment
root.config(menu=menubar)             # Tk | Attach menu to window | Returns None
widget.bind('<Button-3>', show_menu)  # Widget | Bind context menu to right-click | Returns None

# Menu Index Types
menu.entryconfig(0, ...)              # Integer index (0-based)
menu.entryconfig('active', ...)       # Currently highlighted item
menu.entryconfig('last', ...)         # Last menu item
menu.entryconfig('@100', ...)         # Item at pixel coordinate
menu.entryconfig('none', ...)         # No menu entry

# ═══════════════════════════════════════════════════════════════════════════
# WIDGET CREATION - CLASSIC WIDGETS
# ═══════════════════════════════════════════════════════════════════════════
tkinter.Label(parent, text)           # Parent | Create text label | Returns Label widget
tkinter.Button(parent, text, command) # Parent | Create button | Returns Button widget
tkinter.Entry(parent)                 # Parent | Create text input | Returns Entry widget
tkinter.Text(parent)                  # Parent | Create multiline text | Returns Text widget
tkinter.Frame(parent)                 # Parent | Create container | Returns Frame widget
tkinter.Canvas(parent)                # Parent | Create drawing area | Returns Canvas widget
tkinter.Listbox(parent)               # Parent | Create list selector | Returns Listbox widget
tkinter.Scrollbar(parent)             # Parent | Create scrollbar | Returns Scrollbar widget
tkinter.Scale(parent)                 # Parent | Create slider | Returns Scale widget
tkinter.Checkbutton(parent, variable) # Parent | Create checkbox | Returns Checkbutton widget
tkinter.Radiobutton(parent, variable) # Parent | Create radio button | Returns Radiobutton widget
tkinter.Message(parent, text)         # Parent | Create multiline label | Returns Message widget
tkinter.Spinbox(parent)               # Parent | Create number spinner | Returns Spinbox widget
tkinter.LabelFrame(parent, text)      # Parent | Create labeled container | Returns LabelFrame widget
tkinter.PanedWindow(parent)           # Parent | Create resizable panes | Returns PanedWindow widget
tkinter.Toplevel(parent)              # Parent | Create new window | Returns Toplevel widget

# ═══════════════════════════════════════════════════════════════════════════
# THEMED WIDGETS (ttk) - MODERN APPEARANCE
# ═══════════════════════════════════════════════════════════════════════════
from tkinter import ttk
ttk.Label(parent, text)               # Parent | Create themed label | Returns ttk.Label
ttk.Button(parent, text, command)     # Parent | Create themed button | Returns ttk.Button
ttk.Entry(parent)                     # Parent | Create themed entry | Returns ttk.Entry
ttk.Frame(parent)                     # Parent | Create themed frame | Returns ttk.Frame
ttk.Checkbutton(parent, variable)     # Parent | Create themed checkbox | Returns ttk.Checkbutton
ttk.Radiobutton(parent, variable)     # Parent | Create themed radio | Returns ttk.Radiobutton
ttk.Combobox(parent)                  # Parent | Create dropdown list | Returns ttk.Combobox
ttk.Progressbar(parent)               # Parent | Create progress bar | Returns ttk.Progressbar
ttk.Separator(parent)                 # Parent | Create separator line | Returns ttk.Separator
ttk.Notebook(parent)                  # Parent | Create tabbed interface | Returns ttk.Notebook
ttk.Treeview(parent)                  # Parent | Create tree/table view | Returns ttk.Treeview
ttk.Scrollbar(parent)                 # Parent | Create themed scrollbar | Returns ttk.Scrollbar
ttk.Scale(parent)                     # Parent | Create themed slider | Returns ttk.Scale
ttk.Sizegrip(parent)                  # Parent | Create resize grip | Returns ttk.Sizegrip
ttk.LabelFrame(parent, text)          # Parent | Create themed labeled frame | Returns ttk.LabelFrame

# ═══════════════════════════════════════════════════════════════════════════
# GEOMETRY MANAGERS - LAYOUT POSITIONING
# ═══════════════════════════════════════════════════════════════════════════
# Grid Manager (Recommended)
widget.grid()                         # Widget | Place in grid (0,0) | Returns None
widget.grid(row=n, column=m)          # Widget | Place at grid position | Returns None
widget.grid(sticky='nsew')            # Widget | Stretch to fill cell | Returns None
widget.grid(padx=n, pady=m)           # Widget | Add external padding | Returns None
widget.grid(ipadx=n, ipady=m)         # Widget | Add internal padding | Returns None
widget.grid(rowspan=n, columnspan=m)  # Widget | Span multiple cells | Returns None
widget.grid_forget()                  # Widget | Remove from grid | Returns None
widget.grid_remove()                  # Widget | Hide (preserve space) | Returns None
widget.grid_info()                    # Widget | Get grid configuration | Returns dict
parent.grid_rowconfigure(n, weight=1) # Parent | Make row expandable | Returns None
parent.grid_columnconfigure(n, weight=1) # Parent | Make column expandable | Returns None

# Pack Manager (Simple layout)
widget.pack()                         # Widget | Pack with default (top) | Returns None
widget.pack(side='left')              # Widget | Pack to side | Returns None (left/right/top/bottom)
widget.pack(fill='both')              # Widget | Fill available space | Returns None (x/y/both/none)
widget.pack(expand=True)              # Widget | Expand to fill parent | Returns None
widget.pack(padx=n, pady=m)           # Widget | Add external padding | Returns None
widget.pack(ipadx=n, ipady=m)         # Widget | Add internal padding | Returns None
widget.pack(anchor='nw')              # Widget | Anchor position | Returns None
widget.pack_forget()                  # Widget | Remove from pack | Returns None
widget.pack_info()                    # Widget | Get pack configuration | Returns dict

# Place Manager (Absolute positioning)
widget.place(x=n, y=m)                # Widget | Place at coordinates | Returns None
widget.place(relx=0.5, rely=0.5)      # Widget | Place at relative position (0-1) | Returns None
widget.place(anchor='center')         # Widget | Set anchor point | Returns None
widget.place(width=n, height=m)       # Widget | Set absolute size | Returns None
widget.place(relwidth=0.5, relheight=0.5) # Widget | Set relative size | Returns None
widget.place_forget()                 # Widget | Remove from place | Returns None
widget.place_info()                   # Widget | Get place configuration | Returns dict

# ═══════════════════════════════════════════════════════════════════════════
# WIDGET CONFIGURATION & OPTIONS
# ═══════════════════════════════════════════════════════════════════════════
widget['option'] = value              # Widget | Set option via dict | Returns None
widget.config(option=value)           # Widget | Set option via method | Returns None
widget.configure(option=value)        # Widget | Set option (alias) | Returns None
widget.config()                       # Widget | Get all options | Returns dict
widget['option']                      # Widget | Get option value | Returns current value
widget.cget('option')                 # Widget | Get option value | Returns current value
widget.keys()                         # Widget | Get all option names | Returns list of strings

# Common Widget Options
text='string'                         # Text to display
font=('family', size, 'style')        # Font configuration
fg='color' or foreground='color'      # Text color
bg='color' or background='color'      # Background color
width=n, height=m                     # Widget dimensions
relief='style'                        # Border style (flat/raised/sunken/groove/ridge)
borderwidth=n or bd=n                 # Border width in pixels
padx=n, pady=m                        # External padding
state='normal'/'disabled'/'readonly'  # Widget state
cursor='cursor_name'                  # Mouse cursor type
justify='left'/'center'/'right'       # Text alignment
anchor='n'/'s'/'e'/'w'/'ne'/'nw'/'se'/'sw'/'center' # Content anchor point
command=function                      # Callback function (Button, Menu, etc.)
variable=tkvar                        # Associated Tkinter variable
image=photo                           # Image to display
compound='top'/'bottom'/'left'/'right'/'center' # Text+image placement

# ═══════════════════════════════════════════════════════════════════════════
# TKINTER VARIABLES - DATA BINDING
# ═══════════════════════════════════════════════════════════════════════════
tkinter.StringVar()                   # None | Create string variable | Returns StringVar
tkinter.IntVar()                      # None | Create integer variable | Returns IntVar
tkinter.DoubleVar()                   # None | Create float variable | Returns DoubleVar
tkinter.BooleanVar()                  # None | Create boolean variable | Returns BooleanVar

var.get()                             # Variable | Get current value | Returns value
var.set(value)                        # Variable | Set value | Returns None
var.trace('w', callback)              # Variable | Watch for changes | Returns trace id
var.trace_remove('write', trace_id)   # Variable | Remove trace callback | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# EVENT BINDING & HANDLING
# ═══════════════════════════════════════════════════════════════════════════
widget.bind('<event>', callback)      # Widget | Bind event to function | Returns binding id
widget.bind('<event>', callback, '+') # Widget | Add binding (don't replace) | Returns binding id
widget.unbind('<event>')              # Widget | Remove binding | Returns None
widget.bind_all('<event>', callback)  # Widget | Bind to all widgets | Returns binding id
widget.bind_class('class', '<event>', callback) # Widget | Bind to widget class | Returns binding id

# Common Event Patterns
'<Button-1>'                          # Left mouse click
'<Button-2>'                          # Middle mouse click
'<Button-3>'                          # Right mouse click
'<Double-Button-1>'                   # Double left-click
'<Motion>'                            # Mouse movement
'<Enter>'                             # Mouse enters widget
'<Leave>'                             # Mouse leaves widget
'<Key>'                               # Any key press
'<Return>'                            # Enter key
'<Escape>'                            # Escape key
'<space>'                             # Space bar
'<a>'                                 # 'a' key
'<Control-a>'                         # Ctrl+A
'<Alt-a>'                             # Alt+A
'<Shift-a>'                           # Shift+A
'<FocusIn>'                           # Widget gains focus
'<FocusOut>'                          # Widget loses focus
'<Configure>'                         # Widget resized/moved

# Event Object Attributes
event.widget                          # Widget that triggered event
event.x, event.y                      # Mouse coordinates (relative to widget)
event.x_root, event.y_root            # Mouse coordinates (screen absolute)
event.char                            # Character typed
event.keysym                          # Key symbol name
event.keycode                         # Numeric key code
event.num                             # Mouse button number
event.width, event.height             # Widget dimensions (Configure event)
event.type                            # Event type

# ═══════════════════════════════════════════════════════════════════════════
# DIALOG MODULES - PRE-BUILT DIALOGS
# ═══════════════════════════════════════════════════════════════════════════
from tkinter import messagebox
messagebox.showinfo(title, message)   # Strings | Show info dialog | Returns 'ok'
messagebox.showwarning(title, message) # Strings | Show warning dialog | Returns 'ok'
messagebox.showerror(title, message)  # Strings | Show error dialog | Returns 'ok'
messagebox.askquestion(title, message) # Strings | Show yes/no dialog | Returns 'yes'/'no'
messagebox.askokcancel(title, message) # Strings | Show OK/Cancel dialog | Returns True/False
messagebox.askyesno(title, message)   # Strings | Show Yes/No dialog | Returns True/False
messagebox.askretrycancel(title, message) # Strings | Show Retry/Cancel | Returns True/False

from tkinter import filedialog
filedialog.askopenfilename()          # None | Choose file to open | Returns filepath string
filedialog.askopenfilenames()         # None | Choose multiple files | Returns list of paths
filedialog.askopenfile()              # None | Open file for reading | Returns file object
filedialog.asksaveasfilename()        # None | Choose save location | Returns filepath string
filedialog.asksaveasfile()            # None | Open file for writing | Returns file object
filedialog.askdirectory()             # None | Choose directory | Returns directory path

from tkinter import colorchooser
colorchooser.askcolor()               # None | Choose color | Returns (rgb_tuple, hex_string)

from tkinter import simpledialog
simpledialog.askstring(title, prompt) # Strings | Get string input | Returns string or None
simpledialog.askinteger(title, prompt) # Strings | Get integer input | Returns int or None
simpledialog.askfloat(title, prompt)  # Strings | Get float input | Returns float or None

# ═══════════════════════════════════════════════════════════════════════════
# WIDGET-SPECIFIC METHODS - TEXT WIDGET
# ═══════════════════════════════════════════════════════════════════════════
text.insert(index, string)            # Text widget | Insert text | Returns None
text.delete(start, end)               # Text widget | Delete text range | Returns None
text.get(start, end)                  # Text widget | Get text content | Returns string
text.mark_set('mark', index)          # Text widget | Set bookmark | Returns None
text.tag_add(tag, start, end)         # Text widget | Add tag to range | Returns None
text.tag_config(tag, options)         # Text widget | Configure tag style | Returns None
text.see(index)                       # Text widget | Scroll to position | Returns None
text.search(pattern, start, end)      # Text widget | Search text | Returns index or ''

# Text Widget Indexes
'1.0'                                 # Line 1, character 0 (start)
'2.5'                                 # Line 2, character 5
'end'                                 # End of text
'insert'                              # Current cursor position
'sel.first'                           # Start of selection
'sel.last'                            # End of selection
'@x,y'                                # Character at pixel coordinates

# ═══════════════════════════════════════════════════════════════════════════
# WIDGET-SPECIFIC METHODS - CANVAS WIDGET
# ═══════════════════════════════════════════════════════════════════════════
canvas.create_line(x1, y1, x2, y2)    # Canvas | Draw line | Returns item id
canvas.create_rectangle(x1, y1, x2, y2) # Canvas | Draw rectangle | Returns item id
canvas.create_oval(x1, y1, x2, y2)    # Canvas | Draw oval/circle | Returns item id
canvas.create_polygon(coords)         # Canvas | Draw polygon | Returns item id
canvas.create_arc(x1, y1, x2, y2)     # Canvas | Draw arc | Returns item id
canvas.create_text(x, y, text)        # Canvas | Draw text | Returns item id
canvas.create_image(x, y, image)      # Canvas | Draw image | Returns item id
canvas.create_window(x, y, window)    # Canvas | Embed widget | Returns item id
canvas.coords(item_id, coords)        # Canvas | Move/reshape item | Returns None
canvas.itemconfig(item_id, option=val) # Canvas | Configure item | Returns None
canvas.delete(item_id)                # Canvas | Delete item | Returns None
canvas.delete('all')                  # Canvas | Clear canvas | Returns None
canvas.move(item_id, dx, dy)          # Canvas | Move item by offset | Returns None
canvas.tag_bind(item_id, event, callback) # Canvas | Bind event to item | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# WIDGET-SPECIFIC METHODS - LISTBOX WIDGET
# ═══════════════════════════════════════════════════════════════════════════
listbox.insert(index, item)           # Listbox | Add item | Returns None
listbox.delete(index)                 # Listbox | Remove item | Returns None
listbox.get(index)                    # Listbox | Get item text | Returns string
listbox.curselection()                # Listbox | Get selected indices | Returns tuple of ints
listbox.size()                        # Listbox | Get item count | Returns int
listbox.see(index)                    # Listbox | Scroll to item | Returns None
listbox.selection_set(index)          # Listbox | Select item | Returns None
listbox.selection_clear(first, last)  # Listbox | Deselect items | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# WIDGET-SPECIFIC METHODS - ENTRY WIDGET
# ═══════════════════════════════════════════════════════════════════════════
entry.get()                           # Entry | Get text content | Returns string
entry.delete(first, last)             # Entry | Delete text range | Returns None
entry.insert(index, string)           # Entry | Insert text | Returns None
entry.select_range(start, end)        # Entry | Select text range | Returns None
entry.select_clear()                  # Entry | Clear selection | Returns None
entry.icursor(index)                  # Entry | Set cursor position | Returns None
entry.xview(index)                    # Entry | Scroll horizontally | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# WIDGET-SPECIFIC METHODS - COMBOBOX (ttk)
# ═══════════════════════════════════════════════════════════════════════════
combobox['values'] = tuple            # Combobox | Set dropdown items | Returns None
combobox.get()                        # Combobox | Get selected value | Returns string
combobox.set(value)                   # Combobox | Set value | Returns None
combobox.current()                    # Combobox | Get selected index | Returns int
combobox.current(index)               # Combobox | Select by index | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# WIDGET-SPECIFIC METHODS - NOTEBOOK (ttk)
# ═══════════════════════════════════════════════════════════════════════════
notebook.add(child, text='Tab')       # Notebook | Add tab | Returns None
notebook.select(tab_id)               # Notebook | Switch to tab | Returns None
notebook.forget(tab_id)               # Notebook | Remove tab | Returns None
notebook.index('current')             # Notebook | Get current tab index | Returns int
notebook.tab(tab_id, option=value)    # Notebook | Configure tab | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# WIDGET-SPECIFIC METHODS - TREEVIEW (ttk)
# ═══════════════════════════════════════════════════════════════════════════
treeview.insert(parent, index, text)  # Treeview | Add item | Returns item id
treeview.delete(item_id)              # Treeview | Remove item | Returns None
treeview.item(item_id, option=value)  # Treeview | Configure item | Returns dict or None
treeview.selection()                  # Treeview | Get selected items | Returns tuple
treeview.set(item_id, column, value)  # Treeview | Set cell value | Returns None
treeview.get_children(item_id)        # Treeview | Get child items | Returns tuple

# ═══════════════════════════════════════════════════════════════════════════
# WINDOW MANAGER METHODS (wm_* methods)
# ═══════════════════════════════════════════════════════════════════════════
root.wm_title(string)                 # Window | Set title (same as title()) | Returns None
root.wm_geometry(string)              # Window | Set size/position | Returns None
root.wm_minsize(w, h)                 # Window | Set min size | Returns None
root.wm_maxsize(w, h)                 # Window | Set max size | Returns None
root.wm_resizable(w, h)               # Window | Set resizable | Returns None
root.wm_protocol('WM_DELETE_WINDOW', func) # Window | Handle close button | Returns None
root.wm_state('zoomed'/'normal'/'iconic') # Window | Set window state | Returns None
root.wm_attributes('-alpha', value)   # Window | Set attributes | Returns None
root.wm_transient(parent)             # Window | Set as temporary window | Returns None
root.wm_iconbitmap(path)              # Window | Set window icon | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# WIDGET INFO METHODS (winfo_* methods)
# ═══════════════════════════════════════════════════════════════════════════
widget.winfo_width()                  # Widget | Get current width | Returns int pixels
widget.winfo_height()                 # Widget | Get current height | Returns int pixels
widget.winfo_x()                      # Widget | Get x position | Returns int pixels
widget.winfo_y()                      # Widget | Get y position | Returns int pixels
widget.winfo_rootx()                  # Widget | Get screen x position | Returns int pixels
widget.winfo_rooty()                  # Widget | Get screen y position | Returns int pixels
widget.winfo_reqwidth()               # Widget | Get requested width | Returns int pixels
widget.winfo_reqheight()              # Widget | Get requested height | Returns int pixels
widget.winfo_parent()                 # Widget | Get parent pathname | Returns string
widget.winfo_children()               # Widget | Get child widgets | Returns tuple
widget.winfo_exists()                 # Widget | Check if exists | Returns bool
widget.winfo_id()                     # Widget | Get window identifier | Returns int
widget.winfo_name()                   # Widget | Get widget name | Returns string
widget.winfo_class()                  # Widget | Get widget class | Returns string

# ═══════════════════════════════════════════════════════════════════════════
# IMAGE HANDLING
# ═══════════════════════════════════════════════════════════════════════════
tkinter.PhotoImage(file='path.png')   # Filepath | Load PNG/GIF image | Returns PhotoImage
tkinter.PhotoImage(data=base64_data)  # Base64 | Load from data | Returns PhotoImage
tkinter.BitmapImage(file='path.xbm')  # Filepath | Load XBM image | Returns BitmapImage
photo.subsample(x, y)                 # PhotoImage | Scale down image | Returns PhotoImage
photo.zoom(x, y)                      # PhotoImage | Scale up image | Returns PhotoImage
photo.copy()                          # PhotoImage | Duplicate image | Returns PhotoImage
photo.width()                         # PhotoImage | Get width | Returns int
photo.height()                        # PhotoImage | Get height | Returns int

# ═══════════════════════════════════════════════════════════════════════════
# FONT HANDLING
# ═══════════════════════════════════════════════════════════════════════════
from tkinter import font
font.families()                       # None | List available fonts | Returns tuple of strings
font.Font(family, size, weight, slant) # Font params | Create font | Returns Font object
custom_font = font.Font(family='Arial', size=12, weight='bold')
widget.config(font=custom_font)       # Widget | Apply custom font | Returns None

# Font Tuple Format
('Helvetica', 12)                     # Family and size
('Courier', 10, 'bold')               # Family, size, and weight
('Times', 14, 'italic')               # Family, size, and slant
('Arial', 11, 'bold italic')          # Family, size, weight and slant

# ═══════════════════════════════════════════════════════════════════════════
# TIMER & SCHEDULING METHODS
# ═══════════════════════════════════════════════════════════════════════════
widget.after(ms, callback)            # Widget | Schedule function | Returns timer id
widget.after(ms, callback, *args)     # Widget | Schedule with args | Returns timer id
widget.after_cancel(timer_id)         # Widget | Cancel scheduled task | Returns None
widget.after_idle(callback)           # Widget | Run when idle | Returns timer id
widget.update()                       # Widget | Process pending events | Returns None
widget.update_idletasks()             # Widget | Process idle tasks | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# FOCUS MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
widget.focus()                        # Widget | Set keyboard focus | Returns None
widget.focus_set()                    # Widget | Set focus (same) | Returns None
widget.focus_force()                  # Widget | Force focus | Returns None
widget.focus_get()                    # Widget | Get focused widget | Returns widget or None
widget.focus_displayof()              # Widget | Get display focus | Returns widget
widget.focus_lastfor()                # Widget | Get last focus | Returns widget
widget.tk_focusNext()                 # Widget | Get next in tab order | Returns widget
widget.tk_focusPrev()                 # Widget | Get previous in tab order | Returns widget

# ═══════════════════════════════════════════════════════════════════════════
# CLIPBOARD OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════
widget.clipboard_clear()              # Widget | Clear clipboard | Returns None
widget.clipboard_append(string)       # Widget | Add to clipboard | Returns None
widget.clipboard_get()                # Widget | Get clipboard content | Returns string
widget.selection_get()                # Widget | Get selection | Returns string
widget.selection_clear()              # Widget | Clear selection | Returns None
widget.selection_own()                # Widget | Own selection | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# SPECIAL OPTION DATA TYPES & VALUES
# ═══════════════════════════════════════════════════════════════════════════
# Relief Styles
relief='flat'                         # No border
relief='raised'                       # Raised border
relief='sunken'                       # Sunken border
relief='groove'                       # Grooved border
relief='ridge'                        # Ridged border

# Anchor Points (alignment)
anchor='n'                            # North (top center)
anchor='s'                            # South (bottom center)
anchor='e'                            # East (right center)
anchor='w'                            # West (left center)
anchor='ne'                           # Northeast (top right)
anchor='nw'                           # Northwest (top left)
anchor='se'                           # Southeast (bottom right)
anchor='sw'                           # Southwest (bottom left)
anchor='center'                       # Center

# Sticky Values (grid)
sticky='n'                            # Stick to top
sticky='s'                            # Stick to bottom
sticky='e'                            # Stick to right
sticky='w'                            # Stick to left
sticky='ns'                           # Stretch vertically
sticky='ew'                           # Stretch horizontally
sticky='nsew'                         # Fill entire cell

# Cursor Types
cursor='arrow'                        # Standard pointer
cursor='hand2'                        # Pointing hand
cursor='watch'                        # Busy/waiting
cursor='crosshair'                    # Crosshair
cursor='ibeam'                        # Text cursor
cursor='plus'                         # Plus sign
cursor='xterm'                        # X-shaped cursor

# Colors
bg='red', fg='blue'                   # Named colors
bg='#FF0000'                          # Hex RGB (8-bit)
bg='#FFFF00000000'                    # Hex RGB (16-bit)

# ═══════════════════════════════════════════════════════════════════════════
# SCROLLABLE WIDGETS PATTERN
# ═══════════════════════════════════════════════════════════════════════════
# Vertical Scrollbar
scrollbar = Scrollbar(parent, orient='vertical')
widget.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=widget.yview)

# Horizontal Scrollbar
scrollbar = Scrollbar(parent, orient='horizontal')
widget.config(xscrollcommand=scrollbar.set)
scrollbar.config(command=widget.xview)

# ═══════════════════════════════════════════════════════════════════════════
# VALIDATION PATTERNS
# ═══════════════════════════════════════════════════════════════════════════
vcmd = (root.register(validate_func), '%P') # Register validation
entry = Entry(root, validate='key', validatecommand=vcmd)

# Validation Modes
validate='none'                       # No validation
validate='focus'                      # Validate on focus in/out
validate='focusin'                    # Validate on focus in
validate='focusout'                   # Validate on focus out
validate='key'                        # Validate on keystroke
validate='all'                        # Validate on all events

# Validation Substitution Codes
'%d'                                  # Type of action (1=insert, 0=delete, -1=other)
'%i'                                  # Index of char being inserted/deleted
'%P'                                  # Value after edit (proposed value)
'%s'                                  # Value before edit
'%S'                                  # Text being inserted/deleted
'%v'                                  # Validation type
'%V'                                  # Reason for callback
'%W'                                  # Name of widget

# ═══════════════════════════════════════════════════════════════════════════
# STYLE CONFIGURATION (ttk widgets)
# ═══════════════════════════════════════════════════════════════════════════
from tkinter import ttk
style = ttk.Style()
style.theme_use('clam')               # Set theme (clam/alt/default/classic)
style.configure('TButton', background='blue') # Configure widget style
style.map('TButton', background=[('active', 'red')]) # Configure state-based style
style.layout('TButton')               # Get widget layout
style.element_options('Button.label') # Get element options
```

---

## MENU-SPECIFIC PATTERNS & EXAMPLES

### Basic Menu Bar
```python
from tkinter import *

root = Tk()
root.title("Menu Example")

# Create menubar
menubar = Menu(root)
root.config(menu=menubar)

# File menu
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit menu
edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

root.mainloop()
```

### Context Menu (Right-Click)
```python
def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="Copy", command=copy)
context_menu.add_command(label="Paste", command=paste)
context_menu.add_command(label="Delete", command=delete)

widget.bind("<Button-3>", show_context_menu)
```

### Menu with Checkbuttons
```python
view_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=view_menu)

show_toolbar = BooleanVar()
show_statusbar = BooleanVar()

view_menu.add_checkbutton(label="Toolbar", variable=show_toolbar, command=toggle_toolbar)
view_menu.add_checkbutton(label="Status Bar", variable=show_statusbar, command=toggle_statusbar)
```

### Menu with Radiobuttons
```python
options_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Options", menu=options_menu)

theme_var = StringVar()
theme_var.set("light")

options_menu.add_radiobutton(label="Light Theme", variable=theme_var, value="light", command=set_theme)
options_menu.add_radiobutton(label="Dark Theme", variable=theme_var, value="dark", command=set_theme)
```

### Nested Submenus
```python
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)

recent_menu = Menu(file_menu, tearoff=0)
file_menu.add_cascade(label="Recent Files", menu=recent_menu)
recent_menu.add_command(label="Document1.txt", command=open_recent_1)
recent_menu.add_command(label="Document2.txt", command=open_recent_2)
```

### Dynamic Menu Updates
```python
# Add items dynamically
menu.add_command(label="New Item", command=callback)

# Remove items
menu.delete(0)  # Delete first item
menu.delete(2, 4)  # Delete items 2-4

# Modify existing items
menu.entryconfig(0, label="Updated Label", state='disabled')

# Insert items
menu.insert_command(1, label="Inserted", command=callback)
```

---

## COMMON GUI PATTERNS

### Basic Window Template
```python
import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Application")
        self.geometry("800x600")
        self.create_menu()
        self.create_widgets()
    
    def create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.quit)
    
    def create_widgets(self):
        frame = ttk.Frame(self, padding=10)
        frame.grid(row=0, column=0, sticky='nsew')
        
        label = ttk.Label(frame, text="Hello World!")
        label.grid(row=0, column=0)
        
        button = ttk.Button(frame, text="Click Me", command=self.on_click)
        button.grid(row=1, column=0, pady=10)
    
    def on_click(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
```

### Form Input Pattern
```python
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Form Example")

# Create form fields
ttk.Label(root, text="Name:").grid(row=0, column=0, sticky=W, padx=5, pady=5)
name_entry = ttk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(root, text="Email:").grid(row=1, column=0, sticky=W, padx=5, pady=5)
email_entry = ttk.Entry(root, width=30)
email_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(root, text="Country:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
country_combo = ttk.Combobox(root, width=27, values=["USA", "Canada", "UK", "Other"])
country_combo.grid(row=2, column=1, padx=5, pady=5)

def submit():
    print(f"Name: {name_entry.get()}")
    print(f"Email: {email_entry.get()}")
    print(f"Country: {country_combo.get()}")

ttk.Button(root, text="Submit", command=submit).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
```

---

## THREAD-SAFE GUI UPDATES

```python
import threading
from tkinter import *

def long_task():
    # Perform long-running task
    result = perform_calculation()
    # Update GUI from thread
    root.after(0, lambda: update_label(result))

def update_label(text):
    label.config(text=text)

# Run task in separate thread
thread = threading.Thread(target=long_task)
thread.start()
```

---

## IMPORTANT CONCEPTS

### Widget Hierarchy
- All widgets must have a parent (except root window)
- Parent passed as first argument: `Label(parent, text="...")`
- Hierarchy determines widget containment and layout

### Event Loop
- `mainloop()` must be called to display GUI and handle events
- Blocks until window is closed
- All GUI updates must happen in main thread

### Geometry Management
- **Must** call a geometry manager (grid/pack/place) for widget to appear
- Cannot mix grid() and pack() in same parent
- grid() is recommended for most layouts

### Tkinter Variables
- Required for data binding with Entry, Checkbutton, Radiobutton
- Automatically update widget when variable changes
- Use `.get()` and `.set()` methods

### Threading Model
- Tkinter is NOT thread-safe
- Use `widget.after()` to schedule GUI updates from threads
- Long tasks should run in separate threads to avoid freezing UI

---

## RELATED MODULES

```python
tkinter                  # Main module
tkinter.ttk              # Themed widgets
tkinter.messagebox       # Message dialogs
tkinter.filedialog       # File selection dialogs
tkinter.colorchooser     # Color picker dialog
tkinter.simpledialog     # Simple input dialogs
tkinter.font             # Font configuration
tkinter.scrolledtext     # Text widget with scrollbar
tkinter.dnd              # Drag-and-drop (experimental)
```

---

## MENU COMMAND QUICK TIPS

1. **Always set `tearoff=0`** when creating menus to disable the tear-off feature
2. **Use `add_cascade()`** for submenus, `add_command()` for clickable items
3. **Bind context menus** to `<Button-3>` (right-click) event
4. **Use separators** to group related menu items visually
5. **Store menu references** if you need to update them dynamically
6. **Use variables** (StringVar, BooleanVar) with checkbuttons/radiobuttons in menus
7. **Configure menu items** with `entryconfig()` to enable/disable or change labels

---

## EXTERNAL RESOURCES

- **Official Tcl/Tk Documentation**: https://www.tcl.tk/man/tcl8.6/TkCmd/
- **TkDocs Tutorial**: https://tkdocs.com/
- **Tkinter 8.5 Reference**: https://www.tkdocs.com/shipman/
- **Effbot Tkinter Guide**: http://effbot.org/tkinterbook/

---

**Version**: Python 3.11+ | Tkinter 8.6+  
**Last Updated**: December 2025
