# Domain / Data Modeling Classes Reference

## Overview
Classes for representing business concepts and data structures in your domain.

---

## 1. ENTITY / MODEL CLASS

### Purpose
Represents a real-world thing with identity, state, and behavior that persists over time.

### When to Use
- Business objects (User, Order, Product, Account)
- Things with unique identity (not just values)
- Objects that change state over their lifecycle
- Objects you need to track, store, and retrieve

### Key Characteristics
- **Has unique identity** (ID, UUID)
- **Mutable state** that changes over time
- **Business logic** methods
- **Lifecycle** (created, modified, deleted)
- **Can be persisted** to database

### Class Anatomy

#### Instance Attributes
- `id` - Unique identifier
- Domain-specific data fields
- `created_at`, `updated_at` - Timestamps
- Status/state fields

#### Instance Methods
- Business logic operations
- State transitions
- Validation methods
- Computed properties

#### Special Methods
- `__init__()` - Initialize with data
- `__eq__()`, `__hash__()` - Identity-based equality
- `__str__()`, `__repr__()` - String representations

### Complete Example

```python
# Order status constants
STATUS_PENDING = "pending"
STATUS_CONFIRMED = "confirmed"
STATUS_SHIPPED = "shipped"
STATUS_DELIVERED = "delivered"
STATUS_CANCELLED = "cancelled"

class Order:
    """Represents a customer order (Entity/Model)."""
    
    def __init__(self, id, customer_id, total, timestamp=None):
        """Initialize order entity.
        
        Args:
            id: Unique order identifier
            customer_id: Customer who placed order
            total: Order total amount (float)
            timestamp: Creation timestamp (float, optional)
        """
        self.id = id
        self.customer_id = customer_id
        self.total = total
        self.status = STATUS_PENDING
        self.items = []
        # Use provided timestamp or 0.0 as placeholder
        self.created_at = timestamp if timestamp is not None else 0.0
        self.updated_at = timestamp if timestamp is not None else 0.0
        self.shipped_at = None
        self.delivered_at = None
    
    def add_item(self, product_id, quantity, price):
        """Add an item to the order.
        
        Args:
            product_id: Product identifier
            quantity: Quantity ordered
            price: Price per unit (float)
        """
        if self.status != STATUS_PENDING:
            raise ValueError(f"Cannot add items to {self.status} order")
        
        self.items.append({
            'product_id': product_id,
            'quantity': quantity,
            'price': price
        })
        self._recalculate_total()
        self._touch()
    
    def confirm(self):
        """Confirm the order."""
        if self.status != STATUS_PENDING:
            raise ValueError(f"Cannot confirm {self.status} order")
        
        if not self.items:
            raise ValueError("Cannot confirm empty order")
        
        self.status = STATUS_CONFIRMED
        self._touch()
    
    def ship(self, timestamp=None):
        """Mark order as shipped.
        
        Args:
            timestamp: Ship timestamp (float, optional)
        """
        if self.status != STATUS_CONFIRMED:
            raise ValueError(f"Cannot ship {self.status} order")
        
        self.status = STATUS_SHIPPED
        self.shipped_at = timestamp if timestamp is not None else 0.0
        self._touch(timestamp)
    
    def deliver(self, timestamp=None):
        """Mark order as delivered.
        
        Args:
            timestamp: Delivery timestamp (float, optional)
        """
        if self.status != STATUS_SHIPPED:
            raise ValueError(f"Cannot deliver {self.status} order")
        
        self.status = STATUS_DELIVERED
        self.delivered_at = timestamp if timestamp is not None else 0.0
        self._touch(timestamp)
    
    def cancel(self):
        """Cancel the order."""
        if self.status in (STATUS_DELIVERED, STATUS_CANCELLED):
            raise ValueError(f"Cannot cancel {self.status} order")
        
        self.status = STATUS_CANCELLED
        self._touch()
    
    def is_modifiable(self):
        """Check if order can be modified."""
        return self.status == STATUS_PENDING
    
    def _recalculate_total(self):
        """Recalculate order total."""
        self.total = sum(
            item['quantity'] * item['price']
            for item in self.items
        )
    
    def _touch(self, timestamp=None):
        """Update the modified timestamp.
        
        Args:
            timestamp: Update timestamp (float, optional)
        """
        self.updated_at = timestamp if timestamp is not None else 0.0
    
    def __eq__(self, other):
        """Equality based on identity (ID)."""
        if not isinstance(other, Order):
            return False
        return self.id == other.id
    
    def __hash__(self):
        """Hash based on ID for use in sets/dicts."""
        return hash(self.id)
    
    def __str__(self):
        return f"Order {self.id}: ${self.total} ({self.status})"
    
    def __repr__(self):
        return f"Order(id='{self.id}', total={self.total}, status={self.status})"


# Usage
order = Order("ORD-001", "CUST-123", 0.00)
order.add_item("PROD-A", 2, 19.99)
order.add_item("PROD-B", 1, 9.99)

print(order)  # Order ORD-001: $49.97 (pending)

order.confirm()
order.ship()
order.deliver()

print(order.status)  # delivered
```

---

## 2. VALUE OBJECT CLASS

### Purpose
Represents a value or concept without identity - defined entirely by its attributes.

### When to Use
- Measurements (Money, Distance, Weight)
- Coordinates (Point, Rectangle)
- Ranges (DateRange, PriceRange)
- Descriptive values (Color, Address, Email)

### Key Characteristics
- **No identity** - two value objects with same data are identical
- **Immutable** - cannot change after creation
- **Equality by value** - compared by their attributes
- **Self-validating** - ensures data integrity
- **Replaceable** - create new instead of modifying

### Class Anatomy

#### Instance Attributes
- All attributes are read-only (via properties or naming convention)
- Value data fields

#### Instance Methods
- Operations that return new value objects
- Validation methods
- Conversion methods
- Formatting methods

#### Special Methods
- `__init__()` - Validate and set immutable state
- `__eq__()` - Value-based equality
- `__hash__()` - Allow use in sets/dicts
- `__str__()` - Human-readable format

### Complete Example

```python
class Money:
    """Immutable value object representing monetary amount."""
    
    def __init__(self, amount, currency="USD"):
        """Initialize money value.
        
        Args:
            amount: Monetary amount (float)
            currency: Currency code (ISO 4217)
            
        Raises:
            ValueError: If amount is negative or currency invalid
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        
        if not isinstance(currency, str) or len(currency) != 3:
            raise ValueError("Currency must be 3-letter code")
        
        # Make immutable by using private attributes
        self._amount = float(amount)
        self._currency = currency.upper()
    
    @property
    def amount(self):
        """Get the amount (read-only)."""
        return self._amount
    
    @property
    def currency(self):
        """Get the currency (read-only)."""
        return self._currency
    
    def add(self, other):
        """Add two money values.
        
        Args:
            other: Money to add
            
        Returns:
            New Money instance
            
        Raises:
            ValueError: If currencies don't match
        """
        if self.currency != other.currency:
            raise ValueError(f"Cannot add {self.currency} and {other.currency}")
        
        return Money(self.amount + other.amount, self.currency)
    
    def subtract(self, other):
        """Subtract money values."""
        if self.currency != other.currency:
            raise ValueError(f"Cannot subtract {self.currency} and {other.currency}")
        
        return Money(self.amount - other.amount, self.currency)
    
    def multiply(self, factor):
        """Multiply by a factor."""
        return Money(self.amount * factor, self.currency)
    
    def allocate(self, ratios):
        """Allocate money according to ratios.
        
        Args:
            ratios: List of integer ratios
            
        Returns:
            List of Money allocations
        """
        total_ratio = sum(ratios)
        allocations = []
        remainder = self.amount
        
        for ratio in ratios[:-1]:
            allocation = (self.amount * ratio) // total_ratio
            allocations.append(Money(allocation, self.currency))
            remainder -= allocation
        
        # Last allocation gets remainder
        allocations.append(Money(remainder, self.currency))
        return allocations
    
    def __eq__(self, other):
        """Value-based equality."""
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency
    
    def __hash__(self):
        """Hash for use in sets/dicts."""
        return hash((self.amount, self.currency))
    
    def __str__(self):
        return f"{self.currency} {self.amount:.2f}"
    
    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"
    
    def __lt__(self, other):
        """Less than comparison."""
        if self.currency != other.currency:
            raise ValueError("Cannot compare different currencies")
        return self.amount < other.amount


# Usage
price = Money(19.99, "USD")
tax = Money(2.00, "USD")

total = price.add(tax)
print(total)  # USD 21.99

# Immutability - this doesn't modify original
discounted = price.multiply(0.8)
print(price)       # USD 19.99 (unchanged)
print(discounted)  # USD 15.99

# Value equality
same_price = Money(19.99, "USD")
print(price == same_price)  # True (same value)

# Can use in sets/dicts
prices = {price, same_price}  # Only one item (same value)
```

---

## 3. RECORD / DTO CLASS

### Purpose
Simple data carrier with minimal logic - transfers data between layers or systems.

### When to Use
- API request/response objects
- Data transfer between layers
- Configuration data
- Query results
- Serialization targets

### Key Characteristics
- **Public attributes** - direct access to data
- **Minimal logic** - no business rules
- **Easy serialization** - to/from JSON, dict, etc.
- **Validation optional** - or delegated elsewhere
- **Often use dataclasses** in Python

### Class Anatomy

#### Instance Attributes
- Public data fields
- Type annotations

#### Instance Methods
- `to_dict()` - Convert to dictionary
- `from_dict()` - Create from dictionary
- Simple validation (optional)

#### Special Methods
- Can be auto-generated with properties for immutability

### Complete Example

```python
class UserDTO:
    """Data Transfer Object for User data."""
    
    def __init__(self, id, username, email, created_at, is_active=True, roles=None, last_login=None):
        """Initialize user DTO.
        
        Args:
            id: User identifier
            username: Username string
            email: Email address
            created_at: Creation timestamp (float from time.time())
            is_active: Active status (bool)
            roles: List of role strings
            last_login: Last login timestamp or None
        """
        self.id = id
        self.username = username
        self.email = email
        self.created_at = created_at
        self.is_active = is_active
        self.roles = roles if roles is not None else []
        self.last_login = last_login
    
    def to_dict(self):
        """Convert to dictionary for serialization."""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at,
            'is_active': self.is_active,
            'roles': self.roles.copy(),  # Return copy to maintain immutability
            'last_login': self.last_login
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create from dictionary."""
        return cls(
            id=data['id'],
            username=data['username'],
            email=data['email'],
            created_at=data['created_at'],
            is_active=data.get('is_active', True),
            roles=data.get('roles', []),
            last_login=data.get('last_login')
        )
    
    def __repr__(self):
        return f"UserDTO(id='{self.id}', username='{self.username}')"


class OrderItemDTO:
    """DTO for order line item."""
    
    def __init__(self, product_id, product_name, quantity, unit_price, subtotal):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.unit_price = unit_price
        self.subtotal = subtotal
    
    def to_dict(self):
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'quantity': self.quantity,
            'unit_price': self.unit_price,
            'subtotal': self.subtotal
        }


class OrderDTO:
    """DTO for order data."""
    
    def __init__(self, id, customer_id, customer_name, items, total, status, created_at):
        self.id = id
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.items = items  # list of OrderItemDTO objects
        self.total = total
        self.status = status
        self.created_at = created_at
    
    def to_dict(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'customer_name': self.customer_name,
            'items': [item.to_dict() for item in self.items],
            'total': self.total,
            'status': self.status,
            'created_at': self.created_at
        }


class ProductRecord:
    """Record class for product data."""
    
    def __init__(self, id, name, price, category, in_stock=True):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock
    
    def to_dict(self):
        """Convert to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'category': self.category,
            'in_stock': self.in_stock
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create from dictionary."""
        return cls(**data)
    
    def __repr__(self):
        return f"ProductRecord(id='{self.id}', name='{self.name}')"


# Usage
user = UserDTO(
    id="U123",
    username="alice",
    email="alice@example.com",
    created_at=1732838400.0,  # timestamp value (e.g., from time.time())
    roles=["user", "admin"]
)

# Easy serialization
user_dict = user.to_dict()
print(user_dict)

# Deserialization
restored_user = UserDTO.from_dict(user_dict)
print(restored_user.id == user.id)  # Compare by value

# Product record
product = ProductRecord("P001", "Laptop", 999.99, "Electronics")
product_data = product.to_dict()
```

---

## COMPARISON SUMMARY

| Aspect | Entity/Model | Value Object | Record/DTO |
|--------|--------------|--------------|------------|
| Identity | Has unique ID | No identity | May have ID |
| Mutability | Mutable | Immutable | Either |
| Equality | By ID | By value | Either |
| Logic | Rich behavior | Operations | Minimal |
| Persistence | Yes | Via entity | Transport only |
| Lifecycle | Tracked | None | None |

## TYPICAL USAGE PATTERNS

### Entity manages Value Objects
```python
class Customer:  # Entity
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = EmailAddress(email)  # Value Object
        self.balance = Money(0.0, "USD")  # Value Object
```

### Entity converts to DTO for API
```python
class Order:  # Entity
    def to_dto(self):  # Returns OrderDTO
        return OrderDTO(
            id=self.id,
            customer_id=self.customer_id,
            total=float(self.total),
            status=self.status,
            created_at=self.created_at
        )
```

### DTO hydrates Entity
```python
@classmethod
def from_dto(cls, dto):  # Entity from UserDTO
    return cls(
        id=dto.id,
        username=dto.username,
        email=dto.email
    )
```

