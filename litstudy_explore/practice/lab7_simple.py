#!/usr/bin/env python3
"""
Lab 7: Simple Literature Search Program
=======================================

This is a simplified version that demonstrates the core functionality
without complex dependencies that might cause import issues.
"""

import sys
import os
import json
import pandas as pd
from datetime import datetime
import requests
import feedparser
import logging
from typing import Dict, Any, Optional, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('lab7_simple.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SimpleLiteratureSearch:
    """
    A simplified literature search class that demonstrates core functionality.
    """
    
    def __init__(self):
        """Initialize the literature search."""
        self.results = {}
        self.combined_results = []
        
    def search_arxiv_simple(self, query: str, max_results: int = 50) -> List[Dict]:
        """
        Search arXiv using the simple API.
        
        Args:
            query: Search query string
            max_results: Maximum number of results to return
            
        Returns:
            List of dictionaries containing paper information
        """
        logger.info("Searching arXiv for: '%s'", query)
        
        try:
            # arXiv API endpoint
            url = f"http://export.arxiv.org/api/query"
            params = {
                'search_query': f'all:{query}',
                'start': 0,
                'max_results': max_results,
                'sortBy': 'relevance',
                'sortOrder': 'descending'
            }
            
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            
            # Parse the XML response
            feed = feedparser.parse(response.content)
            papers = []
            
            for entry in feed.entries:
                paper = {
                    'title': entry.title,
                    'authors': [author.name for author in entry.authors],
                    'abstract': entry.summary,
                    'published': entry.published,
                    'doi': entry.get('arxiv_doi', ''),
                    'source': 'arXiv',
                    'url': entry.link
                }
                papers.append(paper)
            
            logger.info("Found %d papers from arXiv", len(papers))
            return papers
            
        except Exception as e:
            logger.error("Error searching arXiv: %s", e)
            return []
    
    def search_crossref_simple(self, query: str, max_results: int = 50) -> List[Dict]:
        """
        Search CrossRef using their API.
        
        Args:
            query: Search query string
            max_results: Maximum number of results to return
            
        Returns:
            List of dictionaries containing paper information
        """
        logger.info("Searching CrossRef for: '%s'", query)
        
        try:
            # CrossRef API endpoint
            url = "https://api.crossref.org/works"
            params = {
                'query': query,
                'rows': min(max_results, 100),  # CrossRef limit
                'sort': 'relevance',
                'order': 'desc'
            }
            
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            papers = []
            
            for item in data.get('message', {}).get('items', []):
                paper = {
                    'title': item.get('title', [''])[0],
                    'authors': [author.get('given', '') + ' ' + author.get('family', '') 
                              for author in item.get('author', [])],
                    'abstract': item.get('abstract', ''),
                    'published': item.get('published-print', {}).get('date-parts', [[None]])[0],
                    'doi': item.get('DOI', ''),
                    'source': 'CrossRef',
                    'url': f"https://doi.org/{item.get('DOI', '')}"
                }
                papers.append(paper)
            
            logger.info("Found %d papers from CrossRef", len(papers))
            return papers
            
        except Exception as e:
            logger.error("Error searching CrossRef: %s", e)
            return []
    
    def search_all_databases(self, query: str, max_results_per_db: int = 30) -> Dict[str, List[Dict]]:
        """
        Search all available databases for the given query.
        
        Args:
            query: Search query string
            max_results_per_db: Maximum results per database
            
        Returns:
            Dictionary mapping database names to lists of papers
        """
        logger.info("Starting comprehensive search for: '%s'", query)
        
        results = {}
        
        # Search arXiv
        results['arxiv'] = self.search_arxiv_simple(query, max_results_per_db)
        
        # Search CrossRef
        results['crossref'] = self.search_crossref_simple(query, max_results_per_db)
        
        self.results = results
        return results
    
    def combine_results(self) -> List[Dict]:
        """
        Combine results from all databases into a single list.
        
        Returns:
            Combined list of papers
        """
        logger.info("Combining results from all databases")
        
        combined = []
        for db_name, results in self.results.items():
            if results:
                combined.extend(results)
                logger.info("Added %d papers from %s", len(results), db_name)
        
        self.combined_results = combined
        logger.info("Total combined papers: %d", len(combined))
        return combined
    
    def analyze_results(self) -> Dict[str, Any]:
        """
        Perform basic analysis on the combined results.
        
        Returns:
            Dictionary containing analysis results
        """
        if not self.combined_results:
            logger.warning("No results to analyze. Run search first.")
            return {}
        
        logger.info("Analyzing combined results")
        
        analysis = {}
        
        # Basic statistics
        analysis['total_papers'] = len(self.combined_results)
        analysis['databases_used'] = list(self.results.keys())
        analysis['papers_per_database'] = {db: len(results) for db, results in self.results.items()}
        
        # Year analysis
        years = []
        for paper in self.combined_results:
            if paper.get('published'):
                try:
                    if isinstance(paper['published'], list):
                        year = paper['published'][0] if paper['published'] else None
                    else:
                        year = paper['published'][:4] if len(str(paper['published'])) >= 4 else None
                    if year:
                        years.append(int(year))
                except (ValueError, TypeError, IndexError):
                    continue
        
        if years:
            analysis['year_range'] = [min(years), max(years)]
            analysis['unique_years'] = len(set(years))
        
        # Author analysis
        all_authors = []
        for paper in self.combined_results:
            authors = paper.get('authors', [])
            if isinstance(authors, list):
                all_authors.extend(authors)
        
        if all_authors:
            from collections import Counter
            author_counts = Counter(all_authors)
            analysis['top_authors'] = dict(author_counts.most_common(10))
            analysis['unique_authors'] = len(set(all_authors))
        
        return analysis
    
    def save_results(self, output_dir: str = "lab7_simple_output") -> None:
        """
        Save results to various formats.
        
        Args:
            output_dir: Directory to save output files
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save combined results as JSON
        json_file = os.path.join(output_dir, f"combined_results_{timestamp}.json")
        try:
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(self.combined_results, f, indent=2, ensure_ascii=False)
            logger.info("Results saved to %s", json_file)
        except Exception as e:
            logger.error("Error saving JSON results: %s", e)
        
        # Save analysis results
        analysis = self.analyze_results()
        analysis_file = os.path.join(output_dir, f"analysis_{timestamp}.json")
        try:
            with open(analysis_file, 'w', encoding='utf-8') as f:
                json.dump(analysis, f, indent=2, ensure_ascii=False)
            logger.info("Analysis saved to %s", analysis_file)
        except Exception as e:
            logger.error("Error saving analysis: %s", e)
        
        # Save as CSV
        try:
            csv_file = os.path.join(output_dir, f"papers_{timestamp}.csv")
            papers_data = []
            for paper in self.combined_results:
                paper_data = {
                    'title': paper.get('title', ''),
                    'authors': '; '.join(paper.get('authors', [])),
                    'published': str(paper.get('published', '')),
                    'abstract': paper.get('abstract', ''),
                    'doi': paper.get('doi', ''),
                    'source': paper.get('source', ''),
                    'url': paper.get('url', '')
                }
                papers_data.append(paper_data)
            
            df = pd.DataFrame(papers_data)
            df.to_csv(csv_file, index=False, encoding='utf-8')
            logger.info("Results saved to %s", csv_file)
        except Exception as e:
            logger.error("Error saving CSV: %s", e)


def main():
    """
    Main function to run the simple literature search.
    """
    print("=" * 60)
    print("Lab 7: Simple Literature Search")
    print("=" * 60)
    
    # Configuration
    SEARCH_QUERIES = [
        "AI literacy framework",
        "academic writing",
        "AI literacy education"
    ]
    
    MAX_RESULTS_PER_DB = 20
    
    # Initialize search
    search = SimpleLiteratureSearch()
    
    print(f"Search queries: {SEARCH_QUERIES}")
    print(f"Max results per database: {MAX_RESULTS_PER_DB}")
    print()
    
    # Perform searches
    all_results = {}
    for i, query in enumerate(SEARCH_QUERIES, 1):
        print(f"Search {i}/{len(SEARCH_QUERIES)}: '{query}'")
        print("-" * 40)
        
        results = search.search_all_databases(query, MAX_RESULTS_PER_DB)
        all_results[query] = results
        
        # Print summary for this query
        total_papers = sum(len(papers) for papers in results.values())
        print(f"Total papers found: {total_papers}")
        for db_name, papers in results.items():
            print(f"  {db_name}: {len(papers)} papers")
        print()
    
    # Combine all results
    print("Combining all results...")
    search.combined_results = []
    for query_results in all_results.values():
        for db_results in query_results.values():
            search.combined_results.extend(db_results)
    
    print(f"Total combined papers: {len(search.combined_results)}")
    print()
    
    # Analyze results
    print("Analyzing results...")
    analysis = search.analyze_results()
    
    print("Analysis Summary:")
    print(f"  Total papers: {analysis.get('total_papers', 0)}")
    print(f"  Databases used: {', '.join(analysis.get('databases_used', []))}")
    print(f"  Papers per database: {analysis.get('papers_per_database', {})}")
    
    if analysis.get('year_range'):
        print(f"  Publication years: {analysis['year_range'][0]}-{analysis['year_range'][1]}")
    
    if analysis.get('unique_authors'):
        print(f"  Unique authors: {analysis['unique_authors']}")
    
    print()
    
    # Save results
    print("Saving results...")
    search.save_results()
    
    print("=" * 60)
    print("Lab 7 completed successfully!")
    print("Check the 'lab7_simple_output' directory for results.")
    print("=" * 60)


if __name__ == "__main__":
    main()
