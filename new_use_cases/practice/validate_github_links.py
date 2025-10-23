#!/usr/bin/env python3
"""
Script to validate GitHub repository links from the CSV file
"""

import csv
import requests
import time
from urllib.parse import urlparse

def validate_github_url(url):
    """Validate if a GitHub URL is accessible"""
    try:
        # Add a small delay to avoid rate limiting
        time.sleep(0.5)
        
        # Set headers to mimic a browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            return True, "Valid"
        elif response.status_code == 404:
            return False, "Repository not found"
        elif response.status_code == 403:
            return False, "Access forbidden (private repo or rate limited)"
        else:
            return False, f"HTTP {response.status_code}"
            
    except requests.exceptions.Timeout:
        return False, "Timeout"
    except requests.exceptions.ConnectionError:
        return False, "Connection error"
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    input_file = 'academic_research_repos_verified.csv'
    output_file = 'academic_research_repos_validated.csv'
    
    print("Validating GitHub repository links...")
    print("=" * 50)
    
    validated_repos = []
    
    with open(input_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            repo_name = row['Repository Name']
            github_link = row['GitHub Link']
            
            print(f"Validating: {repo_name}")
            print(f"URL: {github_link}")
            
            is_valid, status = validate_github_url(github_link)
            
            print(f"Status: {status}")
            print("-" * 30)
            
            # Add validation status to the row
            row['Validation Status'] = status
            row['Is Valid'] = is_valid
            
            validated_repos.append(row)
    
    # Write validated results to new CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Repository Name', 'Basic Functions', 'GitHub Link', 'Validation Status', 'Is Valid']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in validated_repos:
            # Only write the fields that are in fieldnames
            filtered_row = {k: v for k, v in row.items() if k in fieldnames}
            writer.writerow(filtered_row)
    
    # Print summary
    valid_count = sum(1 for row in validated_repos if row['Is Valid'])
    total_count = len(validated_repos)
    
    print(f"\nValidation Summary:")
    print(f"Total repositories: {total_count}")
    print(f"Valid repositories: {valid_count}")
    print(f"Invalid repositories: {total_count - valid_count}")
    print(f"\nResults saved to: {output_file}")

if __name__ == "__main__":
    main()
