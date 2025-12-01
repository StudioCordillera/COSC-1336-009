# Python OOP Class Application Categories

## Overview
Comprehensive catalog of class types organized by purpose. This document serves as a decision guide for choosing the right class pattern for your problem domain.

---

## CATEGORY INDEX

1. **UI / Interaction Classes** - User interface and interaction components
2. **Domain / Data Modeling Classes** - Business entities and data structures
3. **Collection / Container Classes** - Managing groups of objects
4. **Behavior / Logic Classes** - Business logic and algorithms
5. **Creation / Lifecycle Classes** - Object instantiation and management
6. **Integration / Infrastructure Classes** - External systems and adapters
7. **Configuration / State Classes** - Settings and state management
8. **Events / Messaging Classes** - Event-driven and message passing
9. **Utility / Support Classes** - Helper functions and tools

---

## 1. UI / INTERACTION CLASSES

Classes that handle user interface and interaction logic.

### Menu Class
**Purpose**: Represents a menu or navigation structure with options and commands
**When to Use**: Building CLI menus, navigation systems, command interfaces
**Key Characteristics**: Options list, selection handling, nested submenus

### Widget / Element Class
**Purpose**: Represents a specific UI element (button, input, panel, card)
**When to Use**: Creating reusable UI components
**Key Characteristics**: Render method, event handlers, state management

### Screen / Page Class
**Purpose**: Represents a complete view composed of multiple elements
**When to Use**: Organizing full application screens or pages
**Key Characteristics**: Layout composition, lifecycle methods, navigation

### Dialog / Popup Class
**Purpose**: Temporary overlay with its own logic and state
**When to Use**: Modal interactions, confirmations, input collection
**Key Characteristics**: Show/hide, result handling, focus management

---

## 2. DOMAIN / DATA MODELING CLASSES

Classes representing business concepts and data.

### Entity / Model Class
**Purpose**: Represents real-world things with identity and state
**When to Use**: Modeling business objects (User, Order, Product)
**Key Characteristics**: Unique identity, lifecycle, business methods, persistence

### Value Object Class
**Purpose**: Small, immutable value types without identity
**When to Use**: Representing concepts like Money, Coordinate, Color, DateRange
**Key Characteristics**: Immutability, equality by value, no identity

### Record / DTO Class
**Purpose**: Simple data carrier with minimal logic
**When to Use**: Transferring data between layers, API responses
**Key Characteristics**: Public attributes, no business logic, serialization

---

## 3. COLLECTION / CONTAINER CLASSES

Classes for managing groups of objects.

### Collection Class
**Purpose**: Owns and manages a group of elements
**When to Use**: Custom collections with domain-specific operations
**Key Characteristics**: Add, remove, find, iterate, count

### Repository Class
**Purpose**: High-level collection with persistence semantics
**When to Use**: Abstracting data storage and retrieval
**Key Characteristics**: Save, load, query, domain-focused interface

### Cache Class
**Purpose**: Collection optimized for fast lookup with eviction
**When to Use**: Performance optimization, reducing expensive operations
**Key Characteristics**: Get/set, expiration, capacity limits, hit/miss tracking

### Composite Class
**Purpose**: Tree-like structure where items contain items of same type
**When to Use**: Hierarchies (org charts, file systems, UI trees)
**Key Characteristics**: Add child, remove child, traverse, recursive operations

---

## 4. BEHAVIOR / LOGIC CLASSES

Classes encapsulating business logic and algorithms.

### Service / Manager Class
**Purpose**: Performs operations, coordinates multiple objects
**When to Use**: Business processes, orchestration, no UI
**Key Characteristics**: Stateless, dependency injection, single responsibility

### Controller / Coordinator Class
**Purpose**: Mediates between input, domain, and output
**When to Use**: MVC/MVP patterns, flow control
**Key Characteristics**: Handle requests, coordinate models/views, routing

### Strategy Class
**Purpose**: Encapsulates one pluggable algorithm or behavior variant
**When to Use**: Multiple ways to do something, runtime algorithm selection
**Key Characteristics**: Common interface, interchangeable, no state

### Policy / Rule Class
**Purpose**: Encapsulates business rules and constraints
**When to Use**: Complex decision logic, rule engines
**Key Characteristics**: Evaluate, apply, compose multiple rules

### Validator Class
**Purpose**: Checks data and reports problems
**When to Use**: Input validation, business rule enforcement
**Key Characteristics**: Validate method, error collection, composable rules

---

## 5. CREATION / LIFECYCLE CLASSES

Classes managing object creation and lifecycle.

### Factory Class
**Purpose**: Centralizes how objects are constructed
**When to Use**: Complex creation logic, multiple creation variants
**Key Characteristics**: Create methods, encapsulate instantiation, type selection

### Builder Class
**Purpose**: Step-by-step construction of complex objects
**When to Use**: Objects with many optional parameters, readable construction
**Key Characteristics**: Fluent interface, incremental building, final build step

### Pool Class
**Purpose**: Manages reusable set of objects (checkout/return)
**When to Use**: Expensive object creation, resource management
**Key Characteristics**: Acquire, release, size limits, object reuse

---

## 6. INTEGRATION / INFRASTRUCTURE CLASSES

Classes interfacing with external systems.

### Adapter Class
**Purpose**: Converts one interface/protocol to another
**When to Use**: Integrating incompatible interfaces
**Key Characteristics**: Wraps adaptee, implements target interface, translation

### Wrapper / Decorator Class
**Purpose**: Wraps another object to extend or modify behavior
**When to Use**: Adding functionality without inheritance
**Key Characteristics**: Delegates to wrapped object, transparent interface

### Facade Class
**Purpose**: Simplified front interface to complex subsystem
**When to Use**: Hiding complexity, providing convenience methods
**Key Characteristics**: Simple methods, delegates to subsystem, convenience

### Gateway / Client Class
**Purpose**: Talks to external systems (API, database, filesystem)
**When to Use**: External service integration
**Key Characteristics**: Connection management, protocol handling, error translation

---

## 7. CONFIGURATION / STATE CLASSES

Classes managing settings and state.

### Configuration / Settings Class
**Purpose**: Holds application options and configuration values
**When to Use**: Application settings, user preferences
**Key Characteristics**: Load/save, validation, defaults, immutability

### State / State Machine Class
**Purpose**: Represents modes and transitions between them
**When to Use**: Workflow, connection states, UI states
**Key Characteristics**: Current state, valid transitions, state-specific behavior

### Context / Session Class
**Purpose**: Tracks current environment (user, preferences, current item)
**When to Use**: Request handling, user sessions, scoped data
**Key Characteristics**: Current values, scope lifetime, cleanup

---

## 8. EVENTS / MESSAGING CLASSES

Classes for event-driven and messaging patterns.

### Event Class
**Purpose**: Represents something that happened
**When to Use**: Logging, event-driven architecture, pub/sub
**Key Characteristics**: Timestamp, event data, immutable, type

### Command Class
**Purpose**: Represents intention to perform an action
**When to Use**: Command pattern, undo/redo, queuing
**Key Characteristics**: Execute, undo, parameters, encapsulation

### Notification / Message Class
**Purpose**: Carries information between parts of the system
**When to Use**: Loose coupling, async communication
**Key Characteristics**: Sender, recipient, payload, routing info

---

## 9. UTILITY / SUPPORT CLASSES

Classes providing helper functions and utilities.

### Utility / Helper Class
**Purpose**: Group of related functions
**When to Use**: Shared utilities, no state needed
**Key Characteristics**: Static methods, no instance creation, pure functions

### Math / String / Date Helper Class
**Purpose**: Specialized utility collections
**When to Use**: Common operations in specific domains
**Key Characteristics**: Static methods, domain-specific, side-effect free

### Logger Class
**Purpose**: Handles logging and tracing
**When to Use**: Debugging, monitoring, audit trails
**Key Characteristics**: Log levels, formatters, handlers, configuration

---

## DECISION TREE

### Start Here: What is the primary purpose?

```
Is it about USER INTERACTION?
├─ Yes → UI / Interaction Classes (Menu, Widget, Screen, Dialog)
└─ No ↓

Does it REPRESENT A REAL-WORLD CONCEPT?
├─ Yes → Domain / Data Modeling Classes (Entity, Value Object, Record)
└─ No ↓

Does it MANAGE A GROUP OF OBJECTS?
├─ Yes → Collection / Container Classes (Collection, Repository, Cache, Composite)
└─ No ↓

Does it ENCAPSULATE BUSINESS LOGIC?
├─ Yes → Behavior / Logic Classes (Service, Controller, Strategy, Policy, Validator)
└─ No ↓

Is it about CREATING OR MANAGING LIFECYCLES?
├─ Yes → Creation / Lifecycle Classes (Factory, Builder, Pool)
└─ No ↓

Does it INTEGRATE WITH EXTERNAL SYSTEMS?
├─ Yes → Integration / Infrastructure Classes (Adapter, Wrapper, Facade, Gateway)
└─ No ↓

Does it MANAGE SETTINGS OR STATE?
├─ Yes → Configuration / State Classes (Configuration, State Machine, Context)
└─ No ↓

Is it about EVENTS OR MESSAGES?
├─ Yes → Events / Messaging Classes (Event, Command, Notification)
└─ No ↓

Is it a SHARED UTILITY?
└─ Yes → Utility / Support Classes (Helper, Logger)
```

---

## COMMON COMBINATIONS

Real applications often combine multiple patterns:

### Web Application Layer
```
Controller (Behavior) 
    ↓ uses
Entity (Domain) 
    ↓ persisted by
Repository (Collection) 
    ↓ talks to
Gateway (Integration)
```

### UI Component System
```
Screen (UI)
    ↓ contains
Widget (UI)
    ↓ manages
State (Configuration)
    ↓ triggers
Event (Messaging)
```

### Business Process
```
Service (Behavior)
    ↓ validates with
Validator (Behavior)
    ↓ creates via
Factory (Creation)
    ↓ produces
Entity (Domain)
```

### Data Pipeline
```
Facade (Integration)
    ↓ uses
Adapter (Integration)
    ↓ processes
DTO (Domain)
    ↓ stored in
Cache (Collection)
```

---

## SELECTION GUIDELINES

### Use Entity/Model when:
- ✅ The thing has a unique identity
- ✅ Its state changes over time
- ✅ You track it across its lifecycle
- ❌ It's just a value (use Value Object)

### Use Service when:
- ✅ Operation involves multiple entities
- ✅ Logic doesn't belong to one entity
- ✅ You need orchestration
- ❌ It's part of entity's core responsibility

### Use Repository when:
- ✅ You need persistence abstraction
- ✅ Querying is domain-focused
- ✅ You want to hide storage details
- ❌ You just need in-memory collection

### Use Factory when:
- ✅ Creation logic is complex
- ✅ Multiple creation variants exist
- ✅ Creation requires external resources
- ❌ Simple constructor is sufficient

### Use Adapter when:
- ✅ You need to integrate incompatible interfaces
- ✅ You can't modify the adaptee
- ❌ You control both interfaces (just align them)

---

## ANTI-PATTERNS TO AVOID

### God Object
**Problem**: One class does everything
**Solution**: Break into Service, Entity, Repository as appropriate

### Anemic Domain Model
**Problem**: Entities with only data, all logic in services
**Solution**: Move behavior into Entity where it belongs

### Utility Hell
**Problem**: Everything is a static utility class
**Solution**: Use proper OOP patterns with instance methods

### Over-Engineering
**Problem**: Using patterns where simple code suffices
**Solution**: Start simple, add patterns when complexity demands it

---

## NEXT STEPS

For detailed implementation guides with complete code examples, see:

- `04_UI_INTERACTION_REFERENCE.md`
- `05_DOMAIN_DATA_REFERENCE.md`
- `06_COLLECTION_CONTAINER_REFERENCE.md`
- `07_BEHAVIOR_LOGIC_REFERENCE.md`
- `08_CREATION_LIFECYCLE_REFERENCE.md`
- `09_INTEGRATION_INFRASTRUCTURE_REFERENCE.md`
- `10_CONFIGURATION_STATE_REFERENCE.md`
- `11_EVENTS_MESSAGING_REFERENCE.md`
- `12_UTILITY_SUPPORT_REFERENCE.md`

