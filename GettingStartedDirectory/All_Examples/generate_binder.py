"""
PDF Binder Generator for Python Examples
Creates a comprehensive grayscale binder with TOC, sections, and page numbering
"""

import os
import re
from pathlib import Path
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import black, white, Color
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak, 
                                KeepTogether, Table, TableStyle, Preformatted, XPreformatted,
                                PageTemplate, Frame, NextPageTemplate, BaseDocTemplate, FrameBreak)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas

# Base directory
BASE_DIR = Path(__file__).parent

# Grayscale colors
GRAY_DARK = Color(0.2, 0.2, 0.2)
GRAY_MED = Color(0.4, 0.4, 0.4)
GRAY_LIGHT = Color(0.6, 0.6, 0.6)
GRAY_VLIGHT = Color(0.85, 0.85, 0.85)
GRAY_BG = Color(0.95, 0.95, 0.95)

# Categories in logical order - updated with new folder names
CATEGORIES = [
    ("C1 - Python Basics", "Python Basics", "Foundational concepts including variables, data types, operators, and basic I/O"),
    ("C2 - Python Decisions", "Python Decisions & Conditionals", "Control flow with if/elif/else statements and boolean logic"),
    ("C2 - Python Loops", "Python Loops & Iteration", "For loops, while loops, and iteration patterns"),
    ("C1 - Python Functions", "Python Functions & Modules", "Function definitions, parameters, return values, and modules"),
    ("C5 - Python Strings", "Python Strings & String Methods", "String manipulation, formatting, and string methods"),
    ("C4 - Python Lists", "Python Lists & List Operations", "List creation, manipulation, and common list operations"),
    ("C4 - Python Tuples", "Python Tuples & Tuple Operations", "Tuple basics, immutability, and tuple methods"),
    ("C6 - Python Dictionary", "Python Dictionaries", "Dictionary operations, keys, values, and dictionary methods"),
    ("C6 - Python Set", "Python Sets & Set Operations", "Set creation, operations, and set mathematics"),
    ("C3 - Python Files", "Python File I/O Operations", "Reading from and writing to files"),
    ("C3 - Python Exceptions", "Python Exception Handling", "Try/except blocks and error handling patterns"),
    ("C7-C8 - Python OOP", "Python Object-Oriented Programming", "Classes, objects, inheritance, and OOP principles")
]

class NumberedCanvas(canvas.Canvas):
    """Custom canvas for page numbering and headers/footers"""
    
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []
        
    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()
        
    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_elements(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)
        
    def draw_page_elements(self, page_count):
        """Draw header, footer, and page numbers"""
        self.saveState()
        self.setFont('Helvetica', 8)
        self.setFillColor(GRAY_MED)
        
        # Get page number (starts at 1)
        page_num = self._pageNumber
        
        # Header (skip on cover page)
        if page_num > 1:
            self.drawString(0.75*inch, letter[1] - 0.5*inch, 
                          "Python Programming Examples Collection")
            self.drawRightString(letter[0] - 0.75*inch, letter[1] - 0.5*inch, 
                               f"Page {page_num} of {page_count}")
            # Header line
            self.setStrokeColor(GRAY_LIGHT)
            self.setLineWidth(0.5)
            self.line(0.75*inch, letter[1] - 0.55*inch, 
                     letter[0] - 0.75*inch, letter[1] - 0.55*inch)
        
        # Footer
        if page_num > 1:
            self.drawCentredString(letter[0]/2, 0.5*inch, 
                                  f"COSC 1336 - Programming Fundamentals")
            # Footer line
            self.setStrokeColor(GRAY_LIGHT)
            self.line(0.75*inch, 0.55*inch, letter[0] - 0.75*inch, 0.55*inch)
        
        self.restoreState()

def clean_boilerplate(content):
    """Remove boilerplate comments from code"""
    lines = content.split('\n')
    cleaned_lines = []
    skip_mode = False
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('# Name') or stripped.startswith('# Date') or \
           stripped.startswith('# Program') or stripped.startswith('# Class') or \
           stripped.startswith('# -'):
            skip_mode = True
            continue
        elif stripped.startswith('# Description'):
            skip_mode = True
            continue
        elif skip_mode and (stripped.startswith('#') or stripped == ''):
            continue
        else:
            skip_mode = False
            cleaned_lines.append(line)
    
    while cleaned_lines and not cleaned_lines[0].strip():
        cleaned_lines.pop(0)
    
    return '\n'.join(cleaned_lines)

def generate_title_from_filename(filename):
    """Generate a readable title from filename"""
    name = filename.replace('.py', '').replace('.txt', '')
    name = re.sub(r'^\d+\s+', '', name)
    title = name.replace('_', ' ').replace('-', ' ')
    title = ' '.join(word.capitalize() for word in title.split())
    return title

def create_binder():
    """Create the complete binder PDF"""
    print("=" * 70)
    print("Python Examples Binder Generator")
    print("=" * 70)
    print()
    
    output_file = BASE_DIR / "PDF_Examples" / "Python_Programming_Examples_BINDER.pdf"
    output_file.parent.mkdir(exist_ok=True)
    
    # Create multi-column PDF document
    doc = BaseDocTemplate(
        str(output_file),
        pagesize=letter,
        topMargin=0.6*inch,
        bottomMargin=0.6*inch,
        leftMargin=0.5*inch,
        rightMargin=0.5*inch
    )
    
    # Define frame layout for 2-column pages
    frame_width = (letter[0] - 1.2*inch) / 2  # Split width into 2 columns with gap
    frame_height = letter[1] - 1.4*inch
    
    # Left and right column frames
    frame_left = Frame(
        0.5*inch, 0.7*inch, frame_width, frame_height,
        id='col1', showBoundary=0, leftPadding=0, rightPadding=6
    )
    frame_right = Frame(
        0.5*inch + frame_width + 0.2*inch, 0.7*inch, frame_width, frame_height,
        id='col2', showBoundary=0, leftPadding=6, rightPadding=0
    )
    
    # Single column frame for cover/TOC
    frame_single = Frame(
        0.5*inch, 0.7*inch, letter[0] - 1*inch, frame_height,
        id='single', showBoundary=0
    )
    
    # Define page templates
    doc.addPageTemplates([
        PageTemplate(id='SingleColumn', frames=[frame_single]),
        PageTemplate(id='TwoColumn', frames=[frame_left, frame_right])
    ])
    
    # Styles
    styles = getSampleStyleSheet()
    
    # Cover page style
    cover_title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=GRAY_DARK,
        spaceAfter=8,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    cover_subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=GRAY_MED,
        spaceAfter=8,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    cover_info_style = ParagraphStyle(
        'CoverInfo',
        parent=styles['Normal'],
        fontSize=12,
        textColor=GRAY_MED,
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    # TOC styles
    toc_title_style = ParagraphStyle(
        'TOCTitle',
        parent=styles['Heading1'],
        fontSize=14,
        textColor=GRAY_DARK,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    toc_section_style = ParagraphStyle(
        'TOCSection',
        parent=styles['Normal'],
        fontSize=13,
        textColor=GRAY_DARK,
        spaceAfter=8,
        fontName='Helvetica-Bold',
        leftIndent=0
    )
    
    toc_entry_style = ParagraphStyle(
        'TOCEntry',
        parent=styles['Normal'],
        fontSize=12,
        textColor=GRAY_MED,
        spaceAfter=4,
        leftIndent=20,
        fontName='Helvetica'
    )
    
    # Section styles
    section_title_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading1'],
        fontSize=13,
        textColor=GRAY_DARK,
        spaceAfter=6,
        fontName='Helvetica-Bold'
    )
    
    section_desc_style = ParagraphStyle(
        'SectionDesc',
        parent=styles['Normal'],
        fontSize=12,
        textColor=GRAY_MED,
        spaceAfter=10,
        alignment=TA_JUSTIFY,
        fontName='Helvetica-Oblique',
        leftIndent=0
    )
    
    # Example styles - optimized for 2-column layout
    example_title_style = ParagraphStyle(
        'ExampleTitle',
        parent=styles['Heading2'],
        fontSize=12,
        textColor=GRAY_DARK,
        spaceAfter=4,
        spaceBefore=8,
        fontName='Helvetica-Bold'
    )
    
    filename_style = ParagraphStyle(
        'FilenameStyle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=GRAY_MED,
        spaceAfter=4,
        fontName='Courier',
        leftIndent=0
    )
    
    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Code'],
        fontSize=12,
        fontName='Courier',
        leftIndent=0,
        rightIndent=0,
        spaceAfter=8,
        spaceBefore=4,
        backColor=GRAY_BG,
        borderColor=GRAY_LIGHT,
        borderWidth=0.5,
        borderPadding=6
    )
    
    # Build document
    story = []
    
    # === COVER PAGE ===
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Python Programming", cover_title_style))
    story.append(Paragraph("Examples Collection", cover_title_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Decorative box
    box_table = Table([['']], colWidths=[5*inch], rowHeights=[0.3*inch])
    box_table.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 2, GRAY_DARK),
        ('BACKGROUND', (0, 0), (-1, -1), GRAY_VLIGHT),
    ]))
    story.append(box_table)
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("Complete Reference Guide", cover_subtitle_style))
    story.append(Spacer(1, 0.05*inch))
    story.append(Paragraph("COSC 1336 - Programming Fundamentals", cover_info_style))
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%B %d, %Y')}", cover_info_style))
    story.append(Paragraph("12 Sections • 300+ Examples", cover_info_style))
    
    story.append(PageBreak())
    
    # === TABLE OF CONTENTS ===
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("Table of Contents", toc_title_style))
    story.append(Spacer(1, 0.05*inch))
    
    # Add TOC entries
    section_num = 1
    for folder_name, display_name, description in CATEGORIES:
        folder_path = BASE_DIR / folder_name
        if not folder_path.exists():
            continue
            
        story.append(Paragraph(f"Section {section_num}: {display_name}", toc_section_style))
        
        py_files = sorted(Path(folder_path).glob('*.py'))
        example_count = len([f for f in py_files if f.name != 'generate_pdfs.py' and f.name != 'generate_binder.py'])
        story.append(Paragraph(f"<i>{example_count} examples</i>", toc_entry_style))
        
        section_num += 1
    
    story.append(PageBreak())
    
    # Switch to two-column layout for content
    story.append(NextPageTemplate('TwoColumn'))
    story.append(PageBreak())
    
    # === CONTENT SECTIONS ===
    section_num = 1
    total_examples = 0
    
    for folder_name, display_name, description in CATEGORIES:
        folder_path = BASE_DIR / folder_name
        
        if not folder_path.exists():
            print(f"⚠ Skipping {folder_name} - directory not found")
            continue
        
        print(f"Processing Section {section_num}: {display_name}")
        
        # Section header
        story.append(Paragraph(f"Section {section_num}", section_desc_style))
        story.append(Paragraph(display_name, section_title_style))
        story.append(Paragraph(description, section_desc_style))
        story.append(Spacer(1, 0.05*inch))
        
        # Get all Python files
        py_files = sorted(Path(folder_path).glob('*.py'))
        section_count = 0
        
        for py_file in py_files:
            if py_file.name in ['generate_pdfs.py', 'generate_binder.py']:
                continue
                
            try:
                # Read file content
                try:
                    with open(py_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                except UnicodeDecodeError:
                    with open(py_file, 'r', encoding='latin-1') as f:
                        content = f.read()
                
                clean_content = clean_boilerplate(content)
                
                if not clean_content.strip():
                    continue
                
                # Fix encoding issues that cause black boxes
                clean_content = clean_content.replace('\u2019', "'")  # Right single quote
                clean_content = clean_content.replace('\u2018', "'")  # Left single quote
                clean_content = clean_content.replace('\u201c', '"')  # Left double quote
                clean_content = clean_content.replace('\u201d', '"')  # Right double quote
                clean_content = clean_content.replace('\u2013', '-')  # En dash
                clean_content = clean_content.replace('\u2014', '--')  # Em dash
                clean_content = clean_content.replace('\u2026', '...')  # Ellipsis
                
                title = generate_title_from_filename(py_file.name)
                
                # Create example block
                elements = []
                elements.append(Paragraph(title, example_title_style))
                elements.append(Paragraph(f"<i>Source: {py_file.name}</i>", filename_style))
                
                # Use XPreformatted to preserve indentation (no maxLineLength param)
                code_para = XPreformatted(clean_content, code_style)
                elements.append(code_para)
                
                story.append(KeepTogether(elements))
                section_count += 1
                
            except Exception as e:
                print(f"  ✗ Error processing {py_file.name}: {e}")
                continue
        
        total_examples += section_count
        print(f"  ✓ Added {section_count} examples")
        
        # Add page break between sections
        story.append(PageBreak())
        section_num += 1
    
    # Build PDF with custom canvas
    print("\nGenerating PDF...")
    doc.build(story, canvasmaker=NumberedCanvas)
    
    print()
    print("=" * 70)
    print(f"✓ Binder created successfully!")
    print(f"  File: {output_file.name}")
    print(f"  Location: {output_file.parent}")
    print(f"  Sections: {section_num - 1}")
    print(f"  Total Examples: {total_examples}")
    print("=" * 70)

if __name__ == "__main__":
    create_binder()
