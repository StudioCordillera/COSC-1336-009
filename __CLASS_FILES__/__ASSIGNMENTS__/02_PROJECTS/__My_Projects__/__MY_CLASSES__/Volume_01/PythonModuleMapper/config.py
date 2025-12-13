# Configuration Management
# Using Strategy Pattern for environment-based configuration

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Any, Optional
from abc import ABC, abstractmethod


@dataclass
class DatabaseConfig:
    """Database configuration using dependency injection"""
    connection_string: str
    pool_size: int = 5
    echo: bool = False
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DatabaseConfig':
        return cls(**data)


@dataclass
class APIConfig:
    """API configuration"""
    host: str = "127.0.0.1"
    port: int = 5000
    workers: int = 4
    queue_size: int = 100
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'APIConfig':
        return cls(**data)


@dataclass
class ObsidianConfig:
    """Obsidian vault configuration"""
    vault_path: Path
    modules_folder: str = "Modules"
    classes_folder: str = "Classes"
    functions_folder: str = "Functions"
    taxonomy_folder: str = "Taxonomy"
    relationships_folder: str = "Relationships"
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ObsidianConfig':
        data['vault_path'] = Path(data['vault_path'])
        return cls(**data)


@dataclass
class ScannerConfig:
    """Module scanner configuration"""
    scan_paths: list[Path] = field(default_factory=list)
    excluded_patterns: list[str] = field(default_factory=list)
    max_depth: int = 10
    batch_size: int = 50
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ScannerConfig':
        data['scan_paths'] = [Path(p) for p in data.get('scan_paths', [])]
        return cls(**data)


@dataclass
class TaxonomyConfig:
    """Taxonomy categorization configuration"""
    category_definitions: Dict[str, list[str]] = field(default_factory=dict)
    custom_mappings: Dict[str, str] = field(default_factory=dict)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TaxonomyConfig':
        return cls(**data)


# Strategy Pattern: Configuration Loading Strategy
class ConfigLoadStrategy(ABC):
    """Abstract strategy for loading configuration"""
    
    @abstractmethod
    def load(self, source: Any) -> Dict[str, Any]:
        """Load configuration from source"""
        pass


class JsonConfigLoader(ConfigLoadStrategy):
    """Load configuration from JSON file"""
    
    def load(self, source: Path) -> Dict[str, Any]:
        import json
        with open(source, 'r') as f:
            return json.load(f)


class YamlConfigLoader(ConfigLoadStrategy):
    """Load configuration from YAML file"""
    
    def load(self, source: Path) -> Dict[str, Any]:
        try:
            import yaml
            with open(source, 'r') as f:
                return yaml.safe_load(f)
        except ImportError:
            raise ImportError("PyYAML required for YAML config files")


class EnvConfigLoader(ConfigLoadStrategy):
    """Load configuration from environment variables"""
    
    def load(self, source: Optional[str] = None) -> Dict[str, Any]:
        import os
        prefix = source or "MODMAPPER_"
        
        config = {}
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                config[config_key] = value
        
        return config


# Builder Pattern: Application Configuration Builder
class ApplicationConfigBuilder:
    """Build complete application configuration using Builder pattern"""
    
    def __init__(self):
        self._config: Dict[str, Any] = {}
        self._loader_strategy: Optional[ConfigLoadStrategy] = None
    
    def with_loader_strategy(self, strategy: ConfigLoadStrategy) -> 'ApplicationConfigBuilder':
        """Set configuration loading strategy"""
        self._loader_strategy = strategy
        return self
    
    def load_from_file(self, filepath: Path) -> 'ApplicationConfigBuilder':
        """Load configuration from file"""
        if not self._loader_strategy:
            # Auto-detect based on extension
            if filepath.suffix == '.json':
                self._loader_strategy = JsonConfigLoader()
            elif filepath.suffix in ['.yaml', '.yml']:
                self._loader_strategy = YamlConfigLoader()
            else:
                raise ValueError(f"Unsupported config file type: {filepath.suffix}")
        
        self._config = self._loader_strategy.load(filepath)
        return self
    
    def load_from_env(self, prefix: str = "MODMAPPER_") -> 'ApplicationConfigBuilder':
        """Load configuration from environment variables"""
        loader = EnvConfigLoader()
        env_config = loader.load(prefix)
        self._config.update(env_config)
        return self
    
    def with_database(self, db_config: DatabaseConfig) -> 'ApplicationConfigBuilder':
        """Add database configuration"""
        self._config['database'] = db_config
        return self
    
    def with_api(self, api_config: APIConfig) -> 'ApplicationConfigBuilder':
        """Add API configuration"""
        self._config['api'] = api_config
        return self
    
    def with_obsidian(self, obsidian_config: ObsidianConfig) -> 'ApplicationConfigBuilder':
        """Add Obsidian configuration"""
        self._config['obsidian'] = obsidian_config
        return self
    
    def with_scanner(self, scanner_config: ScannerConfig) -> 'ApplicationConfigBuilder':
        """Add scanner configuration"""
        self._config['scanner'] = scanner_config
        return self
    
    def with_taxonomy(self, taxonomy_config: TaxonomyConfig) -> 'ApplicationConfigBuilder':
        """Add taxonomy configuration"""
        self._config['taxonomy'] = taxonomy_config
        return self
    
    def build(self) -> 'ApplicationConfig':
        """Build final configuration object"""
        return ApplicationConfig(
            database=self._config.get('database') or DatabaseConfig.from_dict(
                self._config.get('database_config', {})
            ),
            api=self._config.get('api') or APIConfig.from_dict(
                self._config.get('api_config', {})
            ),
            obsidian=self._config.get('obsidian') or ObsidianConfig.from_dict(
                self._config.get('obsidian_config', {})
            ),
            scanner=self._config.get('scanner') or ScannerConfig.from_dict(
                self._config.get('scanner_config', {})
            ),
            taxonomy=self._config.get('taxonomy') or TaxonomyConfig.from_dict(
                self._config.get('taxonomy_config', {})
            )
        )


@dataclass
class ApplicationConfig:
    """Complete application configuration with dependency injection"""
    database: DatabaseConfig
    api: APIConfig
    obsidian: ObsidianConfig
    scanner: ScannerConfig
    taxonomy: TaxonomyConfig
    
    @classmethod
    def create_default(cls) -> 'ApplicationConfig':
        """Create default configuration"""
        return cls(
            database=DatabaseConfig(
                connection_string="sqlite:///module_knowledge.db"
            ),
            api=APIConfig(),
            obsidian=ObsidianConfig(
                vault_path=Path("./PythonModules")
            ),
            scanner=ScannerConfig(),
            taxonomy=TaxonomyConfig(
                category_definitions={
                    'constructors': ['__init__', '__new__'],
                    'magic_methods': ['__str__', '__repr__', '__call__', '__len__'],
                    'decorators': ['property', 'staticmethod', 'classmethod'],
                    'data_structures': ['list', 'dict', 'set', 'tuple'],
                    'control_flow': ['if', 'for', 'while', 'try', 'except'],
                    'io_operations': ['open', 'read', 'write', 'close']
                }
            )
        )
    
    @classmethod
    def from_file(cls, config_path: Path) -> 'ApplicationConfig':
        """Load configuration from file using builder"""
        builder = ApplicationConfigBuilder()
        return builder.load_from_file(config_path).build()
    
    @classmethod
    def from_env(cls, prefix: str = "MODMAPPER_") -> 'ApplicationConfig':
        """Load configuration from environment variables"""
        builder = ApplicationConfigBuilder()
        return builder.load_from_env(prefix).build()


# Example usage
if __name__ == '__main__':
    # Using Builder pattern with fluent interface
    config = (ApplicationConfigBuilder()
              .with_database(DatabaseConfig(
                  connection_string="sqlite:///test.db",
                  echo=True
              ))
              .with_api(APIConfig(
                  host="0.0.0.0",
                  port=8080
              ))
              .build())
    
    print(f"Database: {config.database.connection_string}")
    print(f"API: {config.api.host}:{config.api.port}")
