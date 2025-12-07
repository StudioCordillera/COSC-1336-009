# DASHBOARD - CLI MENU SYSTEM STANDARDIZATION

> **READ THIS BEFORE AND AFTER EVERY SPRINT ITERATION**

---

## PROJECT SCOPE

### PRIMARY OBJECTIVE
Extract, formalize, and unify standards across three documentation sources:
1. **menuNav.py** - Navigation map and UI component design definitions
2. **CLI-Menu-Component-Taxonomy.md** - Component classification by complexity
3. **Visual Design Assets** - ASCII/Unicode UI pattern library

### DELIVERABLES
1. **MenuNav Standard** - Formal specification from menuNav.py conventions
2. **Taxonomy Standard** - Perfected component classification system
3. **Visual Pattern Catalog** - Component-to-visual mappings
4. **Relational Topic Map** - Cross-standard connections
5. **Unified Catalog** - Comprehensive integration document
6. **Optimum Pathways Catalog** - Expanded perfected final reference

---

## CRITICAL RULES

### 🔴 MISSION CRITICAL
- **ALWAYS read this DASHBOARD.MD BEFORE starting any sprint**
- **ALWAYS read this DASHBOARD.MD AFTER completing any sprint**
- **NEVER skip the pre/post-sprint dashboard review**
- Assume 0-shot context at start of every iteration
- Track ALL progress in TRACKING.CSV

### WORKFLOW SEQUENCE (STRICT ORDER)
```
1. Read DASHBOARD.MD
2. Check TRACKING.CSV for current phase
3. Complete assigned task
4. Update TRACKING.CSV
5. Read DASHBOARD.MD again
6. Proceed to next task OR pause for user check-in
```

### TASK DEPENDENCIES
```
ENTRYPOINT → DASHBOARD.MD → TRACKING.CSV → MenuNav Standard → Taxonomy Standard
                                                    ↓
                                            Visual Survey → Pattern Mapping
                                                    ↓
                                        Relational Map → Unified Catalog → Final Catalog
```

**DO NOT READ taxonomy.md UNTIL menuNav.py standard is COMPLETED**

---

## STANDARDS & CONVENTIONS

### Documentation Format
- **Headers**: Use double-line box borders (`╔═══╗`) for major sections
- **Subsections**: Use single-line box borders (`┌───┐`) or plain headers
- **Dividers**: Use `═══` for major breaks, `───` for subsections
- **Code blocks**: Preserve exact whitespace and indentation
- **Hierarchies**: Use nested indentation (2 or 4 spaces consistent)

### Component Definition Structure
Every component must define:
```
1. TYPE (Primitive, Container, Navigation, etc.)
2. STATES (enumerated list)
3. DESIGN (hierarchical component tree)
4. DEPENDENCIES (parent components/layers)
5. COMPLEXITY METRICS (LOC, state vars, difficulty)
```

### Naming Conventions
- **Files**: SCREAMING_SNAKE_CASE for project files (DASHBOARD.MD)
- **Components**: PascalCase (Button, MenuWrapper)
- **Properties**: snake_case (menu_wrapper, choice_object)
- **Constants**: SCREAMING_SNAKE_CASE (MAIN_MENU, FORK)
- **Methods**: snake_case with verb prefix (get_setup_params)

### Visual Pattern Standards
- Box drawing characters MUST be consistent within a pattern
- Use `+---+` for simple grids
- Use `┌───┐` for soft containers
- Use `╔═══╗` for prominent/formal containers
- Use `[____]` for input fields
- Use `[Button]` for action buttons
- Maintain 80-column max width where practical

### Taxonomy Standards
- Components classified by **Deployment Complexity Layers (0-9)**
- Difficulty rating: ⭐ (Trivial) to ⭐⭐⭐⭐⭐ (Very Hard)
- Track: LOC, State Variables, Dependencies, Event Handlers
- Organize by: Primitives → Elements → Controls → Containers → Views → Applications

---

## PROGRESS TRACKING

### Sprint Structure
- **Sprint**: Single atomic task completion (1 todo item)
- **Phase**: Logical group of related sprints (e.g., "Standards Extraction")
- **Project**: Complete end-to-end delivery (all 10 todos)

### CSV Tracking Requirements
Log after EVERY sprint:
- Sprint ID (incremental)
- Phase name
- Task description
- Status (NOT_STARTED, IN_PROGRESS, COMPLETED)
- Timestamp
- Output files created/modified
- Notes/blockers

---

## SCOPE DEFINITIONS

### PHASE 1: Foundation (Tasks 1-3)
**Objective**: Establish project infrastructure
- Create ENTRYPOINT
- Populate DASHBOARD.MD
- Initialize TRACKING.CSV

### PHASE 2: Standards Extraction (Tasks 4-5)
**Objective**: Formalize existing documentation
- Extract menuNav.py conventions → publish MenuNav Standard
- Perfect taxonomy.md → publish Taxonomy Standard

**⚠️ CRITICAL**: Do NOT read taxonomy.md until Task 4 is COMPLETED

### PHASE 3: Pattern Analysis (Tasks 6-7)
**Objective**: Map visual designs to component model
- Survey visual design files for content patterns
- Extract UI component construction patterns
- Map taxonomy patterns to visual samples
- Follow menuNav standard for organization

### PHASE 4: Integration (Tasks 8-9)
**Objective**: Connect all standards
- Build relational topic map between all standards
- Create unified catalog integrating all work

### PHASE 5: Optimization (Task 10)
**Objective**: Finalize perfect reference
- Expand catalog with optimal pathways
- Perfect cross-references and navigation
- Ensure 0-shot usability

---

## QUALITY STANDARDS

### For Standard Documents
- ✅ Complete component definitions (type, states, design, dependencies)
- ✅ Consistent terminology throughout
- ✅ Clear hierarchy and organization
- ✅ Examples for complex concepts
- ✅ Cross-references to related components

### For Catalogs
- ✅ Comprehensive coverage (no gaps)
- ✅ Navigable structure (TOC, indexes)
- ✅ Visual examples where applicable
- ✅ Difficulty/complexity ratings
- ✅ Usage patterns and best practices

### For Mappings
- ✅ Bidirectional relationships
- ✅ Explicit dependency chains
- ✅ Visual representations (diagrams/tables)
- ✅ Concrete examples
- ✅ Edge case handling

---

## OUTPUT FILE NAMING

Follow this convention for all generated files:

```
01_MENUNAV_STANDARD.md              # Task 4 output
02_TAXONOMY_STANDARD.md             # Task 5 output
03_VISUAL_PATTERN_SURVEY.md         # Task 6 output
04_COMPONENT_VISUAL_MAPPING.md      # Task 7 output
05_RELATIONAL_TOPIC_MAP.md          # Task 8 output
06_UNIFIED_CATALOG.md               # Task 9 output
07_OPTIMUM_PATHWAYS_CATALOG.md      # Task 10 output
```

All outputs should be created in the CLAUDE/ directory.

---

## HIDDEN SCOPE DETECTION

As you work, you may discover:
- **Implicit patterns** not explicitly documented
- **Missing taxonomic layers** between existing ones
- **Undocumented conventions** in visual designs
- **Relationship patterns** between standards

**When discovered**:
1. Note in TRACKING.CSV under "Notes" column
2. Document in the current standard being worked on
3. Flag for inclusion in Relational Map phase
4. Update DASHBOARD.MD if it affects project scope

---

## SELF-MANAGEMENT PROTOCOL

### At Start of Each Sprint
1. ✅ Read ENTRYPOINT
2. ✅ Read DASHBOARD.MD (this file) completely
3. ✅ Check TRACKING.CSV for current status
4. ✅ Review previous sprint notes
5. ✅ Identify current task dependencies

### During Sprint
1. ✅ Follow conventions from DASHBOARD.MD
2. ✅ Document discoveries inline
3. ✅ Maintain consistent formatting
4. ✅ Cross-reference related concepts
5. ✅ Build comprehensive, not minimal, deliverables

### At End of Each Sprint
1. ✅ Update TRACKING.CSV with completion status
2. ✅ Log output files created
3. ✅ Note any blockers or discoveries
4. ✅ Read DASHBOARD.MD again
5. ✅ Confirm next task in sequence
6. ✅ Pause for user confirmation if switching phases

---

## CONTEXT ASSUMPTIONS

### You Have Access To
- menuNav.py (attached, navigation structure)
- CLI-Menu-Component-Taxonomy.md (attached, classification system)
- Visual design files in 00_IMPORT/ directory
- ui_design_mapping.py (previously created visual mappings)

### You Should Create
- All standard documents (01-07 prefix)
- All tracking updates in TRACKING.CSV
- All mappings and catalogs
- Any supporting diagrams or examples

### User Will Provide
- Re-prompting if you run out of steam
- Confirmation at phase boundaries
- Course corrections if needed
- Additional context if requested

---

## SUCCESS CRITERIA

### Project Completion Requires
- ✅ All 10 tasks marked COMPLETED in TRACKING.CSV
- ✅ All 7 output documents created and populated
- ✅ Full bidirectional traceability between standards
- ✅ 0-shot readable documentation (new user can understand immediately)
- ✅ Consistent conventions applied throughout
- ✅ Comprehensive coverage (no undefined terms or gaps)

---

**END OF DASHBOARD - Remember to read again after completing current sprint**
