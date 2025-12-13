"""
Obsidian Vault Generator

Creates and maintains an Obsidian knowledge vault from the database.
Generates markdown files with frontmatter, WikiLinks, and organized structure.

Design Patterns:
- Builder Pattern: VaultBuilder for constructing vault structure
- Template Method: Note templates for different entity types
- Strategy Pattern: Different link generation strategies
- Factory Pattern: NoteFactory creates appropriate note types

All dependencies injected via constructors.
"""

from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime
import re
import json
import logging

# Import database components
from models import DatabaseSessionFactory, UnitOfWork, Module, Class, Function


# ============================================================================
# Vault Configuration
# ============================================================================

@dataclass
class VaultConfig:
    """Configuration for Obsidian vault structure"""
    root_path: Path
    modules_dir: str = "Modules"
    classes_dir: str = "Classes"
    functions_dir: str = "Functions"
    taxonomy_dir: str = "Taxonomy"
    relationships_dir: str = "Relationships"
    
    def get_modules_path(self) -> Path:
        return self.root_path / self.modules_dir
    
    def get_classes_path(self) -> Path:
        return self.root_path / self.classes_dir
    
    def get_functions_path(self) -> Path:
        return self.root_path / self.functions_dir
    
    def get_taxonomy_path(self) -> Path:
        return self.root_path / self.taxonomy_dir
    
    def get_relationships_path(self) -> Path:
        return self.root_path / self.relationships_dir


# ============================================================================
# Note Templates
# ============================================================================

class NoteTemplate:
    """Base template for Obsidian notes"""
    
    def generate_frontmatter(self, metadata: Dict[str, Any]) -> str:
        """Generate YAML frontmatter"""
        lines = ["---"]
        for key, value in metadata.items():
            if isinstance(value, list):
                lines.append(f"{key}:")
                for item in value:
                    lines.append(f"  - {item}")
            else:
                lines.append(f"{key}: {value}")
        lines.append("---")
        return "\n".join(lines)
    
    def sanitize_filename(self, name: str) -> str:
        """Sanitize name for filename"""
        # Replace invalid characters
        safe = re.sub(r'[<>:"/\\|?*]', '_', name)
        # Remove leading/trailing spaces and dots
        safe = safe.strip('. ')
        return safe
    
    def create_wikilink(self, target: str, display: Optional[str] = None) -> str:
        """Create Obsidian WikiLink"""
        if display:
            return f"[[{target}|{display}]]"
        return f"[[{target}]]"


class ModuleNoteTemplate(NoteTemplate):
    """Template for module notes"""
    
    def generate(self, module: Module, classes: List[Class], functions: List[Function],
                 imports: List[str], imported_by: List[str]) -> str:
        """Generate module note content"""
        
        # Frontmatter
        metadata = {
            'type': 'module',
            'name': module.name,
            'filepath': module.filepath,
            'is_package': module.is_package,
            'analyzed_at': module.analyzed_at.isoformat() if module.analyzed_at else None,
            'tags': ['python', 'module']
        }
        content = [self.generate_frontmatter(metadata)]
        content.append("")
        
        # Title
        content.append(f"# Module: {module.name}")
        content.append("")
        
        # Overview
        content.append("## Overview")
        content.append("")
        if module.docstring:
            content.append(module.docstring)
            content.append("")
        content.append(f"**Filepath:** `{module.filepath}`")
        content.append(f"**Type:** {'Package' if module.is_package else 'Module'}")
        content.append(f"**Analyzed:** {module.analyzed_at.strftime('%Y-%m-%d %H:%M:%S') if module.analyzed_at else 'Unknown'}")
        content.append("")
        
        # Imports
        if imports:
            content.append("## Dependencies")
            content.append("")
            content.append("This module imports:")
            for imp in imports:
                content.append(f"- {self.create_wikilink(f'Modules/{imp}', imp)}")
            content.append("")
        
        # Imported By
        if imported_by:
            content.append("## Used By")
            content.append("")
            content.append("This module is imported by:")
            for imp in imported_by:
                content.append(f"- {self.create_wikilink(f'Modules/{imp}', imp)}")
            content.append("")
        
        # Classes
        if classes:
            content.append("## Classes")
            content.append("")
            for cls in classes:
                content.append(f"- {self.create_wikilink(f'Classes/{cls.name}', cls.name)} (line {cls.lineno})")
            content.append("")
        
        # Functions
        if functions:
            content.append("## Functions")
            content.append("")
            for func in functions:
                if not func.class_id:  # Module-level functions only
                    async_marker = "async " if func.is_async else ""
                    # Use ID in filename to ensure uniqueness
                    content.append(f"- {self.create_wikilink(f'Functions/{func.name}_{func.id}', f'{async_marker}{func.name}()')} (line {func.lineno})")
            content.append("")
        
        return "\n".join(content)


class ClassNoteTemplate(NoteTemplate):
    """Template for class notes"""
    
    def generate(self, cls: Class, module: Module, methods: List[Function],
                 base_classes: List[str], derived_classes: List[str]) -> str:
        """Generate class note content"""
        
        # Frontmatter
        metadata = {
            'type': 'class',
            'name': cls.name,
            'module': module.name,
            'lineno': cls.lineno,
            'tags': ['python', 'class']
        }
        content = [self.generate_frontmatter(metadata)]
        content.append("")
        
        # Title
        content.append(f"# Class: {cls.name}")
        content.append("")
        
        # Overview
        content.append("## Overview")
        content.append("")
        if cls.docstring:
            content.append(cls.docstring)
            content.append("")
        content.append(f"**Module:** {self.create_wikilink(f'Modules/{module.name}', module.name)}")
        content.append(f"**Line:** {cls.lineno}")
        content.append("")
        
        # Inheritance
        if base_classes or derived_classes:
            content.append("## Inheritance")
            content.append("")
            
            if base_classes:
                content.append("**Inherits from:**")
                for base in base_classes:
                    content.append(f"- {self.create_wikilink(f'Classes/{base}', base)}")
                content.append("")
            
            if derived_classes:
                content.append("**Subclasses:**")
                for derived in derived_classes:
                    content.append(f"- {self.create_wikilink(f'Classes/{derived}', derived)}")
                content.append("")
        
        # Methods
        if methods:
            content.append("## Methods")
            content.append("")
            
            # Group by category
            constructors = [m for m in methods if m.name in ['__init__', '__new__', '__del__']]
            magic = [m for m in methods if m.name.startswith('__') and m.name.endswith('__') and m not in constructors]
            regular = [m for m in methods if m not in constructors and m not in magic]
            
            if constructors:
                content.append("### Constructors")
                for method in constructors:
                    async_marker = "async " if method.is_async else ""
                    content.append(f"- {self.create_wikilink(f'Functions/{method.name}_{method.id}', f'{async_marker}{method.name}()')} (line {method.lineno})")
                content.append("")
            
            if magic:
                content.append("### Magic Methods")
                for method in magic:
                    content.append(f"- {self.create_wikilink(f'Functions/{method.name}_{method.id}', f'{method.name}()')} (line {method.lineno})")
                content.append("")
            
            if regular:
                content.append("### Methods")
                for method in regular:
                    async_marker = "async " if method.is_async else ""
                    content.append(f"- {self.create_wikilink(f'Functions/{method.name}_{method.id}', f'{async_marker}{method.name}()')} (line {method.lineno})")
                content.append("")
        
        return "\n".join(content)


class FunctionNoteTemplate(NoteTemplate):
    """Template for function notes"""
    
    def generate(self, func: Function, module: Module, parent_class: Optional[Class],
                 taxonomy_categories: List[str]) -> str:
        """Generate function note content"""
        
        # Frontmatter
        metadata = {
            'type': 'function',
            'name': func.name,
            'module': module.name,
            'lineno': func.lineno,
            'is_async': func.is_async,
            'is_method': func.class_id is not None,
            'tags': ['python', 'function']
        }
        
        if taxonomy_categories:
            metadata['categories'] = taxonomy_categories
        
        content = [self.generate_frontmatter(metadata)]
        content.append("")
        
        # Title
        async_marker = "async " if func.is_async else ""
        content.append(f"# Function: {async_marker}{func.name}()")
        content.append("")
        
        # Overview
        content.append("## Overview")
        content.append("")
        
        if func.docstring:
            content.append(func.docstring)
            content.append("")
            
        # Signature
        args_list = []
        if func.args:
            try:
                args_data = json.loads(func.args)
                for arg in args_data:
                    arg_str = arg['name']
                    if 'type' in arg:
                        arg_str += f": {arg['type']}"
                    args_list.append(arg_str)
            except json.JSONDecodeError:
                pass
        
        signature = f"def {func.name}({', '.join(args_list)})"
        if func.returns:
            signature += f" -> {func.returns}"
        
        content.append("```python")
        if func.decorators:
            try:
                decorators = json.loads(func.decorators)
                for dec in decorators:
                    content.append(f"@{dec}")
            except json.JSONDecodeError:
                pass
        content.append(signature)
        content.append("```")
        content.append("")
        
        content.append(f"**Module:** {self.create_wikilink(f'Modules/{module.name}', module.name)}")
        
        if parent_class:
            content.append(f"**Class:** {self.create_wikilink(f'Classes/{parent_class.name}', parent_class.name)}")
            content.append(f"**Type:** Method")
        else:
            content.append(f"**Type:** Module-level function")
        
        content.append(f"**Line:** {func.lineno}")
        
        if func.is_async:
            content.append(f"**Async:** Yes (coroutine)")
        
        content.append("")
        
        # Taxonomy
        if taxonomy_categories:
            content.append("## Categories")
            content.append("")
            for category in taxonomy_categories:
                content.append(f"- {self.create_wikilink(f'Taxonomy/{category}', category)}")
            content.append("")
        
        return "\n".join(content)


# ============================================================================
# Vault Builder
# ============================================================================

class ObsidianVaultBuilder:
    """
    Builds Obsidian vault structure from database.
    
    Dependency Injection:
    - config: VaultConfig with paths
    - session_factory: Database session factory
    """
    
    def __init__(
        self,
        config: VaultConfig,
        session_factory: DatabaseSessionFactory
    ):
        self.config = config
        self.session_factory = session_factory
        
        # Templates
        self.module_template = ModuleNoteTemplate()
        self.class_template = ClassNoteTemplate()
        self.function_template = FunctionNoteTemplate()
    
    def initialize_vault(self):
        """Create vault directory structure"""
        self.config.root_path.mkdir(parents=True, exist_ok=True)
        self.config.get_modules_path().mkdir(exist_ok=True)
        self.config.get_classes_path().mkdir(exist_ok=True)
        self.config.get_functions_path().mkdir(exist_ok=True)
        self.config.get_taxonomy_path().mkdir(exist_ok=True)
        self.config.get_relationships_path().mkdir(exist_ok=True)
    
    def write_note(self, path: Path, content: str):
        """Write note to file"""
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')
    
    def generate_module_notes(self):
        """Generate notes for all modules"""
        with self.session_factory.create_session() as session:
            uow = UnitOfWork(session)
            
            modules = uow.modules.get_all()
            
            for module in modules:
                # Get related data
                classes = uow.classes.find_by_module(module.id)
                functions = uow.functions.find_by_module(module.id)
                
                # Get imports
                import_rels = uow.relationships.find_by_source('module', module.id, 'imports')
                imports = []
                for rel in import_rels:
                    target = uow.modules.get_by_id(rel.to_id)
                    if target:
                        imports.append(target.name)
                
                # Get imported by
                imported_by_rels = uow.relationships.find_by_target('module', module.id, 'imports')
                imported_by = []
                for rel in imported_by_rels:
                    source = uow.modules.get_by_id(rel.from_id)
                    if source:
                        imported_by.append(source.name)
                
                # Generate note
                content = self.module_template.generate(
                    module, classes, functions, imports, imported_by
                )
                
                # Write file
                filename = self.module_template.sanitize_filename(module.name) + ".md"
                filepath = self.config.get_modules_path() / filename
                self.write_note(filepath, content)
                
                print(f"✓ Generated module: {module.name}")
    
    def generate_class_notes(self):
        """Generate notes for all classes"""
        with self.session_factory.create_session() as session:
            uow = UnitOfWork(session)
            
            classes = uow.classes.get_all()
            
            for cls in classes:
                # Get module
                module = uow.modules.get_by_id(cls.module_id)
                if not module:
                    continue
                
                # Get methods
                methods = uow.functions.find_by_class(cls.id)
                
                # Get base classes
                base_rels = uow.relationships.find_by_source('class', cls.id, 'inherits')
                base_classes = []
                for rel in base_rels:
                    base = uow.classes.get_by_id(rel.to_id)
                    if base:
                        base_classes.append(base.name)
                
                # Get derived classes
                derived_rels = uow.relationships.find_by_target('class', cls.id, 'inherits')
                derived_classes = []
                for rel in derived_rels:
                    derived = uow.classes.get_by_id(rel.from_id)
                    if derived:
                        derived_classes.append(derived.name)
                
                # Generate note
                content = self.class_template.generate(
                    cls, module, methods, base_classes, derived_classes
                )
                
                # Write file
                filename = self.class_template.sanitize_filename(cls.name) + ".md"
                filepath = self.config.get_classes_path() / filename
                self.write_note(filepath, content)
                
                print(f"✓ Generated class: {cls.name}")
    
    def generate_function_notes(self):
        """Generate notes for all functions"""
        with self.session_factory.create_session() as session:
            uow = UnitOfWork(session)
            
            functions = uow.functions.get_all()
            
            for func in functions:
                # Get module
                module = uow.modules.get_by_id(func.module_id)
                if not module:
                    continue
                
                # Get parent class if method
                parent_class = None
                if func.class_id:
                    parent_class = uow.classes.get_by_id(func.class_id)
                
                # Get taxonomy categories
                taxonomy_rels = uow.relationships.find_by_source('function', func.id, 'categorized_as')
                categories = []
                for rel in taxonomy_rels:
                    taxonomy = uow.taxonomy.get_by_id(rel.to_id)
                    if taxonomy:
                        categories.append(taxonomy.category)
                
                # Generate note
                content = self.function_template.generate(
                    func, module, parent_class, categories
                )
                
                # Write file - use func.id to ensure uniqueness
                filename = self.function_template.sanitize_filename(f"{func.name}_{func.id}") + ".md"
                filepath = self.config.get_functions_path() / filename
                self.write_note(filepath, content)
                
                print(f"✓ Generated function: {func.name}")
    
    def generate_taxonomy_index(self):
        """Generate taxonomy category index notes"""
        with self.session_factory.create_session() as session:
            uow = UnitOfWork(session)
            
            # Get all taxonomy categories
            taxonomies = uow.taxonomy.get_all()
            
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
                    rels = uow.relationships.find_by_target('taxonomy', taxonomy.id, 'categorized_as')
                    for rel in rels:
                        func = uow.functions.get_by_id(rel.from_id)
                        if func:
                            module = uow.modules.get_by_id(func.module_id)
                            module_name = module.name if module else "unknown"
                            content.append(f"- [[Functions/{func.name}_{func.id}|{func.name}]] (from {module_name})")
                
                content.append("")
                
                # Write file
                filename = self.module_template.sanitize_filename(category) + ".md"
                filepath = self.config.get_taxonomy_path() / filename
                self.write_note(filepath, "\n".join(content))
                
                print(f"✓ Generated taxonomy: {category}")
    
    def build_complete_vault(self):
        """Build complete vault from database"""
        print("=" * 70)
        print("Building Obsidian Vault")
        print("=" * 70)
        print()
        
        self.initialize_vault()
        print("✓ Initialized vault structure")
        print()
        
        print("Generating module notes...")
        self.generate_module_notes()
        print()
        
        print("Generating class notes...")
        self.generate_class_notes()
        print()
        
        print("Generating function notes...")
        self.generate_function_notes()
        print()
        
        print("Generating taxonomy indexes...")
        self.generate_taxonomy_index()
        print()
        
        print("=" * 70)
        print("✓ Vault generation complete!")
        print(f"Location: {self.config.root_path}")
        print("=" * 70)


# ============================================================================
# Example Usage
# ============================================================================

if __name__ == '__main__':
    # Configuration
    vault_path = Path(__file__).parent / "PythonModules"
    db_url = "sqlite:///python_modules.db"
    
    # Create builder
    config = VaultConfig(root_path=vault_path)
    session_factory = DatabaseSessionFactory(db_url)
    builder = ObsidianVaultBuilder(config, session_factory)
    
    # Build vault
    builder.build_complete_vault()
