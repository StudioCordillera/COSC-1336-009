# Database Models using SQLAlchemy ORM
# Following Repository Pattern for data access abstraction

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, Text, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, Session
from sqlalchemy.pool import StaticPool, NullPool
from datetime import datetime
from typing import Optional, List
from abc import ABC, abstractmethod

Base = declarative_base()

# Many-to-many relationship table for class inheritance
class_inheritance = Table(
    'class_inheritance',
    Base.metadata,
    Column('child_id', Integer, ForeignKey('classes.id'), primary_key=True),
    Column('parent_id', Integer, ForeignKey('classes.id'), primary_key=True)
)


class Module(Base):
    """Module entity - represents a Python module"""
    __tablename__ = 'modules'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False, index=True)
    filepath = Column(String(512), nullable=False)
    is_package = Column(Boolean, default=False)
    analyzed_at = Column(DateTime, default=datetime.utcnow)
    checksum = Column(String(64))  # For change detection
    docstring = Column(Text, nullable=True)
    
    # Relationships
    classes = relationship('Class', back_populates='module', cascade='all, delete-orphan')
    functions = relationship('Function', back_populates='module', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f"<Module(name='{self.name}', is_package={self.is_package})>"


class Class(Base):
    """Class entity - represents a Python class"""
    __tablename__ = 'classes'
    
    id = Column(Integer, primary_key=True)
    module_id = Column(Integer, ForeignKey('modules.id'), nullable=False, index=True)
    name = Column(String(255), nullable=False, index=True)
    lineno = Column(Integer, nullable=False)
    parent_class_id = Column(Integer, ForeignKey('classes.id'), nullable=True)  # For nested classes
    taxonomy_category = Column(String(100), index=True)
    docstring = Column(Text, nullable=True)
    
    # Relationships
    module = relationship('Module', back_populates='classes')
    methods = relationship('Function', back_populates='parent_class', cascade='all, delete-orphan')
    nested_classes = relationship('Class', remote_side=[id], backref='parent_class')
    
    # Many-to-many: base classes
    base_classes = relationship(
        'Class',
        secondary=class_inheritance,
        primaryjoin=id == class_inheritance.c.child_id,
        secondaryjoin=id == class_inheritance.c.parent_id,
        backref='derived_classes'
    )
    
    def __repr__(self):
        return f"<Class(name='{self.name}', module='{self.module.name if self.module else None}')>"


class Function(Base):
    """Function entity - represents a Python function or method"""
    __tablename__ = 'functions'
    
    id = Column(Integer, primary_key=True)
    module_id = Column(Integer, ForeignKey('modules.id'), nullable=False, index=True)
    class_id = Column(Integer, ForeignKey('classes.id'), nullable=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    lineno = Column(Integer, nullable=False)
    is_async = Column(Boolean, default=False)
    is_method = Column(Boolean, default=False)
    taxonomy_category = Column(String(100), index=True)
    docstring = Column(Text, nullable=True)
    args = Column(Text, nullable=True)  # JSON string of arguments
    returns = Column(String(255), nullable=True)  # Return type annotation
    decorators = Column(Text, nullable=True)  # JSON string of decorators
    
    # Relationships
    module = relationship('Module', back_populates='functions')
    parent_class = relationship('Class', back_populates='methods')
    
    def __repr__(self):
        return f"<Function(name='{self.name}', is_async={self.is_async})>"


class Relationship(Base):
    """Relationship entity - tracks cross-references between entities"""
    __tablename__ = 'relationships'
    
    id = Column(Integer, primary_key=True)
    from_type = Column(String(50), nullable=False, index=True)  # 'module', 'class', 'function'
    from_id = Column(Integer, nullable=False, index=True)
    to_type = Column(String(50), nullable=False, index=True)
    to_id = Column(Integer, nullable=False, index=True)
    relationship_type = Column(String(100), nullable=False, index=True)  # 'inherits', 'calls', 'imports', 'uses'
    
    def __repr__(self):
        return f"<Relationship({self.from_type}:{self.from_id} -> {self.to_type}:{self.to_id} [{self.relationship_type}])>"


class Taxonomy(Base):
    """Taxonomy entity - categorizes language constructs"""
    __tablename__ = 'taxonomy'
    
    id = Column(Integer, primary_key=True)
    category = Column(String(100), nullable=False, index=True)
    subcategory = Column(String(100), nullable=True, index=True)
    description = Column(Text, nullable=True)
    pattern = Column(String(255), nullable=True)  # Regex or pattern to match
    
    def __repr__(self):
        return f"<Taxonomy(category='{self.category}', subcategory='{self.subcategory}')>"


# Repository Pattern: Abstract base repository
class Repository(ABC):
    """Abstract repository for data access"""
    
    def __init__(self, session: Session):
        self.session = session
    
    @abstractmethod
    def add(self, entity):
        """Add new entity"""
        pass
    
    @abstractmethod
    def get_by_id(self, entity_id: int):
        """Get entity by ID"""
        pass
    
    @abstractmethod
    def get_all(self) -> List:
        """Get all entities"""
        pass
    
    @abstractmethod
    def update(self, entity):
        """Update existing entity"""
        pass
    
    @abstractmethod
    def delete(self, entity_id: int):
        """Delete entity by ID"""
        pass
    
    def commit(self):
        """Commit transaction"""
        self.session.commit()
    
    def rollback(self):
        """Rollback transaction"""
        self.session.rollback()


class ModuleRepository(Repository):
    """Repository for Module entities"""
    
    def add(self, entity: Module) -> Module:
        self.session.add(entity)
        return entity
    
    def get_by_id(self, entity_id: int) -> Optional[Module]:
        return self.session.query(Module).filter(Module.id == entity_id).first()
    
    def get_by_name(self, name: str) -> Optional[Module]:
        return self.session.query(Module).filter(Module.name == name).first()
    
    def get_all(self) -> List[Module]:
        return self.session.query(Module).all()
    
    def update(self, entity: Module) -> Module:
        self.session.merge(entity)
        return entity
    
    def delete(self, entity_id: int):
        module = self.get_by_id(entity_id)
        if module:
            self.session.delete(module)


class ClassRepository(Repository):
    """Repository for Class entities"""
    
    def add(self, entity: Class) -> Class:
        self.session.add(entity)
        return entity
    
    def get_by_id(self, entity_id: int) -> Optional[Class]:
        return self.session.query(Class).filter(Class.id == entity_id).first()
    
    def get_by_name(self, name: str) -> List[Class]:
        return self.session.query(Class).filter(Class.name == name).all()
    
    def get_by_module(self, module_id: int) -> List[Class]:
        return self.session.query(Class).filter(Class.module_id == module_id).all()
    
    def get_all(self) -> List[Class]:
        return self.session.query(Class).all()
    
    def update(self, entity: Class) -> Class:
        self.session.merge(entity)
        return entity
    
    def delete(self, entity_id: int):
        cls = self.get_by_id(entity_id)
        if cls:
            self.session.delete(cls)


class FunctionRepository(Repository):
    """Repository for Function entities"""
    
    def add(self, entity: Function) -> Function:
        self.session.add(entity)
        return entity
    
    def get_by_id(self, entity_id: int) -> Optional[Function]:
        return self.session.query(Function).filter(Function.id == entity_id).first()
    
    def get_by_name(self, name: str) -> List[Function]:
        return self.session.query(Function).filter(Function.name == name).all()
    
    def get_by_module(self, module_id: int) -> List[Function]:
        return self.session.query(Function).filter(Function.module_id == module_id).all()
    
    def get_by_class(self, class_id: int) -> List[Function]:
        return self.session.query(Function).filter(Function.class_id == class_id).all()
    
    def get_all(self) -> List[Function]:
        return self.session.query(Function).all()
    
    def update(self, entity: Function) -> Function:
        self.session.merge(entity)
        return entity
    
    def delete(self, entity_id: int):
        func = self.get_by_id(entity_id)
        if func:
            self.session.delete(func)


class RelationshipRepository(Repository):
    """Repository for Relationship entities"""
    
    def add(self, entity: Relationship) -> Relationship:
        self.session.add(entity)
        return entity
    
    def get_by_id(self, entity_id: int) -> Optional[Relationship]:
        return self.session.query(Relationship).filter(Relationship.id == entity_id).first()
    
    def get_relationships_from(self, from_type: str, from_id: int) -> List[Relationship]:
        return self.session.query(Relationship).filter(
            Relationship.from_type == from_type,
            Relationship.from_id == from_id
        ).all()
    
    def get_relationships_to(self, to_type: str, to_id: int) -> List[Relationship]:
        return self.session.query(Relationship).filter(
            Relationship.to_type == to_type,
            Relationship.to_id == to_id
        ).all()
    
    def get_by_type(self, relationship_type: str) -> List[Relationship]:
        return self.session.query(Relationship).filter(
            Relationship.relationship_type == relationship_type
        ).all()
    
    def get_all(self) -> List[Relationship]:
        return self.session.query(Relationship).all()
    
    def update(self, entity: Relationship) -> Relationship:
        self.session.merge(entity)
        return entity
    
    def delete(self, entity_id: int):
        rel = self.get_by_id(entity_id)
        if rel:
            self.session.delete(rel)


class TaxonomyRepository(Repository):
    """Repository for Taxonomy entities"""
    
    def add(self, entity: Taxonomy) -> Taxonomy:
        self.session.add(entity)
        return entity
    
    def get_by_id(self, entity_id: int) -> Optional[Taxonomy]:
        return self.session.query(Taxonomy).filter(Taxonomy.id == entity_id).first()
    
    def get_by_category(self, category: str) -> List[Taxonomy]:
        return self.session.query(Taxonomy).filter(Taxonomy.category == category).all()
    
    def get_all(self) -> List[Taxonomy]:
        return self.session.query(Taxonomy).all()
    
    def update(self, entity: Taxonomy) -> Taxonomy:
        self.session.merge(entity)
        return entity
    
    def delete(self, entity_id: int):
        tax = self.get_by_id(entity_id)
        if tax:
            self.session.delete(tax)


# Factory Pattern: Database Session Factory
class DatabaseSessionFactory:
    """Factory for creating database sessions with dependency injection"""
    
    def __init__(self, connection_string: str, echo: bool = False, pool_size: int = 5):
        """
        Initialize database factory
        
        Args:
            connection_string: SQLAlchemy connection string
            echo: Whether to echo SQL statements
            pool_size: Connection pool size
        """
        self.connection_string = connection_string
        self.echo = echo
        
        # Create engine with appropriate settings
        if connection_string.startswith('sqlite'):
            # SQLite specific settings
            if ':memory:' in connection_string:
                pool_class = StaticPool
            else:
                pool_class = NullPool
                
            self.engine = create_engine(
                connection_string,
                echo=echo,
                connect_args={'check_same_thread': False},
                poolclass=pool_class
            )
        else:
            self.engine = create_engine(
                connection_string,
                echo=echo,
                pool_size=pool_size,
                max_overflow=10
            )
        
        self.SessionLocal = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)
    
    def create_tables(self):
        """Create all tables in database"""
        Base.metadata.create_all(self.engine)
    
    def drop_tables(self):
        """Drop all tables in database"""
        Base.metadata.drop_all(self.engine)
    
    def get_session(self) -> Session:
        """Get new database session"""
        return self.SessionLocal()
    
    def get_repositories(self, session: Session) -> dict:
        """Get all repositories for a session"""
        return {
            'module': ModuleRepository(session),
            'class': ClassRepository(session),
            'function': FunctionRepository(session),
            'relationship': RelationshipRepository(session),
            'taxonomy': TaxonomyRepository(session)
        }


# Unit of Work Pattern: Manage transactions
class UnitOfWork:
    """Unit of Work pattern for managing database transactions"""
    
    def __init__(self, session_factory: DatabaseSessionFactory):
        self.session_factory = session_factory
        self.session: Optional[Session] = None
        self.repositories: Optional[dict] = None
    
    def __enter__(self):
        self.session = self.session_factory.get_session()
        self.repositories = self.session_factory.get_repositories(self.session)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.session.rollback()
        self.session.close()
    
    def commit(self):
        """Commit all changes"""
        self.session.commit()
    
    def rollback(self):
        """Rollback all changes"""
        self.session.rollback()


# Example usage
if __name__ == '__main__':
    # Create database factory with dependency injection
    db_factory = DatabaseSessionFactory(
        connection_string="sqlite:///module_knowledge.db",
        echo=True
    )
    
    # Create tables
    db_factory.create_tables()
    
    # Use Unit of Work pattern
    with UnitOfWork(db_factory) as uow:
        # Add a module
        module = Module(
            name="collections",
            filepath="/usr/lib/python3.x/collections.py",
            is_package=False
        )
        uow.repositories['module'].add(module)
        uow.commit()
        
        print(f"Added module: {module}")
