# Python Module Knowledge Graph - Project Dashboard

> **CRITICAL**: Read this file + tasks.csv + ENTRYPOINT.txt before/after EVERY iteration

## Mission
Build automated system: recursive Python module scanner → API queue → relational database → Obsidian knowledge vault with relationship mapping for language fundamentals research.

## Core Requirements
- API accepts module discovery submissions from recursive scanner
- Queue system processes modules asynchronously  
- Database stores modules/classes/functions with relationships
- Taxonomy maps to fundamental language categories (__init__ → constructors, etc)
- Obsidian vault publishes linked nodes showing cross-references
- Query interface finds all mentions/dependencies of any construct

---

## Phase 1: Data Collection Pipeline
**Goal**: Receive, queue, and store module data

### Sprint 1: Foundation (Tasks 1-4) ✅
- [x] API endpoint schema design
- [x] Database schema with relationships
- [x] SQLAlchemy ORM models  
- [x] API receiver with job queue

### Sprint 2: Processing (Tasks 5-7) ✅
- [x] Recursive module scanner with API integration
- [x] Async queue workers with Observer pattern
- [x] Database writer with relationship tracking (imports, inheritance, methods)

**Deliverables**: Working API accepting modules, storing in DB with relationships ✅
**Progress**: 7/19 tasks complete (36.8%)

---

## Phase 2: Knowledge Graph Construction
**Goal**: Build relationship network and taxonomy

### Sprint 3: Mapping (Tasks 8-10) ✅
- [x] Taxonomy for fundamental categories
- [x] Relationship graph builder
- [x] Query interface for cross-references

### Sprint 4: Publishing (Tasks 11-13) ✅
- [x] Obsidian vault structure with MCP integration
- [x] Markdown generator with links  
- [x] Canvas graph data export

**Deliverables**: Queryable knowledge graph published to Obsidian
**Progress**: 13/19 tasks complete (68.4%)

---

## Phase 3: Refinement & Interface
**Goal**: Usability, testing, and optimization

### Sprint 5: Control (Tasks 14-16)
- [x] CLI interface for system control
- [x] Logging and monitoring
- [x] Integration tests

### Sprint 6: Polish (Tasks 17-19)
- [x] Documentation and examples
- [x] Performance optimization
- [ ] Web dashboard (optional)

**Deliverables**: Robust, tested, documented system with CLI
**Progress**: 18/19 tasks complete (94.7%)

---

## Database Schema (Core Entities)

```
modules: id, name, filepath, is_package, analyzed_at
classes: id, module_id, name, lineno, parent_id, taxonomy_category
functions: id, module_id, class_id, name, lineno, is_async, taxonomy_category
relationships: id, from_type, from_id, to_type, to_id, relationship_type
taxonomy: id, category, subcategory, description
```

## Taxonomy Categories (Initial)
- Constructors: `__init__`, `__new__`
- Magic Methods: `__str__`, `__repr__`, `__call__`
- Data Structures: list, dict, set operations
- Control Flow: if/else, loops, exceptions
- I/O Operations: file, network, database
- Decorators: @property, @staticmethod, @classmethod

## Obsidian Vault Structure
```
/Modules/           # One note per module
/Classes/           # One note per class
/Functions/         # One note per function
/Taxonomy/          # Category overview notes
/Relationships/     # Dependency graphs
```

## API Endpoints
- `POST /api/submit` - Submit module for processing
- `GET /api/status/{job_id}` - Check processing status
- `GET /api/query/{construct}` - Find all mentions
- `GET /api/dependencies/{module}` - Get dependency tree

## Architecture & Patterns

**config.py**: Configuration management
- Builder Pattern: `ApplicationConfigBuilder` for fluent config construction
- Strategy Pattern: `ConfigLoadStrategy` (JSON/YAML/Env loaders)
- Dependency Injection: All configs injected via constructors

**models.py**: Database layer
- Repository Pattern: Abstract repositories for each entity
- Unit of Work Pattern: Transaction management
- Factory Pattern: `DatabaseSessionFactory` for session creation
- ORM: SQLAlchemy models (Module, Class, Function, Relationship, Taxonomy)

**scanner.py**: Module discovery
- Command Pattern: `ScanModuleCommand` for module operations
- Strategy Pattern: `ScanStrategy` (Recursive/SysPath scanners)
- Observer Pattern: `ScanObserver` for event notification
- Iterator Pattern: `ModuleIterator` for module traversal

**api.py**: API endpoint handler
- Command Pattern: `SubmitModuleCommand`, `HealthCheckCommand`, `GetMetricsCommand`
- Observer Pattern: `QueueObserver`, `LoggingObserver`, `MetricsObserver`
- Strategy Pattern: `QueueStrategy`, `InMemoryQueueStrategy`

**api_server.py**: FastAPI REST wrapper
- FastAPI endpoints: POST /api/v1/modules, GET /api/v1/health, GET /api/v1/metrics
- Dependency injection via Depends()
- Pydantic models for validation

**api_client.py**: HTTP client for scanner
- Retry logic and batch submission
- Context manager support
- Injected base_url and timeout

## Current Status
**Phase**: 1 | **Sprint**: 2 | **Tasks Completed**: 6/19
- [x] Task 1: API endpoint schema designed
- [x] Task 2: Database schema with relationships
- [x] Task 3: SQLAlchemy ORM models with Repository pattern
- [x] Task 4: API receiver endpoint with queue system
- [x] Task 5: Scanner integrated with API client (batch mode)
- [x] Task 6: Async workers processing queue to database

## Iteration Protocol
1. Read: ENTRYPOINT.txt → DASHBOARD.md → tasks.csv
2. Execute: Next pending task from tasks.csv
3. Update: Mark task complete, note blockers
4. Commit: Update tasks.csv status column
5. Repeat: Move to next task

## Critical Requirements
- **Dependency Injection**: All dependencies injected via constructors/config
- **Design Patterns**: Use templates from `UNIFIED_PATTERNS/` directory
- **No Hardcoding**: All paths, configs externalized
- **Pattern-Based**: Builder, Strategy, Command, Observer patterns required

## File Paths
- **Patterns Library**: `../__My_Projects__/EXAMPLES/Highest Quality Github Examples/UNIFIED_PATTERNS/`
- **Knowledge Library**: `../../../__LIBRARY__/`
- **Module Mapper**: Current directory
- **Obsidian Vault**: `../../../__OBSIDIAN_VAULT__/KNOWLEDGE_BASE/`

## Notes
- Keep this file under 200 lines for fast reads
- CSV tracks granular progress
- Add new tasks to CSV as discovered
- Update status after each session
