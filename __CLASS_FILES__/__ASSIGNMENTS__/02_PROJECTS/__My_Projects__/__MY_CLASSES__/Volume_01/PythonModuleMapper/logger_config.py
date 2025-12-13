import logging
import sys
from logging.handlers import RotatingFileHandler
import os

def setup_logging(log_file='system.log', log_level=logging.INFO, console_level=logging.INFO):
    """
    Sets up the logging configuration for the application.
    
    Args:
        log_file (str): Path to the log file.
        log_level (int): Logging level for the file handler.
        console_level (int): Logging level for the console handler.
    """
    
    # Create a custom logger
    logger = logging.getLogger("PythonModuleMapper")
    logger.setLevel(logging.DEBUG) # Capture everything at the root level, handlers filter it

    # Create handlers
    c_handler = logging.StreamHandler(sys.stdout)
    f_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=5)

    # Set levels for handlers
    c_handler.setLevel(console_level)
    f_handler.setLevel(log_level)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(levelname)s: %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    # Check if handlers already exist to avoid duplicates
    if not logger.handlers:
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

    return logger

def get_logger(name):
    """
    Returns a child logger with the given name.
    """
    return logging.getLogger(f"PythonModuleMapper.{name}")
