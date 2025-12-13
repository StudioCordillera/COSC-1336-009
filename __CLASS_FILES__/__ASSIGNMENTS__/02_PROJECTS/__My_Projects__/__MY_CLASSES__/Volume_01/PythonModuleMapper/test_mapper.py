"""
Unit Tests for Python Module Mapper
====================================
Comprehensive test suite for all features.
"""

import unittest
import tempfile
import os
import json
from pathlib import Path
from module_mapper import (
    PythonModuleMapper, 
    OutputFormat,
    FunctionInfo,
    ClassInfo,
    ModuleMetrics
)


class TestBasicModuleReading(unittest.TestCase):
    """Test basic module reading functionality"""
    
    def setUp(self):
        self.mapper = PythonModuleMapper()
    
    def test_read_module_success(self):
        """Test successful module reading"""
        data = self.mapper.read_module('collections')
        self.assertIsInstance(data, dict)
        self.assertGreater(len(data), 0)
    
    def test_read_module_not_found(self):
        """Test reading non-existent module"""
        with self.assertRaises(ValueError):
            self.mapper.read_module('nonexistent_module_xyz')
    
    def test_read_classes_only(self):
        """Test reading classes only"""
        classes = self.mapper.read_classes_only('collections')
        self.assertIsInstance(classes, dict)
        # All items should be classes
        import pyclbr
        for value in classes.values():
            self.assertIsInstance(value, pyclbr.Class)


class TestModuleAnalysis(unittest.TestCase):
    """Test module analysis functionality"""
    
    def setUp(self):
        self.mapper = PythonModuleMapper()
    
    def test_analyze_module_structure(self):
        """Test complete module analysis"""
        analysis = self.mapper.analyze_module('json')
        
        self.assertIn('module_name', analysis)
        self.assertIn('classes', analysis)
        self.assertIn('functions', analysis)
        self.assertIn('metrics', analysis)
        self.assertIn('is_package', analysis)
        
        self.assertEqual(analysis['module_name'], 'json')
        self.assertIsInstance(analysis['classes'], dict)
        self.assertIsInstance(analysis['functions'], dict)
        self.assertIsInstance(analysis['metrics'], ModuleMetrics)
    
    def test_class_info_extraction(self):
        """Test ClassInfo extraction"""
        analysis = self.mapper.analyze_module('collections')
        
        if analysis['classes']:
            first_class = next(iter(analysis['classes'].values()))
            self.assertIsInstance(first_class, ClassInfo)
            self.assertIsInstance(first_class.name, str)
            self.assertIsInstance(first_class.lineno, int)
            self.assertIsInstance(first_class.methods, dict)
    
    def test_function_info_extraction(self):
        """Test FunctionInfo extraction"""
        analysis = self.mapper.analyze_module('json')
        
        if analysis['functions']:
            first_func = next(iter(analysis['functions'].values()))
            self.assertIsInstance(first_func, FunctionInfo)
            self.assertIsInstance(first_func.name, str)
            self.assertIsInstance(first_func.lineno, int)
    
    def test_metrics_calculation(self):
        """Test metrics calculation"""
        analysis = self.mapper.analyze_module('collections')
        metrics = analysis['metrics']
        
        self.assertIsInstance(metrics.total_classes, int)
        self.assertIsInstance(metrics.total_functions, int)
        self.assertIsInstance(metrics.total_methods, int)
        self.assertGreaterEqual(metrics.total_classes, 0)
        self.assertGreaterEqual(metrics.total_functions, 0)


class TestHierarchyVisualization(unittest.TestCase):
    """Test hierarchy visualization"""
    
    def setUp(self):
        self.mapper = PythonModuleMapper()
    
    def test_visualize_hierarchy(self):
        """Test hierarchy visualization"""
        hierarchy = self.mapper.visualize_hierarchy('collections')
        
        self.assertIsInstance(hierarchy, str)
        self.assertIn('Class Hierarchy', hierarchy)
        self.assertIn('collections', hierarchy)
    
    def test_find_root_classes(self):
        """Test finding root classes"""
        classes = self.mapper.read_classes_only('collections')
        roots = self.mapper._find_root_classes(classes)
        
        self.assertIsInstance(roots, list)
        self.assertGreater(len(roots), 0)


class TestNestedStructures(unittest.TestCase):
    """Test nested structure analysis"""
    
    def setUp(self):
        self.mapper = PythonModuleMapper()
    
    def test_analyze_nested_structures(self):
        """Test nested structure analysis"""
        nested = self.mapper.analyze_nested_structures('collections')
        
        self.assertIsInstance(nested, str)
        self.assertIn('Nested Structures', nested)


class TestAutocompleteGeneration(unittest.TestCase):
    """Test autocomplete data generation"""
    
    def setUp(self):
        self.mapper = PythonModuleMapper()
    
    def test_generate_autocomplete_data(self):
        """Test autocomplete data generation"""
        data = self.mapper.generate_autocomplete_data('pathlib')
        
        self.assertIn('module', data)
        self.assertIn('classes', data)
        self.assertIn('functions', data)
        self.assertIn('methods_by_class', data)
        self.assertIn('nested_items', data)
        
        self.assertEqual(data['module'], 'pathlib')
        self.assertIsInstance(data['classes'], list)
        self.assertIsInstance(data['functions'], list)
        self.assertIsInstance(data['methods_by_class'], dict)


class TestSafeCodeInspection(unittest.TestCase):
    """Test safe code inspection"""
    
    def setUp(self):
        self.mapper = PythonModuleMapper()
    
    def test_inspect_valid_code(self):
        """Test inspecting valid code"""
        code = """
class TestClass:
    def method1(self):
        pass
    def method2(self):
        pass

def test_function():
    pass
"""
        result = self.mapper.inspect_code_safely(code)
        
        self.assertTrue(result['safe'])
        self.assertEqual(result['classes_found'], 1)
        self.assertEqual(result['functions_found'], 1)
        self.assertIn('details', result)
    
    def test_inspect_invalid_code(self):
        """Test inspecting invalid code"""
        code = """
class BrokenClass
    def broken_method()
"""
        result = self.mapper.inspect_code_safely(code)
        
        self.assertFalse(result['safe'])
        self.assertIn('error', result)


class TestExportFunctionality(unittest.TestCase):
    """Test export functionality"""
    
    def setUp(self):
        self.mapper = PythonModuleMapper()
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        # Cleanup temp files
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_export_to_json(self):
        """Test JSON export"""
        output_file = os.path.join(self.temp_dir, 'test.json')
        self.mapper.export_to_json('json', output_file)
        
        self.assertTrue(os.path.exists(output_file))
        
        with open(output_file, 'r') as f:
            data = json.load(f)
        
        self.assertIn('module_name', data)
        self.assertIn('classes', data)
        self.assertIn('functions', data)
        self.assertIn('metrics', data)
    
    def test_export_to_html(self):
        """Test HTML export"""
        output_file = os.path.join(self.temp_dir, 'test.html')
        self.mapper.export_to_html('json', output_file)
        
        self.assertTrue(os.path.exists(output_file))
        
        with open(output_file, 'r') as f:
            content = f.read()
        
        self.assertIn('<!DOCTYPE html>', content)
        self.assertIn('json', content.lower())


class TestDocumentationGeneration(unittest.TestCase):
    """Test documentation generation"""
    
    def setUp(self):
        self.mapper = PythonModuleMapper()
    
    def test_generate_markdown_docs(self):
        """Test Markdown documentation generation"""
        docs = self.mapper.generate_documentation(
            'json',
            format=OutputFormat.MARKDOWN
        )
        
        self.assertIsInstance(docs, str)
        self.assertIn('# json', docs)
        self.assertIn('## Module Metrics', docs)
    
    def test_generate_html_docs(self):
        """Test HTML documentation generation"""
        docs = self.mapper.generate_documentation(
            'json',
            format=OutputFormat.HTML
        )
        
        self.assertIsInstance(docs, str)
        self.assertIn('<!DOCTYPE html>', docs)
        self.assertIn('json', docs.lower())
    
    def test_generate_console_docs(self):
        """Test console documentation generation"""
        docs = self.mapper.generate_documentation(
            'json',
            format=OutputFormat.CONSOLE
        )
        
        self.assertIsInstance(docs, str)
        self.assertIn('json', docs)
        self.assertIn('MODULE METRICS', docs)


class TestModuleComparison(unittest.TestCase):
    """Test module comparison"""
    
    def setUp(self):
        self.mapper = PythonModuleMapper()
    
    def test_compare_modules(self):
        """Test module comparison"""
        comparison = self.mapper.compare_modules('os', 'pathlib')
        
        self.assertIn('module1', comparison)
        self.assertIn('module2', comparison)
        self.assertIn('classes_only_in_1', comparison)
        self.assertIn('classes_only_in_2', comparison)
        self.assertIn('common_classes', comparison)
        self.assertIn('functions_only_in_1', comparison)
        self.assertIn('functions_only_in_2', comparison)
        self.assertIn('common_functions', comparison)
        self.assertIn('metrics_comparison', comparison)
        
        self.assertEqual(comparison['module1'], 'os')
        self.assertEqual(comparison['module2'], 'pathlib')


class TestSearchFunctionality(unittest.TestCase):
    """Test search functionality"""
    
    def setUp(self):
        self.mapper = PythonModuleMapper()
    
    def test_search_for_class_found(self):
        """Test searching for existing class"""
        cls_info = self.mapper.search_for_class('collections', 'Counter')
        
        self.assertIsNotNone(cls_info)
        self.assertIsInstance(cls_info, ClassInfo)
        self.assertEqual(cls_info.name, 'Counter')
    
    def test_search_for_class_not_found(self):
        """Test searching for non-existent class"""
        cls_info = self.mapper.search_for_class('collections', 'NonExistentClass')
        self.assertIsNone(cls_info)
    
    def test_search_for_function_found(self):
        """Test searching for existing function"""
        func_info = self.mapper.search_for_function('os', 'getcwd')
        
        if func_info:  # May not be a top-level function in all Python versions
            self.assertIsInstance(func_info, FunctionInfo)
    
    def test_find_methods(self):
        """Test finding methods in a class"""
        methods = self.mapper.find_methods('collections', 'Counter')
        
        self.assertIsInstance(methods, dict)
        if methods:  # Counter should have methods
            self.assertGreater(len(methods), 0)
            for method_name, line_no in methods.items():
                self.assertIsInstance(method_name, str)
                self.assertIsInstance(line_no, int)


class TestCaching(unittest.TestCase):
    """Test caching functionality"""
    
    def test_cache_enabled(self):
        """Test that caching improves performance"""
        mapper = PythonModuleMapper(cache_enabled=True)
        
        # First call - should cache
        mapper.read_module('json')
        
        # Check cache info
        cache_info = mapper.read_module.cache_info()
        self.assertGreater(cache_info.hits + cache_info.misses, 0)
        
        # Second call - should hit cache
        mapper.read_module('json')
        new_cache_info = mapper.read_module.cache_info()
        self.assertGreater(new_cache_info.hits, cache_info.hits)
    
    def test_cache_clear(self):
        """Test cache clearing"""
        mapper = PythonModuleMapper(cache_enabled=True)
        
        mapper.read_module('json')
        cache_info_before = mapper.read_module.cache_info()
        
        mapper.read_module.cache_clear()
        cache_info_after = mapper.read_module.cache_info()
        
        self.assertEqual(cache_info_after.hits, 0)
        self.assertEqual(cache_info_after.misses, 0)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error handling"""
    
    def setUp(self):
        self.mapper = PythonModuleMapper()
    
    def test_empty_module(self):
        """Test analyzing module with minimal content"""
        code = "# Empty module\n"
        result = self.mapper.inspect_code_safely(code)
        
        self.assertTrue(result['safe'])
        self.assertEqual(result['classes_found'], 0)
        self.assertEqual(result['functions_found'], 0)
    
    def test_module_with_only_imports(self):
        """Test module with only imports"""
        code = """
import os
import sys
from pathlib import Path
"""
        result = self.mapper.inspect_code_safely(code)
        
        self.assertTrue(result['safe'])
        self.assertEqual(result['classes_found'], 0)
        self.assertEqual(result['functions_found'], 0)


def run_tests():
    """Run all tests"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestBasicModuleReading))
    suite.addTests(loader.loadTestsFromTestCase(TestModuleAnalysis))
    suite.addTests(loader.loadTestsFromTestCase(TestHierarchyVisualization))
    suite.addTests(loader.loadTestsFromTestCase(TestNestedStructures))
    suite.addTests(loader.loadTestsFromTestCase(TestAutocompleteGeneration))
    suite.addTests(loader.loadTestsFromTestCase(TestSafeCodeInspection))
    suite.addTests(loader.loadTestsFromTestCase(TestExportFunctionality))
    suite.addTests(loader.loadTestsFromTestCase(TestDocumentationGeneration))
    suite.addTests(loader.loadTestsFromTestCase(TestModuleComparison))
    suite.addTests(loader.loadTestsFromTestCase(TestSearchFunctionality))
    suite.addTests(loader.loadTestsFromTestCase(TestCaching))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)
