"""
Relationship Graph Builder

Traverses relationship network to answer queries about dependencies,
inheritance, and taxonomy categorization.

Design Patterns:
- Strategy Pattern: QueryStrategy for different query types
- Repository Pattern: Uses existing repositories for data access
- Builder Pattern: GraphQuery builder for complex queries

All dependencies injected via constructors.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, Dict, Any, Set, Tuple
from enum import Enum
from functools import lru_cache

# Import models
from models import (
    DatabaseSessionFactory, UnitOfWork,
    Module, Class, Function, Relationship, Taxonomy
)
from logger_config import get_logger

logger = get_logger("graph")


# ============================================================================
# Graph Node Types
# ============================================================================

@dataclass
class GraphNode:
    """Node in the relationship graph"""
    entity_type: str  # 'module', 'class', 'function', 'taxonomy'
    entity_id: int
    name: str
    metadata: Dict[str, Any]


@dataclass
class GraphEdge:
    """Edge in the relationship graph"""
    from_node: GraphNode
    to_node: GraphNode
    relationship_type: str  # 'imports', 'inherits', 'categorized_as', 'calls'
    metadata: Dict[str, Any]


@dataclass
class GraphPath:
    """Path through the graph"""
    nodes: List[GraphNode]
    edges: List[GraphEdge]
    
    def __len__(self):
        return len(self.nodes)
    
    def to_string(self) -> str:
        """Convert path to string representation"""
        if not self.nodes:
            return "Empty path"
        
        parts = [self.nodes[0].name]
        for i, edge in enumerate(self.edges):
            parts.append(f" --{edge.relationship_type}--> ")
            parts.append(self.nodes[i + 1].name)
        
        return "".join(parts)


# ============================================================================
# Graph Builder: Query and Traverse Relationships
# ============================================================================

class RelationshipGraphBuilder:
    """
    Builds and queries relationship graphs.
    
    Dependency Injection:
    - db_factory: Database session factory for repository access
    """
    
    def __init__(self, db_factory: DatabaseSessionFactory):
        self.db_factory = db_factory
    
    # ========================================================================
    # Module Dependency Queries
    # ========================================================================
    
    @lru_cache(maxsize=1024)
    def find_dependencies(self, module_name: str) -> List[GraphNode]:
        """
        Find all modules that this module imports.
        
        Args:
            module_name: Name of the module
            
        Returns:
            List of GraphNode objects representing imported modules
        """
        with UnitOfWork(self.db_factory) as uow:
            # Get module
            module = uow.repositories['module'].get_by_name(module_name)
            if not module:
                return []
            
            # Find import relationships
            # Optimized: Use get_relationships_from instead of get_all
            relationships = uow.repositories['relationship'].get_relationships_from(
                from_type='module', 
                from_id=module.id
            )
            
            imports = [
                r for r in relationships
                if r.relationship_type == 'imports'
            ]
            
            # Get imported modules
            result = []
            for rel in imports:
                imported_module = uow.repositories['module'].get_by_id(rel.to_id)
                if imported_module:
                    result.append(GraphNode(
                        entity_type='module',
                        entity_id=imported_module.id,
                        name=imported_module.name,
                        metadata={'filepath': imported_module.filepath}
                    ))
            
            return result
    
    @lru_cache(maxsize=1024)
    def find_dependents(self, module_name: str) -> List[GraphNode]:
        """
        Find all modules that import this module.
        
        Args:
            module_name: Name of the module
            
        Returns:
            List of GraphNode objects representing dependent modules
        """
        with UnitOfWork(self.db_factory) as uow:
            # Get module
            module = uow.repositories['module'].get_by_name(module_name)
            if not module:
                return []
            
            # Find import relationships pointing to this module
            # Optimized: Use get_relationships_to instead of get_all
            relationships = uow.repositories['relationship'].get_relationships_to(
                to_type='module',
                to_id=module.id
            )
            
            imports = [
                r for r in relationships
                if r.relationship_type == 'imports'
            ]
            
            # Get dependent modules
            result = []
            for rel in imports:
                dependent_module = uow.repositories['module'].get_by_id(rel.from_id)
                if dependent_module:
                    result.append(GraphNode(
                        entity_type='module',
                        entity_id=dependent_module.id,
                        name=dependent_module.name,
                        metadata={'filepath': dependent_module.filepath}
                    ))
            
            return result
    
    def get_dependency_chain(
        self,
        module_name: str,
        max_depth: int = 10
    ) -> List[GraphPath]:
        """
        Get full dependency chain (transitive dependencies).
        
        Args:
            module_name: Starting module
            max_depth: Maximum traversal depth
            
        Returns:
            List of paths showing dependency chains
        """
        logger.debug(f"Tracing dependency chain for {module_name} (depth={max_depth})")
        with UnitOfWork(self.db_factory) as uow:
            # Get starting module
            module = uow.repositories['module'].get_by_name(module_name)
            if not module:
                logger.warning(f"Module {module_name} not found")
                return []
            
            visited = set()
            paths = []
            
            def traverse(current_id: int, current_path: List[Tuple[int, str]], depth: int):
                if depth > max_depth or current_id in visited:
                    return
                
                visited.add(current_id)
                
                # Find dependencies
                relationships = uow.repositories['relationship'].get_all()
                imports = [
                    r for r in relationships
                    if r.from_type == 'module' and r.from_id == current_id
                    and r.relationship_type == 'imports'
                ]
                
                if not imports:
                    # Leaf node - save path
                    if len(current_path) > 1:
                        path_nodes = []
                        path_edges = []
                        
                        for i, (mod_id, mod_name) in enumerate(current_path):
                            mod = uow.repositories['module'].get_by_id(mod_id)
                            node = GraphNode(
                                entity_type='module',
                                entity_id=mod_id,
                                name=mod_name,
                                metadata={'filepath': mod.filepath if mod else 'unknown'}
                            )
                            path_nodes.append(node)
                            
                            if i > 0:
                                edge = GraphEdge(
                                    from_node=path_nodes[i-1],
                                    to_node=node,
                                    relationship_type='imports',
                                    metadata={}
                                )
                                path_edges.append(edge)
                        
                        paths.append(GraphPath(nodes=path_nodes, edges=path_edges))
                else:
                    # Continue traversal
                    for rel in imports:
                        imported_module = uow.repositories['module'].get_by_id(rel.to_id)
                        if imported_module:
                            traverse(
                                rel.to_id,
                                current_path + [(rel.to_id, imported_module.name)],
                                depth + 1
                            )
            
            # Start traversal
            traverse(module.id, [(module.id, module.name)], 0)
            
            return paths
    
    # ========================================================================
    # Class Inheritance Queries
    # ========================================================================
    
    def find_base_classes(self, class_name: str) -> List[GraphNode]:
        """
        Find all base classes that this class inherits from.
        
        Args:
            class_name: Name of the class
            
        Returns:
            List of GraphNode objects representing base classes
        """
        with UnitOfWork(self.db_factory) as uow:
            # Get all classes with this name
            classes = uow.repositories['class'].get_by_name(class_name)
            if not classes:
                return []
            
            # Use first match (TODO: improve resolution)
            cls = classes[0]
            
            # Find inheritance relationships
            relationships = uow.repositories['relationship'].get_all()
            inherits = [
                r for r in relationships
                if r.from_type == 'class' and r.from_id == cls.id
                and r.relationship_type == 'inherits'
            ]
            
            # Get base classes
            result = []
            for rel in inherits:
                base_class = uow.repositories['class'].get_by_id(rel.to_id)
                if base_class:
                    module = uow.repositories['module'].get_by_id(base_class.module_id)
                    result.append(GraphNode(
                        entity_type='class',
                        entity_id=base_class.id,
                        name=base_class.name,
                        metadata={
                            'module': module.name if module else 'unknown',
                            'lineno': base_class.lineno
                        }
                    ))
            
            return result
    
    def find_derived_classes(self, class_name: str) -> List[GraphNode]:
        """
        Find all classes that inherit from this class.
        
        Args:
            class_name: Name of the base class
            
        Returns:
            List of GraphNode objects representing derived classes
        """
        with UnitOfWork(self.db_factory) as uow:
            # Get all classes with this name
            classes = uow.repositories['class'].get_by_name(class_name)
            if not classes:
                return []
            
            # Use first match
            cls = classes[0]
            
            # Find inheritance relationships pointing to this class
            relationships = uow.repositories['relationship'].get_all()
            inherits = [
                r for r in relationships
                if r.to_type == 'class' and r.to_id == cls.id
                and r.relationship_type == 'inherits'
            ]
            
            # Get derived classes
            result = []
            for rel in inherits:
                derived_class = uow.repositories['class'].get_by_id(rel.from_id)
                if derived_class:
                    module = uow.repositories['module'].get_by_id(derived_class.module_id)
                    result.append(GraphNode(
                        entity_type='class',
                        entity_id=derived_class.id,
                        name=derived_class.name,
                        metadata={
                            'module': module.name if module else 'unknown',
                            'lineno': derived_class.lineno
                        }
                    ))
            
            return result
    
    def get_inheritance_tree(
        self,
        class_name: str,
        max_depth: int = 10
    ) -> Dict[str, Any]:
        """
        Get full inheritance hierarchy as tree structure.
        
        Args:
            class_name: Root class name
            max_depth: Maximum traversal depth
            
        Returns:
            Tree structure with base classes and derived classes
        """
        with UnitOfWork(self.db_factory) as uow:
            classes = uow.repositories['class'].get_by_name(class_name)
            if not classes:
                return {'error': 'Class not found'}
            
            cls = classes[0]
            module = uow.repositories['module'].get_by_id(cls.module_id)
            
            def build_tree(cls_id: int, depth: int, direction: str) -> Dict[str, Any]:
                if depth > max_depth:
                    return {}
                
                current_class = uow.repositories['class'].get_by_id(cls_id)
                if not current_class:
                    return {}
                
                current_module = uow.repositories['module'].get_by_id(current_class.module_id)
                
                tree = {
                    'name': current_class.name,
                    'module': current_module.name if current_module else 'unknown',
                    'lineno': current_class.lineno
                }
                
                # Get relationships based on direction
                relationships = uow.repositories['relationship'].get_all()
                
                if direction == 'bases':
                    # Find base classes
                    inherits = [
                        r for r in relationships
                        if r.from_type == 'class' and r.from_id == cls_id
                        and r.relationship_type == 'inherits'
                    ]
                    if inherits:
                        tree['bases'] = [
                            build_tree(r.to_id, depth + 1, direction)
                            for r in inherits
                        ]
                
                elif direction == 'derived':
                    # Find derived classes
                    inherits = [
                        r for r in relationships
                        if r.to_type == 'class' and r.to_id == cls_id
                        and r.relationship_type == 'inherits'
                    ]
                    if inherits:
                        tree['derived'] = [
                            build_tree(r.from_id, depth + 1, direction)
                            for r in inherits
                        ]
                
                return tree
            
            # Build tree in both directions
            result = {
                'class': cls.name,
                'module': module.name if module else 'unknown',
                'base_tree': build_tree(cls.id, 0, 'bases'),
                'derived_tree': build_tree(cls.id, 0, 'derived')
            }
            
            return result
    
    # ========================================================================
    # Taxonomy Queries
    # ========================================================================
    
    def find_by_category(self, category: str) -> List[GraphNode]:
        """
        Find all functions with a specific taxonomy category.
        
        Args:
            category: Taxonomy category (e.g., 'constructor', 'magic_method')
            
        Returns:
            List of GraphNode objects representing functions
        """
        with UnitOfWork(self.db_factory) as uow:
            # Find taxonomy entries with this category
            taxonomies = uow.repositories['taxonomy'].get_all()
            matching_taxonomies = [t for t in taxonomies if t.category == category]
            
            if not matching_taxonomies:
                return []
            
            # Find functions with these taxonomies
            result = []
            relationships = uow.repositories['relationship'].get_all()
            
            for taxonomy in matching_taxonomies:
                # Find relationships pointing to this taxonomy
                categorizations = [
                    r for r in relationships
                    if r.to_type == 'taxonomy' and r.to_id == taxonomy.id
                    and r.relationship_type == 'categorized_as'
                ]
                
                for rel in categorizations:
                    func = uow.repositories['function'].get_by_id(rel.from_id)
                    if func:
                        module = uow.repositories['module'].get_by_id(func.module_id)
                        parent_class = None
                        if func.class_id:
                            parent_class = uow.repositories['class'].get_by_id(func.class_id)
                        
                        result.append(GraphNode(
                            entity_type='function',
                            entity_id=func.id,
                            name=func.name,
                            metadata={
                                'module': module.name if module else 'unknown',
                                'class': parent_class.name if parent_class else None,
                                'is_method': func.is_method,
                                'is_async': func.is_async,
                                'taxonomy': taxonomy.category,
                                'subcategory': taxonomy.subcategory
                            }
                        ))
            
            return result
    
    def find_all_constructors(self) -> List[GraphNode]:
        """Find all constructors (__init__, __new__)"""
        return self.find_by_category('constructor')
    
    def find_all_magic_methods(self) -> List[GraphNode]:
        """Find all magic/dunder methods"""
        return self.find_by_category('magic_method')
    
    def find_all_properties(self) -> List[GraphNode]:
        """Find all @property methods"""
        return self.find_by_category('property')
    
    def find_all_async_functions(self) -> List[GraphNode]:
        """Find all async functions"""
        return self.find_by_category('async_function')
    
    @lru_cache(maxsize=128)
    def get_taxonomy_distribution(self) -> Dict[str, int]:
        """
        Get distribution of functions by taxonomy category.
        
        Returns:
            Dictionary mapping category to count
        """
        with UnitOfWork(self.db_factory) as uow:
            taxonomies = uow.repositories['taxonomy'].get_all()
            
            distribution = {}
            
            for taxonomy in taxonomies:
                category = taxonomy.category
                
                # Count functions with this taxonomy
                # Optimized: Use get_relationships_to instead of get_all
                categorizations = uow.repositories['relationship'].get_relationships_to(
                    to_type='taxonomy',
                    to_id=taxonomy.id
                )
                
                # Filter for 'categorized_as' relationship type
                count = sum(1 for r in categorizations if r.relationship_type == 'categorized_as')
                
                if category in distribution:
                    distribution[category] += count
                else:
                    distribution[category] = count
            
            return distribution
    
    # ========================================================================
    # Cross-Reference Queries
    # ========================================================================
    
    @lru_cache(maxsize=1024)
    def find_all_uses_of(self, construct_name: str) -> Dict[str, List[GraphNode]]:
        """
        Find all uses of a construct (module, class, or function).
        
        Args:
            construct_name: Name to search for
            
        Returns:
            Dictionary with keys 'as_module', 'as_class', 'as_function'
        """
        result = {
            'as_module': [],
            'as_class': [],
            'as_function': []
        }
        
        with UnitOfWork(self.db_factory) as uow:
            # Check if it's a module
            module = uow.repositories['module'].get_by_name(construct_name)
            if module:
                result['as_module'].append(GraphNode(
                    entity_type='module',
                    entity_id=module.id,
                    name=module.name,
                    metadata={
                        'filepath': module.filepath,
                        'is_package': module.is_package
                    }
                ))
            
            # Check if it's a class
            classes = uow.repositories['class'].get_by_name(construct_name)
            for cls in classes:
                mod = uow.repositories['module'].get_by_id(cls.module_id)
                result['as_class'].append(GraphNode(
                    entity_type='class',
                    entity_id=cls.id,
                    name=cls.name,
                    metadata={
                        'module': mod.name if mod else 'unknown',
                        'lineno': cls.lineno
                    }
                ))
            
            # Check if it's a function
            functions = uow.repositories['function'].get_by_name(construct_name)
            for func in functions:
                mod = uow.repositories['module'].get_by_id(func.module_id)
                parent_class = None
                if func.class_id:
                    parent_class = uow.repositories['class'].get_by_id(func.class_id)
                
                result['as_function'].append(GraphNode(
                    entity_type='function',
                    entity_id=func.id,
                    name=func.name,
                    metadata={
                        'module': mod.name if mod else 'unknown',
                        'class': parent_class.name if parent_class else None,
                        'is_method': func.is_method,
                        'lineno': func.lineno
                    }
                ))
        
        return result


    # ========================================================================
    # Visualization Queries
    # ========================================================================

    def get_full_graph(self) -> List[Dict[str, Any]]:
        """
        Get the full graph in Cytoscape.js format.
        """
        elements = []
        with UnitOfWork(self.db_factory) as uow:
            # Add Modules
            modules = uow.repositories['module'].get_all()
            for mod in modules:
                elements.append({
                    "data": {
                        "id": f"m_{mod.id}",
                        "label": mod.name,
                        "type": "module"
                    }
                })

            # Add Classes
            classes = uow.repositories['class'].get_all()
            for cls in classes:
                elements.append({
                    "data": {
                        "id": f"c_{cls.id}",
                        "label": cls.name,
                        "type": "class",
                        "parent": f"m_{cls.module_id}"
                    }
                })

            # Add Functions
            functions = uow.repositories['function'].get_all()
            for func in functions:
                elements.append({
                    "data": {
                        "id": f"f_{func.id}",
                        "label": func.name,
                        "type": "function",
                        "parent": f"m_{func.module_id}"
                    }
                })

            # Add Relationships
            relationships = uow.repositories['relationship'].get_all()
            for rel in relationships:
                source_prefix = {'module': 'm_', 'class': 'c_', 'function': 'f_'}.get(rel.from_type)
                target_prefix = {'module': 'm_', 'class': 'c_', 'function': 'f_'}.get(rel.to_type)
                
                if source_prefix and target_prefix:
                    elements.append({
                        "data": {
                            "id": f"r_{rel.id}",
                            "source": f"{source_prefix}{rel.from_id}",
                            "target": f"{target_prefix}{rel.to_id}",
                            "type": rel.relationship_type
                        }
                    })
                    
        return elements

    def search_graph(self, query: str) -> List[Dict[str, Any]]:
        """
        Search for nodes matching query and return them with 1-hop neighbors.
        """
        elements = []
        node_ids = set() # Set of (type, id) tuples
        
        with UnitOfWork(self.db_factory) as uow:
            # 1. Find matching entities
            matching_modules = [m for m in uow.repositories['module'].get_all() if query.lower() in m.name.lower()]
            matching_classes = [c for c in uow.repositories['class'].get_all() if query.lower() in c.name.lower()]
            matching_functions = [f for f in uow.repositories['function'].get_all() if query.lower() in f.name.lower()]
            
            for m in matching_modules: node_ids.add(('module', m.id))
            for c in matching_classes: node_ids.add(('class', c.id))
            for f in matching_functions: node_ids.add(('function', f.id))
            
            # 2. Find relationships connected to these nodes
            relationships = uow.repositories['relationship'].get_all()
            relevant_rels = []
            
            for rel in relationships:
                if (rel.from_type, rel.from_id) in node_ids or (rel.to_type, rel.to_id) in node_ids:
                    relevant_rels.append(rel)
                    node_ids.add((rel.from_type, rel.from_id))
                    node_ids.add((rel.to_type, rel.to_id))
            
            # 3. Construct elements
            # Add all identified nodes
            for type_, id_ in node_ids:
                if type_ == 'module':
                    m = uow.repositories['module'].get_by_id(id_)
                    if m: elements.append({"data": {"id": f"m_{m.id}", "label": m.name, "type": "module"}})
                elif type_ == 'class':
                    c = uow.repositories['class'].get_by_id(id_)
                    if c: elements.append({"data": {"id": f"c_{c.id}", "label": c.name, "type": "class", "parent": f"m_{c.module_id}"}})
                elif type_ == 'function':
                    f = uow.repositories['function'].get_by_id(id_)
                    if f: elements.append({"data": {"id": f"f_{f.id}", "label": f.name, "type": "function", "parent": f"m_{f.module_id}"}})

            # Add edges
            for rel in relevant_rels:
                source_prefix = {'module': 'm_', 'class': 'c_', 'function': 'f_'}.get(rel.from_type)
                target_prefix = {'module': 'm_', 'class': 'c_', 'function': 'f_'}.get(rel.to_type)
                if source_prefix and target_prefix:
                    elements.append({
                        "data": {
                            "id": f"r_{rel.id}",
                            "source": f"{source_prefix}{rel.from_id}",
                            "target": f"{target_prefix}{rel.to_id}",
                            "type": rel.relationship_type
                        }
                    })
                    
        return elements


# ============================================================================
# Example Usage
# ============================================================================

if __name__ == '__main__':
    from pathlib import Path
    
    # This would be used with actual database
    print("=" * 70)
    print("Relationship Graph Builder - Example Usage")
    print("=" * 70)
    print()
    print("Example queries:")
    print("  1. graph.find_dependencies('my_module')")
    print("  2. graph.find_dependents('base_module')")
    print("  3. graph.find_base_classes('DerivedClass')")
    print("  4. graph.find_derived_classes('BaseClass')")
    print("  5. graph.find_all_constructors()")
    print("  6. graph.find_by_category('magic_method')")
    print("  7. graph.get_inheritance_tree('MyClass')")
    print("  8. graph.get_dependency_chain('app')")
    print("  9. graph.find_all_uses_of('__init__')")
    print(" 10. graph.get_taxonomy_distribution()")
    print()
    print("=" * 70)
