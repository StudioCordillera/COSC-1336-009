# Python Module Knowledge Graph

A comprehensive research tool that builds a relational knowledge graph of Python modules, classes, and functions. It scans standard library or custom modules, maps their relationships (imports, inheritance), and generates a navigable Obsidian vault with visual graphs.

## Features

### Core Functionality
- ✅ **Recursive Module Scanner** - Discovers modules, classes, and functions using `pyclbr` (no import execution)
- ✅ **Relational Database** - Stores entities and relationships in SQLite
- ✅ **Taxonomy Mapping** - Categorizes constructs (e.g., Constructors, Magic Methods, I/O)
- ✅ **Dependency Graphing** - Tracks imports and inheritance chains

### Visualization & Output
- ✅ **Obsidian Vault Generation** - Creates a full knowledge base with WikiLinks
- ✅ **Canvas Graphing** - Generates `.canvas` files for visual exploration of module relationships
- ✅ **CLI Interface** - Unified command-line tool for all operations
- ✅ **Query Interface** - Search the graph for specific constructs or patterns

## Installation

1. Clone the repository
2. Install dependencies (standard library only + SQLAlchemy)
   ```bash
   pip install sqlalchemy
   ```

## Quick Start

The system is controlled via the `cli.py` script.

```bash
# 1. Populate database with standard library modules
python cli.py populate

# 2. Query the database
python cli.py query "json" --type module

# 3. Generate Obsidian Vault
python cli.py generate-vault --out ./MyVault
```

## Architecture

The project follows a modular architecture with strict separation of concerns:

- **Scanner**: `scanner.py` - Discovers code structure
- **Database**: `models.py` - SQLAlchemy ORM models
- **Graph**: `graph.py` - Relationship traversal logic
- **Vault**: `generate_vault.py` - Obsidian markdown/canvas generation
- **CLI**: `cli.py` - Command-line interface

See [ARCHITECTURE.md](ARCHITECTURE.md) for design patterns and details.

## Usage

See [USAGE.md](USAGE.md) for detailed workflows and examples.

### CLI Commands

- `scan <module>`: Scan a single module and output JSON
- `populate`: Scan standard library and populate database
- `query <term>`: Search the knowledge graph
- `generate-vault`: Create Obsidian vault from database

### Programmatic API

See `examples.py` for complete code examples.

```python
from models import DatabaseSessionFactory
from graph import RelationshipGraphBuilder
from query import QueryInterface

# 1. Connect to database
factory = DatabaseSessionFactory("sqlite:///python_modules.db")

# 2. Build graph
graph = RelationshipGraphBuilder(factory)

# 3. Query
query = QueryInterface(graph)
results = query.search_by_name("json")

for node in results.nodes:
    print(f"Found: {node.name} ({node.entity_type})")
```


## Data Models

The system uses SQLAlchemy models to represent the code structure:

- **ModuleModel**: Represents a Python module
- **ClassModel**: Represents a class definition
- **FunctionModel**: Represents a function or method
- **ArgumentModel**: Represents function arguments

## License

MIT License

## Contributing

Contributions are welcome! Please ensure you run the test suite before submitting a PR.













