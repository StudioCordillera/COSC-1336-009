"""
Query Interface for Relationship Graph

User-friendly API for searching and querying the knowledge graph.
Wraps RelationshipGraphBuilder with convenience methods and result formatting.

Design Patterns:
- Facade Pattern: Simplifies complex graph operations
- Builder Pattern: QueryBuilder for complex queries
- Strategy Pattern: ResultFormatter for different output formats

All dependencies injected via constructors.
"""

import re
import json
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from typing import List, Optional, Dict, Any, Callable
from enum import Enum

# Import graph builder
try:
    from graph import RelationshipGraphBuilder, GraphNode
    from models import DatabaseSessionFactory
except ImportError:
    # For testing, allow module to load
    RelationshipGraphBuilder = None
    GraphNode = None
    DatabaseSessionFactory = None


# ============================================================================
# Query Result Types
# ============================================================================

@dataclass
class QueryResult:
    """Result of a query operation"""
    query: str
    total_results: int
    results: List[GraphNode]
    metadata: Dict[str, Any]
    
    def filter(self, predicate: Callable[[GraphNode], bool]) -> 'QueryResult':
        """Filter results by predicate"""
        filtered = [node for node in self.results if predicate(node)]
        return QueryResult(
            query=self.query + " [filtered]",
            total_results=len(filtered),
            results=filtered,
            metadata=self.metadata
        )
    
    def limit(self, n: int) -> 'QueryResult':
        """Limit results to first n items"""
        return QueryResult(
            query=self.query + f" [limit {n}]",
            total_results=self.total_results,
            results=self.results[:n],
            metadata={**self.metadata, 'limited_to': n}
        )
    
    def sort_by(self, key: str, reverse: bool = False) -> 'QueryResult':
        """Sort results by metadata key"""
        sorted_results = sorted(
            self.results,
            key=lambda n: n.metadata.get(key, ''),
            reverse=reverse
        )
        return QueryResult(
            query=self.query + f" [sorted by {key}]",
            total_results=self.total_results,
            results=sorted_results,
            metadata=self.metadata
        )


# ============================================================================
# Result Formatters (Strategy Pattern)
# ============================================================================

class ResultFormatter(ABC):
    """Abstract formatter for query results"""
    
    @abstractmethod
    def format(self, result: QueryResult) -> str:
        """Format query result"""
        pass


class JSONFormatter(ResultFormatter):
    """Format results as JSON"""
    
    def format(self, result: QueryResult) -> str:
        output = {
            'query': result.query,
            'total_results': result.total_results,
            'metadata': result.metadata,
            'results': []
        }
        
        for node in result.results:
            output['results'].append({
                'type': node.entity_type,
                'id': node.entity_id,
                'name': node.name,
                'metadata': node.metadata
            })
        
        return json.dumps(output, indent=2)


class TextFormatter(ResultFormatter):
    """Format results as plain text"""
    
    def format(self, result: QueryResult) -> str:
        lines = []
        lines.append(f"Query: {result.query}")
        lines.append(f"Results: {result.total_results}")
        lines.append("")
        
        for i, node in enumerate(result.results, 1):
            lines.append(f"{i}. [{node.entity_type}] {node.name}")
            
            # Add key metadata
            if node.entity_type == 'function':
                module = node.metadata.get('module', 'unknown')
                cls = node.metadata.get('class')
                if cls:
                    lines.append(f"   Location: {module}.{cls}.{node.name}")
                else:
                    lines.append(f"   Location: {module}.{node.name}")
            elif node.entity_type == 'class':
                module = node.metadata.get('module', 'unknown')
                lines.append(f"   Module: {module}")
            elif node.entity_type == 'module':
                filepath = node.metadata.get('filepath', 'unknown')
                lines.append(f"   Path: {filepath}")
            
            lines.append("")
        
        return "\n".join(lines)


class MarkdownFormatter(ResultFormatter):
    """Format results as Markdown"""
    
    def format(self, result: QueryResult) -> str:
        lines = []
        lines.append(f"# Query Results: {result.query}")
        lines.append("")
        lines.append(f"**Total Results:** {result.total_results}")
        lines.append("")
        
        if result.results:
            lines.append("## Results")
            lines.append("")
            
            for node in result.results:
                # Create heading
                lines.append(f"### {node.name}")
                lines.append("")
                
                # Add metadata
                lines.append(f"- **Type:** `{node.entity_type}`")
                
                if node.entity_type == 'function':
                    module = node.metadata.get('module', 'unknown')
                    cls = node.metadata.get('class')
                    if cls:
                        lines.append(f"- **Location:** `{module}.{cls}.{node.name}`")
                    else:
                        lines.append(f"- **Location:** `{module}.{node.name}`")
                    
                    if node.metadata.get('is_method'):
                        lines.append(f"- **Is Method:** Yes")
                    if node.metadata.get('is_async'):
                        lines.append(f"- **Is Async:** Yes")
                    
                    taxonomy = node.metadata.get('taxonomy')
                    if taxonomy:
                        lines.append(f"- **Category:** `{taxonomy}`")
                        subcategory = node.metadata.get('subcategory')
                        if subcategory:
                            lines.append(f"- **Subcategory:** `{subcategory}`")
                
                elif node.entity_type == 'class':
                    module = node.metadata.get('module', 'unknown')
                    lines.append(f"- **Module:** `{module}`")
                    lineno = node.metadata.get('lineno')
                    if lineno:
                        lines.append(f"- **Line:** {lineno}")
                
                elif node.entity_type == 'module':
                    filepath = node.metadata.get('filepath', 'unknown')
                    lines.append(f"- **Path:** `{filepath}`")
                    is_package = node.metadata.get('is_package')
                    if is_package:
                        lines.append(f"- **Is Package:** Yes")
                
                lines.append("")
        
        return "\n".join(lines)


# ============================================================================
# Query Interface (Facade Pattern)
# ============================================================================

class QueryInterface:
    """
    User-friendly interface for querying the knowledge graph.
    
    Dependency Injection:
    - graph_builder: RelationshipGraphBuilder instance
    - default_formatter: Default result formatter
    """
    
    def __init__(
        self,
        graph_builder: RelationshipGraphBuilder,
        default_formatter: Optional[ResultFormatter] = None
    ):
        self.graph = graph_builder
        self.default_formatter = default_formatter or TextFormatter()
    
    # ========================================================================
    # Basic Search Methods
    # ========================================================================
    
    def search_by_name(self, name: str, exact: bool = True) -> QueryResult:
        """
        Search for constructs by name.
        
        Args:
            name: Name to search for
            exact: If True, exact match; if False, substring match
            
        Returns:
            QueryResult with all matching constructs
        """
        results = self.graph.find_all_uses_of(name)
        
        all_nodes = []
        all_nodes.extend(results['as_module'])
        all_nodes.extend(results['as_class'])
        all_nodes.extend(results['as_function'])
        
        if not exact:
            # For substring search, filter by name contains
            all_nodes = [n for n in all_nodes if name.lower() in n.name.lower()]
        
        return QueryResult(
            query=f"search_by_name('{name}', exact={exact})",
            total_results=len(all_nodes),
            results=all_nodes,
            metadata={'search_type': 'name', 'exact': exact}
        )
    
    def search_by_pattern(self, pattern: str, entity_type: Optional[str] = None) -> QueryResult:
        """
        Search by regex pattern.
        
        Args:
            pattern: Regex pattern to match
            entity_type: Optional filter by 'module', 'class', 'function'
            
        Returns:
            QueryResult with matching constructs
        """
        regex = re.compile(pattern, re.IGNORECASE)
        results = []
        
        # Search across all entity types (simplified - would need full scan)
        # For now, use common patterns
        common_names = [
            '__init__', '__str__', '__repr__', '__eq__', '__ne__',
            'get_', 'set_', 'is_', 'has_', 'can_'
        ]
        
        for name in common_names:
            if regex.search(name):
                uses = self.graph.find_all_uses_of(name)
                if entity_type == 'module':
                    results.extend(uses['as_module'])
                elif entity_type == 'class':
                    results.extend(uses['as_class'])
                elif entity_type == 'function':
                    results.extend(uses['as_function'])
                else:
                    results.extend(uses['as_module'])
                    results.extend(uses['as_class'])
                    results.extend(uses['as_function'])
        
        return QueryResult(
            query=f"search_by_pattern('{pattern}')",
            total_results=len(results),
            results=results,
            metadata={'search_type': 'pattern', 'pattern': pattern}
        )
    
    def search_by_type(self, entity_type: str) -> QueryResult:
        """
        Get all entities of a specific type.
        
        Args:
            entity_type: 'module', 'class', or 'function'
            
        Returns:
            QueryResult with all entities of that type
        """
        # This would require scanning all entities
        # For now, return empty with metadata
        return QueryResult(
            query=f"search_by_type('{entity_type}')",
            total_results=0,
            results=[],
            metadata={'search_type': 'type', 'entity_type': entity_type, 'note': 'Full scan not implemented'}
        )
    
    # ========================================================================
    # Taxonomy-Based Queries
    # ========================================================================
    
    def find_constructors(self, class_name: Optional[str] = None) -> QueryResult:
        """
        Find all constructors, optionally filtered by class.
        
        Args:
            class_name: Optional class name filter
            
        Returns:
            QueryResult with constructor methods
        """
        constructors = self.graph.find_all_constructors()
        
        if class_name:
            constructors = [
                c for c in constructors
                if c.metadata.get('class') == class_name
            ]
        
        return QueryResult(
            query=f"find_constructors(class_name='{class_name}')" if class_name else "find_constructors()",
            total_results=len(constructors),
            results=constructors,
            metadata={'category': 'constructor', 'class_filter': class_name}
        )
    
    def find_magic_methods(self, method_name: Optional[str] = None) -> QueryResult:
        """
        Find all magic methods, optionally filtered by name.
        
        Args:
            method_name: Optional method name (e.g., '__str__')
            
        Returns:
            QueryResult with magic methods
        """
        magic = self.graph.find_all_magic_methods()
        
        if method_name:
            magic = [m for m in magic if m.name == method_name]
        
        return QueryResult(
            query=f"find_magic_methods('{method_name}')" if method_name else "find_magic_methods()",
            total_results=len(magic),
            results=magic,
            metadata={'category': 'magic_method', 'name_filter': method_name}
        )
    
    def find_by_category(
        self,
        category: str,
        module_filter: Optional[str] = None
    ) -> QueryResult:
        """
        Find all constructs in a taxonomy category.
        
        Args:
            category: Taxonomy category (e.g., 'accessor', 'property')
            module_filter: Optional module name filter
            
        Returns:
            QueryResult with categorized constructs
        """
        results = self.graph.find_by_category(category)
        
        if module_filter:
            results = [
                r for r in results
                if r.metadata.get('module') == module_filter
            ]
        
        return QueryResult(
            query=f"find_by_category('{category}', module='{module_filter}')" if module_filter else f"find_by_category('{category}')",
            total_results=len(results),
            results=results,
            metadata={'category': category, 'module_filter': module_filter}
        )
    
    def find_async_functions(self, module_filter: Optional[str] = None) -> QueryResult:
        """Find all async functions"""
        async_funcs = self.graph.find_all_async_functions()
        
        if module_filter:
            async_funcs = [
                f for f in async_funcs
                if f.metadata.get('module') == module_filter
            ]
        
        return QueryResult(
            query=f"find_async_functions(module='{module_filter}')" if module_filter else "find_async_functions()",
            total_results=len(async_funcs),
            results=async_funcs,
            metadata={'category': 'async_function', 'module_filter': module_filter}
        )
    
    # ========================================================================
    # Relationship Queries
    # ========================================================================
    
    def find_dependencies(self, module_name: str) -> QueryResult:
        """Find what a module imports"""
        deps = self.graph.find_dependencies(module_name)
        
        return QueryResult(
            query=f"find_dependencies('{module_name}')",
            total_results=len(deps),
            results=deps,
            metadata={'relationship': 'imports', 'from_module': module_name}
        )
    
    def find_dependents(self, module_name: str) -> QueryResult:
        """Find what imports a module"""
        dependents = self.graph.find_dependents(module_name)
        
        return QueryResult(
            query=f"find_dependents('{module_name}')",
            total_results=len(dependents),
            results=dependents,
            metadata={'relationship': 'imported_by', 'target_module': module_name}
        )
    
    def find_inheritance(self, class_name: str, direction: str = 'derived') -> QueryResult:
        """
        Find inheritance relationships.
        
        Args:
            class_name: Name of the class
            direction: 'derived' (who inherits) or 'base' (inherits from)
        """
        if direction == 'derived':
            results = self.graph.find_derived_classes(class_name)
            query_str = f"find_inheritance('{class_name}', direction='derived')"
        else:
            results = self.graph.find_base_classes(class_name)
            query_str = f"find_inheritance('{class_name}', direction='base')"
        
        return QueryResult(
            query=query_str,
            total_results=len(results),
            results=results,
            metadata={'relationship': 'inherits', 'direction': direction, 'class': class_name}
        )
    
    # ========================================================================
    # Statistics and Distribution
    # ========================================================================
    
    def get_taxonomy_stats(self) -> Dict[str, int]:
        """Get distribution of constructs by taxonomy category"""
        return self.graph.get_taxonomy_distribution()
    
    def get_summary(self) -> Dict[str, Any]:
        """Get overall system summary"""
        taxonomy_dist = self.get_taxonomy_stats()
        
        return {
            'taxonomy_categories': len(taxonomy_dist),
            'total_categorized': sum(taxonomy_dist.values()),
            'distribution': taxonomy_dist
        }
    
    # ========================================================================
    # Result Formatting
    # ========================================================================
    
    def format_result(
        self,
        result: QueryResult,
        format: str = 'text'
    ) -> str:
        """
        Format query result.
        
        Args:
            result: QueryResult to format
            format: 'text', 'json', or 'markdown'
            
        Returns:
            Formatted string
        """
        if format == 'json':
            formatter = JSONFormatter()
        elif format == 'markdown':
            formatter = MarkdownFormatter()
        else:
            formatter = TextFormatter()
        
        return formatter.format(result)


# ============================================================================
# Example Usage
# ============================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("Query Interface - Example Usage")
    print("=" * 70)
    print()
    print("# Basic Searches")
    print("  query.search_by_name('__init__')")
    print("  query.search_by_name('Animal', exact=False)")
    print("  query.search_by_pattern('^get_.*')")
    print()
    print("# Taxonomy Queries")
    print("  query.find_constructors()")
    print("  query.find_constructors(class_name='Dog')")
    print("  query.find_magic_methods()")
    print("  query.find_magic_methods(method_name='__str__')")
    print("  query.find_by_category('accessor')")
    print("  query.find_async_functions()")
    print()
    print("# Relationship Queries")
    print("  query.find_dependencies('dog')")
    print("  query.find_dependents('animal')")
    print("  query.find_inheritance('Dog', direction='base')")
    print("  query.find_inheritance('Animal', direction='derived')")
    print()
    print("# Statistics")
    print("  query.get_taxonomy_stats()")
    print("  query.get_summary()")
    print()
    print("# Result Operations")
    print("  result.filter(lambda n: n.metadata.get('is_async'))")
    print("  result.limit(10)")
    print("  result.sort_by('name')")
    print()
    print("# Formatting")
    print("  query.format_result(result, format='text')")
    print("  query.format_result(result, format='json')")
    print("  query.format_result(result, format='markdown')")
    print()
    print("=" * 70)
