"""
Integration Tests for Relationship Graph Builder

Tests graph traversal queries using relationship data from workers.
"""

import asyncio
import os
from pathlib import Path

# Import components
from api import InMemoryQueueStrategy, ModuleDiscoveryResult
from models import DatabaseSessionFactory
from workers import WorkerPool, LoggingWorkerObserver
from graph import RelationshipGraphBuilder


def create_test_data_with_complex_relationships():
    """Create test data with complex relationships for graph queries"""
    
    # Module 1: Base animal class
    animal = ModuleDiscoveryResult(
        module_name='animal',
        filepath='/fake/animal.py',
        is_package=False,
        classes=[
            {
                'name': 'Animal',
                'lineno': 1,
                'methods': ['__init__', '__str__', 'speak'],
                'bases': [],
                'parent': None
            }
        ],
        functions=[
            {'name': '__init__', 'lineno': 2, 'parent': 'Animal', 'is_async': False},
            {'name': '__str__', 'lineno': 5, 'parent': 'Animal', 'is_async': False},
            {'name': 'speak', 'lineno': 8, 'parent': 'Animal', 'is_async': False},
        ],
        imports=[],
        checksum='anim1',
        discovered_at='2024-01-01T00:00:00',
        scanner_version='1.0.0'
    )
    
    # Module 2: Dog inherits from Animal, imports animal
    dog = ModuleDiscoveryResult(
        module_name='dog',
        filepath='/fake/dog.py',
        is_package=False,
        classes=[
            {
                'name': 'Dog',
                'lineno': 3,
                'methods': ['__init__', 'bark', 'get_name'],
                'bases': ['Animal'],
                'parent': None
            }
        ],
        functions=[
            {'name': '__init__', 'lineno': 4, 'parent': 'Dog', 'is_async': False},
            {'name': 'bark', 'lineno': 7, 'parent': 'Dog', 'is_async': False},
            {'name': 'get_name', 'lineno': 10, 'parent': 'Dog', 'is_async': False},
        ],
        imports=['animal'],
        checksum='dog1',
        discovered_at='2024-01-01T00:00:00',
        scanner_version='1.0.0'
    )
    
    # Module 3: Cat inherits from Animal, imports animal
    cat = ModuleDiscoveryResult(
        module_name='cat',
        filepath='/fake/cat.py',
        is_package=False,
        classes=[
            {
                'name': 'Cat',
                'lineno': 3,
                'methods': ['__init__', 'meow', 'get_color'],
                'bases': ['Animal'],
                'parent': None
            }
        ],
        functions=[
            {'name': '__init__', 'lineno': 4, 'parent': 'Cat', 'is_async': False},
            {'name': 'meow', 'lineno': 7, 'parent': 'Cat', 'is_async': False},
            {'name': 'get_color', 'lineno': 10, 'parent': 'Cat', 'is_async': False},
        ],
        imports=['animal'],
        checksum='cat1',
        discovered_at='2024-01-01T00:00:00',
        scanner_version='1.0.0'
    )
    
    # Module 4: Pet store that imports both dog and cat
    pet_store = ModuleDiscoveryResult(
        module_name='pet_store',
        filepath='/fake/pet_store.py',
        is_package=False,
        classes=[],
        functions=[
            {'name': 'sell_pet', 'lineno': 1, 'parent': None, 'is_async': False},
            {'name': 'get_inventory', 'lineno': 5, 'parent': None, 'is_async': False},
            {'name': 'process_order', 'lineno': 10, 'parent': None, 'is_async': True},
        ],
        imports=['dog', 'cat'],
        checksum='store1',
        discovered_at='2024-01-01T00:00:00',
        scanner_version='1.0.0'
    )
    
    return [animal, dog, cat, pet_store]


async def test_dependency_queries():
    """Test module dependency queries"""
    print("=" * 70)
    print("TEST: Module Dependency Queries")
    print("=" * 70)
    
    # Setup database
    db_path = Path('test_graph.db')
    if db_path.exists():
        os.remove(db_path)
    
    db_factory = DatabaseSessionFactory(f'sqlite:///{db_path}')
    db_factory.create_tables()
    
    # Process test data
    queue = InMemoryQueueStrategy()
    test_modules = create_test_data_with_complex_relationships()
    for module in test_modules:
        queue.enqueue(module, priority=1)
    
    pool = WorkerPool(
        queue_strategy=queue,
        db_factory=db_factory,
        num_workers=1,
        observers=[LoggingWorkerObserver()]
    )
    
    print("\n--- Processing modules ---\n")
    await pool.process_until_empty()
    
    # Create graph builder
    graph = RelationshipGraphBuilder(db_factory)
    
    # Test dependency queries
    print("\n--- Testing Dependency Queries ---\n")
    
    # 1. Find what dog imports
    deps = graph.find_dependencies('dog')
    print(f"dog imports: {[d.name for d in deps]}")
    assert len(deps) == 1 and deps[0].name == 'animal', "dog should import animal"
    print("✓ find_dependencies('dog') correct")
    
    # 2. Find what depends on animal
    dependents = graph.find_dependents('animal')
    dependent_names = sorted([d.name for d in dependents])
    print(f"animal imported by: {dependent_names}")
    assert 'dog' in dependent_names and 'cat' in dependent_names, "animal should be imported by dog and cat"
    print("✓ find_dependents('animal') correct")
    
    # 3. Find what pet_store imports
    store_deps = graph.find_dependencies('pet_store')
    store_dep_names = sorted([d.name for d in store_deps])
    print(f"pet_store imports: {store_dep_names}")
    assert store_dep_names == ['cat', 'dog'], "pet_store should import cat and dog"
    print("✓ find_dependencies('pet_store') correct")
    
    # 4. Get dependency chain
    chain = graph.get_dependency_chain('pet_store', max_depth=5)
    print(f"\nDependency chains from pet_store: {len(chain)}")
    for i, path in enumerate(chain):
        print(f"  Chain {i+1}: {path.to_string()}")
    print(f"✓ get_dependency_chain found {len(chain)} paths")
    
    print("\n✅ All dependency queries passed!")
    
    # Cleanup
    db_factory.engine.dispose()
    import time
    time.sleep(0.5)
    try:
        db_path.unlink()
    except PermissionError:
        pass


async def test_inheritance_queries():
    """Test class inheritance queries"""
    print("\n" + "=" * 70)
    print("TEST: Class Inheritance Queries")
    print("=" * 70)
    
    # Setup
    db_path = Path('test_inheritance.db')
    if db_path.exists():
        os.remove(db_path)
    
    db_factory = DatabaseSessionFactory(f'sqlite:///{db_path}')
    db_factory.create_tables()
    
    # Process test data
    queue = InMemoryQueueStrategy()
    test_modules = create_test_data_with_complex_relationships()
    for module in test_modules:
        queue.enqueue(module, priority=1)
    
    pool = WorkerPool(
        queue_strategy=queue,
        db_factory=db_factory,
        num_workers=1,
        observers=[LoggingWorkerObserver()]
    )
    
    print("\n--- Processing modules ---\n")
    await pool.process_until_empty()
    
    # Create graph builder
    graph = RelationshipGraphBuilder(db_factory)
    
    # Test inheritance queries
    print("\n--- Testing Inheritance Queries ---\n")
    
    # 1. Find base classes of Dog
    dog_bases = graph.find_base_classes('Dog')
    print(f"Dog inherits from: {[b.name for b in dog_bases]}")
    assert len(dog_bases) == 1 and dog_bases[0].name == 'Animal', "Dog should inherit from Animal"
    print("✓ find_base_classes('Dog') correct")
    
    # 2. Find derived classes of Animal
    animal_derived = graph.find_derived_classes('Animal')
    derived_names = sorted([d.name for d in animal_derived])
    print(f"Animal inherited by: {derived_names}")
    assert derived_names == ['Cat', 'Dog'], "Animal should be inherited by Cat and Dog"
    print("✓ find_derived_classes('Animal') correct")
    
    # 3. Get inheritance tree
    tree = graph.get_inheritance_tree('Animal')
    print(f"\nInheritance tree for Animal:")
    print(f"  Base classes: {tree.get('base_tree', {})}")
    print(f"  Derived classes: {len(tree.get('derived_tree', {}).get('derived', []))} direct children")
    assert len(tree.get('derived_tree', {}).get('derived', [])) == 2, "Animal should have 2 derived classes"
    print("✓ get_inheritance_tree('Animal') correct")
    
    print("\n✅ All inheritance queries passed!")
    
    # Cleanup
    db_factory.engine.dispose()
    import time
    time.sleep(0.5)
    try:
        db_path.unlink()
    except PermissionError:
        pass


async def test_taxonomy_queries():
    """Test taxonomy category queries"""
    print("\n" + "=" * 70)
    print("TEST: Taxonomy Category Queries")
    print("=" * 70)
    
    # Setup
    db_path = Path('test_taxonomy_graph.db')
    if db_path.exists():
        os.remove(db_path)
    
    db_factory = DatabaseSessionFactory(f'sqlite:///{db_path}')
    db_factory.create_tables()
    
    # Process test data
    queue = InMemoryQueueStrategy()
    test_modules = create_test_data_with_complex_relationships()
    for module in test_modules:
        queue.enqueue(module, priority=1)
    
    pool = WorkerPool(
        queue_strategy=queue,
        db_factory=db_factory,
        num_workers=1,
        observers=[LoggingWorkerObserver()]
    )
    
    print("\n--- Processing modules ---\n")
    await pool.process_until_empty()
    
    # Create graph builder
    graph = RelationshipGraphBuilder(db_factory)
    
    # Test taxonomy queries
    print("\n--- Testing Taxonomy Queries ---\n")
    
    # 1. Find all constructors
    constructors = graph.find_all_constructors()
    constructor_info = [(c.name, c.metadata.get('class')) for c in constructors]
    print(f"Constructors found: {len(constructors)}")
    for name, cls in constructor_info:
        print(f"  - {name} in {cls}")
    assert len(constructors) >= 3, "Should find at least 3 __init__ methods"
    print("✓ find_all_constructors() correct")
    
    # 2. Find all magic methods
    magic = graph.find_all_magic_methods()
    print(f"\nMagic methods found: {len(magic)}")
    for m in magic:
        print(f"  - {m.name} in {m.metadata.get('class')} ({m.metadata.get('subcategory')})")
    assert len(magic) >= 1, "Should find at least 1 magic method (__str__)"
    print("✓ find_all_magic_methods() correct")
    
    # 3. Find accessors
    accessors = graph.find_by_category('accessor')
    print(f"\nAccessors found: {len(accessors)}")
    for a in accessors:
        print(f"  - {a.name} in {a.metadata.get('class') or 'module'}")
    assert len(accessors) >= 2, "Should find at least 2 get_* methods"
    print("✓ find_by_category('accessor') correct")
    
    # 4. Find async functions
    async_funcs = graph.find_all_async_functions()
    print(f"\nAsync functions found: {len(async_funcs)}")
    for af in async_funcs:
        print(f"  - {af.name} in {af.metadata.get('module')}")
    assert len(async_funcs) >= 1, "Should find at least 1 async function"
    print("✓ find_all_async_functions() correct")
    
    # 5. Get taxonomy distribution
    distribution = graph.get_taxonomy_distribution()
    print(f"\nTaxonomy distribution:")
    for category, count in sorted(distribution.items()):
        print(f"  {category}: {count}")
    assert len(distribution) > 0, "Should have taxonomy distribution"
    print("✓ get_taxonomy_distribution() correct")
    
    print("\n✅ All taxonomy queries passed!")
    
    # Cleanup
    db_factory.engine.dispose()
    import time
    time.sleep(0.5)
    try:
        db_path.unlink()
    except PermissionError:
        pass


async def test_cross_reference_queries():
    """Test cross-reference queries"""
    print("\n" + "=" * 70)
    print("TEST: Cross-Reference Queries")
    print("=" * 70)
    
    # Setup
    db_path = Path('test_xref.db')
    if db_path.exists():
        os.remove(db_path)
    
    db_factory = DatabaseSessionFactory(f'sqlite:///{db_path}')
    db_factory.create_tables()
    
    # Process test data
    queue = InMemoryQueueStrategy()
    test_modules = create_test_data_with_complex_relationships()
    for module in test_modules:
        queue.enqueue(module, priority=1)
    
    pool = WorkerPool(
        queue_strategy=queue,
        db_factory=db_factory,
        num_workers=1,
        observers=[LoggingWorkerObserver()]
    )
    
    print("\n--- Processing modules ---\n")
    await pool.process_until_empty()
    
    # Create graph builder
    graph = RelationshipGraphBuilder(db_factory)
    
    # Test cross-reference queries
    print("\n--- Testing Cross-Reference Queries ---\n")
    
    # 1. Find all uses of __init__
    init_uses = graph.find_all_uses_of('__init__')
    print(f"__init__ found as:")
    print(f"  - module: {len(init_uses['as_module'])}")
    print(f"  - class: {len(init_uses['as_class'])}")
    print(f"  - function: {len(init_uses['as_function'])}")
    for func in init_uses['as_function']:
        print(f"    • {func.metadata.get('class') or 'standalone'}.{func.name}")
    assert len(init_uses['as_function']) >= 3, "Should find at least 3 __init__ methods"
    print("✓ find_all_uses_of('__init__') correct")
    
    # 2. Find all uses of Animal (class name)
    animal_uses = graph.find_all_uses_of('Animal')
    print(f"\nAnimal found as:")
    print(f"  - module: {len(animal_uses['as_module'])}")
    print(f"  - class: {len(animal_uses['as_class'])}")
    print(f"  - function: {len(animal_uses['as_function'])}")
    assert len(animal_uses['as_class']) == 1, "Should find Animal class"
    print("✓ find_all_uses_of('Animal') correct (class)")
    
    # 3. Find all uses of animal (module name)
    animal_mod_uses = graph.find_all_uses_of('animal')
    print(f"\nanimal (module) found as:")
    print(f"  - module: {len(animal_mod_uses['as_module'])}")
    assert len(animal_mod_uses['as_module']) == 1, "Should find animal module"
    print("✓ find_all_uses_of('animal') correct (module)")
    
    print("\n✅ All cross-reference queries passed!")
    
    # Cleanup
    db_factory.engine.dispose()
    import time
    time.sleep(0.5)
    try:
        db_path.unlink()
    except PermissionError:
        pass


if __name__ == '__main__':
    # Run tests
    asyncio.run(test_dependency_queries())
    asyncio.run(test_inheritance_queries())
    asyncio.run(test_taxonomy_queries())
    asyncio.run(test_cross_reference_queries())
    
    print("\n" + "=" * 70)
    print("🎉 All graph traversal tests passed!")
    print("=" * 70)
