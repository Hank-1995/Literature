#!/usr/bin/env python3
"""
Secure Credentials Setup for Lab 7
==================================

This script helps you set up your Scopus API credentials securely.
"""

import os
import sys

def setup_credentials():
    """Interactive setup for Scopus API credentials."""
    print("Lab 7: Secure Credentials Setup")
    print("=" * 40)
    print()
    print("This script will help you set up your Scopus API credentials securely.")
    print("Your credentials will be stored as environment variables.")
    print()
    
    # Get Scopus API Key
    api_key = input("Enter your Scopus API Key: ").strip()
    if not api_key:
        print("Error: API Key is required.")
        return False
    
    # Get Scopus Institutional Token
    inst_token = input("Enter your Scopus Institutional Token: ").strip()
    if not inst_token:
        print("Error: Institutional Token is required.")
        return False
    
    # Set environment variables for current session
    os.environ['SCOPUS_API_KEY'] = api_key
    os.environ['SCOPUS_INST_TOKEN'] = inst_token
    
    print()
    print("✅ Credentials set for current session!")
    print()
    print("To make these permanent, add to your shell profile:")
    print(f"export SCOPUS_API_KEY='{api_key}'")
    print(f"export SCOPUS_INST_TOKEN='{inst_token}'")
    print()
    print("Or create a .env file in this directory with:")
    print(f"SCOPUS_API_KEY={api_key}")
    print(f"SCOPUS_INST_TOKEN={inst_token}")
    print()
    
    return True

def test_credentials():
    """Test if credentials are working."""
    api_key = os.getenv('SCOPUS_API_KEY')
    inst_token = os.getenv('SCOPUS_INST_TOKEN')
    
    if not api_key or not inst_token:
        print("❌ Credentials not found. Run setup first.")
        return False
    
    print("Testing Scopus API connection...")
    try:
        import requests
        
        url = "https://api.elsevier.com/content/search/scopus"
        headers = {
            'Accept': 'application/json',
            'X-ELS-APIKey': api_key
        }
        if inst_token:
            headers['X-ELS-Insttoken'] = inst_token
        
        params = {
            'query': 'test',
            'count': 1
        }
        
        response = requests.get(url, headers=headers, params=params, timeout=10)
        
        if response.status_code == 200:
            print("✅ Scopus API connection successful!")
            return True
        else:
            print(f"❌ Scopus API error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return False

def main():
    """Main function."""
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test_credentials()
    else:
        if setup_credentials():
            print("Would you like to test the credentials? (y/n): ", end='')
            if input().lower().startswith('y'):
                test_credentials()

if __name__ == "__main__":
    main()
