"""
CLI Interface for Python Module Mapper

Command-line interface to control the scanner, API, and vault generation.
Uses Command pattern for extensible CLI operations.
"""

import argparse
import asyncio
import sys
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Optional
import logging

# Import components
from models import DatabaseSessionFactory
from graph import RelationshipGraphBuilder
from query import QueryInterface, TextFormatter, JSONFormatter, MarkdownFormatter
from scanner import ScanModuleCommand
from logger_config import setup_logging, get_logger
import json

# Import scripts as modules
import populate_db
import generate_vault

logger = get_logger("cli")

class CLICommand(ABC):
    """Abstract base class for CLI commands"""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Command name"""
        pass
        
    @property
    @abstractmethod
    def description(self) -> str:
        """Command description"""
        pass
        
    @abstractmethod
    def configure_parser(self, parser: argparse.ArgumentParser):
        """Configure argument parser"""
        pass
        
    @abstractmethod
    def execute(self, args: argparse.Namespace):
        """Execute the command"""
        pass

class ScanCommand(CLICommand):
    """Command to scan a single module"""
    
    @property
    def name(self) -> str:
        return "scan"
        
    @property
    def description(self) -> str:
        return "Scan a single module and output JSON"
        
    def configure_parser(self, parser: argparse.ArgumentParser):
        parser.add_argument("module", help="Module name to scan")
        
    def execute(self, args: argparse.Namespace):
        logger.info(f"Scanning module '{args.module}'...")
        command = ScanModuleCommand(args.module)
        result = command.execute()
        
        if result['success']:
            print(json.dumps(result['data'], indent=2, default=str))
        else:
            logger.error(f"Error: {result.get('error')}")

class PopulateCommand(CLICommand):
    """Command to populate database from standard library"""
    
    @property
    def name(self) -> str:
        return "populate"
        
    @property
    def description(self) -> str:
        return "Populate database with standard library modules"
        
    def configure_parser(self, parser: argparse.ArgumentParser):
        parser.add_argument("--db", default="python_modules.db", help="Database file path")
        
    def execute(self, args: argparse.Namespace):
        logger.info("Starting database population...")
        db_path = Path(args.db)
        asyncio.run(populate_db.populate(db_path))

class GenerateVaultCommand(CLICommand):
    """Command to generate Obsidian vault"""
    
    @property
    def name(self) -> str:
        return "generate-vault"
        
    @property
    def description(self) -> str:
        return "Generate Obsidian vault from database"
        
    def configure_parser(self, parser: argparse.ArgumentParser):
        parser.add_argument("--db", default="python_modules.db", help="Database file path")
        parser.add_argument("--out", default=None, help="Vault root directory")
        
    def execute(self, args: argparse.Namespace):
        logger.info("Starting vault generation...")
        db_path = Path(args.db)
        vault_root = Path(args.out) if args.out else None
        generate_vault.main(db_path, vault_root)

class QueryCommand(CLICommand):
    """Command to query the knowledge graph"""
    
    @property
    def name(self) -> str:
        return "query"
        
    @property
    def description(self) -> str:
        return "Query the knowledge graph"
        
    def configure_parser(self, parser: argparse.ArgumentParser):
        parser.add_argument("term", help="Search term")
        parser.add_argument("--type", choices=["module", "class", "function", "all"], default="all", help="Filter by type")
        parser.add_argument("--format", choices=["text", "json", "markdown"], default="text", help="Output format")
        parser.add_argument("--db", default="python_modules.db", help="Database file path")
        
    def execute(self, args: argparse.Namespace):
        db_path = Path(args.db)
        if not db_path.exists():
            logger.error(f"Error: Database {db_path} not found.")
            return
            
        db_url = f"sqlite:///{db_path}"
        session_factory = DatabaseSessionFactory(db_url)
        graph_builder = RelationshipGraphBuilder(session_factory)
        query_interface = QueryInterface(graph_builder)
        
        logger.info(f"Searching for '{args.term}'...")
        
        # Execute search
        if args.type == "all":
            results = query_interface.search_by_name(args.term)
        else:
            # TODO: Add specific type search to QueryInterface if needed, 
            # for now filtering results manually or using search_by_name which returns all
            results = query_interface.search_by_name(args.term)
            results = results.filter(lambda n: n.type == args.type)
            
        # Format results
        if args.format == "json":
            formatter = JSONFormatter()
        elif args.format == "markdown":
            formatter = MarkdownFormatter()
        else:
            formatter = TextFormatter()
            
        print(formatter.format(results))

class CLI:
    """CLI Invoker"""
    
    def __init__(self):
        self.commands: List[CLICommand] = [
            ScanCommand(),
            PopulateCommand(),
            GenerateVaultCommand(),
            QueryCommand()
        ]
        
    def run(self):
        parser = argparse.ArgumentParser(description="Python Module Mapper CLI")
        parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose logging")
        subparsers = parser.add_subparsers(dest="command", help="Command to execute")
        
        # Register commands
        for command in self.commands:
            cmd_parser = subparsers.add_parser(command.name, help=command.description)
            command.configure_parser(cmd_parser)
            
        args = parser.parse_args()
        
        # Setup logging
        log_level = logging.DEBUG if args.verbose else logging.INFO
        setup_logging(log_level=logging.DEBUG, console_level=log_level)
        
        if not args.command:
            parser.print_help()
            return
            
        # Find and execute command
        for command in self.commands:
            if command.name == args.command:
                try:
                    command.execute(args)
                except Exception as e:
                    logger.exception(f"Command '{command.name}' failed: {e}")
                    sys.exit(1)
                return

if __name__ == "__main__":
    cli = CLI()
    cli.run()
