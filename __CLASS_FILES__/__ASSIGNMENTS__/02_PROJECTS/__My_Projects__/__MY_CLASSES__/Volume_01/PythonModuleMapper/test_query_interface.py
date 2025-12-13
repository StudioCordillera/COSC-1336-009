"""
Integration Tests for QueryInterface

Tests the user-facing query interface with real database operations.
Validates search methods, result formatting, and filtering operations.
"""

import unittest
import json
import asyncio
from pathlib import Path

# Import components
from models import DatabaseSessionFactory, Base
from api import InMemoryQueueStrategy, ModuleDiscoveryResult
from workers import QueueProcessor, WorkerPool
from taxonomy import TaxonomyMapper
from graph import RelationshipGraphBuilder
from query import QueryInterface, JSONFormatter, TextFormatter, MarkdownFormatter
from sqlalchemy import create_engine


class TestQueryInterface(unittest.TestCase):
    """
    Integration test suite for QueryInterface.
    
    Tests:
    1. Basic search methods (name, pattern, type)
    2. Taxonomy queries (constructors, magic methods, categories)
    3. Relationship queries (dependencies, inheritance)
    4. Result formatting (JSON, text, markdown)
    5. Result operations (filter, limit, sort)
    """
    
    @classmethod
    def setUpClass(cls):
        """Initialize test environment once"""
        # Create test database
        cls.db_path = Path(__file__).parent / "test_query.db"
        cls.db_url = f"sqlite:///{cls.db_path}"
        
        # Clean up old database
        if cls.db_path.exists():
            cls.db_path.unlink()
        
        # Initialize database
        engine = create_engine(cls.db_url)
        Base.metadata.create_all(engine)
        
        # Create components
        cls.session_factory = DatabaseSessionFactory(cls.db_url)
        cls.queue = InMemoryQueueStrategy()
        cls.taxonomy_mapper = TaxonomyMapper()
        cls.processor = QueueProcessor(
            queue_strategy=cls.queue,
            db_factory=cls.session_factory,
            taxonomy_mapper=cls.taxonomy_mapper
        )
        cls.graph_builder = RelationshipGraphBuilder(cls.session_factory)
        cls.query = QueryInterface(cls.graph_builder)
        
        # Create test data
        cls._create_test_data()
    
    @classmethod
    def _create_test_data(cls):
        """Create comprehensive test data with various constructs"""
        
        # Module 1: animal (base classes)
        animal = ModuleDiscoveryResult(
            module_name='animal',
            filepath='/fake/animal.py',
            is_package=False,
            classes=[
                {
                    'name': 'Animal',
                    'lineno': 3,
                    'methods': ['__init__', '__str__', '__eq__', 'get_name', 'set_name', 'is_alive'],
                    'bases': [],
                    'parent': None
                },
                {
                    'name': 'Bird',
                    'lineno': 20,
                    'methods': ['__init__', 'can_fly'],
                    'bases': ['Animal'],
                    'parent': None
                }
            ],
            functions=[
                {'name': '__init__', 'lineno': 4, 'parent': 'Animal', 'is_async': False},
                {'name': '__str__', 'lineno': 7, 'parent': 'Animal', 'is_async': False},
                {'name': '__eq__', 'lineno': 10, 'parent': 'Animal', 'is_async': False},
                {'name': 'get_name', 'lineno': 13, 'parent': 'Animal', 'is_async': False},
                {'name': 'set_name', 'lineno': 16, 'parent': 'Animal', 'is_async': False},
                {'name': 'is_alive', 'lineno': 19, 'parent': 'Animal', 'is_async': False},
                {'name': '__init__', 'lineno': 21, 'parent': 'Bird', 'is_async': False},
                {'name': 'can_fly', 'lineno': 25, 'parent': 'Bird', 'is_async': False},
            ],
            imports=[],
            checksum='abc1',
            discovered_at='2024-01-01T00:00:00',
            scanner_version='1.0.0'
        )
        
        # Module 2: dog (derived class with async)
        dog = ModuleDiscoveryResult(
            module_name='dog',
            filepath='/fake/dog.py',
            is_package=False,
            classes=[
                {
                    'name': 'Dog',
                    'lineno': 4,
                    'methods': ['__init__', '__repr__', 'get_breed', 'fetch_data'],
                    'bases': ['Animal'],
                    'parent': None
                },
                {
                    'name': 'ServiceDog',
                    'lineno': 18,
                    'methods': ['__init__', 'service_type'],
                    'bases': ['Dog'],
                    'parent': None
                }
            ],
            functions=[
                {'name': '__init__', 'lineno': 5, 'parent': 'Dog', 'is_async': False},
                {'name': '__repr__', 'lineno': 9, 'parent': 'Dog', 'is_async': False},
                {'name': 'get_breed', 'lineno': 12, 'parent': 'Dog', 'is_async': False},
                {'name': 'fetch_data', 'lineno': 15, 'parent': 'Dog', 'is_async': True},
                {'name': '__init__', 'lineno': 19, 'parent': 'ServiceDog', 'is_async': False},
                {'name': 'service_type', 'lineno': 24, 'parent': 'ServiceDog', 'is_async': False},
            ],
            imports=['animal'],
            checksum='abc2',
            discovered_at='2024-01-01T00:00:00',
            scanner_version='1.0.0'
        )
        
        # Module 3: cat (another derived class)
        cat = ModuleDiscoveryResult(
            module_name='cat',
            filepath='/fake/cat.py',
            is_package=False,
            classes=[
                {
                    'name': 'Cat',
                    'lineno': 4,
                    'methods': ['__init__', '__str__', 'get_color', 'has_claws'],
                    'bases': ['Animal'],
                    'parent': None
                }
            ],
            functions=[
                {'name': '__init__', 'lineno': 5, 'parent': 'Cat', 'is_async': False},
                {'name': '__str__', 'lineno': 9, 'parent': 'Cat', 'is_async': False},
                {'name': 'get_color', 'lineno': 12, 'parent': 'Cat', 'is_async': False},
                {'name': 'has_claws', 'lineno': 15, 'parent': 'Cat', 'is_async': False},
            ],
            imports=['animal'],
            checksum='abc3',
            discovered_at='2024-01-01T00:00:00',
            scanner_version='1.0.0'
        )
        
        # Module 4: pet_store (uses multiple modules)
        pet_store = ModuleDiscoveryResult(
            module_name='pet_store',
            filepath='/fake/pet_store.py',
            is_package=False,
            classes=[
                {
                    'name': 'PetStore',
                    'lineno': 5,
                    'methods': ['__init__', 'get_inventory', 'process_order', 'calculate_price'],
                    'bases': [],
                    'parent': None
                }
            ],
            functions=[
                {'name': '__init__', 'lineno': 6, 'parent': 'PetStore', 'is_async': False},
                {'name': 'get_inventory', 'lineno': 10, 'parent': 'PetStore', 'is_async': False},
                {'name': 'process_order', 'lineno': 13, 'parent': 'PetStore', 'is_async': True},
                {'name': 'calculate_price', 'lineno': 17, 'parent': 'PetStore', 'is_async': False},
            ],
            imports=['dog', 'cat', 'animal'],
            checksum='abc4',
            discovered_at='2024-01-01T00:00:00',
            scanner_version='1.0.0'
        )
        
        # Enqueue modules
        cls.queue.enqueue(animal)
        cls.queue.enqueue(dog)
        cls.queue.enqueue(cat)
        cls.queue.enqueue(pet_store)
        
        # Process queue
        pool = WorkerPool(
            queue_strategy=cls.queue,
            db_factory=cls.session_factory,
            num_workers=1,
            taxonomy_mapper=cls.taxonomy_mapper
        )
        asyncio.run(pool.process_until_empty())
    
    @classmethod
    def tearDownClass(cls):
        """Clean up test environment"""
        # Remove test database
        if cls.db_path.exists():
            cls.db_path.unlink()
    
    # ========================================================================
    # Test Basic Search Methods
    # ========================================================================
    
    def test_search_by_name_exact(self):
        """Test exact name search"""
        # Search for __init__
        result = self.query.search_by_name('__init__', exact=True)
        
        self.assertGreaterEqual(result.total_results, 4, "Should find at least 4 __init__ methods")
        self.assertTrue(all(n.name == '__init__' for n in result.results), "All results should be __init__")
    
    def test_search_by_name_substring(self):
        """Test substring name search"""
        # Search for 'Animal' (should find class and methods)
        result = self.query.search_by_name('Animal', exact=False)
        
        self.assertGreaterEqual(result.total_results, 1, "Should find Animal class")
        
        # Check that 'Animal' is in all result names
        for node in result.results:
            self.assertIn('animal', node.name.lower(), f"Result {node.name} should contain 'animal'")
    
    def test_search_by_pattern(self):
        """Test regex pattern search"""
        # Search for get_* methods
        result = self.query.search_by_pattern('^get_')
        
        self.assertGreaterEqual(result.total_results, 3, "Should find at least 3 get_ methods")
    
    # ========================================================================
    # Test Taxonomy Queries
    # ========================================================================
    
    def test_find_constructors(self):
        """Test finding all constructors"""
        result = self.query.find_constructors()
        
        self.assertGreaterEqual(result.total_results, 4, "Should find at least 4 constructors")
        
        # Verify all are __init__ methods
        for node in result.results:
            self.assertEqual(node.name, '__init__', "All constructors should be __init__")
            self.assertEqual(node.entity_type, 'function', "Should be function entities")
    
    def test_find_constructors_filtered(self):
        """Test finding constructors for specific class"""
        result = self.query.find_constructors(class_name='Dog')
        
        self.assertGreaterEqual(result.total_results, 1, "Should find Dog constructor")
        
        # Verify it's Dog's constructor
        for node in result.results:
            self.assertEqual(node.metadata.get('class'), 'Dog', "Should be Dog's constructor")
    
    def test_find_magic_methods(self):
        """Test finding all magic methods"""
        result = self.query.find_magic_methods()
        
        self.assertGreaterEqual(result.total_results, 2, "Should find at least 2 magic methods (__str__, __repr__, __eq__)")
    
    def test_find_magic_methods_filtered(self):
        """Test finding specific magic method"""
        result = self.query.find_magic_methods(method_name='__str__')
        
        self.assertGreaterEqual(result.total_results, 2, "Should find at least 2 __str__ methods (Animal, Cat)")
        
        # Verify all are __str__
        for node in result.results:
            self.assertEqual(node.name, '__str__', "All should be __str__ methods")
    
    def test_find_by_category_accessor(self):
        """Test finding accessors"""
        result = self.query.find_by_category('accessor')
        
        # Should find: get_name, get_breed, get_color, get_inventory
        self.assertGreaterEqual(result.total_results, 4, "Should find at least 4 accessor methods")
    
    def test_find_async_functions(self):
        """Test finding async functions"""
        result = self.query.find_async_functions()
        
        # Should find: fetch_data, process_order
        self.assertGreaterEqual(result.total_results, 2, "Should find at least 2 async functions")
        
        # Verify all are async
        for node in result.results:
            self.assertTrue(node.metadata.get('is_async'), "All should be async functions")
    
    # ========================================================================
    # Test Relationship Queries
    # ========================================================================
    
    def test_find_dependencies(self):
        """Test finding module dependencies"""
        result = self.query.find_dependencies('dog')
        
        # dog.py imports animal
        self.assertGreaterEqual(result.total_results, 1, "dog should import animal")
        
        # Check animal is in results
        module_names = [n.name for n in result.results]
        self.assertIn('animal', module_names, "Should find animal import")
    
    def test_find_dependents(self):
        """Test finding what imports a module"""
        result = self.query.find_dependents('animal')
        
        # animal is imported by dog, cat, pet_store
        self.assertGreaterEqual(result.total_results, 2, "animal should be imported by at least 2 modules")
        
        # Check dog and cat are in results
        module_names = [n.name for n in result.results]
        self.assertTrue(any(name in ['dog', 'cat', 'pet_store'] for name in module_names), 
                       "Should find dog, cat, or pet_store")
    
    def test_find_inheritance_derived(self):
        """Test finding derived classes"""
        result = self.query.find_inheritance('Animal', direction='derived')
        
        # Animal has Dog, Cat, Bird derived
        self.assertGreaterEqual(result.total_results, 2, "Animal should have at least 2 derived classes")
        
        # Check for Dog and Cat
        class_names = [n.name for n in result.results]
        self.assertTrue(any(name in ['Dog', 'Cat', 'Bird'] for name in class_names), 
                       "Should find Dog, Cat, or Bird")
    
    def test_find_inheritance_base(self):
        """Test finding base classes"""
        result = self.query.find_inheritance('Dog', direction='base')
        
        # Dog inherits from Animal
        self.assertGreaterEqual(result.total_results, 1, "Dog should inherit from Animal")
        
        # Check Animal is in results
        class_names = [n.name for n in result.results]
        self.assertIn('Animal', class_names, "Should find Animal base class")
    
    # ========================================================================
    # Test Statistics
    # ========================================================================
    
    def test_taxonomy_stats(self):
        """Test getting taxonomy distribution"""
        stats = self.query.get_taxonomy_stats()
        
        self.assertIsInstance(stats, dict, "Stats should be dictionary")
        self.assertGreater(len(stats), 0, "Should have taxonomy categories")
        
        # Check for expected categories
        self.assertIn('constructor', stats, "Should have constructor category")
        self.assertIn('accessor', stats, "Should have accessor category")
    
    def test_summary(self):
        """Test getting overall summary"""
        summary = self.query.get_summary()
        
        self.assertIn('taxonomy_categories', summary, "Summary should include category count")
        self.assertIn('total_categorized', summary, "Summary should include total count")
        self.assertIn('distribution', summary, "Summary should include distribution")
        
        self.assertGreater(summary['taxonomy_categories'], 0, "Should have categories")
        self.assertGreater(summary['total_categorized'], 0, "Should have categorized items")
    
    # ========================================================================
    # Test Result Operations
    # ========================================================================
    
    def test_result_filter(self):
        """Test filtering results"""
        # Get all constructors
        result = self.query.find_constructors()
        
        # Filter for Dog's constructor
        filtered = result.filter(lambda n: n.metadata.get('class') == 'Dog')
        
        self.assertLessEqual(filtered.total_results, result.total_results, "Filtered should have fewer or equal results")
        
        # Verify all are Dog's constructors
        for node in filtered.results:
            self.assertEqual(node.metadata.get('class'), 'Dog', "All should be Dog's constructor")
    
    def test_result_limit(self):
        """Test limiting results"""
        result = self.query.find_constructors()
        
        # Limit to 2
        limited = result.limit(2)
        
        self.assertEqual(len(limited.results), min(2, result.total_results), "Should limit to 2 results")
        self.assertIn('limit 2', limited.query, "Query should indicate limit")
    
    def test_result_sort(self):
        """Test sorting results"""
        result = self.query.find_constructors()
        
        if result.total_results > 1:
            # Sort by name
            sorted_result = result.sort_by('name')
            
            # Check results are sorted
            names = [n.name for n in sorted_result.results]
            self.assertEqual(names, sorted(names), "Results should be sorted by name")
    
    # ========================================================================
    # Test Result Formatting
    # ========================================================================
    
    def test_format_text(self):
        """Test text formatting"""
        result = self.query.find_constructors()
        
        text = self.query.format_result(result, format='text')
        
        self.assertIsInstance(text, str, "Should return string")
        self.assertIn('Query:', text, "Should include query")
        self.assertIn('Results:', text, "Should include result count")
        self.assertIn('[function]', text, "Should include entity type")
    
    def test_format_json(self):
        """Test JSON formatting"""
        result = self.query.find_constructors()
        
        json_str = self.query.format_result(result, format='json')
        
        # Parse JSON to validate
        data = json.loads(json_str)
        
        self.assertIn('query', data, "Should include query")
        self.assertIn('total_results', data, "Should include total")
        self.assertIn('results', data, "Should include results array")
        self.assertIsInstance(data['results'], list, "Results should be list")
    
    def test_format_markdown(self):
        """Test Markdown formatting"""
        result = self.query.find_constructors()
        
        markdown = self.query.format_result(result, format='markdown')
        
        self.assertIsInstance(markdown, str, "Should return string")
        self.assertIn('# Query Results:', markdown, "Should include heading")
        self.assertIn('**Total Results:**', markdown, "Should include result count")
        self.assertIn('### ', markdown, "Should include result headings")
        self.assertIn('**Type:**', markdown, "Should include entity type")


if __name__ == '__main__':
    print("=" * 70)
    print("Running QueryInterface Integration Tests")
    print("=" * 70)
    print()
    
    # Run tests with verbose output
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQueryInterface)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print()
    print("=" * 70)
    if result.wasSuccessful():
        print("✓ ALL TESTS PASSED")
    else:
        print("✗ SOME TESTS FAILED")
    print("=" * 70)
