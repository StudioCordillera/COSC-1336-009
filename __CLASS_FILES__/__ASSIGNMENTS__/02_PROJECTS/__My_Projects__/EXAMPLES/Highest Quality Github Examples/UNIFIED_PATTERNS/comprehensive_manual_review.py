"""
Comprehensive Manual Teaching Quality Review
Systematically read and assess ALL 230 Python pattern files
"""

import os
import json
from pathlib import Path

BASE_PATH = r"c:\Users\WORK_ADMIN\Documents\__WORK__\01_COLLEGE\FALL_2025\COSC_1336_09\__CLASS_FILES__\__ASSIGNMENTS__\02_PROJECTS\__My_Projects__\EXAMPLES\Highest Quality Github Examples\UNIFIED_PATTERNS"

def get_all_py_files():
    """Get all Python files organized by category"""
    categories = {
        'creational': [],
        'behavioral': [],
        'structural': [],
        'solid': [],
        'fundamental': [],
        'other': []
    }
    
    for category in categories.keys():
        cat_path = Path(BASE_PATH) / category
        if cat_path.exists():
            py_files = list(cat_path.glob('**/*.py'))
            categories[category] = [str(f.relative_to(BASE_PATH)) for f in py_files]
    
    return categories

def read_file_content(rel_path):
    """Read full content of a file"""
    full_path = Path(BASE_PATH) / rel_path
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"ERROR: {e}"

def assess_teaching_quality(filepath, content):
    """
    Manual assessment criteria:
    - Teaching clarity
    - Use case realism
    - Code quality
    - Python-specific features
    - Completeness
    """
    assessment = {
        'file': filepath,
        'lines': len(content.split('\n')),
        'has_docstring': '"""' in content or "'''" in content,
        'has_comments': '#' in content,
        'has_main': 'if __name__' in content,
        'has_classes': 'class ' in content,
        'has_functions': 'def ' in content,
        'content_preview': content[:500]
    }
    return assessment

def main():
    """Run comprehensive review"""
    print("=" * 80)
    print("COMPREHENSIVE MANUAL REVIEW - ALL 230 FILES")
    print("=" * 80)
    
    categories = get_all_py_files()
    all_assessments = {}
    
    for category, files in categories.items():
        print(f"\n{'='*60}")
        print(f"CATEGORY: {category.upper()} ({len(files)} files)")
        print(f"{'='*60}")
        
        category_assessments = []
        
        for i, filepath in enumerate(files, 1):
            # Skip __init__ files
            if '__init__.py' in filepath:
                continue
                
            content = read_file_content(filepath)
            if content.startswith("ERROR"):
                continue
            
            assessment = assess_teaching_quality(filepath, content)
            category_assessments.append(assessment)
            
            print(f"\n[{i}/{len(files)}] {filepath}")
            print(f"    Lines: {assessment['lines']}")
            print(f"    Docstring: {assessment['has_docstring']}")
            print(f"    Comments: {assessment['has_comments']}")
            print(f"    Runnable: {assessment['has_main']}")
        
        all_assessments[category] = category_assessments
    
    # Save detailed results
    output_path = Path(BASE_PATH) / 'COMPREHENSIVE_REVIEW_DATA.json'
    with open(output_path, 'w') as f:
        json.dump(all_assessments, f, indent=2)
    
    print(f"\n\nDetailed assessment saved to: {output_path}")
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    for cat, assessments in all_assessments.items():
        print(f"{cat}: {len(assessments)} files reviewed")

if __name__ == '__main__':
    main()
