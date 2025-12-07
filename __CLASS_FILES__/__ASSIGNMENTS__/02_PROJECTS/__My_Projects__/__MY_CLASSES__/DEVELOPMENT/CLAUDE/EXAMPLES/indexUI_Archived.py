# AUTHORED BY CLAUDE CODE 3.5 SONNET

class UICanvas:
    """Fixed-size canvas for line-based UI construction"""
    
    def __init__(self, width, height, fill_char=' '):
        self.width = width
        self.height = height
        self.lines = [fill_char * width for _ in range(height)]
    
    def __setitem__(self, line_num, text):
        """Replace line by index (0-based)"""
        if 0 <= line_num < self.height:
            # Truncate or pad to width
            self.lines[line_num] = text[:self.width].ljust(self.width)
        else:
            raise IndexError(f"Line {line_num} out of range (0-{self.height-1})")
    
    def __getitem__(self, line_num):
        """Get line by index"""
        return self.lines[line_num]
    
    def set_region(self, start_line, text_block):
        """Set multiple lines from a block of text"""
        for i, line in enumerate(text_block.split('\n')):
            if start_line + i < self.height:
                self[start_line + i] = line
    
    def write_at(self, line, col, text):
        """Write text at specific position"""
        if 0 <= line < self.height:
            current = list(self.lines[line])
            for i, char in enumerate(text):
                if col + i < self.width:
                    current[col + i] = char
            self.lines[line] = ''.join(current)
    
    def render(self):
        """Get final string"""
        return '\n'.join(self.lines)
    
    def clear_line(self, line_num, fill_char=' '):
        """Clear specific line"""
        self[line_num] = fill_char * self.width
    
    def __str__(self):
        return self.render()


# NOW YOU CAN DO WHAT YOU WANT!
canvas = UICanvas(width=50, height=20)

# Replace by line index - easy!
canvas[0] = "═" * 50
canvas[1] = "Header Text".center(50)
canvas[2] = "═" * 50
canvas[5] = "  • Item 1"
canvas[6] = "  • Item 2"
canvas[7] = "  • Item 3"
canvas[10] = "Status: Ready".center(50)
canvas[19] = "[OK]  [Cancel]".center(50)

print(canvas)

# Update specific position
canvas.write_at(line=5, col=10, text="UPDATED")

# Set multiple lines at once
canvas.set_region(15, """
Footer Line 1
Footer Line 2
Footer Line 3
""".strip())

print(canvas)
