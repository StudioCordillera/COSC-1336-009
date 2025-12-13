"""
Taxonomy Mapper for Fundamental Categories

Categorizes Python constructs into fundamental language categories for research:
- Constructors (__init__, __new__)
- Magic methods (__str__, __repr__, __eq__, etc.)
- Properties (@property, @setter, @getter)
- Accessors (get_*, set_*, _get_*, _set_*)
- Class methods (@classmethod)
- Static methods (@staticmethod)
- Decorators (@decorator)
- Abstract methods (@abstractmethod)

Design Patterns:
- Strategy Pattern: TaxonomyStrategy for different categorization rules
- Chain of Responsibility: Multiple strategies tried in order
- Repository Pattern: TaxonomyRepository for database access

All dependencies injected via constructors.
"""

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, Dict, Any, Set
from enum import Enum

# Import models for taxonomy storage
from models import Taxonomy


# ============================================================================
# Taxonomy Categories
# ============================================================================

class TaxonomyCategory(Enum):
    """Fundamental Python construct categories"""
    CONSTRUCTOR = "constructor"
    DESTRUCTOR = "destructor"
    MAGIC_METHOD = "magic_method"
    PROPERTY = "property"
    ACCESSOR = "accessor"
    MUTATOR = "mutator"
    CLASS_METHOD = "class_method"
    STATIC_METHOD = "static_method"
    ABSTRACT_METHOD = "abstract_method"
    DECORATOR = "decorator"
    GENERATOR = "generator"
    ASYNC_FUNCTION = "async_function"
    CONTEXT_MANAGER = "context_manager"
    OPERATOR_OVERLOAD = "operator_overload"
    COMPARISON = "comparison"
    CONTAINER = "container"
    CALLABLE = "callable"
    ATTRIBUTE_ACCESS = "attribute_access"
    DESCRIPTOR = "descriptor"
    METACLASS = "metaclass"
    PRIVATE_METHOD = "private_method"
    PROTECTED_METHOD = "protected_method"
    PUBLIC_METHOD = "public_method"
    REGULAR_FUNCTION = "regular_function"


@dataclass
class TaxonomyMatch:
    """Result of taxonomy categorization"""
    category: TaxonomyCategory
    subcategory: Optional[str] = None
    confidence: float = 1.0
    pattern_matched: Optional[str] = None
    description: Optional[str] = None


# ============================================================================
# Strategy Pattern: Taxonomy Categorization Strategies
# ============================================================================

class TaxonomyStrategy(ABC):
    """Abstract strategy for categorizing constructs"""
    
    @abstractmethod
    def categorize(
        self,
        name: str,
        is_method: bool = False,
        is_async: bool = False,
        parent_class: Optional[str] = None,
        decorators: Optional[List[str]] = None
    ) -> Optional[TaxonomyMatch]:
        """
        Categorize a construct.
        
        Args:
            name: Name of function/method/class
            is_method: True if this is a class method
            is_async: True if async function
            parent_class: Name of parent class if method
            decorators: List of decorator names if available
            
        Returns:
            TaxonomyMatch if categorized, None if not matched
        """
        pass


class ConstructorStrategy(TaxonomyStrategy):
    """Categorize constructors and destructors"""
    
    def categorize(
        self,
        name: str,
        is_method: bool = False,
        is_async: bool = False,
        parent_class: Optional[str] = None,
        decorators: Optional[List[str]] = None
    ) -> Optional[TaxonomyMatch]:
        
        if name == "__init__":
            return TaxonomyMatch(
                category=TaxonomyCategory.CONSTRUCTOR,
                subcategory="initializer",
                pattern_matched="__init__",
                description="Instance constructor/initializer"
            )
        
        if name == "__new__":
            return TaxonomyMatch(
                category=TaxonomyCategory.CONSTRUCTOR,
                subcategory="allocator",
                pattern_matched="__new__",
                description="Class instance allocator"
            )
        
        if name == "__del__":
            return TaxonomyMatch(
                category=TaxonomyCategory.DESTRUCTOR,
                subcategory="finalizer",
                pattern_matched="__del__",
                description="Destructor/finalizer"
            )
        
        return None


class MagicMethodStrategy(TaxonomyStrategy):
    """Categorize magic/dunder methods"""
    
    # Magic method categories
    COMPARISON_METHODS = {"__eq__", "__ne__", "__lt__", "__le__", "__gt__", "__ge__"}
    OPERATOR_METHODS = {"__add__", "__sub__", "__mul__", "__truediv__", "__floordiv__", 
                        "__mod__", "__pow__", "__and__", "__or__", "__xor__"}
    CONTAINER_METHODS = {"__len__", "__getitem__", "__setitem__", "__delitem__", 
                         "__contains__", "__iter__", "__next__"}
    ATTRIBUTE_METHODS = {"__getattr__", "__setattr__", "__delattr__", "__getattribute__"}
    REPRESENTATION_METHODS = {"__str__", "__repr__", "__format__", "__bytes__"}
    CONTEXT_METHODS = {"__enter__", "__exit__", "__aenter__", "__aexit__"}
    
    def categorize(
        self,
        name: str,
        is_method: bool = False,
        is_async: bool = False,
        parent_class: Optional[str] = None,
        decorators: Optional[List[str]] = None
    ) -> Optional[TaxonomyMatch]:
        
        # Skip constructor/destructor (handled by ConstructorStrategy)
        if name in {"__init__", "__new__", "__del__"}:
            return None
        
        # Check specific subcategories
        if name in self.COMPARISON_METHODS:
            return TaxonomyMatch(
                category=TaxonomyCategory.COMPARISON,
                subcategory="comparison_operator",
                pattern_matched=name,
                description=f"Comparison operator {name}"
            )
        
        if name in self.OPERATOR_METHODS:
            return TaxonomyMatch(
                category=TaxonomyCategory.OPERATOR_OVERLOAD,
                subcategory="arithmetic_operator",
                pattern_matched=name,
                description=f"Operator overload {name}"
            )
        
        if name in self.CONTAINER_METHODS:
            return TaxonomyMatch(
                category=TaxonomyCategory.CONTAINER,
                subcategory="container_protocol",
                pattern_matched=name,
                description=f"Container protocol {name}"
            )
        
        if name in self.ATTRIBUTE_METHODS:
            return TaxonomyMatch(
                category=TaxonomyCategory.ATTRIBUTE_ACCESS,
                subcategory="attribute_protocol",
                pattern_matched=name,
                description=f"Attribute access {name}"
            )
        
        if name in self.REPRESENTATION_METHODS:
            return TaxonomyMatch(
                category=TaxonomyCategory.MAGIC_METHOD,
                subcategory="representation",
                pattern_matched=name,
                description=f"Object representation {name}"
            )
        
        if name in self.CONTEXT_METHODS:
            return TaxonomyMatch(
                category=TaxonomyCategory.CONTEXT_MANAGER,
                subcategory="context_protocol",
                pattern_matched=name,
                description=f"Context manager {name}"
            )
        
        if name == "__call__":
            return TaxonomyMatch(
                category=TaxonomyCategory.CALLABLE,
                subcategory="callable_protocol",
                pattern_matched="__call__",
                description="Makes instance callable"
            )
        
        # Generic magic method
        if name.startswith("__") and name.endswith("__"):
            return TaxonomyMatch(
                category=TaxonomyCategory.MAGIC_METHOD,
                subcategory="generic",
                pattern_matched="__*__",
                description=f"Magic method {name}"
            )
        
        return None


class DecoratorStrategy(TaxonomyStrategy):
    """Categorize by decorators"""
    
    def categorize(
        self,
        name: str,
        is_method: bool = False,
        is_async: bool = False,
        parent_class: Optional[str] = None,
        decorators: Optional[List[str]] = None
    ) -> Optional[TaxonomyMatch]:
        
        if not decorators:
            return None
        
        # Check for property decorators
        if "property" in decorators:
            return TaxonomyMatch(
                category=TaxonomyCategory.PROPERTY,
                subcategory="getter",
                pattern_matched="@property",
                description="Property getter"
            )
        
        if any(d.endswith(".setter") for d in decorators):
            return TaxonomyMatch(
                category=TaxonomyCategory.PROPERTY,
                subcategory="setter",
                pattern_matched="@*.setter",
                description="Property setter"
            )
        
        if any(d.endswith(".deleter") for d in decorators):
            return TaxonomyMatch(
                category=TaxonomyCategory.PROPERTY,
                subcategory="deleter",
                pattern_matched="@*.deleter",
                description="Property deleter"
            )
        
        # Check for class/static methods
        if "classmethod" in decorators:
            return TaxonomyMatch(
                category=TaxonomyCategory.CLASS_METHOD,
                pattern_matched="@classmethod",
                description="Class method"
            )
        
        if "staticmethod" in decorators:
            return TaxonomyMatch(
                category=TaxonomyCategory.STATIC_METHOD,
                pattern_matched="@staticmethod",
                description="Static method"
            )
        
        # Check for abstract methods
        if "abstractmethod" in decorators:
            return TaxonomyMatch(
                category=TaxonomyCategory.ABSTRACT_METHOD,
                pattern_matched="@abstractmethod",
                description="Abstract method"
            )
        
        return None


class AccessorStrategy(TaxonomyStrategy):
    """Categorize accessor/mutator patterns"""
    
    GETTER_PATTERNS = [
        r"^get_[\w]+$",      # get_value
        r"^_get_[\w]+$",     # _get_value
        r"^is_[\w]+$",       # is_valid
        r"^has_[\w]+$",      # has_permission
        r"^can_[\w]+$",      # can_access
    ]
    
    SETTER_PATTERNS = [
        r"^set_[\w]+$",      # set_value
        r"^_set_[\w]+$",     # _set_value
    ]
    
    def categorize(
        self,
        name: str,
        is_method: bool = False,
        is_async: bool = False,
        parent_class: Optional[str] = None,
        decorators: Optional[List[str]] = None
    ) -> Optional[TaxonomyMatch]:
        
        # Check getter patterns
        for pattern in self.GETTER_PATTERNS:
            if re.match(pattern, name):
                return TaxonomyMatch(
                    category=TaxonomyCategory.ACCESSOR,
                    subcategory="getter",
                    pattern_matched=pattern,
                    description=f"Accessor method {name}"
                )
        
        # Check setter patterns
        for pattern in self.SETTER_PATTERNS:
            if re.match(pattern, name):
                return TaxonomyMatch(
                    category=TaxonomyCategory.MUTATOR,
                    subcategory="setter",
                    pattern_matched=pattern,
                    description=f"Mutator method {name}"
                )
        
        return None


class VisibilityStrategy(TaxonomyStrategy):
    """Categorize by Python naming conventions for visibility"""
    
    def categorize(
        self,
        name: str,
        is_method: bool = False,
        is_async: bool = False,
        parent_class: Optional[str] = None,
        decorators: Optional[List[str]] = None
    ) -> Optional[TaxonomyMatch]:
        
        if not is_method:
            return None
        
        # Skip magic methods (handled elsewhere)
        if name.startswith("__") and name.endswith("__"):
            return None
        
        # Private methods (name mangling)
        if name.startswith("__") and not name.endswith("__"):
            return TaxonomyMatch(
                category=TaxonomyCategory.PRIVATE_METHOD,
                pattern_matched="__*",
                description="Private method (name mangled)",
                confidence=0.9
            )
        
        # Protected methods (single underscore)
        if name.startswith("_") and not name.startswith("__"):
            return TaxonomyMatch(
                category=TaxonomyCategory.PROTECTED_METHOD,
                pattern_matched="_*",
                description="Protected method (convention)",
                confidence=0.8
            )
        
        # Public methods
        if not name.startswith("_"):
            return TaxonomyMatch(
                category=TaxonomyCategory.PUBLIC_METHOD,
                pattern_matched="[a-zA-Z]*",
                description="Public method",
                confidence=0.7
            )
        
        return None


class AsyncStrategy(TaxonomyStrategy):
    """Categorize async functions"""
    
    def categorize(
        self,
        name: str,
        is_method: bool = False,
        is_async: bool = False,
        parent_class: Optional[str] = None,
        decorators: Optional[List[str]] = None
    ) -> Optional[TaxonomyMatch]:
        
        if is_async:
            return TaxonomyMatch(
                category=TaxonomyCategory.ASYNC_FUNCTION,
                subcategory="coroutine",
                pattern_matched="async def",
                description="Async function/coroutine",
                confidence=0.9
            )
        
        return None


# ============================================================================
# Taxonomy Mapper: Coordinate strategies
# ============================================================================

class TaxonomyMapper:
    """
    Maps Python constructs to taxonomy categories using strategy chain.
    
    Dependency Injection:
    - strategies: List of TaxonomyStrategy instances (applied in order)
    """
    
    def __init__(self, strategies: Optional[List[TaxonomyStrategy]] = None):
        """
        Initialize with strategies.
        
        Args:
            strategies: List of strategies to try (in order)
                       If None, uses default strategy chain
        """
        if strategies is None:
            # Default strategy chain (order matters!)
            self.strategies = [
                ConstructorStrategy(),
                DecoratorStrategy(),
                MagicMethodStrategy(),
                AccessorStrategy(),
                AsyncStrategy(),
                VisibilityStrategy(),  # Lowest priority (fallback)
            ]
        else:
            self.strategies = strategies
    
    def categorize(
        self,
        name: str,
        is_method: bool = False,
        is_async: bool = False,
        parent_class: Optional[str] = None,
        decorators: Optional[List[str]] = None
    ) -> List[TaxonomyMatch]:
        """
        Categorize a construct using strategy chain.
        
        Returns all matching categories (construct may fit multiple).
        Higher confidence matches come first.
        """
        matches = []
        
        for strategy in self.strategies:
            match = strategy.categorize(
                name=name,
                is_method=is_method,
                is_async=is_async,
                parent_class=parent_class,
                decorators=decorators
            )
            
            if match:
                matches.append(match)
        
        # Sort by confidence (highest first)
        matches.sort(key=lambda m: m.confidence, reverse=True)
        
        return matches
    
    def get_primary_category(
        self,
        name: str,
        is_method: bool = False,
        is_async: bool = False,
        parent_class: Optional[str] = None,
        decorators: Optional[List[str]] = None
    ) -> Optional[TaxonomyMatch]:
        """Get the primary (highest confidence) category"""
        matches = self.categorize(
            name=name,
            is_method=is_method,
            is_async=is_async,
            parent_class=parent_class,
            decorators=decorators
        )
        
        return matches[0] if matches else None


# ============================================================================
# Helper Functions
# ============================================================================

def create_taxonomy_entity(match: TaxonomyMatch) -> Taxonomy:
    """Create a Taxonomy database entity from a match"""
    return Taxonomy(
        category=match.category.value,
        subcategory=match.subcategory,
        description=match.description,
        pattern=match.pattern_matched
    )


# ============================================================================
# Example Usage
# ============================================================================

if __name__ == '__main__':
    mapper = TaxonomyMapper()
    
    # Test cases
    test_cases = [
        ("__init__", True, False, "MyClass", None),
        ("__str__", True, False, "MyClass", None),
        ("get_value", True, False, "MyClass", None),
        ("set_name", True, False, "MyClass", None),
        ("_private_method", True, False, "MyClass", None),
        ("public_method", True, False, "MyClass", None),
        ("async_task", False, True, None, None),
        ("my_property", True, False, "MyClass", ["property"]),
        ("class_builder", True, False, "MyClass", ["classmethod"]),
    ]
    
    print("=" * 70)
    print("Taxonomy Mapper - Test Cases")
    print("=" * 70)
    
    for name, is_method, is_async, parent, decorators in test_cases:
        matches = mapper.categorize(
            name=name,
            is_method=is_method,
            is_async=is_async,
            parent_class=parent,
            decorators=decorators
        )
        
        print(f"\n{name}:")
        if matches:
            for match in matches:
                print(f"  - {match.category.value}")
                if match.subcategory:
                    print(f"    subcategory: {match.subcategory}")
                print(f"    confidence: {match.confidence}")
                print(f"    pattern: {match.pattern_matched}")
        else:
            print("  - No category match")
    
    print("\n" + "=" * 70)
