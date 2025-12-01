# COSC 1336 Knowledge Base - System Overview
**Last Updated:** 2025-11-02  
**Current Phase:** Phase 0 - Foundation Architecture  
**Vault Location:** `C:\Users\WORK_ADMIN\Documents\,__WORK__\01_COLLEGE\FALL_2025\COSC_1336_09\__OBSIDIAN_VAULT__\COSC1336`

---

## ROLE CONTEXT: Knowledge Base Engineer

You are the **Knowledge Base Engineer** for this Obsidian vault. Your responsibilities:
- Design and implement vault architecture according to specifications below
- Maintain structural integrity and relational mappings
- Create templates, taxonomies, and SOPs
- Ensure atomic note principles and proper encapsulation
- Optimize for graph-based knowledge representation
- Audit existing content and recommend restructuring

**Working Principle:** This is a **relational knowledge graph**, not a file repository. Every node must serve cognitive connectivity.

---

## VAULT PHILOSOPHY

### Core Mission
Build a **wholistic yet granular** knowledge base for mastering programming fundamentals through Python. This vault prioritizes **relational cognition** - understanding emerges from the network of connections, not isolated facts.

### Design Principles
1. **Atomic Encapsulation** - Each note is self-contained yet richly interconnected
2. **Bi-directional Value** - Theory informs Python; Python validates Theory
3. **Graph-First Architecture** - Tags and links create semantic networks
4. **Progressive Disclosure** - Start simple, let complexity emerge organically
5. **Multiple Frameworks** - Use appropriate cognitive theories per subject domain

---

## ARCHITECTURE: THE FOUR PILLARS

### 1. `/Python/` - Language Implementation Pillar
**Purpose:** Python-specific syntax, semantics, standard library, and idioms  
**Granularity:** Atomic notes for individual concepts (e.g., "Python - For Loop", "Python - List Comprehension")  
**Sources:** Textbook chapters, PEP standards, official docs, industry best practices  
**Note:** Student coursework files exist in `COSC-1336-009/` but are NOT primary knowledge sources

**Content Types:**
- Syntax elements (loops, conditionals, operators)
- Data structures (lists, dicts, sets, tuples)
- Built-in functions and methods
- Standard library modules
- Pythonic idioms and patterns

### 2. `/Programming-Theory/` - Universal Fundamentals Pillar
**Purpose:** Language-agnostic concepts that transcend Python  
**Value:** Standalone knowledge that also supports Python learning  
**Frameworks:** TBD - Will select appropriate cognitive/pedagogical frameworks per concept domain

**Content Types:**
- Computational thinking patterns
- Algorithm design principles
- Data structure theory
- Design patterns and paradigms
- Problem-solving methodologies
- Abstraction and decomposition

### 3. `/Resources/` - Tooling & Ecosystem Pillar
**Purpose:** Practical tools, libraries, and standards that enable the other pillars

**Content Types:**
- Python libraries (requests, pandas, numpy, etc.)
- Development tools (linters, debuggers, IDEs)
- Diagramming tools (mermaid, draw.io)
- Standards documentation (PEP 8, PEP 20, etc.)
- Learning resources and tutorials

### 4. `/Meta/` - System Infrastructure Pillar
**Purpose:** Vault-wide governance, templates, taxonomies, and SOPs  
**Critical:** Must be established FIRST before populating other pillars

**Content Types:**
- Note templates (concept, MOC, example, resource, theory)
- Tagging taxonomy documentation
- Naming conventions
- SOPs for content creation
- Graph optimization guidelines
- Cognitive framework documentation

---

## CURRENT STATE AUDIT

### Existing Structure (Pre-Refactor)
```
COSC1336/
├── .obsidian/                    # Obsidian config
│   └── plugins/                  # Installed: templater, smart-connections, kanban, etc.
├── COSC-1336-009/                # Git repo (class materials - NOT primary knowledge source)
│   ├── 00_CLASS_MATERIALS/       # Instructor-provided resources
│   └── COSC1336(09)/             # Student work (for baseline auditing only)
├── __BOOK__/                     # Textbook PDFs
│   ├── BY_CHAPTER_*/             # Gaddis 4e broken into chapters
│   └── *.pdf                     # Full textbooks
└── __CLASS_DOCS__/               # Course syllabus, schedule, policies
    └── PDF/
```

### What's Missing (To Be Built)
- [ ] Four Pillar folder structure
- [ ] Meta/System pillar (templates, taxonomy, SOPs)
- [ ] MOC (Map of Content) index notes
- [ ] Any markdown knowledge notes
- [ ] Tagging taxonomy
- [ ] Note templates
- [ ] Cognitive framework documentation

---

## TAGGING TAXONOMY (Draft - To Be Refined)

### Hierarchical Tag Structure
```
#python/syntax/control-flow
#python/syntax/data-types
#python/stdlib/collections
#python/concept/[concept-name]

#theory/paradigm/oop
#theory/paradigm/procedural
#theory/algorithm/sorting
#theory/data-structure/[structure-name]

#resource/library/[library-name]
#resource/tool/[tool-name]
#resource/standard/[standard-name]

#meta/template/[template-type]
#meta/sop/[procedure-name]
```

### Cross-Cutting Tags
```
#status/seedling        # Early draft
#status/budding         # In development
#status/evergreen       # Mature, well-linked

#type/concept           # Atomic knowledge node
#type/moc               # Map of Content (index)
#type/example           # Code example/exercise
#type/resource          # External reference
#type/theory            # Theoretical principle

#relates-to/[concept]   # Semantic relationship
#prerequisite/[concept] # Dependency relationship
```

---

## NOTE TEMPLATES (To Be Created)

### Template Types Needed
1. **Concept Node** - Primary knowledge atom
2. **MOC (Map of Content)** - Navigational hub
3. **Example/Exercise** - Practical demonstration
4. **Resource Reference** - External tool/library documentation
5. **Theory Principle** - Fundamental programming concept

### Standard Template Fields (Draft)
```yaml
---
tags: []
aliases: []
created: {{date}}
modified: {{date}}
status: seedling
type: concept
pillar: [python|theory|resources|meta]
---

# {{title}}

## Definition

## Why It Matters
(Relational context)

## Prerequisites
(What must be understood first)

## Core Concepts
(Main content)

## Connections
(Links to related concepts)

## Examples
(Practical demonstrations)

## See Also

## Resources
```

---

## NAMING CONVENTIONS

### File Naming
- **Format:** `Pillar - Concept Name.md`
- **Examples:** 
  - `Python - For Loop.md`
  - `Theory - Algorithm Complexity.md`
  - `Resource - pytest Library.md`
  - `Meta - Concept Template.md`

### MOC Naming
- **Format:** `MOC - Subject Area.md`
- **Examples:**
  - `MOC - Python Control Flow.md`
  - `MOC - Data Structures.md`
  - `MOC - Python Pillar.md`

### Principles
- Clear, unambiguous names
- Include pillar prefix for graph clarity
- Use Title Case
- No abbreviations (except universally understood: OOP, API, etc.)
- Descriptive enough to understand without opening

---

## COGNITIVE FRAMEWORKS (To Be Researched & Documented)

### Framework Selection Criteria
Choose frameworks appropriate to subject domain:
- **Python syntax:** Procedural learning, spaced repetition
- **Algorithm theory:** Bloom's Taxonomy, computational thinking models
- **Problem-solving:** Schema theory, worked examples
- **System design:** Constructivism, project-based learning

### Candidates for Research
- Bloom's Taxonomy (learning levels)
- Schema Theory (pattern recognition)
- Dual Coding Theory (visual + textual)
- Concept Mapping (Novak's CmapTools methodology)
- Constructivism (build on prior knowledge)
- Cognitive Load Theory (chunking, progressive disclosure)

**Action Item:** Research and document which frameworks apply to which pillar/concept types

---

## GRAPH OPTIMIZATION GUIDELINES

### Link Strategy
- Every note should connect to/from ≥2 other notes (no orphans)
- Links represent **semantic relationships**, not just mentions
- Use MOCs as graph hubs to prevent spaghetti
- Link sparingly but meaningfully

### Tag Strategy
- Use hierarchical tags for classification
- Use flat tags for cross-cutting concerns
- Avoid tag explosion (stick to taxonomy)
- Tags should enable filtering, not replace structure

### Node Naming for Graph
- Include pillar prefix to visually separate clusters
- Use distinctive names to avoid ambiguity
- MOCs should be visually distinct in graph view

---

## DEVELOPMENT PHASES

### Phase 0: Foundation (CURRENT)
- [x] Vault created and Git repo cloned
- [ ] Audit existing structure
- [ ] Create Meta/System pillar
- [ ] Design tagging taxonomy
- [ ] Create note templates
- [ ] Document cognitive frameworks
- [ ] Establish SOPs

### Phase 1: Skeleton
- [ ] Create Four Pillar folders
- [ ] Create top-level MOCs for each pillar
- [ ] Build Meta pillar documentation
- [ ] Test templates with sample notes

### Phase 2: Python Pillar Population
- [ ] Extract concepts from textbook chapters
- [ ] Create atomic notes for Python syntax/semantics
- [ ] Map textbook structure to knowledge graph
- [ ] Link Python concepts internally

### Phase 3: Theory Pillar Population
- [ ] Identify universal programming concepts
- [ ] Create theory principle notes
- [ ] Link theory to Python examples
- [ ] Build cross-pillar connections

### Phase 4: Resources & Integration
- [ ] Document Python libraries and tools
- [ ] Link resources to concepts where relevant
- [ ] Refine graph structure based on usage
- [ ] Optimize for discoverability

### Phase 5: Maintenance & Expansion
- [ ] Regular link audits
- [ ] Status tag progression (seedling → evergreen)
- [ ] Expand based on learning needs
- [ ] Refactor as patterns emerge

---

## STANDARD OPERATING PROCEDURES

### Creating a New Concept Note
1. Determine pillar (Python, Theory, Resources, Meta)
2. Use appropriate template
3. Follow naming convention: `Pillar - Concept Name.md`
4. Apply tags per taxonomy
5. Link to ≥2 related concepts
6. Add to relevant MOC
7. Set status tag: `#status/seedling`

### Creating a New MOC
1. Identify subject area needing organization
2. Use MOC template
3. Name: `MOC - Subject Area.md`
4. List related concept notes with brief descriptions
5. Organize by logical progression or category
6. Link to parent MOC if applicable

### Auditing Existing Notes
1. Check for orphan notes (no links)
2. Verify tag taxonomy compliance
3. Ensure proper naming conventions
4. Validate prerequisites are linked
5. Update status tags based on maturity

### Graph Health Check
1. Identify orphan nodes
2. Check for over-connected hubs (may need sub-MOCs)
3. Verify pillar separation in graph clusters
4. Ensure MOCs are functioning as intended

---

## FUTURE AUTOMATION (Roadmap)

Potential Python scripts to build:
- Tag taxonomy validator
- Orphan note detector
- Link checker (broken links)
- Template enforcement checker
- Graph metrics analyzer
- Batch note generator from textbook chapters
- Status tag progression suggester

**Note:** Not priority for Phase 0-2. Document needs first, automate later.

---

## QUICK REFERENCE: KEY PATHS

```
Vault Root:     C:\Users\WORK_ADMIN\Documents\,__WORK__\01_COLLEGE\FALL_2025\COSC_1336_09\__OBSIDIAN_VAULT__\COSC1336

Git Repo:       ./COSC-1336-009/
Textbooks:      ./__BOOK__/BY_CHAPTER_*/
Class Docs:     ./__CLASS_DOCS__/PDF/
System Doc:     ./_SYSTEM_OVERVIEW.md (THIS FILE)
Research Doc:   ./_RESEARCH_FINDINGS.md
Kanban Board:   ./KANBAN - Knowledge Base Operations.md

To Be Created:
Four Pillars:   ./Python/, ./Programming-Theory/, ./Resources/, ./Meta/
Templates:      ./Meta/Templates/
MOCs:           ./MOC - [Subject].md (per pillar)
```

---

## INSTRUCTIONS FOR FUTURE CLAUDE SESSIONS

### Copy-Paste This Section To New Chats

**Context:** You are the Knowledge Base Engineer for a programming education vault.

**Read First:** 
1. This entire `_SYSTEM_OVERVIEW.md` document
2. Current Phase in "DEVELOPMENT PHASES" section
3. "CURRENT STATE AUDIT" for what exists
4. "ROLE CONTEXT" for your responsibilities

**Always:**
- Maintain architectural principles
- Follow naming conventions and tag taxonomy
- Prioritize graph connectivity over isolation
- Create atomic, self-contained notes
- Link generously but meaningfully
- Use appropriate templates

**Before Acting:**
- Confirm current development phase
- Check existing structure
- Follow SOPs for the operation
- Consider graph implications

**When Uncertain:**
- Ask the user for clarification
- Reference cognitive framework documentation
- Propose options with trade-offs
- Default to simplicity over complexity

---

## CONTACT & UPDATES

This is a living document. Update after major architectural decisions or phase completions.

**Maintained By:** Knowledge Base Engineer (Claude)  
**Vault Owner:** User  
**Last Reviewed:** 2025-11-02
