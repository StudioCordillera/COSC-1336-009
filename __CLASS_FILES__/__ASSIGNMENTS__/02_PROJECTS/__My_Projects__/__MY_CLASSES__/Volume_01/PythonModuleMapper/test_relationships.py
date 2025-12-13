"""
Integration Tests for Relationship Tracking

Tests that workers correctly create relationship entries for:
- Imports (module→module)
- Inheritance (class→class)
- Method-to-class linking (function→class)
"""

import asyncio
import os
from pathlib import Path

# Import components
from api import InMemoryQueueStrategy, ModuleDiscoveryResult
from models import DatabaseSessionFactory, UnitOfWork
from workers import QueueProcessor, Worker, WorkerPool, LoggingWorkerObserver


def create_test_modules_with_relationships():
    """Create test data with imports and inheritance"""
    
    # Module 1: Base classes
    module1 = ModuleDiscoveryResult(
        module_name='animal',
        filepath='/fake/animal.py',
        is_package=False,
        classes=[
            {
                'name': 'Animal',
                'lineno': 1,
                'methods': ['__init__', 'speak'],
                'bases': [],  # No base classes
                'parent': None
            }
        ],
        functions=[
            {
                'name': '__init__',
                'lineno': 2,
                'parent': 'Animal',
                'is_async': False
            },
            {
                'name': 'speak',
                'lineno': 5,
                'parent': 'Animal',
                'is_async': False
            }
        ],
        imports=[],  # No imports
        checksum='abc123',
        discovered_at='2024-01-01T00:00:00',
        scanner_version='1.0.0'
    )
    
    # Module 2: Derived class with imports
    module2 = ModuleDiscoveryResult(
        module_name='dog',
        filepath='/fake/dog.py',
        is_package=False,
        classes=[
            {
                'name': 'Dog',
                'lineno': 3,
                'methods': ['__init__', 'bark'],
                'bases': ['Animal'],  # Inherits from Animal
                'parent': None
            }
        ],
        functions=[
            {
                'name': '__init__',
                'lineno': 4,
                'parent': 'Dog',
                'is_async': False
            },
            {
                'name': 'bark',
                'lineno': 7,
                'parent': 'Dog',
                'is_async': False
            }
        ],
        imports=['animal'],  # Imports animal module
        checksum='def456',
        discovered_at='2024-01-01T00:00:00',
        scanner_version='1.0.0'
    )
    
    # Module 3: Another derived class
    module3 = ModuleDiscoveryResult(
        module_name='cat',
        filepath='/fake/cat.py',
        is_package=False,
        classes=[
            {
                'name': 'Cat',
                'lineno': 3,
                'methods': ['__init__', 'meow'],
                'bases': ['Animal'],  # Also inherits from Animal
                'parent': None
            }
        ],
        functions=[
            {
                'name': '__init__',
                'lineno': 4,
                'parent': 'Cat',
                'is_async': False
            },
            {
                'name': 'meow',
                'lineno': 7,
                'parent': 'Cat',
                'is_async': False
            }
        ],
        imports=['animal'],  # Imports animal module
        checksum='ghi789',
        discovered_at='2024-01-01T00:00:00',
        scanner_version='1.0.0'
    )
    
    return [module1, module2, module3]


async def test_relationship_tracking():
    """Test that relationships are correctly tracked in database"""
    print("=" * 70)
    print("TEST: Relationship Tracking (Imports, Inheritance, Method Linking)")
    print("=" * 70)
    
    # Setup
    db_path = Path('test_relationships.db')
    if db_path.exists():
        os.remove(db_path)
    
    db_factory = DatabaseSessionFactory(f'sqlite:///{db_path}')
    db_factory.create_tables()
    
    queue = InMemoryQueueStrategy()
    
    # Enqueue test modules
    test_modules = create_test_modules_with_relationships()
    for module in test_modules:
        queue.enqueue(module, priority=1)
    
    print(f"\n✓ Enqueued {len(test_modules)} modules with relationships")
    
    # Create worker pool
    observer = LoggingWorkerObserver()
    pool = WorkerPool(
        queue_strategy=queue,
        db_factory=db_factory,
        num_workers=2,
        observers=[observer]
    )
    
    # Process all modules
    print("\n--- Starting workers ---\n")
    await pool.process_until_empty()
    
    # Verify results
    print("\n--- Verifying Relationships ---\n")
    
    with UnitOfWork(db_factory) as uow:
        # Check modules
        modules = uow.repositories['module'].get_all()
        print(f"✓ Modules created: {len(modules)}")
        for mod in modules:
            print(f"  - {mod.name}")
        
        # Check classes
        classes = uow.repositories['class'].get_all()
        print(f"\n✓ Classes created: {len(classes)}")
        for cls in classes:
            print(f"  - {cls.name} (module: {cls.module.name})")
        
        # Check functions (should be linked to classes)
        functions = uow.repositories['function'].get_all()
        print(f"\n✓ Functions created: {len(functions)}")
        methods = [f for f in functions if f.is_method]
        standalone = [f for f in functions if not f.is_method]
        print(f"  - Methods (linked to classes): {len(methods)}")
        for func in methods:
            print(f"    • {func.name} -> {func.parent_class.name if func.parent_class else 'ORPHANED'}")
        print(f"  - Standalone functions: {len(standalone)}")
        
        # Check relationships
        relationships = uow.repositories['relationship'].get_all()
        print(f"\n✓ Relationships created: {len(relationships)}")
        
        # Group by type
        imports = [r for r in relationships if r.relationship_type == 'imports']
        inherits = [r for r in relationships if r.relationship_type == 'inherits']
        
        print(f"\n  Import Relationships: {len(imports)}")
        for rel in imports:
            from_mod = uow.repositories['module'].get_by_id(rel.from_id)
            to_mod = uow.repositories['module'].get_by_id(rel.to_id)
            print(f"    • {from_mod.name} imports {to_mod.name}")
        
        print(f"\n  Inheritance Relationships: {len(inherits)}")
        for rel in inherits:
            from_cls = uow.repositories['class'].get_by_id(rel.from_id)
            to_cls = uow.repositories['class'].get_by_id(rel.to_id)
            print(f"    • {from_cls.name} inherits from {to_cls.name}")
        
        # Verify expected results
        print("\n--- Validation ---\n")
        
        assert len(modules) == 3, f"Expected 3 modules, got {len(modules)}"
        print("✓ Module count correct")
        
        assert len(classes) == 3, f"Expected 3 classes, got {len(classes)}"
        print("✓ Class count correct")
        
        assert len(methods) == 6, f"Expected 6 methods, got {len(methods)}"
        print("✓ Method count correct")
        
        assert len(imports) == 2, f"Expected 2 import relationships, got {len(imports)}"
        print("✓ Import relationship count correct")
        
        assert len(inherits) == 2, f"Expected 2 inheritance relationships, got {len(inherits)}"
        print("✓ Inheritance relationship count correct")
        
        # Verify methods are linked to classes
        orphaned = [f for f in methods if f.class_id is None]
        assert len(orphaned) == 0, f"Found {len(orphaned)} orphaned methods"
        print("✓ All methods linked to classes")
    
    print("\n" + "=" * 70)
    print("✅ ALL TESTS PASSED - Relationships tracked correctly!")
    print("=" * 70)
    
    # Cleanup (close connections first)
    db_factory.engine.dispose()
    import time
    time.sleep(0.5)
    try:
        db_path.unlink()
    except PermissionError:
        print(f"⚠️ Could not delete {db_path} (still in use)")


async def test_cross_module_inheritance():
    """Test inheritance relationships across modules"""
    print("\n" + "=" * 70)
    print("TEST: Cross-Module Inheritance Resolution")
    print("=" * 70)
    
    # Setup
    db_path = Path('test_cross_module.db')
    if db_path.exists():
        os.remove(db_path)
    
    db_factory = DatabaseSessionFactory(f'sqlite:///{db_path}')
    db_factory.create_tables()
    
    queue = InMemoryQueueStrategy()
    
    # Process modules in order (base first, then derived)
    test_modules = create_test_modules_with_relationships()
    for module in test_modules:
        queue.enqueue(module, priority=1)
    
    pool = WorkerPool(
        queue_strategy=queue,
        db_factory=db_factory,
        num_workers=1,  # Sequential processing
        observers=[LoggingWorkerObserver()]
    )
    
    print("\n--- Processing modules sequentially ---\n")
    await pool.process_until_empty()
    
    # Verify cross-module inheritance
    print("\n--- Verifying Cross-Module Inheritance ---\n")
    
    with UnitOfWork(db_factory) as uow:
        # Get Dog class
        dog_classes = uow.repositories['class'].get_by_name('Dog')
        assert len(dog_classes) > 0, "Dog class not found"
        dog_cls = dog_classes[0]
        
        # Get Cat class
        cat_classes = uow.repositories['class'].get_by_name('Cat')
        assert len(cat_classes) > 0, "Cat class not found"
        cat_cls = cat_classes[0]
        
        # Get Animal class
        animal_classes = uow.repositories['class'].get_by_name('Animal')
        assert len(animal_classes) > 0, "Animal class not found"
        animal_cls = animal_classes[0]
        
        # Find inheritance relationships
        dog_inherits = [r for r in uow.repositories['relationship'].get_all()
                        if r.from_id == dog_cls.id and r.relationship_type == 'inherits']
        cat_inherits = [r for r in uow.repositories['relationship'].get_all()
                        if r.from_id == cat_cls.id and r.relationship_type == 'inherits']
        
        assert len(dog_inherits) > 0, "Dog inheritance not tracked"
        assert dog_inherits[0].to_id == animal_cls.id, "Dog doesn't inherit from Animal"
        print(f"✓ Dog inherits from Animal (cross-module)")
        
        assert len(cat_inherits) > 0, "Cat inheritance not tracked"
        assert cat_inherits[0].to_id == animal_cls.id, "Cat doesn't inherit from Animal"
        print(f"✓ Cat inherits from Animal (cross-module)")
    
    print("\n✅ Cross-module inheritance resolution works!")
    print("=" * 70)
    
    # Cleanup (close connections first)
    db_factory.engine.dispose()
    import time
    time.sleep(0.5)
    try:
        db_path.unlink()
    except PermissionError:
        print(f"⚠️ Could not delete {db_path} (still in use)")


if __name__ == '__main__':
    # Run tests
    asyncio.run(test_relationship_tracking())
    asyncio.run(test_cross_module_inheritance())
    
    print("\n🎉 All relationship tests passed!")
