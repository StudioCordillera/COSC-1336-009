"""
PDF Generator for Python Examples
Creates styled PDFs from organized Python example files
"""

import os
import re
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, Table, TableStyle
from reportlab.platypus import Preformatted
from reportlab.lib.enums import TA_LEFT, TA_CENTER

# Base directory containing all examples
BASE_DIR = Path(__file__).parent

# Directory mappings
CATEGORIES = {
    "Examples -  Python Basics": "Python Basics",
    "Examples - Python Decisions": "Python Decisions & Conditionals",
    "Examples - Python Dictionary": "Python Dictionaries",
    "Examples - Python Exceptions": "Python Exception Handling",
    "Examples - Python Files": "Python File I/O Operations",
    "Examples - Python Functions": "Python Functions & Modules",
    "Examples - Python Lists": "Python Lists & List Operations",
    "Examples - Python Loops": "Python Loops & Iteration",
    "Examples - Python OOP": "Python Object-Oriented Programming",
    "Examples - Python Set": "Python Sets & Set Operations",
    "Examples - Python Strings": "Python Strings & String Methods",
    "Examples - Python Tuples": "Python Tuples & Tuple Operations"
}

def clean_boilerplate(content):
    """Remove boilerplate comments from code"""
    lines = content.split('\n')
    cleaned_lines = []
    skip_mode = False
    
    for line in lines:
        stripped = line.strip()
        # Skip boilerplate headers
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
    
    # Remove leading empty lines
    while cleaned_lines and not cleaned_lines[0].strip():
        cleaned_lines.pop(0)
    
    return '\n'.join(cleaned_lines)

def generate_title_from_filename(filename):
    """Generate a readable title from filename"""
    # Remove extension and number prefix
    name = filename.replace('.py', '').replace('.txt', '')
    name = re.sub(r'^\d+\s+', '', name)  # Remove leading numbers
    
    # Convert to title case and clean up
    title = name.replace('_', ' ').replace('-', ' ')
    title = ' '.join(word.capitalize() for word in title.split())
    
    return title

def create_styled_pdf(category_folder, category_name, output_path):
    """Create a styled PDF for a category"""
    print(f"Creating PDF for: {category_name}")
    
    # Create PDF
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=letter,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch,
        leftMargin=0.75*inch,
        rightMargin=0.75*inch
    )
    
    # Styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=HexColor('#2C3E50'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    category_style = ParagraphStyle(
        'CategoryStyle',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=HexColor('#7F8C8D'),
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Oblique'
    )
    
    example_title_style = ParagraphStyle(
        'ExampleTitle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=HexColor('#3498DB'),
        spaceAfter=6,
        spaceBefore=20,
        fontName='Helvetica-Bold',
        borderWidth=0,
        borderPadding=8,
        borderColor=HexColor('#3498DB'),
        borderRadius=4,
        backColor=HexColor('#EBF5FB')
    )
    
    filename_style = ParagraphStyle(
        'FilenameStyle',
        parent=styles['Normal'],
        fontSize=9,
        textColor=HexColor('#95A5A6'),
        spaceAfter=12,
        fontName='Courier',
        leftIndent=10
    )
    
    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Code'],
        fontSize=9,
        fontName='Courier',
        leftIndent=20,
        rightIndent=20,
        spaceAfter=20,
        spaceBefore=10,
        backColor=HexColor('#F8F9FA'),
        borderColor=HexColor('#DEE2E6'),
        borderWidth=1,
        borderPadding=10,
        borderRadius=4
    )
    
    # Build document content
    story = []
    
    # Title page
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph(category_name, title_style))
    story.append(Paragraph("Python Programming Examples Collection", category_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Decorative line
    line_table = Table([['']], colWidths=[6.5*inch])
    line_table.setStyle(TableStyle([
        ('LINEABOVE', (0, 0), (-1, 0), 2, HexColor('#3498DB')),
        ('LINEBELOW', (0, 0), (-1, 0), 2, HexColor('#3498DB')),
    ]))
    story.append(line_table)
    story.append(Spacer(1, 0.5*inch))
    
    # Get all Python files
    py_files = sorted(Path(category_folder).glob('*.py'))
    
    if not py_files:
        story.append(Paragraph("No Python examples found in this category.", styles['Normal']))
    else:
        # Process each file
        for idx, py_file in enumerate(py_files):
            if py_file.name == 'generate_pdfs.py':  # Skip the generator script
                continue
                
            try:
                # Read file content with error handling for encoding
                try:
                    with open(py_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                except UnicodeDecodeError:
                    # Try with latin-1 encoding if utf-8 fails
                    with open(py_file, 'r', encoding='latin-1') as f:
                        content = f.read()
                
                # Clean boilerplate
                clean_content = clean_boilerplate(content)
                
                if not clean_content.strip():
                    continue
                
                # Generate title
                title = generate_title_from_filename(py_file.name)
                
                # Create example block
                elements = []
                elements.append(Paragraph(title, example_title_style))
                elements.append(Paragraph(f"<i>File: {py_file.name}</i>", filename_style))
                
                # Add code with proper formatting
                code_para = Preformatted(clean_content, code_style, maxLineLength=80)
                elements.append(code_para)
                
                # Keep each example together on one page if possible
                story.append(KeepTogether(elements))
                
            except Exception as e:
                print(f"Error processing {py_file.name}: {e}")
                continue
    
    # Build PDF
    doc.build(story)
    print(f"✓ Created: {output_path.name}")

def main():
    """Main function to generate all PDFs"""
    print("=" * 60)
    print("Python Examples PDF Generator")
    print("=" * 60)
    print()
    
    output_dir = BASE_DIR / "PDF_Examples"
    output_dir.mkdir(exist_ok=True)
    
    total = 0
    for folder_name, display_name in CATEGORIES.items():
        folder_path = BASE_DIR / folder_name
        
        if not folder_path.exists():
            print(f"⚠ Skipping {folder_name} - directory not found")
            continue
        
        # Create output filename
        safe_name = display_name.replace(' ', '_').replace('&', 'and').replace('/', '_')
        output_file = output_dir / f"{safe_name}.pdf"
        
        try:
            create_styled_pdf(folder_path, display_name, output_file)
            total += 1
        except Exception as e:
            print(f"✗ Error creating PDF for {display_name}: {e}")
    
    print()
    print("=" * 60)
    print(f"Complete! Generated {total} PDF files in:")
    print(f"  {output_dir}")
    print("=" * 60)

if __name__ == "__main__":
    main()
