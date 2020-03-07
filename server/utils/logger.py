"""This module abstracts logging configuration"""
# ---------------------------------------------
# System modules
# ---------------------------------------------
import logging

# ---------------------------------------------
# External dependencies
# ---------------------------------------------
# ---------------------------------------------
# Local dependencies
# ---------------------------------------------
import coloredlogs

# ---------------------------------------------


logging.basicConfig(level=logging.INFO)
logging.getLogger("html_tools").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)
coloredlogs.install(level="INFO", logger=logger)
