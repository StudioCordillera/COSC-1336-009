"""
Integration Tests for Taxonomy Mapping

Tests that workers correctly categorize functions/methods using taxonomy mapper.
"""

import asyncio
import os
from pathlib import Path

# Import components
from api import InMemoryQueueStrategy, ModuleDiscoveryResult
from models import DatabaseSessionFactory, UnitOfWork
from workers import WorkerPool, LoggingWorkerObserver
from taxonomy import TaxonomyMapper


def create_test_module_with_various_functions():
    """Create test data with various function types"""
    
    module = ModuleDiscoveryResult(
        module_name='test_taxonomy',
        filepath='/fake/test_taxonomy.py',
        is_package=False,
        classes=[
            {
                'name': 'MyClass',
                'lineno': 1,
                'methods': ['__init__', '__str__', '__eq__', 'get_value', 'set_value', '_private', 'public_method'],
                'bases': [],
                'parent': None
            }
        ],
        functions=[
            # Constructor
            {
                'name': '__init__',
                'lineno': 2,
                'parent': 'MyClass',
                'is_async': False
            },
            # Magic methods
            {
                'name': '__str__',
                'lineno': 5,
                'parent': 'MyClass',
                'is_async': False
            },
            {
                'name': '__eq__',
                'lineno': 8,
                'parent': 'MyClass',
                'is_async': False
            },
            # Accessors
            {
                'name': 'get_value',
                'lineno': 11,
                'parent': 'MyClass',
                'is_async': False
            },
            {
                'name': 'set_value',
                'lineno': 14,
                'parent': 'MyClass',
                'is_async': False
            },
            # Visibility
            {
                'name': '_private',
                'lineno': 17,
                'parent': 'MyClass',
                'is_async': False
            },
            {
                'name': 'public_method',
                'lineno': 20,
                'parent': 'MyClass',
                'is_async': False
            },
            # Standalone async function
            {
                'name': 'async_task',
                'lineno': 23,
                'parent': None,
                'is_async': True
            },
            # Standalone function
            {
                'name': 'helper_function',
                'lineno': 26,
                'parent': None,
                'is_async': False
            },
        ],
        imports=[],
        checksum='tax123',
        discovered_at='2024-01-01T00:00:00',
        scanner_version='1.0.0'
    )
    
    return module


async def test_taxonomy_integration():
    """Test that taxonomy categorization works in full pipeline"""
    print("=" * 70)
    print("TEST: Taxonomy Integration with Workers")
    print("=" * 70)
    
    # Setup
    db_path = Path('test_taxonomy.db')
    if db_path.exists():
        os.remove(db_path)
    
    db_factory = DatabaseSessionFactory(f'sqlite:///{db_path}')
    db_factory.create_tables()
    
    queue = InMemoryQueueStrategy()
    
    # Enqueue test module
    test_module = create_test_module_with_various_functions()
    queue.enqueue(test_module, priority=1)
    
    print(f"\n✓ Enqueued module with {len(test_module.functions)} functions")
    
    # Create worker pool with taxonomy mapper
    taxonomy_mapper = TaxonomyMapper()
    observer = LoggingWorkerObserver()
    pool = WorkerPool(
        queue_strategy=queue,
        db_factory=db_factory,
        num_workers=1,
        observers=[observer],
        taxonomy_mapper=taxonomy_mapper
    )
    
    # Process module
    print("\n--- Starting worker ---\n")
    await pool.process_until_empty()
    
    # Verify results
    print("\n--- Verifying Taxonomy Categorization ---\n")
    
    with UnitOfWork(db_factory) as uow:
        # Check functions
        functions = uow.repositories['function'].get_all()
        print(f"✓ Functions created: {len(functions)}")
        
        # Check taxonomies
        taxonomies = uow.repositories['taxonomy'].get_all()
        print(f"✓ Taxonomy categories created: {len(taxonomies)}")
        
        for tax in taxonomies:
            print(f"  - {tax.category}")
            if tax.subcategory:
                print(f"    subcategory: {tax.subcategory}")
            if tax.pattern:
                print(f"    pattern: {tax.pattern}")
        
        # Check taxonomy relationships
        relationships = uow.repositories['relationship'].get_all()
        taxonomy_rels = [r for r in relationships if r.relationship_type == 'categorized_as']
        
        print(f"\n✓ Taxonomy relationships: {len(taxonomy_rels)}")
        
        # Map functions to their categories
        function_categories = {}
        for rel in taxonomy_rels:
            func = uow.repositories['function'].get_by_id(rel.from_id)
            tax = uow.repositories['taxonomy'].get_by_id(rel.to_id)
            if func and tax:
                function_categories[func.name] = tax.category
        
        print("\nFunction → Category Mapping:")
        for func_name, category in sorted(function_categories.items()):
            print(f"  {func_name:<20} → {category}")
        
        # Verify expected categorizations
        print("\n--- Validation ---\n")
        
        expected_mappings = {
            '__init__': 'constructor',
            '__str__': 'magic_method',
            '__eq__': 'comparison',
            'get_value': 'accessor',
            'set_value': 'mutator',
            '_private': 'protected_method',
            'public_method': 'public_method',
            'async_task': 'async_function',
        }
        
        all_correct = True
        for func_name, expected_category in expected_mappings.items():
            actual_category = function_categories.get(func_name)
            if actual_category == expected_category:
                print(f"✓ {func_name}: {expected_category}")
            else:
                print(f"❌ {func_name}: expected {expected_category}, got {actual_category}")
                all_correct = False
        
        assert all_correct, "Some categorizations were incorrect"
        assert len(taxonomy_rels) >= len(expected_mappings), f"Expected at least {len(expected_mappings)} categorizations, got {len(taxonomy_rels)}"
    
    print("\n" + "=" * 70)
    print("✅ ALL TESTS PASSED - Taxonomy integration works!")
    print("=" * 70)
    
    # Cleanup
    db_factory.engine.dispose()
    import time
    time.sleep(0.5)
    try:
        db_path.unlink()
    except PermissionError:
        print(f"⚠️ Could not delete {db_path} (still in use)")


async def test_taxonomy_deduplication():
    """Test that identical taxonomies are not duplicated"""
    print("\n" + "=" * 70)
    print("TEST: Taxonomy Deduplication")
    print("=" * 70)
    
    # Setup
    db_path = Path('test_tax_dedup.db')
    if db_path.exists():
        os.remove(db_path)
    
    db_factory = DatabaseSessionFactory(f'sqlite:///{db_path}')
    db_factory.create_tables()
    
    queue = InMemoryQueueStrategy()
    
    # Create two modules with same function patterns
    module1 = ModuleDiscoveryResult(
        module_name='module1',
        filepath='/fake/module1.py',
        is_package=False,
        classes=[
            {
                'name': 'Class1',
                'lineno': 1,
                'methods': ['__init__', 'get_value'],
                'bases': [],
                'parent': None
            }
        ],
        functions=[
            {'name': '__init__', 'lineno': 2, 'parent': 'Class1', 'is_async': False},
            {'name': 'get_value', 'lineno': 5, 'parent': 'Class1', 'is_async': False},
        ],
        imports=[],
        checksum='dup1',
        discovered_at='2024-01-01T00:00:00',
        scanner_version='1.0.0'
    )
    
    module2 = ModuleDiscoveryResult(
        module_name='module2',
        filepath='/fake/module2.py',
        is_package=False,
        classes=[
            {
                'name': 'Class2',
                'lineno': 1,
                'methods': ['__init__', 'get_value'],
                'bases': [],
                'parent': None
            }
        ],
        functions=[
            {'name': '__init__', 'lineno': 2, 'parent': 'Class2', 'is_async': False},
            {'name': 'get_value', 'lineno': 5, 'parent': 'Class2', 'is_async': False},
        ],
        imports=[],
        checksum='dup2',
        discovered_at='2024-01-01T00:00:00',
        scanner_version='1.0.0'
    )
    
    queue.enqueue(module1, priority=1)
    queue.enqueue(module2, priority=1)
    
    print(f"\n✓ Enqueued 2 modules with identical function patterns")
    
    # Process
    pool = WorkerPool(
        queue_strategy=queue,
        db_factory=db_factory,
        num_workers=1,
        observers=[LoggingWorkerObserver()],
        taxonomy_mapper=TaxonomyMapper()
    )
    
    print("\n--- Processing modules ---\n")
    await pool.process_until_empty()
    
    # Verify deduplication
    print("\n--- Verifying Deduplication ---\n")
    
    with UnitOfWork(db_factory) as uow:
        # Count functions (should be 4: 2 __init__, 2 get_value)
        functions = uow.repositories['function'].get_all()
        print(f"✓ Total functions: {len(functions)} (expected 4)")
        assert len(functions) == 4, f"Expected 4 functions, got {len(functions)}"
        
        # Count taxonomy categories (should be unique)
        taxonomies = uow.repositories['taxonomy'].get_all()
        print(f"✓ Unique taxonomy categories: {len(taxonomies)}")
        
        # Should have 2 unique patterns: constructor and accessor
        categories = set(t.category for t in taxonomies)
        print(f"  Categories: {categories}")
        
        # Count taxonomy relationships (should be 4: one per function)
        relationships = uow.repositories['relationship'].get_all()
        taxonomy_rels = [r for r in relationships if r.relationship_type == 'categorized_as']
        print(f"✓ Taxonomy relationships: {len(taxonomy_rels)} (expected 4)")
        assert len(taxonomy_rels) == 4, f"Expected 4 relationships, got {len(taxonomy_rels)}"
        
        # Verify no duplicate taxonomies
        taxonomy_signatures = set()
        for t in taxonomies:
            signature = (t.category, t.subcategory, t.pattern)
            assert signature not in taxonomy_signatures, f"Duplicate taxonomy found: {signature}"
            taxonomy_signatures.add(signature)
        
        print("✓ No duplicate taxonomies")
    
    print("\n✅ Deduplication works correctly!")
    print("=" * 70)
    
    # Cleanup
    db_factory.engine.dispose()
    import time
    time.sleep(0.5)
    try:
        db_path.unlink()
    except PermissionError:
        print(f"⚠️ Could not delete {db_path} (still in use)")


if __name__ == '__main__':
    # Run tests
    asyncio.run(test_taxonomy_integration())
    asyncio.run(test_taxonomy_deduplication())
    
    print("\n🎉 All taxonomy tests passed!")
