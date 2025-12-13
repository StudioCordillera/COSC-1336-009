"""
Example Usage: Python Module Knowledge Graph
============================================
Demonstrates programmatic usage of the library components.
"""

import sys
from pathlib import Path
from models import DatabaseSessionFactory, UnitOfWork
from graph import RelationshipGraphBuilder
from query import QueryInterface

def example_1_query_database():
    """Example 1: Querying the database"""
    print("=" * 70)
    print("EXAMPLE 1: Querying Database")
    print("=" * 70)
    
    # Connect to database
    db_path = "python_modules.db"
    if not Path(db_path).exists():
        print(f"Database {db_path} not found. Run 'python cli.py populate' first.")
        return

    factory = DatabaseSessionFactory(f"sqlite:///{db_path}")
    graph = RelationshipGraphBuilder(factory)
    query = QueryInterface(graph)
    
    # Search for 'json'
    print("\nSearching for 'json':")
    results = query.search_by_name("json")
    for node in results.nodes:
        print(f"  - [{node.entity_type}] {node.name}")

def example_2_dependency_chain():
    """Example 2: Tracing dependencies"""
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Dependency Chain")
    print("=" * 70)
    
    db_path = "python_modules.db"
    if not Path(db_path).exists():
        return

    factory = DatabaseSessionFactory(f"sqlite:///{db_path}")
    graph = RelationshipGraphBuilder(factory)
    
    # Get dependencies for 'json'
    print("\nDependencies for 'json':")
    deps = graph.get_dependencies("json")
    for node in deps:
        print(f"  - {node.name}")

if __name__ == "__main__":
    example_1_query_database()
    example_2_dependency_chain()

