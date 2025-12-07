#!/usr/bin/env python3
"""
Automated Design Pattern Analyzer

Systematically analyzes all pattern files and identifies best-in-class examples
based on code quality, documentation, and principle adherence.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass, field

@dataclass
class PatternScore:
    """Scoring metrics for pattern quality assessment"""
    file_path: str
    score: float = 0.0
    strengths: List[str] = field(default_factory=list)
    weaknesses: List[str] = field(default_factory=list)
    
    # Scoring factors
    has_type_hints: bool = False
    has_docstrings: bool = False
    has_main_guard: bool = False
    has_comments: bool = False
    has_abc_usage: bool = False
    has_real_world_example: bool = False
    is_python3: bool = True
    line_count: int = 0
    complexity_score: float = 0.0

class PatternAnalyzer:
    """Analyzes Python design pattern files for quality metrics"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.categories = ['behavioral', 'creational', 'structural', 'solid', 'fundamental', 'other']
        self.results: Dict[str, List[PatternScore]] = {}
        
    def analyze_file(self, file_path: Path) -> PatternScore:
        """Analyze a single Python file for quality metrics"""
        score = PatternScore(file_path=str(file_path))
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
                
            score.line_count = len(lines)
            
            # Check for type hints
            if re.search(r':\s*(str|int|float|bool|List|Dict|Tuple|Optional|Callable)', content):
                score.has_type_hints = True
                score.score += 2.0
                score.strengths.append("Type hints present")
            
            # Check for docstrings
            docstring_patterns = [
                r'""".*?"""',
                r"'''.*?'''",
                r'def \w+\([^)]*\):\s*"""',
            ]
            if any(re.search(pattern, content, re.DOTALL) for pattern in docstring_patterns):
                score.has_docstrings = True
                score.score += 1.5
                score.strengths.append("Documented with docstrings")
            
            # Check for __main__ guard
            if "if __name__ == '__main__':" in content or 'if __name__ == "__main__":' in content:
                score.has_main_guard = True
                score.score += 1.0
                score.strengths.append("Has __main__ guard")
            
            # Check for comments
            comment_count = sum(1 for line in lines if line.strip().startswith('#'))
            if comment_count > 3:
                score.has_comments = True
                score.score += 0.5
                score.strengths.append(f"{comment_count} comment lines")
            
            # Check for ABC usage
            if 'from abc import' in content or 'import abc' in content:
                score.has_abc_usage = True
                score.score += 1.0
                score.strengths.append("Uses ABC for proper abstraction")
            
            # Check for Python 2 vs 3
            if 'print ' in content and 'print(' not in content:
                score.is_python3 = False
                score.score -= 3.0
                score.weaknesses.append("Python 2 syntax (print statements)")
            
            # Check for real-world examples
            real_world_keywords = [
                'database', 'user', 'order', 'person', 'account', 
                'product', 'customer', 'email', 'payment', 'invoice',
                'django', 'flask', 'http', 'api'
            ]
            if any(keyword in content.lower() for keyword in real_world_keywords):
                score.has_real_world_example = True
                score.score += 1.0
                score.strengths.append("Real-world use case")
            
            # Complexity scoring (simple heuristic)
            class_count = content.count('class ')
            method_count = content.count('def ')
            if 3 <= class_count <= 8 and 5 <= method_count <= 20:
                score.complexity_score = 1.0
                score.score += 1.0
                score.strengths.append(f"Good complexity ({class_count} classes, {method_count} methods)")
            elif class_count > 15 or method_count > 30:
                score.complexity_score = -0.5
                score.score -= 0.5
                score.weaknesses.append("Overly complex")
            
            # File length scoring
            if 30 <= score.line_count <= 150:
                score.score += 0.5
                score.strengths.append(f"Good length ({score.line_count} lines)")
            elif score.line_count < 20:
                score.weaknesses.append("Too minimal")
            elif score.line_count > 300:
                score.weaknesses.append("Too long")
                
        except Exception as e:
            score.weaknesses.append(f"Error reading file: {e}")
            score.score = -10.0
            
        return score
    
    def analyze_category(self, category: str) -> Dict[str, List[PatternScore]]:
        """Analyze all files in a category"""
        category_path = self.base_path / category
        results = {}
        
        if not category_path.exists():
            return results
        
        for py_file in category_path.glob('*.py'):
            if py_file.name.startswith('__'):
                continue
                
            score = self.analyze_file(py_file)
            
            # Group by pattern name (extract base pattern from filename)
            pattern_name = self._extract_pattern_name(py_file.name)
            if pattern_name not in results:
                results[pattern_name] = []
            results[pattern_name].append(score)
        
        return results
    
    def _extract_pattern_name(self, filename: str) -> str:
        """Extract pattern name from filename"""
        # Remove extensions and prefixes
        name = filename.replace('.py', '')
        name = re.sub(r'^(faif_|sbeygi_|refactoring_|exercise_|\d+_)', '', name)
        name = re.sub(r'_(main|example|test)$', '', name)
        return name
    
    def analyze_all(self):
        """Analyze all categories"""
        print("🔍 Starting automated pattern analysis...\n")
        
        for category in self.categories:
            print(f"📂 Analyzing {category}/...")
            self.results[category] = self.analyze_category(category)
            
            # Show top file for each pattern in category
            for pattern_name, scores in self.results[category].items():
                if not scores:
                    continue
                    
                # Sort by score
                scores.sort(key=lambda x: x.score, reverse=True)
                best = scores[0]
                
                if best.score > 5.0:
                    print(f"  ✅ {pattern_name}: {Path(best.file_path).name} (score: {best.score:.1f})")
                elif best.score > 3.0:
                    print(f"  ⚠️  {pattern_name}: {Path(best.file_path).name} (score: {best.score:.1f})")
        
        print("\n✨ Analysis complete!")
    
    def generate_report(self, output_file: str):
        """Generate comprehensive markdown report"""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# Automated Pattern Analysis Report\n\n")
            f.write("**Generated**: December 6, 2025\n\n")
            f.write("---\n\n")
            
            for category in self.categories:
                if category not in self.results or not self.results[category]:
                    continue
                    
                f.write(f"## {category.title()} Patterns\n\n")
                
                for pattern_name, scores in sorted(self.results[category].items()):
                    if not scores:
                        continue
                    
                    scores.sort(key=lambda x: x.score, reverse=True)
                    best = scores[0]
                    
                    f.write(f"### {pattern_name.replace('_', ' ').title()}\n\n")
                    f.write(f"**Best Example**: `{Path(best.file_path).name}`\n")
                    f.write(f"**Score**: {best.score:.1f}/10\n\n")
                    
                    if best.strengths:
                        f.write("**Strengths**:\n")
                        for strength in best.strengths:
                            f.write(f"- ✅ {strength}\n")
                        f.write("\n")
                    
                    if best.weaknesses:
                        f.write("**Weaknesses**:\n")
                        for weakness in best.weaknesses:
                            f.write(f"- ❌ {weakness}\n")
                        f.write("\n")
                    
                    # Show alternatives if they exist
                    if len(scores) > 1:
                        f.write("**Alternatives**:\n")
                        for i, alt in enumerate(scores[1:4], 1):  # Top 3 alternatives
                            f.write(f"{i}. `{Path(alt.file_path).name}` (score: {alt.score:.1f})\n")
                        f.write("\n")
                    
                    f.write("---\n\n")
        
        print(f"📄 Report generated: {output_file}")

def main():
    """Main execution"""
    base_path = r"c:\Users\WORK_ADMIN\Documents\__WORK__\01_COLLEGE\FALL_2025\COSC_1336_09\__CLASS_FILES__\__ASSIGNMENTS__\02_PROJECTS\__My_Projects__\EXAMPLES\Highest Quality Github Examples\UNIFIED_PATTERNS"
    
    analyzer = PatternAnalyzer(base_path)
    analyzer.analyze_all()
    
    # Generate comprehensive report
    output_file = os.path.join(base_path, "AUTOMATED_ANALYSIS.md")
    analyzer.generate_report(output_file)
    
    print(f"\n🎯 Analysis complete! Check {output_file} for full report.")

if __name__ == '__main__':
    main()
