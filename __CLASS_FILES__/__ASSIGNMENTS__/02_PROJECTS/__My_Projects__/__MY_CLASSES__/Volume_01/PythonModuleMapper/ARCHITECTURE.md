# Module Knowledge Graph - Core Architecture

## 🎯 Meta View: System Purpose

This system implements a **recursive Python module discovery pipeline** that:
1. Scans directories/sys.path for Python modules
2. Uses `pyclbr` to safely extract structure without importing
3. Submits discoveries to an API queue for async processing
4. Stores in relational database with taxonomy mapping
5. Publishes to Obsidian vault as linked knowledge graph

**Research Goal**: Query any construct (e.g., `__init__`) to find:
- All modules where it appears
- Dependencies and relationships
- Taxonomy categorization (constructors, magic methods, etc.)
- Visual node map in Obsidian

---

## 🏗️ Architecture Overview

### Design Patterns Used

Following templates from `UNIFIED_PATTERNS/`:

1. **Builder Pattern** (`config.py`)
   - `ApplicationConfigBuilder`: Fluent interface for configuration
   - Separates complex object construction from representation

2. **Strategy Pattern** (`config.py`, `scanner.py`)
   - `ConfigLoadStrategy`: Pluggable config loaders (JSON/YAML/Env)
   - `ScanStrategy`: Different scanning approaches (Recursive/SysPath)

3. **Repository Pattern** (`models.py`)
   - Abstract `Repository` base class
   - Concrete repositories for each entity type
   - Encapsulates data access logic

4. **Unit of Work Pattern** (`models.py`)
   - `UnitOfWork`: Manages database transactions
   - Context manager for automatic commit/rollback

5. **Factory Pattern** (`models.py`)
   - `DatabaseSessionFactory`: Creates DB sessions with config
   - Manages connection pooling and engine setup

6. **Command Pattern** (`scanner.py`)
   - `ScanModuleCommand`: Encapsulates module scan operations
   - Supports undo/redo and deferred execution

7. **Observer Pattern** (`scanner.py`)
   - `ScanObserver`: Event notification for module discovery
   - `APISubmitObserver`: Auto-submits to API on discovery

8. **Iterator Pattern** (`scanner.py`)
   - `ModuleIterator`: Safe iteration through discovered modules
   - Supports reset and has_next checks

---

## 📦 Core Components

### 1. Configuration System (`config.py`)

**Dependency Injection**: All configs passed via constructors

```python
# Builder pattern with fluent interface
config = (ApplicationConfigBuilder()
    .with_database(DatabaseConfig(...))
    .with_api(APIConfig(...))
    .with_obsidian(ObsidianConfig(...))
    .build())
```

**Key Classes**:
- `DatabaseConfig`: Connection strings, pool size
- `APIConfig`: Host, port, workers, queue size
- `ObsidianConfig`: Vault paths, folder structure
- `ScannerConfig`: Scan paths, exclusions, depth
- `TaxonomyConfig`: Category definitions

**Strategies**:
- `JsonConfigLoader`: Load from JSON files
- `YamlConfigLoader`: Load from YAML files
- `EnvConfigLoader`: Load from environment variables

---

### 2. Database Layer (`models.py`)

**Dependency Injection**: Session factory injected into repositories

```python
# Factory creates sessions
db_factory = DatabaseSessionFactory(connection_string="sqlite:///...")
db_factory.create_tables()

# Unit of Work manages transactions
with UnitOfWork(db_factory) as uow:
    module = Module(name="collections", ...)
    uow.repositories['module'].add(module)
    uow.commit()
```

**Entities** (ORM Models):
- `Module`: Python modules (name, filepath, is_package)
- `Class`: Classes with inheritance tracking
- `Function`: Functions/methods with async flag
- `Relationship`: Cross-references (inherits, calls, imports, uses)
- `Taxonomy`: Category mappings

**Repositories**:
- `ModuleRepository`: CRUD for modules
- `ClassRepository`: CRUD for classes
- `FunctionRepository`: CRUD for functions
- `RelationshipRepository`: Query relationships
- `TaxonomyRepository`: Category queries

**Pattern Benefits**:
- Abstraction: Business logic independent of ORM
- Testability: Mock repositories for unit tests
- Transactions: UnitOfWork ensures consistency

---

### 3. Module Scanner (`scanner.py`)

**Dependency Injection**: Strategy and observers injected

```python
# Strategy defines how to scan
strategy = RecursiveScanStrategy(
    max_depth=10,
    excluded_patterns=['test_*']
)

# Observer handles discoveries
observer = APISubmitObserver(api_client=my_api_client)

# Scanner composes them
scanner = ModuleScanner(
    scan_strategy=strategy,
    observers=[observer],
    batch_size=50
)

# Execute scan
modules = scanner.scan(Path('/path/to/code'))
```

**Key Classes**:
- `ModuleCommand`: Abstract command for operations
- `ScanModuleCommand`: Concrete scan command using `pyclbr`
- `ScanStrategy`: Abstract scanning strategy
- `RecursiveScanStrategy`: Recursively scan directories
- `SysPathScanStrategy`: Scan sys.path for importable modules
- `ScanObserver`: Abstract observer for events
- `APISubmitObserver`: Submit to API on discovery
- `ModuleIterator`: Iterate through results
- `ModuleScanner`: Main scanner orchestrator

**Data Flow**:
1. Scanner uses Strategy to discover module names
2. Creates `ScanModuleCommand` for each module
3. Command executes, uses `pyclbr` to extract structure
4. Returns `ModuleDiscoveryResult` dataclass
5. Observers notified (e.g., submit to API)

---

## 🔄 Processing Flow

```
User triggers scan
    ↓
ModuleScanner (strategy pattern)
    ↓
Discover modules (recursive/sys.path)
    ↓
Create ScanModuleCommand for each (command pattern)
    ↓
Execute commands → pyclbr extraction
    ↓
Notify observers (observer pattern)
    ↓
APISubmitObserver → Queue for processing
    ↓
API endpoint receives data
    ↓
Queue worker processes async
    ↓
Write to database (repository + unit of work)
    ↓
Taxonomy mapper categorizes constructs
    ↓
Relationship builder creates cross-references
    ↓
Obsidian generator creates linked notes
    ↓
Query interface for research
```

---

## 🎨 Design Principles Applied

### 1. Dependency Injection
**No hardcoded dependencies**:
```python
# ✅ GOOD: Dependencies injected
scanner = ModuleScanner(
    scan_strategy=strategy,  # Injected
    observers=[observer],     # Injected
    batch_size=config.batch_size  # From config
)

# ❌ BAD: Hardcoded
scanner = ModuleScanner()
scanner.strategy = RecursiveScanStrategy()  # Hardcoded
```

### 2. Open/Closed Principle
**Open for extension, closed for modification**:
```python
# Add new scan strategy without modifying scanner
class GitRepoScanStrategy(ScanStrategy):
    def scan(self, root_path: Path) -> List[str]:
        # Custom implementation
        pass

# Use new strategy
scanner = ModuleScanner(scan_strategy=GitRepoScanStrategy())
```

### 3. Single Responsibility
Each class has one reason to change:
- `DatabaseSessionFactory`: Only manages DB connections
- `ModuleRepository`: Only handles module CRUD
- `ScanModuleCommand`: Only scans one module
- `TaxonomyMapper`: Only categorizes constructs

### 4. Interface Segregation
Abstract bases define minimal contracts:
- `Repository`: add/get/update/delete
- `ScanStrategy`: scan(path)
- `ScanObserver`: on_discovered/on_complete/on_error
- `ConfigLoadStrategy`: load(source)

---

## 📋 Next Steps (In Priority Order)

1. **API Receiver** (Task 4): FastAPI endpoint with queue
2. **Async Workers** (Task 6): Process queue with asyncio
3. **Database Writer** (Task 7): Parse results and write to DB
4. **Taxonomy Mapper** (Task 8): Categorize constructs
5. **Relationship Builder** (Task 9): Track dependencies
6. **Obsidian Generator** (Task 12): Create linked notes

---

## 🧪 Testing Strategy

Each component testable via mocks:

```python
# Mock repository
class MockModuleRepository(Repository):
    def __init__(self):
        self.modules = {}
    
    def add(self, entity):
        self.modules[entity.id] = entity

# Test with mock
uow = MockUnitOfWork(mock_repos)
service = ModuleService(uow)
service.add_module(...)
```

---

## 📁 File Structure

```
PythonModuleMapper/
├── ENTRYPOINT.txt          # 0-shot prompt for AI agents
├── DASHBOARD.md            # Project overview (read every iteration)
├── tasks.csv               # Task tracking (update after each task)
├── config.py               # Configuration with Builder/Strategy patterns
├── models.py               # Database models with Repository/UoW patterns
├── scanner.py              # Module scanner with Command/Observer patterns
├── api.py                  # [TODO] API endpoints (Task 4)
├── workers.py              # [TODO] Async queue workers (Task 6)
├── taxonomy.py             # [TODO] Taxonomy mapper (Task 8)
├── relationships.py        # [TODO] Relationship builder (Task 9)
├── obsidian.py             # [TODO] Obsidian generator (Task 12)
└── cli.py                  # [TODO] CLI interface (Task 14)
```

---

## 🔗 External Dependencies

**Patterns Library**: `../EXAMPLES/Highest Quality Github Examples/UNIFIED_PATTERNS/`
- Used as templates (not modified)
- Reference for pattern implementation

**Knowledge Library**: `../../../__LIBRARY__/`
- OOP patterns documentation
- Gang of Four reference

**Obsidian Vault**: `../../../__OBSIDIAN_VAULT__/KNOWLEDGE_BASE/`
- Target for published knowledge graph

---

## 💡 Key Assumptions

1. **API is REST-based**: POST for submission, GET for queries
2. **Queue is in-memory**: Using Python's asyncio Queue (can swap for Redis/RabbitMQ)
3. **Database is SQLite**: Can swap for PostgreSQL via connection string
4. **Obsidian uses Markdown**: Standard .md files with YAML frontmatter
5. **Taxonomy is configurable**: Loaded from config, not hardcoded
6. **All paths injected**: No filesystem hardcoding

---

## 🚀 Core Script Responsibilities

**Recursive Scanner** (`scanner.py`):
- Traverse directories/sys.path
- Discover Python modules safely
- Create commands for processing
- Notify observers of discoveries

**Database Mapper** (`models.py`):
- Store module metadata
- Track class inheritance
- Record function definitions
- Build relationship graph

**Obsidian Converter** (TODO: `obsidian.py`):
- Generate Markdown files
- Create YAML frontmatter
- Build Wikilinks for relationships
- Export canvas graph data

All orchestrated via dependency injection—no component knows about others' implementation.
