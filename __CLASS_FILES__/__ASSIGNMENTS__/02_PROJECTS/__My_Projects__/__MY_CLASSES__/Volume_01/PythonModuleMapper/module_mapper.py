"""
Python Module Mapper - Ultimate Edition
========================================
Comprehensive tool leveraging ALL pyclbr features for module analysis,
code browsing, and structure visualization.

Features:
- Complete module structure analysis
- Class hierarchy visualization
- Method and function discovery
- Nested definition detection
- Async function identification
- Safe untrusted code inspection
- JSON/HTML export capabilities
- Complexity metrics
- Autocomplete data generation
- Documentation generation
- Package structure analysis
"""

import pyclbr
import sys
import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field, asdict
from enum import Enum
from functools import lru_cache
import tempfile


class OutputFormat(Enum):
    """Available output formats"""
    CONSOLE = "console"
    JSON = "json"
    HTML = "html"
    MARKDOWN = "markdown"


@dataclass
class FunctionInfo:
    """Enhanced function information"""
    name: str
    file: str
    module: str
    lineno: int
    parent: Optional[str] = None
    children: Dict[str, Any] = field(default_factory=dict)
    is_async: bool = False
    is_nested: bool = False


@dataclass
class ClassInfo:
    """Enhanced class information"""
    name: str
    file: str
    module: str
    lineno: int
    parent: Optional[str] = None
    children: Dict[str, Any] = field(default_factory=dict)
    super_classes: List[str] = field(default_factory=list)
    methods: Dict[str, int] = field(default_factory=dict)
    method_count: int = 0
    is_nested: bool = False


@dataclass
class ModuleMetrics:
    """Module complexity metrics"""
    total_classes: int = 0
    total_functions: int = 0
    total_methods: int = 0
    max_methods_per_class: int = 0
    nested_definitions: int = 0
    async_functions: int = 0
    inheritance_chains: int = 0


class PythonModuleMapper:
    """
    Ultimate Python module mapping and analysis tool.
    Implements ALL pyclbr features with extensive functionality.
    """
    
    def __init__(self, cache_enabled: bool = True):
        """
        Initialize the mapper.
        
        Args:
            cache_enabled: Enable LRU caching for module reads
        """
        self.cache_enabled = cache_enabled
        self._cached_modules = {}
    
    # ═══════════════════════════════════════════════════════════════════
    # CORE MODULE READING
    # ═══════════════════════════════════════════════════════════════════
    
    @lru_cache(maxsize=128)
    def read_module(self, module_name: str, path: Optional[List[str]] = None) -> Dict:
        """
        Read module with caching support.
        
        Args:
            module_name: Name of the module to read
            path: Optional custom search paths
            
        Returns:
            Dictionary of module definitions
        """
        try:
            if path:
                return pyclbr.readmodule_ex(module_name, path=path)
            return pyclbr.readmodule_ex(module_name)
        except FileNotFoundError:
            raise ValueError(f"Module '{module_name}' not found")
        except SyntaxError as e:
            raise ValueError(f"Syntax error in '{module_name}': {e}")
        except Exception as e:
            raise ValueError(f"Error reading '{module_name}': {e}")
    
    def read_classes_only(self, module_name: str, path: Optional[List[str]] = None) -> Dict:
        """
        Read only class information (legacy compatibility).
        
        Args:
            module_name: Name of the module
            path: Optional custom search paths
            
        Returns:
            Dictionary of class definitions only
        """
        try:
            if path:
                return pyclbr.readmodule(module_name, path=path)
            return pyclbr.readmodule(module_name)
        except Exception as e:
            raise ValueError(f"Error reading classes from '{module_name}': {e}")
    
    # ═══════════════════════════════════════════════════════════════════
    # STRUCTURE ANALYSIS
    # ═══════════════════════════════════════════════════════════════════
    
    def analyze_module(self, module_name: str, path: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Comprehensive module analysis.
        
        Args:
            module_name: Module to analyze
            path: Optional custom search paths
            
        Returns:
            Complete analysis results
        """
        data = self.read_module(module_name, path)
        
        classes = {}
        functions = {}
        
        for name, descriptor in data.items():
            if name == '__path__':
                continue
                
            if isinstance(descriptor, pyclbr.Class):
                classes[name] = self._extract_class_info(descriptor)
            elif isinstance(descriptor, pyclbr.Function):
                functions[name] = self._extract_function_info(descriptor)
        
        return {
            'module_name': module_name,
            'classes': classes,
            'functions': functions,
            'metrics': self._calculate_metrics(classes, functions),
            'is_package': '__path__' in data
        }
    
    def _extract_class_info(self, descriptor: pyclbr.Class) -> ClassInfo:
        """Extract detailed class information."""
        super_classes = [
            base.name if isinstance(base, pyclbr.Class) else str(base)
            for base in descriptor.super
        ]
        
        return ClassInfo(
            name=descriptor.name,
            file=descriptor.file,
            module=descriptor.module,
            lineno=descriptor.lineno,
            parent=descriptor.parent.name if descriptor.parent else None,
            children={k: self._describe_child(v) for k, v in descriptor.children.items()},
            super_classes=super_classes,
            methods=descriptor.methods,
            method_count=len(descriptor.methods),
            is_nested=descriptor.parent is not None
        )
    
    def _extract_function_info(self, descriptor: pyclbr.Function) -> FunctionInfo:
        """Extract detailed function information."""
        is_async = False
        if sys.version_info >= (3, 10):
            is_async = getattr(descriptor, 'is_async', False)
        
        return FunctionInfo(
            name=descriptor.name,
            file=descriptor.file,
            module=descriptor.module,
            lineno=descriptor.lineno,
            parent=descriptor.parent.name if descriptor.parent else None,
            children={k: self._describe_child(v) for k, v in descriptor.children.items()},
            is_async=is_async,
            is_nested=descriptor.parent is not None
        )
    
    def _describe_child(self, descriptor) -> Dict[str, Any]:
        """Describe a child definition."""
        if isinstance(descriptor, pyclbr.Class):
            return {'type': 'class', 'name': descriptor.name, 'lineno': descriptor.lineno}
        elif isinstance(descriptor, pyclbr.Function):
            return {'type': 'function', 'name': descriptor.name, 'lineno': descriptor.lineno}
        return {'type': 'unknown', 'name': str(descriptor)}
    
    def _calculate_metrics(self, classes: Dict, functions: Dict) -> ModuleMetrics:
        """Calculate complexity metrics."""
        metrics = ModuleMetrics()
        metrics.total_classes = len(classes)
        metrics.total_functions = len(functions)
        
        for cls in classes.values():
            metrics.total_methods += cls.method_count
            metrics.max_methods_per_class = max(metrics.max_methods_per_class, cls.method_count)
            metrics.nested_definitions += len(cls.children)
            
            if cls.super_classes:
                metrics.inheritance_chains += 1
        
        for func in functions.values():
            metrics.nested_definitions += len(func.children)
            if func.is_async:
                metrics.async_functions += 1
        
        return metrics
    
    # ═══════════════════════════════════════════════════════════════════
    # HIERARCHY VISUALIZATION
    # ═══════════════════════════════════════════════════════════════════
    
    def visualize_hierarchy(self, module_name: str, path: Optional[List[str]] = None) -> str:
        """
        Create visual class hierarchy.
        
        Args:
            module_name: Module to visualize
            path: Optional custom search paths
            
        Returns:
            Formatted hierarchy string
        """
        classes = self.read_classes_only(module_name, path)
        lines = [f"Class Hierarchy: {module_name}", "=" * 70, ""]
        
        # Find root classes
        root_classes = self._find_root_classes(classes)
        
        for root in root_classes:
            lines.extend(self._build_hierarchy_tree(root, classes))
        
        return "\n".join(lines)
    
    def _find_root_classes(self, classes: Dict) -> List[str]:
        """Find classes that don't inherit from other module classes."""
        roots = []
        for name, cls in classes.items():
            is_root = True
            for base in cls.super:
                base_name = base.name if isinstance(base, pyclbr.Class) else base
                if base_name in classes and base_name != 'object':
                    is_root = False
                    break
            if is_root:
                roots.append(name)
        return sorted(roots)
    
    def _build_hierarchy_tree(self, class_name: str, all_classes: Dict, 
                             indent: int = 0, visited: set = None) -> List[str]:
        """Build hierarchy tree recursively."""
        if visited is None:
            visited = set()
        
        if class_name in visited:
            return []
        visited.add(class_name)
        
        lines = []
        prefix = "  " * indent
        
        if class_name not in all_classes:
            lines.append(f"{prefix}└─ {class_name} (external)")
            return lines
        
        cls = all_classes[class_name]
        method_count = len(cls.methods)
        lines.append(f"{prefix}└─ {cls.name} (line {cls.lineno}, {method_count} methods)")
        
        # Show methods
        if cls.methods:
            method_names = list(cls.methods.keys())[:5]
            methods_str = ", ".join(method_names)
            if len(cls.methods) > 5:
                methods_str += f", ... (+{len(cls.methods) - 5} more)"
            lines.append(f"{prefix}   Methods: {methods_str}")
        
        # Find and display children
        for name, potential_child in all_classes.items():
            for base in potential_child.super:
                base_name = base.name if isinstance(base, pyclbr.Class) else base
                if base_name == class_name:
                    lines.extend(self._build_hierarchy_tree(name, all_classes, indent + 1, visited))
        
        return lines
    
    # ═══════════════════════════════════════════════════════════════════
    # NESTED STRUCTURE ANALYSIS
    # ═══════════════════════════════════════════════════════════════════
    
    def analyze_nested_structures(self, module_name: str, 
                                  path: Optional[List[str]] = None) -> str:
        """
        Analyze and display nested classes and functions.
        
        Args:
            module_name: Module to analyze
            path: Optional custom search paths
            
        Returns:
            Formatted nested structure string
        """
        data = self.read_module(module_name, path)
        lines = [f"Nested Structures: {module_name}", "=" * 70, ""]
        
        for name, descriptor in sorted(data.items()):
            if name == '__path__':
                continue
            
            if hasattr(descriptor, 'children') and descriptor.children:
                lines.extend(self._print_nested(descriptor))
                lines.append("")
        
        return "\n".join(lines)
    
    def _print_nested(self, descriptor, indent: int = 0) -> List[str]:
        """Recursively print nested structures."""
        lines = []
        prefix = "  " * indent
        
        if isinstance(descriptor, pyclbr.Class):
            method_info = f" ({len(descriptor.methods)} methods)" if descriptor.methods else ""
            lines.append(f"{prefix}Class: {descriptor.name} (line {descriptor.lineno}){method_info}")
        elif isinstance(descriptor, pyclbr.Function):
            async_marker = ""
            if sys.version_info >= (3, 10) and getattr(descriptor, 'is_async', False):
                async_marker = " [async]"
            lines.append(f"{prefix}Function: {descriptor.name} (line {descriptor.lineno}){async_marker}")
        
        # Print children recursively
        for child_name, child_desc in sorted(descriptor.children.items()):
            lines.extend(self._print_nested(child_desc, indent + 1))
        
        return lines
    
    # ═══════════════════════════════════════════════════════════════════
    # AUTOCOMPLETE DATA GENERATION
    # ═══════════════════════════════════════════════════════════════════
    
    def generate_autocomplete_data(self, module_name: str, 
                                   path: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Generate autocomplete/IntelliSense data.
        
        Args:
            module_name: Module to process
            path: Optional custom search paths
            
        Returns:
            Autocomplete data structure
        """
        data = self.read_module(module_name, path)
        
        autocomplete = {
            'module': module_name,
            'classes': [],
            'functions': [],
            'methods_by_class': {},
            'nested_items': []
        }
        
        for name, descriptor in data.items():
            if name == '__path__':
                continue
            
            if isinstance(descriptor, pyclbr.Class):
                autocomplete['classes'].append({
                    'name': name,
                    'lineno': descriptor.lineno,
                    'bases': [b.name if isinstance(b, pyclbr.Class) else str(b) 
                             for b in descriptor.super]
                })
                autocomplete['methods_by_class'][name] = list(descriptor.methods.keys())
                
            elif isinstance(descriptor, pyclbr.Function):
                func_info = {
                    'name': name,
                    'lineno': descriptor.lineno
                }
                if sys.version_info >= (3, 10):
                    func_info['is_async'] = getattr(descriptor, 'is_async', False)
                autocomplete['functions'].append(func_info)
            
            # Track nested items
            if hasattr(descriptor, 'children') and descriptor.children:
                autocomplete['nested_items'].extend(list(descriptor.children.keys()))
        
        return autocomplete
    
    # ═══════════════════════════════════════════════════════════════════
    # SAFE CODE INSPECTION
    # ═══════════════════════════════════════════════════════════════════
    
    def inspect_code_safely(self, code_string: str) -> Dict[str, Any]:
        """
        Safely inspect untrusted code without importing.
        
        Args:
            code_string: Python code to inspect
            
        Returns:
            Analysis results
        """
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code_string)
            temp_path = f.name
        
        try:
            module_dir = os.path.dirname(temp_path)
            module_name = os.path.splitext(os.path.basename(temp_path))[0]
            
            data = self.read_module(module_name, path=[module_dir])
            
            classes = sum(1 for v in data.values() if isinstance(v, pyclbr.Class))
            functions = sum(1 for v in data.values() if isinstance(v, pyclbr.Function))
            
            return {
                'safe': True,
                'classes_found': classes,
                'functions_found': functions,
                'details': self.analyze_module(module_name, path=[module_dir])
            }
        except Exception as e:
            return {
                'safe': False,
                'error': str(e)
            }
        finally:
            try:
                os.unlink(temp_path)
            except:
                pass
    
    # ═══════════════════════════════════════════════════════════════════
    # PACKAGE ANALYSIS
    # ═══════════════════════════════════════════════════════════════════
    
    def analyze_package(self, package_path: Path) -> Dict[str, Any]:
        """
        Analyze entire package structure.
        
        Args:
            package_path: Path to package directory
            
        Returns:
            Complete package analysis
        """
        package_path = Path(package_path)
        results = {
            'package_name': package_path.name,
            'modules': {},
            'total_classes': 0,
            'total_functions': 0,
            'total_methods': 0
        }
        
        for py_file in package_path.rglob('*.py'):
            if py_file.name.startswith('__'):
                continue
            
            rel_path = py_file.relative_to(package_path.parent)
            module_name = str(rel_path.with_suffix('')).replace(os.sep, '.')
            
            try:
                analysis = self.analyze_module(module_name, path=[str(package_path.parent)])
                results['modules'][module_name] = analysis
                
                results['total_classes'] += analysis['metrics'].total_classes
                results['total_functions'] += analysis['metrics'].total_functions
                results['total_methods'] += analysis['metrics'].total_methods
            except Exception as e:
                results['modules'][module_name] = {'error': str(e)}
        
        return results
    
    # ═══════════════════════════════════════════════════════════════════
    # DOCUMENTATION GENERATION
    # ═══════════════════════════════════════════════════════════════════
    
    def generate_documentation(self, module_name: str, 
                              path: Optional[List[str]] = None,
                              format: OutputFormat = OutputFormat.MARKDOWN) -> str:
        """
        Generate documentation from module structure.
        
        Args:
            module_name: Module to document
            path: Optional custom search paths
            format: Output format
            
        Returns:
            Formatted documentation string
        """
        analysis = self.analyze_module(module_name, path)
        
        if format == OutputFormat.MARKDOWN:
            return self._generate_markdown_docs(analysis)
        elif format == OutputFormat.HTML:
            return self._generate_html_docs(analysis)
        else:
            return self._generate_console_docs(analysis)
    
    def _generate_markdown_docs(self, analysis: Dict) -> str:
        """Generate Markdown documentation."""
        lines = [
            f"# {analysis['module_name']} Module Documentation",
            "",
            "## Module Metrics",
            "",
            f"- **Total Classes**: {analysis['metrics'].total_classes}",
            f"- **Total Functions**: {analysis['metrics'].total_functions}",
            f"- **Total Methods**: {analysis['metrics'].total_methods}",
            f"- **Max Methods per Class**: {analysis['metrics'].max_methods_per_class}",
            f"- **Nested Definitions**: {analysis['metrics'].nested_definitions}",
            f"- **Async Functions**: {analysis['metrics'].async_functions}",
            ""
        ]
        
        if analysis['classes']:
            lines.extend(["## Classes", ""])
            for name, cls in sorted(analysis['classes'].items()):
                lines.append(f"### {name}")
                lines.append(f"Defined at line {cls.lineno} in `{cls.file}`")
                lines.append("")
                
                if cls.super_classes:
                    lines.append(f"**Inherits from:** {', '.join(cls.super_classes)}")
                    lines.append("")
                
                if cls.methods:
                    lines.append("**Methods:**")
                    for method, line in sorted(cls.methods.items(), key=lambda x: x[1]):
                        lines.append(f"- `{method}()` (line {line})")
                    lines.append("")
                
                if cls.children:
                    lines.append("**Nested Definitions:**")
                    for child_name, child in cls.children.items():
                        lines.append(f"- {child['type'].capitalize()}: `{child_name}` (line {child['lineno']})")
                    lines.append("")
        
        if analysis['functions']:
            lines.extend(["## Functions", ""])
            for name, func in sorted(analysis['functions'].items()):
                async_marker = " (async)" if func.is_async else ""
                lines.append(f"### {name}(){async_marker}")
                lines.append(f"Defined at line {func.lineno} in `{func.file}`")
                lines.append("")
                
                if func.children:
                    lines.append("**Nested Definitions:**")
                    for child_name, child in func.children.items():
                        lines.append(f"- {child['type'].capitalize()}: `{child_name}` (line {child['lineno']})")
                    lines.append("")
        
        return "\n".join(lines)
    
    def _generate_html_docs(self, analysis: Dict) -> str:
        """Generate HTML documentation."""
        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>{analysis['module_name']} - Module Documentation</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
        .container {{ background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
        h2 {{ color: #34495e; margin-top: 30px; }}
        h3 {{ color: #7f8c8d; }}
        .metric {{ display: inline-block; margin: 10px 20px 10px 0; padding: 10px; background: #ecf0f1; border-radius: 5px; }}
        .metric-value {{ font-size: 24px; font-weight: bold; color: #3498db; }}
        .metric-label {{ font-size: 12px; color: #7f8c8d; }}
        .class-item, .function-item {{ margin: 20px 0; padding: 15px; background: #f8f9fa; border-left: 4px solid #3498db; }}
        .method-list {{ margin: 10px 0; padding-left: 20px; }}
        .code {{ font-family: 'Courier New', monospace; background: #ecf0f1; padding: 2px 6px; border-radius: 3px; }}
        .async-badge {{ background: #e74c3c; color: white; padding: 2px 8px; border-radius: 3px; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{analysis['module_name']} Module Documentation</h1>
        
        <h2>Module Metrics</h2>
        <div class="metrics">
            <div class="metric">
                <div class="metric-value">{analysis['metrics'].total_classes}</div>
                <div class="metric-label">Classes</div>
            </div>
            <div class="metric">
                <div class="metric-value">{analysis['metrics'].total_functions}</div>
                <div class="metric-label">Functions</div>
            </div>
            <div class="metric">
                <div class="metric-value">{analysis['metrics'].total_methods}</div>
                <div class="metric-label">Methods</div>
            </div>
            <div class="metric">
                <div class="metric-value">{analysis['metrics'].async_functions}</div>
                <div class="metric-label">Async Functions</div>
            </div>
        </div>
"""
        
        if analysis['classes']:
            html += "\n        <h2>Classes</h2>\n"
            for name, cls in sorted(analysis['classes'].items()):
                html += f"""        <div class="class-item">
            <h3>{name}</h3>
            <p>Defined at line {cls.lineno} in <span class="code">{cls.file}</span></p>
"""
                if cls.super_classes:
                    html += f"            <p><strong>Inherits from:</strong> {', '.join(f'<span class=\"code\">{b}</span>' for b in cls.super_classes)}</p>\n"
                
                if cls.methods:
                    html += "            <p><strong>Methods:</strong></p>\n            <ul class=\"method-list\">\n"
                    for method in sorted(cls.methods.keys()):
                        html += f"                <li><span class=\"code\">{method}()</span></li>\n"
                    html += "            </ul>\n"
                
                html += "        </div>\n"
        
        if analysis['functions']:
            html += "\n        <h2>Functions</h2>\n"
            for name, func in sorted(analysis['functions'].items()):
                async_badge = '<span class="async-badge">ASYNC</span> ' if func.is_async else ''
                html += f"""        <div class="function-item">
            <h3>{async_badge}{name}()</h3>
            <p>Defined at line {func.lineno} in <span class="code">{func.file}</span></p>
        </div>
"""
        
        html += """    </div>
</body>
</html>"""
        return html
    
    def _generate_console_docs(self, analysis: Dict) -> str:
        """Generate console-friendly documentation."""
        lines = [
            "=" * 70,
            f" {analysis['module_name']} - Module Documentation",
            "=" * 70,
            "",
            "MODULE METRICS:",
            f"  Classes:          {analysis['metrics'].total_classes}",
            f"  Functions:        {analysis['metrics'].total_functions}",
            f"  Total Methods:    {analysis['metrics'].total_methods}",
            f"  Async Functions:  {analysis['metrics'].async_functions}",
            ""
        ]
        
        if analysis['classes']:
            lines.extend(["CLASSES:", "-" * 70])
            for name, cls in sorted(analysis['classes'].items()):
                lines.append(f"\n{name}")
                lines.append(f"  Location: {cls.file}:{cls.lineno}")
                if cls.super_classes:
                    lines.append(f"  Inherits: {', '.join(cls.super_classes)}")
                if cls.methods:
                    lines.append(f"  Methods:  {', '.join(list(cls.methods.keys())[:5])}")
                    if len(cls.methods) > 5:
                        lines.append(f"            ... (+{len(cls.methods) - 5} more)")
        
        if analysis['functions']:
            lines.extend(["", "FUNCTIONS:", "-" * 70])
            for name, func in sorted(analysis['functions'].items()):
                async_marker = " [ASYNC]" if func.is_async else ""
                lines.append(f"\n{name}(){async_marker}")
                lines.append(f"  Location: {func.file}:{func.lineno}")
        
        lines.append("\n" + "=" * 70)
        return "\n".join(lines)
    
    # ═══════════════════════════════════════════════════════════════════
    # EXPORT FUNCTIONALITY
    # ═══════════════════════════════════════════════════════════════════
    
    def export_to_json(self, module_name: str, output_file: str, 
                       path: Optional[List[str]] = None):
        """
        Export module structure to JSON.
        
        Args:
            module_name: Module to export
            output_file: Output JSON file path
            path: Optional custom search paths
        """
        analysis = self.analyze_module(module_name, path)
        
        # Convert dataclasses to dicts
        export_data = {
            'module_name': analysis['module_name'],
            'is_package': analysis['is_package'],
            'metrics': asdict(analysis['metrics']),
            'classes': {k: asdict(v) for k, v in analysis['classes'].items()},
            'functions': {k: asdict(v) for k, v in analysis['functions'].items()}
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
    
    def export_to_html(self, module_name: str, output_file: str,
                       path: Optional[List[str]] = None):
        """
        Export module documentation to HTML.
        
        Args:
            module_name: Module to export
            output_file: Output HTML file path
            path: Optional custom search paths
        """
        analysis = self.analyze_module(module_name, path)
        html = self._generate_html_docs(analysis)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
    
    # ═══════════════════════════════════════════════════════════════════
    # COMPARISON & DIFF
    # ═══════════════════════════════════════════════════════════════════
    
    def compare_modules(self, module1: str, module2: str,
                       path: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Compare two modules and show differences.
        
        Args:
            module1: First module name
            module2: Second module name
            path: Optional custom search paths
            
        Returns:
            Comparison results
        """
        analysis1 = self.analyze_module(module1, path)
        analysis2 = self.analyze_module(module2, path)
        
        classes1 = set(analysis1['classes'].keys())
        classes2 = set(analysis2['classes'].keys())
        
        functions1 = set(analysis1['functions'].keys())
        functions2 = set(analysis2['functions'].keys())
        
        return {
            'module1': module1,
            'module2': module2,
            'classes_only_in_1': list(classes1 - classes2),
            'classes_only_in_2': list(classes2 - classes1),
            'common_classes': list(classes1 & classes2),
            'functions_only_in_1': list(functions1 - functions2),
            'functions_only_in_2': list(functions2 - functions1),
            'common_functions': list(functions1 & functions2),
            'metrics_comparison': {
                module1: asdict(analysis1['metrics']),
                module2: asdict(analysis2['metrics'])
            }
        }
    
    # ═══════════════════════════════════════════════════════════════════
    # SEARCH FUNCTIONALITY
    # ═══════════════════════════════════════════════════════════════════
    
    def search_for_class(self, module_name: str, class_name: str,
                        path: Optional[List[str]] = None) -> Optional[ClassInfo]:
        """
        Search for a specific class in module.
        
        Args:
            module_name: Module to search
            class_name: Class name to find
            path: Optional custom search paths
            
        Returns:
            ClassInfo if found, None otherwise
        """
        analysis = self.analyze_module(module_name, path)
        return analysis['classes'].get(class_name)
    
    def search_for_function(self, module_name: str, function_name: str,
                           path: Optional[List[str]] = None) -> Optional[FunctionInfo]:
        """
        Search for a specific function in module.
        
        Args:
            module_name: Module to search
            function_name: Function name to find
            path: Optional custom search paths
            
        Returns:
            FunctionInfo if found, None otherwise
        """
        analysis = self.analyze_module(module_name, path)
        return analysis['functions'].get(function_name)
    
    def find_methods(self, module_name: str, class_name: str,
                    path: Optional[List[str]] = None) -> Dict[str, int]:
        """
        Get all methods for a specific class.
        
        Args:
            module_name: Module containing the class
            class_name: Class name
            path: Optional custom search paths
            
        Returns:
            Dictionary of method names to line numbers
        """
        cls = self.search_for_class(module_name, class_name, path)
        return cls.methods if cls else {}


def main():
    """Example usage and demonstration."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Ultimate Python Module Mapper")
    parser.add_argument('module', help='Module name to analyze')
    parser.add_argument('--path', nargs='+', help='Custom search paths')
    parser.add_argument('--hierarchy', action='store_true', help='Show class hierarchy')
    parser.add_argument('--nested', action='store_true', help='Show nested structures')
    parser.add_argument('--export-json', help='Export to JSON file')
    parser.add_argument('--export-html', help='Export to HTML file')
    parser.add_argument('--docs', action='store_true', help='Generate documentation')
    parser.add_argument('--autocomplete', action='store_true', help='Generate autocomplete data')
    parser.add_argument('--compare', help='Compare with another module')
    
    args = parser.parse_args()
    
    mapper = PythonModuleMapper()
    
    try:
        if args.hierarchy:
            print(mapper.visualize_hierarchy(args.module, args.path))
        
        elif args.nested:
            print(mapper.analyze_nested_structures(args.module, args.path))
        
        elif args.export_json:
            mapper.export_to_json(args.module, args.export_json, args.path)
            print(f"Exported to {args.export_json}")
        
        elif args.export_html:
            mapper.export_to_html(args.module, args.export_html, args.path)
            print(f"Exported to {args.export_html}")
        
        elif args.docs:
            print(mapper.generate_documentation(args.module, args.path, OutputFormat.CONSOLE))
        
        elif args.autocomplete:
            data = mapper.generate_autocomplete_data(args.module, args.path)
            print(json.dumps(data, indent=2))
        
        elif args.compare:
            comparison = mapper.compare_modules(args.module, args.compare, args.path)
            print(json.dumps(comparison, indent=2))
        
        else:
            # Default: full analysis
            analysis = mapper.analyze_module(args.module, args.path)
            print(mapper._generate_console_docs(analysis))
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
