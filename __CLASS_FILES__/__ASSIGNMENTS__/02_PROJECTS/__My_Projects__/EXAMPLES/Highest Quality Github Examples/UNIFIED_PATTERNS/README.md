# Unified Design Patterns Collection

This directory contains a comprehensive collection of Python design pattern implementations compiled from 5 high-quality GitHub repositories.

## 📂 Directory Structure

```
UNIFIED_PATTERNS/
├── behavioral/          # Behavioral Design Patterns
├── creational/          # Creational Design Patterns  
├── structural/          # Structural Design Patterns
├── fundamental/         # Fundamental Patterns
├── solid/              # SOLID Design Principles
└── other/              # Additional patterns and examples
```

## 📊 Pattern Statistics

- **Behavioral Patterns**: 60+ implementations
- **Creational Patterns**: 21+ implementations
- **Structural Patterns**: 26+ implementations
- **Fundamental Patterns**: 2 implementations
- **SOLID Principles**: 5 implementations
- **Other Patterns**: 50+ implementations
- **Total**: 165+ Python pattern files

## 🔍 Source Repositories

This collection aggregates patterns from:

1. **python-patterns** (faif/python-patterns)
   - Comprehensive collection with behavioral/, creational/, structural/, fundamental/, other/
   - Well-documented, production-ready implementations
   - Files in main category directories

2. **Design-Patterns-in-Python** (Sean-Bradley/Design-Patterns-in-Python)
   - Single-file pattern implementations
   - Clear, concise examples
   - Files in other/ directory

3. **design-patterns-python** (RefactoringGuru patterns)
   - Conceptual implementations following Refactoring.Guru standards
   - Thread-safe and non-thread-safe variants
   - Files in other/ with `refactoring_` prefix

4. **Python-Design-Patterns** (Udemy course materials)
   - Extensive pattern variations and exercises
   - SOLID principles included
   - Files organized in numbered directories (1_patterns/, 2_exercises/, 3_examples/)

5. **python_design_patterns** (Additional implementations)
   - Pattern variations (classic, dynamic, handmade)
   - Includes SOLID principles
   - Flat file structure with descriptive names

## 🎯 Pattern Categories

### Behavioral Patterns
Design patterns that identify common communication patterns between objects:
- Chain of Responsibility
- Command
- Interpreter
- Iterator
- Mediator
- Memento
- Observer
- State
- Strategy
- Template Method
- Visitor

### Creational Patterns
Design patterns that deal with object creation mechanisms:
- Abstract Factory
- Builder
- Factory Method
- Prototype
- Singleton (multiple implementations)
- Borg
- Lazy Evaluation
- Object Pool

### Structural Patterns
Design patterns that ease the design by identifying relationships between entities:
- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Flyweight
- Proxy
- 3-Tier
- Front Controller
- MVC

### Fundamental Patterns
Core programming patterns:
- Delegation Pattern

### SOLID Principles
Object-oriented design principles:
- Single Responsibility Principle
- Open/Closed Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependency Inversion Principle

## 📖 Usage

Each pattern file is self-contained and runnable. To explore a pattern:

```bash
# Example: Run singleton pattern
python creational/singleton.py

# Example: Run observer pattern
python behavioral/observer.py

# Example: Run SOLID principle
python solid/single_responsibility.py
```

## 🔗 Original Repository Links

- [python-patterns](https://github.com/faif/python-patterns) - Collection of design patterns in Python
- [Design-Patterns-in-Python](https://github.com/Sean-Bradley/Design-Patterns-in-Python) - Design patterns implemented in Python
- [design-patterns-python](https://github.com/RefactoringGuru/design-patterns-python) - Refactoring.Guru patterns
- [Python-Design-Patterns](https://github.com/dimztimz/Python-Design-Patterns) - Comprehensive course materials
- [python_design_patterns](https://github.com/tomarraj008/python_design_patterns) - Practical implementations

## 📝 File Naming Conventions

- Files from `python-patterns`: Original names preserved
- Files from `Design-Patterns-in-Python`: Original names in other/ directory
- Files from `design-patterns-python`: Prefixed with `refactoring_` in other/
- Files from `Python-Design-Patterns`: Organized in numbered directories
- Files from `python_design_patterns`: Descriptive names (e.g., `singleton_decorator.py`, `builder_facets.py`)

## 🎓 Learning Path Recommendation

### Beginner Level
1. Start with **Creational Patterns**: singleton.py, factory.py, builder.py
2. Move to **SOLID Principles**: Understand object-oriented design fundamentals
3. Explore **Structural Patterns**: adapter.py, decorator.py, facade.py

### Intermediate Level
1. Study **Behavioral Patterns**: observer.py, strategy.py, command.py
2. Compare implementations: Different repos show various approaches
3. Review **Pattern Variations**: classic vs dynamic vs handmade implementations

### Advanced Level
1. Explore complex patterns: mediator.py, memento.py, interpreter.py
2. Study **Pattern Combinations**: See how patterns work together
3. Analyze **Performance**: Compare metaclass vs decorator singleton implementations

## 🔧 Development

### Running Pattern Examples

```bash
# Navigate to unified patterns directory
cd UNIFIED_PATTERNS

# Run any pattern file
python behavioral/chain_of_responsibility.py
python creational/abstract_factory.py
python structural/proxy.py
```

### Exploring Variations

Many patterns have multiple implementations:
- `singleton.py`, `singleton_decorator.py`, `singleton_metaclass.py`, `monostate.py`
- `decorator.py`, `classic.py`, `dynamic.py`
- `chain_of_res.py`, `broker_chain.py`
- `state.py`, `handmade.py`, `switch.py`

## 📚 Additional Resources

- **Gang of Four Book**: "Design Patterns: Elements of Reusable Object-Oriented Software"
- **Refactoring.Guru**: https://refactoring.guru/design-patterns
- **Python Design Patterns**: https://python-patterns.guide/
- **Real Python**: https://realpython.com/tutorials/patterns/

## ⚖️ License

Each source repository maintains its original license:
- python-patterns: MIT License
- Design-Patterns-in-Python: MIT License  
- design-patterns-python: MIT License
- Python-Design-Patterns: Various (check original repo)
- python_design_patterns: Various (check original repo)

Please refer to the TEMPLATES/ directory for original repository licenses.

---

**Compiled**: December 2025  
**Total Patterns**: 165+ implementations  
**Languages**: Python 3.x  
**Purpose**: Educational and reference resource for design pattern study
