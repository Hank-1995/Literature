#!/usr/bin/env python3
"""
Test script for Lab 7 Literature Search
=======================================

This script tests the basic functionality of the literature search program
without making actual API calls.
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all required modules can be imported."""
    print("Testing imports...")
    
    try:
        import pandas as pd
        print("✓ pandas imported successfully")
    except ImportError as e:
        print(f"✗ Error importing pandas: {e}")
        return False
    
    try:
        import json
        print("✓ json imported successfully")
    except ImportError as e:
        print(f"✗ Error importing json: {e}")
        return False
    
    try:
        from lab7_literature_search import LiteratureSearch
        print("✓ LiteratureSearch class imported successfully")
    except ImportError as e:
        print(f"✗ Error importing LiteratureSearch: {e}")
        return False
    
    return True

def test_config():
    """Test configuration loading."""
    print("\nTesting configuration...")
    
    try:
        from config import SCOPUS_API_KEY, SCOPUS_INST_TOKEN, DEFAULT_QUERIES
        print("✓ Configuration loaded successfully")
        print(f"  Default queries: {DEFAULT_QUERIES}")
        print(f"  Scopus API key available: {'Yes' if SCOPUS_API_KEY else 'No'}")
        return True
    except ImportError as e:
        print(f"✗ Error loading configuration: {e}")
        return False

def test_literature_search_init():
    """Test LiteratureSearch initialization."""
    print("\nTesting LiteratureSearch initialization...")
    
    try:
        from lab7_literature_search import LiteratureSearch
        
        # Test initialization without credentials
        search = LiteratureSearch()
        print("✓ LiteratureSearch initialized without credentials")
        
        # Test initialization with credentials
        search_with_creds = LiteratureSearch(
            scopus_api_key="test_key",
            scopus_inst_token="test_token"
        )
        print("✓ LiteratureSearch initialized with credentials")
        
        return True
    except Exception as e:
        print(f"✗ Error initializing LiteratureSearch: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality without API calls."""
    print("\nTesting basic functionality...")
    
    try:
        from lab7_literature_search import LiteratureSearch
        
        search = LiteratureSearch()
        
        # Test that methods exist
        assert hasattr(search, 'search_arxiv_papers'), "search_arxiv_papers method missing"
        assert hasattr(search, 'search_crossref_papers'), "search_crossref_papers method missing"
        assert hasattr(search, 'search_scopus_papers'), "search_scopus_papers method missing"
        assert hasattr(search, 'combine_results'), "combine_results method missing"
        assert hasattr(search, 'analyze_results'), "analyze_results method missing"
        assert hasattr(search, 'save_results'), "save_results method missing"
        assert hasattr(search, 'generate_plots'), "generate_plots method missing"
        
        print("✓ All required methods are present")
        return True
    except Exception as e:
        print(f"✗ Error testing functionality: {e}")
        return False

def main():
    """Run all tests."""
    print("Lab 7 Literature Search - Test Suite")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_config,
        test_literature_search_init,
        test_basic_functionality
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✓ All tests passed! The program is ready to use.")
        return True
    else:
        print("✗ Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
