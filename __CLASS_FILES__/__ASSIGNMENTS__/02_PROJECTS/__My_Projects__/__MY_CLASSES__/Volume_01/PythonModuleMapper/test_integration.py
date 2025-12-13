"""
Integration Test: CLI Workflow
Tests the full CLI-driven workflow: Populate -> Query -> Generate Vault.
"""

import unittest
import tempfile
import shutil
import os
from pathlib import Path
import argparse
import asyncio
from typing import List

# Import CLI commands
from cli import PopulateCommand, GenerateVaultCommand, QueryCommand, ScanCommand
from models import DatabaseSessionFactory, UnitOfWork

class TestCLIIntegration(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        self.db_path = Path(self.test_dir) / "test_integration.db"
        self.vault_path = Path(self.test_dir) / "TestVault"
        
        # Ensure vault path doesn't exist yet (generator should create it or parts of it)
        # But generate_vault expects the root to exist or creates subdirs? 
        # Let's create the root
        self.vault_path.mkdir()
        
    def tearDown(self):
        # Remove temporary directory
        shutil.rmtree(self.test_dir)
        
    def test_full_workflow(self):
        print("\n" + "="*50)
        print("TESTING FULL CLI WORKFLOW")
        print("="*50)
        
        # 1. Populate Database
        print("\n[Step 1] Populating Database...")
        populate_cmd = PopulateCommand()
        args = argparse.Namespace(db=str(self.db_path))
        
        # Execute populate (this runs async code internally)
        populate_cmd.execute(args)
        
        # Verify DB exists
        self.assertTrue(self.db_path.exists(), "Database file should exist")
        
        # Verify DB content
        db_url = f"sqlite:///{self.db_path}"
        factory = DatabaseSessionFactory(db_url)
        with UnitOfWork(factory) as uow:
            modules = uow.repositories['module'].get_all()
            module_names = [m.name for m in modules]
            print(f"   Found modules: {module_names}")
            self.assertIn("json", module_names, "Module 'json' should be in database")
            self.assertIn("os", module_names, "Module 'os' should be in database")
            
            # Check for classes/functions
            classes = uow.repositories['class'].get_all()
            print(f"   Found {len(classes)} classes")
            self.assertGreater(len(classes), 0, "Should have discovered some classes")
            
    
        # 2. Query Database
        print("\n[Step 2] Querying Database...")
        query_cmd = QueryCommand()
        # Search for 'json'
        args = argparse.Namespace(
            term="json", 
            type="all", 
            format="text", 
            db=str(self.db_path)
        )
        
        # We can't easily capture stdout here without mocking, but we can ensure it runs without error
        try:
            query_cmd.execute(args)
            print("   Query executed successfully")
        except Exception as e:
            self.fail(f"Query command failed: {e}")
            
            
        # 3. Generate Vault
        print("\n[Step 3] Generating Vault...")
        gen_cmd = GenerateVaultCommand()
        args = argparse.Namespace(
            db=str(self.db_path),
            out=str(self.vault_path)
        )
        
        gen_cmd.execute(args)
        
        # Verify Vault Structure
        print(f"   Checking vault at {self.vault_path}")
        
        # Check directories
        for subdir in ["Modules", "Classes", "Functions", "Taxonomy"]:
            path = self.vault_path / subdir
            self.assertTrue(path.exists(), f"Directory {subdir} should exist")
            
        # Check specific files
        json_note = self.vault_path / "Modules" / "json.md"
        self.assertTrue(json_note.exists(), "json.md should exist")
        
        # Check content of a note
        with open(json_note, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn("# Module: json", content, "Note content should contain title")
            self.assertIn("## Overview", content, "Note content should contain Overview section")
            
        # Check Canvas files
        overview_canvas = self.vault_path / "Overview.canvas"
        self.assertTrue(overview_canvas.exists(), "Overview.canvas should exist")
        
        json_canvas = self.vault_path / "Modules" / "json.canvas"
        self.assertTrue(json_canvas.exists(), "json.canvas should exist")
        
        print("\n✅ Full workflow test passed!")

if __name__ == "__main__":
    unittest.main()
