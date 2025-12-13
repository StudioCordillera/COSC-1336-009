# Python Module Knowledge Graph - Usage Guide

This guide provides detailed instructions for using the Python Module Knowledge Graph system.

## Table of Contents
1. [CLI Workflow](#cli-workflow)
2. [Database Population](#database-population)
3. [Querying the Graph](#querying-the-graph)
4. [Generating the Vault](#generating-the-vault)
5. [Obsidian Integration](#obsidian-integration)

---

## CLI Workflow

The primary interface is the `cli.py` script. It supports four main commands:

- `scan`: Analyze a single module
- `populate`: Batch process standard library modules
- `query`: Search the knowledge graph
- `generate-vault`: Export to Obsidian

### General Usage

```bash
python cli.py [COMMAND] [ARGS] [--verbose]
```

---

## Database Population

Before querying or generating a vault, you must populate the database.

### 1. Scan Standard Library
The `populate` command scans a predefined list of standard library modules (e.g., `os`, `sys`, `json`, `collections`) and stores them in the SQLite database.

```bash
python cli.py populate --db python_modules.db
```

**What happens:**
1. Scanner reads module source code using `pyclbr`.
2. Extracts classes, functions, and methods.
3. Identifies imports and inheritance relationships.
4. Stores everything in `python_modules.db`.

---

## Querying the Graph

You can query the database directly from the CLI to find modules, classes, or functions.

### Search by Name
Find any entity matching a name.

```bash
python cli.py query "json"
```

### Filter by Type
Limit results to specific types (`module`, `class`, `function`).

```bash
python cli.py query "dump" --type function
```

### Output Formats
Choose between `text` (default), `json`, or `markdown`.

```bash
python cli.py query "os" --format json
```

---

## Generating the Vault

The system generates a complete Obsidian vault with Markdown notes and Canvas graphs.

```bash
python cli.py generate-vault --db python_modules.db --out ./MyVault
```

**Output Structure:**
```
MyVault/
├── Modules/          # Notes for each module
├── Classes/          # Notes for each class
├── Functions/        # Notes for each function
├── Taxonomy/         # Category notes
├── Overview.canvas   # Visual graph of all modules
└── Modules/
    └── json.canvas   # Visual graph for 'json' module
```

---

## Obsidian Integration

1. Open Obsidian.
2. Select "Open folder as vault".
3. Choose the output directory (e.g., `MyVault`).
4. **Recommended Plugins:**
   - **Dataview**: For dynamic queries (if templates use it).
   - **Excalidraw**: If you want to edit diagrams manually.

### Navigating the Graph
- **Overview.canvas**: Start here to see the high-level module relationships.
- **WikiLinks**: Click any link (e.g., `[[os]]`) to jump to that module's note.
- **Backlinks**: Use Obsidian's "Linked Mentions" pane to see what imports a module.
