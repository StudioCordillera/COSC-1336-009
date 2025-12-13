"""
Test Obsidian Vault Generation with MCP

Creates test data and writes it to Obsidian vault using MCP server.
"""

import asyncio
from pathlib import Path
from sqlalchemy import create_engine

# Import components
from models import DatabaseSessionFactory, Base, UnitOfWork
from api import InMemoryQueueStrategy, ModuleDiscoveryResult
from workers import WorkerPool
from taxonomy import TaxonomyMapper
from obsidian_mcp_vault import ObsidianMCPVaultBuilder


def create_test_data():
    """Create test database with sample data"""
    print("=" * 70)
    print("Creating Test Database")
    print("=" * 70)
    print()
    
    # Create test database
    db_path = Path(__file__).parent / "test_obsidian.db"
    if db_path.exists():
        db_path.unlink()
    
    db_url = f"sqlite:///{db_path}"
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    
    # Create components
    session_factory = DatabaseSessionFactory(db_url)
    queue = InMemoryQueueStrategy()
    taxonomy_mapper = TaxonomyMapper()
    
    # Create test modules
    print("Creating test data...")
    
    # Module 1: shapes (base module)
    shapes = ModuleDiscoveryResult(
        module_name='shapes',
        filepath='/test/shapes.py',
        is_package=False,
        classes=[
            {
                'name': 'Shape',
                'lineno': 3,
                'methods': ['__init__', 'area', 'perimeter'],
                'bases': [],
                'parent': None
            },
            {
                'name': 'Circle',
                'lineno': 15,
                'methods': ['__init__', 'area', 'perimeter', 'get_radius'],
                'bases': ['Shape'],
                'parent': None
            }
        ],
        functions=[
            {'name': '__init__', 'lineno': 4, 'parent': 'Shape', 'is_async': False},
            {'name': 'area', 'lineno': 7, 'parent': 'Shape', 'is_async': False},
            {'name': 'perimeter', 'lineno': 10, 'parent': 'Shape', 'is_async': False},
            {'name': '__init__', 'lineno': 16, 'parent': 'Circle', 'is_async': False},
            {'name': 'area', 'lineno': 19, 'parent': 'Circle', 'is_async': False},
            {'name': 'perimeter', 'lineno': 22, 'parent': 'Circle', 'is_async': False},
            {'name': 'get_radius', 'lineno': 25, 'parent': 'Circle', 'is_async': False},
        ],
        imports=[],
        checksum='test1',
        discovered_at='2024-12-09T00:00:00',
        scanner_version='1.0.0'
    )
    
    # Module 2: geometry (uses shapes)
    geometry = ModuleDiscoveryResult(
        module_name='geometry',
        filepath='/test/geometry.py',
        is_package=False,
        classes=[
            {
                'name': 'Rectangle',
                'lineno': 5,
                'methods': ['__init__', '__str__', 'area', 'perimeter', 'is_square'],
                'bases': ['Shape'],
                'parent': None
            }
        ],
        functions=[
            {'name': '__init__', 'lineno': 6, 'parent': 'Rectangle', 'is_async': False},
            {'name': '__str__', 'lineno': 10, 'parent': 'Rectangle', 'is_async': False},
            {'name': 'area', 'lineno': 13, 'parent': 'Rectangle', 'is_async': False},
            {'name': 'perimeter', 'lineno': 16, 'parent': 'Rectangle', 'is_async': False},
            {'name': 'is_square', 'lineno': 19, 'parent': 'Rectangle', 'is_async': False},
            {'name': 'calculate_distance', 'lineno': 25, 'parent': None, 'is_async': False},
        ],
        imports=['shapes'],
        checksum='test2',
        discovered_at='2024-12-09T00:00:00',
        scanner_version='1.0.0'
    )
    
    # Module 3: async_geometry (async operations)
    async_geo = ModuleDiscoveryResult(
        module_name='async_geometry',
        filepath='/test/async_geometry.py',
        is_package=False,
        classes=[
            {
                'name': 'AsyncCalculator',
                'lineno': 5,
                'methods': ['__init__', 'calculate_area', 'process_shapes'],
                'bases': [],
                'parent': None
            }
        ],
        functions=[
            {'name': '__init__', 'lineno': 6, 'parent': 'AsyncCalculator', 'is_async': False},
            {'name': 'calculate_area', 'lineno': 9, 'parent': 'AsyncCalculator', 'is_async': True},
            {'name': 'process_shapes', 'lineno': 15, 'parent': 'AsyncCalculator', 'is_async': True},
        ],
        imports=['shapes', 'geometry'],
        checksum='test3',
        discovered_at='2024-12-09T00:00:00',
        scanner_version='1.0.0'
    )
    
    # Enqueue modules
    queue.enqueue(shapes)
    queue.enqueue(geometry)
    queue.enqueue(async_geo)
    
    # Process queue
    pool = WorkerPool(
        queue_strategy=queue,
        db_factory=session_factory,
        num_workers=1,
        taxonomy_mapper=taxonomy_mapper
    )
    asyncio.run(pool.process_until_empty())
    
    print("✓ Test data created")
    print()
    
    return db_url


def generate_vault_notes(db_url: str):
    """Generate all notes from database"""
    print("=" * 70)
    print("Generating Vault Notes")
    print("=" * 70)
    print()
    
    session_factory = DatabaseSessionFactory(db_url)
    builder = ObsidianMCPVaultBuilder(session_factory)
    
    # Generate all notes
    all_notes = builder.get_all_notes()
    
    # Write notes to Obsidian
    print()
    print("Writing notes to Obsidian...")
    
    total_written = 0
    total_failed = 0
    
    for category, notes in all_notes.items():
        print(f"Writing {category}...")
        for note in notes:
            if builder.write_note(note['filename'], note['content']):
                print(f"  ✓ {note['filename']}")
                total_written += 1
            else:
                print(f"  ✗ {note['filename']}")
                total_failed += 1
                
    print()
    print(f"Total written: {total_written}")
    print(f"Total failed: {total_failed}")
    
    return all_notes


def main():
    """Main test function"""
    print()
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 15 + "OBSIDIAN VAULT GENERATION TEST" + " " * 22 + "║")
    print("╚" + "=" * 68 + "╝")
    print()
    
    # Create test data
    db_url = create_test_data()
    
    # Generate notes
    all_notes = generate_vault_notes(db_url)
    
    # Display summary
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print(f"Module Notes: {len(all_notes['modules'])}")
    for note in all_notes['modules']:
        print(f"  - {note['filename']}")
    print()
    
    print(f"Class Notes: {len(all_notes['classes'])}")
    for note in all_notes['classes']:
        print(f"  - {note['filename']}")
    print()
    
    print(f"Function Notes: {len(all_notes['functions'])}")
    for note in all_notes['functions'][:5]:  # Show first 5
        print(f"  - {note['filename']}")
    if len(all_notes['functions']) > 5:
        print(f"  ... and {len(all_notes['functions']) - 5} more")
    print()
    
    print(f"Taxonomy Notes: {len(all_notes['taxonomy'])}")
    for note in all_notes['taxonomy']:
        print(f"  - {note['filename']}")
    print()
    
    print("=" * 70)
    print("✓ Test Complete!")
    print("=" * 70)
    print()
    print("Next: Use MCP integration to write these notes to Obsidian vault")
    print()
    
    return all_notes


if __name__ == '__main__':
    notes = main()
    
    # Show sample note
    print()
    print("=" * 70)
    print("SAMPLE NOTE (Module: shapes)")
    print("=" * 70)
    print()
    if notes['modules']:
        print(notes['modules'][0]['content'])
