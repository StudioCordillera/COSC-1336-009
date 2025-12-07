"""
ASCII Standardized Config Module
Standardized ASCII character sets and ANSI escape sequences for cross-platform CLI applications
"""


# ═══════════════════════════════════════════════════════════════════════════
# ASCII CHARACTER SETS
# ═══════════════════════════════════════════════════════════════════════════

class ASCIIChars:
    """Standard ASCII characters for box drawing and UI elements"""
    
    # Box Drawing - Simple (High compatibility)
    BOX_H = '-'
    BOX_V = '|'
    BOX_TL = '+'
    BOX_TR = '+'
    BOX_BL = '+'
    BOX_BR = '+'
    BOX_CROSS = '+'
    BOX_T_DOWN = '+'
    BOX_T_UP = '+'
    BOX_T_RIGHT = '+'
    BOX_T_LEFT = '+'
    
    # Box Drawing - Unicode Single Line (Better visuals)
    BOX_SINGLE_H = '─'
    BOX_SINGLE_V = '│'
    BOX_SINGLE_TL = '┌'
    BOX_SINGLE_TR = '┐'
    BOX_SINGLE_BL = '└'
    BOX_SINGLE_BR = '┘'
    BOX_SINGLE_CROSS = '┼'
    BOX_SINGLE_T_DOWN = '┬'
    BOX_SINGLE_T_UP = '┴'
    BOX_SINGLE_T_RIGHT = '├'
    BOX_SINGLE_T_LEFT = '┤'
    
    # Box Drawing - Unicode Double Line
    BOX_DOUBLE_H = '═'
    BOX_DOUBLE_V = '║'
    BOX_DOUBLE_TL = '╔'
    BOX_DOUBLE_TR = '╗'
    BOX_DOUBLE_BL = '╚'
    BOX_DOUBLE_BR = '╝'
    BOX_DOUBLE_CROSS = '╬'
    BOX_DOUBLE_T_DOWN = '╦'
    BOX_DOUBLE_T_UP = '╩'
    BOX_DOUBLE_T_RIGHT = '╠'
    BOX_DOUBLE_T_LEFT = '╣'
    
    # Block Elements
    BLOCK_FULL = '█'
    BLOCK_DARK = '▓'
    BLOCK_MEDIUM = '▒'
    BLOCK_LIGHT = '░'
    BLOCK_TOP = '▀'
    BLOCK_BOTTOM = '▄'
    BLOCK_LEFT = '▌'
    BLOCK_RIGHT = '▐'
    
    # Arrows & Pointers
    ARROW_UP = '↑'
    ARROW_DOWN = '↓'
    ARROW_LEFT = '←'
    ARROW_RIGHT = '→'
    POINTER_RIGHT = '▶'
    POINTER_LEFT = '◀'
    POINTER_UP = '▲'
    POINTER_DOWN = '▼'
    
    # Shapes
    CIRCLE_FILLED = '●'
    CIRCLE_EMPTY = '○'
    SQUARE_FILLED = '■'
    SQUARE_EMPTY = '□'
    DIAMOND_FILLED = '◆'
    DIAMOND_EMPTY = '◇'
    
    # Status & Symbols
    CHECK_MARK = '✓'
    CROSS_MARK = '✗'
    BULLET = '•'
    STAR_FILLED = '★'
    STAR_EMPTY = '☆'
    WARNING = '⚠'
    INFO = 'ℹ'


# ═══════════════════════════════════════════════════════════════════════════
# ANSI ESCAPE SEQUENCES
# ═══════════════════════════════════════════════════════════════════════════

class ANSIEscapes:
    """ANSI escape sequences for terminal control"""
    
    # Core sequences
    ESC = '\033'
    CSI = '\033['
    
    # Reset
    RESET = '\033[0m'
    
    # Text Formatting
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKETHROUGH = '\033[9m'
    
    # Reset individual attributes
    RESET_BOLD = '\033[22m'
    RESET_ITALIC = '\033[23m'
    RESET_UNDERLINE = '\033[24m'
    RESET_BLINK = '\033[25m'
    RESET_REVERSE = '\033[27m'
    
    # Foreground Colors (Standard)
    FG_BLACK = '\033[30m'
    FG_RED = '\033[31m'
    FG_GREEN = '\033[32m'
    FG_YELLOW = '\033[33m'
    FG_BLUE = '\033[34m'
    FG_MAGENTA = '\033[35m'
    FG_CYAN = '\033[36m'
    FG_WHITE = '\033[37m'
    FG_DEFAULT = '\033[39m'
    
    # Foreground Colors (Bright)
    FG_BRIGHT_BLACK = '\033[90m'
    FG_BRIGHT_RED = '\033[91m'
    FG_BRIGHT_GREEN = '\033[92m'
    FG_BRIGHT_YELLOW = '\033[93m'
    FG_BRIGHT_BLUE = '\033[94m'
    FG_BRIGHT_MAGENTA = '\033[95m'
    FG_BRIGHT_CYAN = '\033[96m'
    FG_BRIGHT_WHITE = '\033[97m'
    
    # Background Colors (Standard)
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    BG_DEFAULT = '\033[49m'
    
    # Background Colors (Bright)
    BG_BRIGHT_BLACK = '\033[100m'
    BG_BRIGHT_RED = '\033[101m'
    BG_BRIGHT_GREEN = '\033[102m'
    BG_BRIGHT_YELLOW = '\033[103m'
    BG_BRIGHT_BLUE = '\033[104m'
    BG_BRIGHT_MAGENTA = '\033[105m'
    BG_BRIGHT_CYAN = '\033[106m'
    BG_BRIGHT_WHITE = '\033[107m'
    
    # Cursor Control
    CURSOR_HIDE = '\033[?25l'
    CURSOR_SHOW = '\033[?25h'
    CURSOR_SAVE = '\033[s'
    CURSOR_RESTORE = '\033[u'
    CURSOR_HOME = '\033[H'
    
    # Screen Control
    CLEAR_SCREEN = '\033[2J'
    CLEAR_LINE = '\033[2K'
    CLEAR_TO_END = '\033[0J'
    CLEAR_TO_START = '\033[1J'
    
    @staticmethod
    def cursor_pos(row: int, col: int) -> str:
        """Move cursor to position (1-based)"""
        return f'\033[{row};{col}H'
    
    @staticmethod
    def cursor_up(n: int = 1) -> str:
        """Move cursor up n lines"""
        return f'\033[{n}A'
    
    @staticmethod
    def cursor_down(n: int = 1) -> str:
        """Move cursor down n lines"""
        return f'\033[{n}B'
    
    @staticmethod
    def cursor_forward(n: int = 1) -> str:
        """Move cursor forward n columns"""
        return f'\033[{n}C'
    
    @staticmethod
    def cursor_back(n: int = 1) -> str:
        """Move cursor back n columns"""
        return f'\033[{n}D'
    
    @staticmethod
    def fg_256(color: int) -> str:
        """Set foreground color using 256-color palette (0-255)"""
        return f'\033[38;5;{color}m'
    
    @staticmethod
    def bg_256(color: int) -> str:
        """Set background color using 256-color palette (0-255)"""
        return f'\033[48;5;{color}m'
    
    @staticmethod
    def fg_rgb(r: int, g: int, b: int) -> str:
        """Set foreground color using RGB (0-255 each)"""
        return f'\033[38;2;{r};{g};{b}m'
    
    @staticmethod
    def bg_rgb(r: int, g: int, b: int) -> str:
        """Set background color using RGB (0-255 each)"""
        return f'\033[48;2;{r};{g};{b}m'


# ═══════════════════════════════════════════════════════════════════════════
# THEME CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

class ThemeConfig:
    """Standardized color theme configuration"""
    
    def __init__(self, name: str = "default"):
        self.name = name
        self._load_theme(name)
    
    def _load_theme(self, name: str):
        """Load theme colors"""
        if name == "dark":
            self._load_dark_theme()
        elif name == "light":
            self._load_light_theme()
        else:
            self._load_default_theme()
    
    def _load_default_theme(self):
        """Default theme colors"""
        self.primary_bg = ANSIEscapes.BG_BLUE
        self.primary_fg = ANSIEscapes.FG_WHITE
        self.secondary_bg = ANSIEscapes.BG_CYAN
        self.secondary_fg = ANSIEscapes.FG_BLACK
        self.accent_bg = ANSIEscapes.BG_YELLOW
        self.accent_fg = ANSIEscapes.FG_BLACK
        self.text_primary = ANSIEscapes.FG_WHITE
        self.text_secondary = ANSIEscapes.FG_BRIGHT_BLACK
        self.border = ANSIEscapes.FG_CYAN
        self.success = ANSIEscapes.FG_GREEN
        self.warning = ANSIEscapes.FG_YELLOW
        self.error = ANSIEscapes.FG_RED
    
    def _load_dark_theme(self):
        """Dark theme with deep backgrounds"""
        self.primary_bg = ANSIEscapes.bg_rgb(28, 28, 34)
        self.primary_fg = ANSIEscapes.fg_rgb(220, 220, 230)
        self.secondary_bg = ANSIEscapes.bg_rgb(35, 35, 42)
        self.secondary_fg = ANSIEscapes.fg_rgb(200, 200, 210)
        self.accent_bg = ANSIEscapes.bg_rgb(40, 80, 140)
        self.accent_fg = ANSIEscapes.fg_rgb(100, 180, 255)
        self.text_primary = ANSIEscapes.fg_rgb(220, 220, 230)
        self.text_secondary = ANSIEscapes.fg_rgb(160, 160, 175)
        self.border = ANSIEscapes.fg_rgb(60, 60, 75)
        self.success = ANSIEscapes.fg_rgb(100, 200, 130)
        self.warning = ANSIEscapes.fg_rgb(220, 180, 100)
        self.error = ANSIEscapes.fg_rgb(220, 100, 100)
    
    def _load_light_theme(self):
        """Light theme with bright backgrounds"""
        self.primary_bg = ANSIEscapes.BG_WHITE
        self.primary_fg = ANSIEscapes.FG_BLACK
        self.secondary_bg = ANSIEscapes.bg_rgb(240, 240, 245)
        self.secondary_fg = ANSIEscapes.FG_BLACK
        self.accent_bg = ANSIEscapes.BG_BLUE
        self.accent_fg = ANSIEscapes.FG_WHITE
        self.text_primary = ANSIEscapes.FG_BLACK
        self.text_secondary = ANSIEscapes.fg_rgb(80, 80, 80)
        self.border = ANSIEscapes.fg_rgb(200, 200, 200)
        self.success = ANSIEscapes.fg_rgb(0, 150, 0)
        self.warning = ANSIEscapes.fg_rgb(200, 100, 0)
        self.error = ANSIEscapes.fg_rgb(200, 0, 0)


# ═══════════════════════════════════════════════════════════════════════════
# UI ELEMENT CONFIG
# ═══════════════════════════════════════════════════════════════════════════

class UIElementConfig:
    """Standardized UI element styling configuration"""
    
    def __init__(self, theme: ThemeConfig = None, use_unicode: bool = True):
        self.theme = theme or ThemeConfig()
        self.use_unicode = use_unicode
        self.chars = ASCIIChars()
        self.ansi = ANSIEscapes()
        
    def get_box_chars(self, style: str = "single") -> dict:
        """
        Get box drawing characters based on style
        
        Args:
            style: 'simple', 'single', or 'double'
        
        Returns:
            Dictionary with box character keys
        """
        if not self.use_unicode or style == "simple":
            return {
                'h': self.chars.BOX_H,
                'v': self.chars.BOX_V,
                'tl': self.chars.BOX_TL,
                'tr': self.chars.BOX_TR,
                'bl': self.chars.BOX_BL,
                'br': self.chars.BOX_BR,
                'cross': self.chars.BOX_CROSS,
                't_down': self.chars.BOX_T_DOWN,
                't_up': self.chars.BOX_T_UP,
                't_right': self.chars.BOX_T_RIGHT,
                't_left': self.chars.BOX_T_LEFT,
            }
        elif style == "double":
            return {
                'h': self.chars.BOX_DOUBLE_H,
                'v': self.chars.BOX_DOUBLE_V,
                'tl': self.chars.BOX_DOUBLE_TL,
                'tr': self.chars.BOX_DOUBLE_TR,
                'bl': self.chars.BOX_DOUBLE_BL,
                'br': self.chars.BOX_DOUBLE_BR,
                'cross': self.chars.BOX_DOUBLE_CROSS,
                't_down': self.chars.BOX_DOUBLE_T_DOWN,
                't_up': self.chars.BOX_DOUBLE_T_UP,
                't_right': self.chars.BOX_DOUBLE_T_RIGHT,
                't_left': self.chars.BOX_DOUBLE_T_LEFT,
            }
        else:  # single
            return {
                'h': self.chars.BOX_SINGLE_H,
                'v': self.chars.BOX_SINGLE_V,
                'tl': self.chars.BOX_SINGLE_TL,
                'tr': self.chars.BOX_SINGLE_TR,
                'bl': self.chars.BOX_SINGLE_BL,
                'br': self.chars.BOX_SINGLE_BR,
                'cross': self.chars.BOX_SINGLE_CROSS,
                't_down': self.chars.BOX_SINGLE_T_DOWN,
                't_up': self.chars.BOX_SINGLE_T_UP,
                't_right': self.chars.BOX_SINGLE_T_RIGHT,
                't_left': self.chars.BOX_SINGLE_T_LEFT,
            }
    
    def draw_box(self, x: int, y: int, width: int, height: int, 
                 style: str = "single", title: str = None) -> str:
        """
        Generate box drawing commands
        
        Returns:
            String with ANSI sequences to draw box
        """
        box = self.get_box_chars(style)
        output = []
        
        # Top line
        top_line = box['tl'] + box['h'] * (width - 2) + box['tr']
        if title:
            title_start = 2
            title_len = min(len(title), width - 4)
            top_line = (box['tl'] + box['h'] + 
                       f" {title[:title_len]} " + 
                       box['h'] * (width - title_len - 5) + 
                       box['tr'])
        
        output.append(self.ansi.cursor_pos(y, x) + 
                     self.theme.border + top_line + self.ansi.RESET)
        
        # Middle lines
        for i in range(1, height - 1):
            line = box['v'] + ' ' * (width - 2) + box['v']
            output.append(self.ansi.cursor_pos(y + i, x) + 
                         self.theme.border + line + self.ansi.RESET)
        
        # Bottom line
        bottom_line = box['bl'] + box['h'] * (width - 2) + box['br']
        output.append(self.ansi.cursor_pos(y + height - 1, x) + 
                     self.theme.border + bottom_line + self.ansi.RESET)
        
        return ''.join(output)
    
    def style_text(self, text: str, style: str = "normal") -> str:
        """
        Apply styling to text
        
        Args:
            text: Text to style
            style: Style name ('normal', 'bold', 'dim', 'highlight', 'success', 'warning', 'error')
        
        Returns:
            Styled text with ANSI codes
        """
        if style == "bold":
            return f"{self.ansi.BOLD}{text}{self.ansi.RESET}"
        elif style == "dim":
            return f"{self.ansi.DIM}{text}{self.ansi.RESET}"
        elif style == "highlight":
            return f"{self.theme.accent_bg}{self.theme.accent_fg}{text}{self.ansi.RESET}"
        elif style == "success":
            return f"{self.theme.success}{text}{self.ansi.RESET}"
        elif style == "warning":
            return f"{self.theme.warning}{text}{self.ansi.RESET}"
        elif style == "error":
            return f"{self.theme.error}{text}{self.ansi.RESET}"
        else:
            return f"{self.theme.text_primary}{text}{self.ansi.RESET}"


# ═══════════════════════════════════════════════════════════════════════════
# CONFIGURATION LOADER
# ═══════════════════════════════════════════════════════════════════════════

class ASCIIConfigLoader:
    """Load and manage ASCII/ANSI configurations"""
    
    def __init__(self, theme_name: str = "default", use_unicode: bool = True):
        self.theme = ThemeConfig(theme_name)
        self.ui_config = UIElementConfig(self.theme, use_unicode)
        self.chars = ASCIIChars()
        self.ansi = ANSIEscapes()
    
    def get_theme(self) -> ThemeConfig:
        """Get current theme configuration"""
        return self.theme
    
    def get_ui_config(self) -> UIElementConfig:
        """Get UI element configuration"""
        return self.ui_config
    
    def set_theme(self, theme_name: str):
        """Change theme"""
        self.theme = ThemeConfig(theme_name)
        self.ui_config.theme = self.theme
    
    def enable_unicode(self, enabled: bool = True):
        """Enable or disable Unicode characters"""
        self.ui_config.use_unicode = enabled
