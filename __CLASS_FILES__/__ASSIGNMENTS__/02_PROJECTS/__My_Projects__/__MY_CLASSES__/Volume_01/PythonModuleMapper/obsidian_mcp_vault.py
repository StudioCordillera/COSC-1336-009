"""
Obsidian Vault Generator with MCP Integration

Uses Obsidian MCP server to create notes directly in the vault.
Generates markdown files with frontmatter, WikiLinks, and organized structure.

Design Patterns:
- Builder Pattern: VaultBuilder for constructing vault structure
- Adapter Pattern: MCPAdapter wraps MCP server calls
- Template Method: Note templates for different entity types

All dependencies injected via constructors.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import requests
import json
import os
import urllib3

# Suppress InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Import database components
from models import DatabaseSessionFactory, UnitOfWork, Module, Class, Function
from obsidian_vault import (
    ModuleNoteTemplate, 
    ClassNoteTemplate, 
    FunctionNoteTemplate,
    NoteTemplate
)


# ============================================================================
# MCP Obsidian Integration
# ============================================================================

class ObsidianMCPVaultBuilder:
    """
    Builds Obsidian vault using MCP server integration.
    
    Uses the mcp_obsidian-mcp-_create_vault_file function to write notes
    directly to the vault through the Obsidian REST API.
    
    Dependency Injection:
    - session_factory: Database session factory
    """
    
    def __init__(self, session_factory: DatabaseSessionFactory):
        self.session_factory = session_factory
        
        # Templates
        self.module_template = ModuleNoteTemplate()
        self.class_template = ClassNoteTemplate()
        self.function_template = FunctionNoteTemplate()
        self.note_template = NoteTemplate()
        
        # Load Obsidian API Config
        self.api_key = None
        self.port = 27124 # Default
        self._load_api_config()

    def _load_api_config(self):
        try:
            # Try to find the config file in the standard location relative to this script
            # The vault is expected to be in ./PythonModules
            config_path = os.path.join(os.path.dirname(__file__), "PythonModules", ".obsidian", "plugins", "obsidian-local-rest-api", "data.json")
            
            if os.path.exists(config_path):
                with open(config_path, 'r') as f:
                    data = json.load(f)
                    self.api_key = data.get('apiKey')
                    self.port = data.get('port', 27124)
                    print(f"Loaded Obsidian API config: Port {self.port}")
            else:
                print(f"Warning: Obsidian API config not found at {config_path}")
                # Fallback to environment variables if needed
                self.api_key = os.environ.get("OBSIDIAN_API_KEY")
        except Exception as e:
            print(f"Error loading Obsidian API config: {e}")
        
        # Track created notes for reporting
        self.created_modules = 0
        self.created_classes = 0
        self.created_functions = 0
        self.created_taxonomy = 0
    
    def write_note(self, filename: str, content: str) -> bool:
        """
        Write note using Obsidian Local REST API.
        Returns True if successful, False otherwise.
        """
        if not self.api_key:
            print(f"Error: No API key available for Obsidian Local REST API. Cannot write {filename}")
            return False

        try:
            # Ensure filename doesn't start with /
            if filename.startswith('/'):
                filename = filename[1:]
                
            url = f"https://127.0.0.1:{self.port}/vault/{filename}"
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "text/markdown"
            }
            
            # We need to verify=False because of self-signed cert
            response = requests.put(url, data=content.encode('utf-8'), headers=headers, verify=False)
            
            if response.status_code in [200, 204, 201]:
                return True
            else:
                print(f"✗ Error writing {filename}: Status {response.status_code} - {response.text}")
                return False
        except Exception as e:
            print(f"✗ Error writing {filename}: {e}")
            return False
    
    def generate_module_notes(self) -> List[Dict[str, str]]:
        """Generate notes for all modules and return list of (filename, content) tuples"""
        notes = []
        
        with UnitOfWork(self.session_factory) as uow:
            modules = uow.repositories['module'].get_all()
            
            for module in modules:
                # Get related data
                classes = uow.repositories['class'].get_by_module(module.id)
                functions = uow.repositories['function'].get_by_module(module.id)
                
                # Get imports
                all_rels = uow.repositories['relationship'].get_all()
                import_rels = [r for r in all_rels 
                              if r.from_type == 'module' and r.from_id == module.id and r.relationship_type == 'imports']
                imports = []
                for rel in import_rels:
                    target = uow.repositories['module'].get_by_id(rel.to_id)
                    if target:
                        imports.append(target.name)
                
                # Get imported by
                imported_by_rels = [r for r in all_rels
                                   if r.to_type == 'module' and r.to_id == module.id and r.relationship_type == 'imports']
                imported_by = []
                for rel in imported_by_rels:
                    source = uow.repositories['module'].get_by_id(rel.from_id)
                    if source:
                        imported_by.append(source.name)
                
                # Generate content
                content = self.module_template.generate(
                    module, classes, functions, imports, imported_by
                )
                
                # Create filename
                filename = f"Modules/{self.module_template.sanitize_filename(module.name)}.md"
                
                notes.append({
                    'filename': filename,
                    'content': content,
                    'name': module.name
                })
        
        return notes
    
    def generate_class_notes(self) -> List[Dict[str, str]]:
        """Generate notes for all classes"""
        notes = []
        
        with UnitOfWork(self.session_factory) as uow:
            classes = uow.repositories['class'].get_all()
            all_rels = uow.repositories['relationship'].get_all()
            
            for cls in classes:
                # Get module
                module = uow.repositories['module'].get_by_id(cls.module_id)
                if not module:
                    continue
                
                # Get methods
                methods = uow.repositories['function'].get_by_class(cls.id)
                
                # Get base classes
                base_rels = [r for r in all_rels
                            if r.from_type == 'class' and r.from_id == cls.id and r.relationship_type == 'inherits']
                base_classes = []
                for rel in base_rels:
                    base = uow.repositories['class'].get_by_id(rel.to_id)
                    if base:
                        base_classes.append(base.name)
                
                # Get derived classes
                derived_rels = [r for r in all_rels
                               if r.to_type == 'class' and r.to_id == cls.id and r.relationship_type == 'inherits']
                derived_classes = []
                for rel in derived_rels:
                    derived = uow.repositories['class'].get_by_id(rel.from_id)
                    if derived:
                        derived_classes.append(derived.name)
                
                # Generate content
                content = self.class_template.generate(
                    cls, module, methods, base_classes, derived_classes
                )
                
                # Create filename
                filename = f"Classes/{self.class_template.sanitize_filename(cls.name)}.md"
                
                notes.append({
                    'filename': filename,
                    'content': content,
                    'name': cls.name
                })
        
        return notes
    
    def generate_function_notes(self) -> List[Dict[str, str]]:
        """Generate notes for all functions"""
        notes = []
        
        with UnitOfWork(self.session_factory) as uow:
            functions = uow.repositories['function'].get_all()
            all_rels = uow.repositories['relationship'].get_all()
            
            for func in functions:
                # Get module
                module = uow.repositories['module'].get_by_id(func.module_id)
                if not module:
                    continue
                
                # Get parent class if method
                parent_class = None
                if func.class_id:
                    parent_class = uow.repositories['class'].get_by_id(func.class_id)
                
                # Get taxonomy categories
                taxonomy_rels = [r for r in all_rels
                                if r.from_type == 'function' and r.from_id == func.id and r.relationship_type == 'categorized_as']
                categories = []
                for rel in taxonomy_rels:
                    taxonomy = uow.repositories['taxonomy'].get_by_id(rel.to_id)
                    if taxonomy:
                        categories.append(taxonomy.category)
                
                # Generate content
                content = self.function_template.generate(
                    func, module, parent_class, categories
                )
                
                # Create filename - use func.id for uniqueness
                filename = f"Functions/{self.function_template.sanitize_filename(func.name)}_{func.id}.md"
                
                notes.append({
                    'filename': filename,
                    'content': content,
                    'name': func.name
                })
        
        return notes
    
    def generate_taxonomy_notes(self) -> List[Dict[str, str]]:
        """Generate taxonomy category index notes"""
        notes = []
        
        with UnitOfWork(self.session_factory) as uow:
            # Get all taxonomy categories
            taxonomies = uow.repositories['taxonomy'].get_all()
            all_rels = uow.repositories['relationship'].get_all()
            
            # Group by category
            by_category: Dict[str, List] = {}
            for taxonomy in taxonomies:
                if taxonomy.category not in by_category:
                    by_category[taxonomy.category] = []
                by_category[taxonomy.category].append(taxonomy)
            
            # Create index note for each category
            for category, tax_list in by_category.items():
                content = []
                
                # Frontmatter
                content.append("---")
                content.append(f"type: taxonomy")
                content.append(f"category: {category}")
                content.append(f"tags: [python, taxonomy, {category}]")
                content.append("---")
                content.append("")
                
                # Title
                content.append(f"# Taxonomy: {category}")
                content.append("")
                
                # Description
                content.append("## Overview")
                content.append("")
                content.append(f"Functions categorized as `{category}`.")
                content.append("")
                
                # Find all functions with this category
                content.append("## Functions")
                content.append("")
                
                for taxonomy in tax_list:
                    # Find functions with this taxonomy
                    rels = [r for r in all_rels
                           if r.to_type == 'taxonomy' and r.to_id == taxonomy.id and r.relationship_type == 'categorized_as']
                    for rel in rels:
                        func = uow.repositories['function'].get_by_id(rel.from_id)
                        if func:
                            module = uow.repositories['module'].get_by_id(func.module_id)
                            module_name = module.name if module else "unknown"
                            content.append(f"- [[Functions/{func.name}_{func.id}|{func.name}]] (from {module_name})")
                
                content.append("")
                
                # Create filename
                filename = f"Taxonomy/{self.note_template.sanitize_filename(category)}.md"
                
                notes.append({
                    'filename': filename,
                    'content': "\n".join(content),
                    'name': category
                })
        
        return notes
    
    def get_all_notes(self) -> Dict[str, List[Dict[str, str]]]:
        """
        Generate all notes and return organized by type.
        Returns dict with 'modules', 'classes', 'functions', 'taxonomy' keys.
        """
        print("=" * 70)
        print("Generating Obsidian Vault Content")
        print("=" * 70)
        print()
        
        print("Generating module notes...")
        modules = self.generate_module_notes()
        print(f"✓ Generated {len(modules)} module notes")
        
        print("Generating class notes...")
        classes = self.generate_class_notes()
        print(f"✓ Generated {len(classes)} class notes")
        
        print("Generating function notes...")
        functions = self.generate_function_notes()
        print(f"✓ Generated {len(functions)} function notes")
        
        print("Generating taxonomy notes...")
        taxonomy = self.generate_taxonomy_notes()
        print(f"✓ Generated {len(taxonomy)} taxonomy notes")
        
        print()
        print("=" * 70)
        print(f"Total: {len(modules) + len(classes) + len(functions) + len(taxonomy)} notes ready")
        print("=" * 70)
        
        return {
            'modules': modules,
            'classes': classes,
            'functions': functions,
            'taxonomy': taxonomy
        }


# ============================================================================
# Example Usage
# ============================================================================

if __name__ == '__main__':
    from pathlib import Path
    
    # Configuration
    db_url = "sqlite:///python_modules.db"
    
    # Check if database exists
    db_path = Path("python_modules.db")
    if not db_path.exists():
        print("Error: Database not found. Please run the scanner first.")
        exit(1)
    
    # Create builder
    session_factory = DatabaseSessionFactory(db_url)
    builder = ObsidianMCPVaultBuilder(session_factory)
    
    # Generate all notes
    all_notes = builder.get_all_notes()
    
    print()
    print("Notes generated successfully!")
    print()
    print("To write to Obsidian vault, use the MCP integration:")
    print("- Call mcp_obsidian-mcp-_create_vault_file for each note")
    print()
    print(f"Module notes: {len(all_notes['modules'])}")
    print(f"Class notes: {len(all_notes['classes'])}")
    print(f"Function notes: {len(all_notes['functions'])}")
    print(f"Taxonomy notes: {len(all_notes['taxonomy'])}")
