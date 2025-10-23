"""
Configuration file for Lab 7 Literature Search
==============================================

This file contains configuration settings and API credentials.
In production, these should be stored as environment variables.
"""

import os

# API Credentials
# For security, set these as environment variables:
# export SCOPUS_API_KEY="your_api_key"
# export SCOPUS_INST_TOKEN="your_institutional_token"

SCOPUS_API_KEY = os.getenv('SCOPUS_API_KEY', '')
SCOPUS_INST_TOKEN = os.getenv('SCOPUS_INST_TOKEN', '')

# Search Configuration
DEFAULT_QUERIES = [
    "AI literacy framework",
    "academic writing",
    "AI literacy education"
]

DEFAULT_MAX_RESULTS = 30
DEFAULT_OUTPUT_DIR = "lab7_output"

# Database Configuration
ENABLED_DATABASES = ['arxiv', 'crossref', 'scopus']

# Logging Configuration
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
