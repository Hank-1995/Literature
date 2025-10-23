#!/usr/bin/env python3
"""
Lab 7: Literature Search using litstudy
=======================================

This program demonstrates how to use the litstudy module to search academic databases
for papers related to "AI literacy framework" and "academic writing".

Functions used:
- search_arxiv(): Search arXiv database
- search_crossref(): Search CrossRef database  
- search_scopus(): Search Scopus database (requires API credentials)

Output: Structured dataset of papers with metadata (title, authors, venue, year, abstract, citations)
"""

import sys
import os
import json
import pandas as pd
from datetime import datetime
from typing import Dict, Any, Optional
import logging

# Add the litstudy module to the path
sys.path.append('/Users/simonwang/Documents/Usage/HKUworkshop/agent4hku/litstudy_explore/scripts/litstudy')

# Import configuration
try:
    from config import SCOPUS_API_KEY as CONFIG_SCOPUS_API_KEY, SCOPUS_INST_TOKEN as CONFIG_SCOPUS_INST_TOKEN, DEFAULT_QUERIES, DEFAULT_MAX_RESULTS
except ImportError:
    # Fallback if config file is not available
    CONFIG_SCOPUS_API_KEY = os.getenv('SCOPUS_API_KEY', '')
    CONFIG_SCOPUS_INST_TOKEN = os.getenv('SCOPUS_INST_TOKEN', '')
    DEFAULT_QUERIES = ["AI literacy framework", "academic writing"]
    DEFAULT_MAX_RESULTS = 30

try:
    from litstudy import (
        search_arxiv, 
        search_crossref, 
        search_scopus,
        DocumentSet,
        compute_year_histogram,
        compute_author_histogram,
        plot_year_histogram,
        plot_author_histogram
    )
except ImportError as e:
    print(f"Error importing litstudy: {e}")
    print("Please ensure the litstudy module is properly installed.")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('lab7_search.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class LiteratureSearch:
    """
    A class to handle literature searches across multiple academic databases.
    """
    
    def __init__(self, scopus_api_key: Optional[str] = None, scopus_inst_token: Optional[str] = None):
        """
        Initialize the literature search with API credentials.
        
        Args:
            scopus_api_key: Scopus API key for authentication
            scopus_inst_token: Scopus institutional token
        """
        self.scopus_api_key = scopus_api_key
        self.scopus_inst_token = scopus_inst_token
        self.results = {}
        self.combined_results = DocumentSet()
        
    def search_arxiv_papers(self, query: str, max_results: int = 50) -> DocumentSet:
        """
        Search arXiv database for papers matching the query.
        
        Args:
            query: Search query string
            max_results: Maximum number of results to return
            
        Returns:
            DocumentSet containing arXiv papers
        """
        logger.info("Searching arXiv for: '%s'", query)
        try:
            results = search_arxiv(query, max_results=max_results)
            logger.info("Found %d papers from arXiv", len(results))
            return results
        except (ConnectionError, TimeoutError, ValueError) as e:
            logger.error("Error searching arXiv: %s", e)
            return DocumentSet()
    
    def search_crossref_papers(self, query: str, max_results: int = 50) -> DocumentSet:
        """
        Search CrossRef database for papers matching the query.
        
        Args:
            query: Search query string
            max_results: Maximum number of results to return
            
        Returns:
            DocumentSet containing CrossRef papers
        """
        logger.info("Searching CrossRef for: '%s'", query)
        try:
            results = search_crossref(query, max_results=max_results)
            logger.info("Found %d papers from CrossRef", len(results))
            return results
        except (ConnectionError, TimeoutError, ValueError) as e:
            logger.error("Error searching CrossRef: %s", e)
            return DocumentSet()
    
    def search_scopus_papers(self, query: str, max_results: int = 50) -> DocumentSet:
        """
        Search Scopus database for papers matching the query.
        
        Args:
            query: Search query string
            max_results: Maximum number of results to return
            
        Returns:
            DocumentSet containing Scopus papers
        """
        if not self.scopus_api_key:
            logger.warning("Scopus API key not provided. Skipping Scopus search.")
            return DocumentSet()
            
        logger.info("Searching Scopus for: '%s'", query)
        try:
            results = search_scopus(
                query, 
                api_key=self.scopus_api_key,
                inst_token=self.scopus_inst_token,
                max_results=max_results
            )
            logger.info("Found %d papers from Scopus", len(results))
            return results
        except (ConnectionError, TimeoutError, ValueError) as e:
            logger.error("Error searching Scopus: %s", e)
            return DocumentSet()
    
    def search_all_databases(self, query: str, max_results_per_db: int = 50) -> Dict[str, DocumentSet]:
        """
        Search all available databases for the given query.
        
        Args:
            query: Search query string
            max_results_per_db: Maximum results per database
            
        Returns:
            Dictionary mapping database names to DocumentSets
        """
        logger.info("Starting comprehensive search for: '%s'", query)
        
        results = {}
        
        # Search arXiv
        results['arxiv'] = self.search_arxiv_papers(query, max_results_per_db)
        
        # Search CrossRef
        results['crossref'] = self.search_crossref_papers(query, max_results_per_db)
        
        # Search Scopus (if credentials available)
        results['scopus'] = self.search_scopus_papers(query, max_results_per_db)
        
        self.results = results
        return results
    
    def combine_results(self) -> DocumentSet:
        """
        Combine results from all databases into a single DocumentSet.
        
        Returns:
            Combined DocumentSet
        """
        logger.info("Combining results from all databases")
        
        combined = DocumentSet()
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
        
        # Year distribution
        try:
            year_hist = compute_year_histogram(self.combined_results)
            analysis['year_distribution'] = dict(year_hist)
        except (ValueError, AttributeError) as e:
            logger.error("Error computing year histogram: %s", e)
            analysis['year_distribution'] = {}
        
        # Author distribution
        try:
            author_hist = compute_author_histogram(self.combined_results)
            analysis['top_authors'] = dict(list(author_hist.items())[:10])  # Top 10 authors
        except (ValueError, AttributeError) as e:
            logger.error("Error computing author histogram: %s", e)
            analysis['top_authors'] = {}
        
        # Basic statistics
        analysis['total_papers'] = len(self.combined_results)
        analysis['databases_used'] = list(self.results.keys())
        analysis['papers_per_database'] = {db: len(results) for db, results in self.results.items()}
        
        return analysis
    
    def save_results(self, output_dir: str = "lab7_output") -> None:
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
                # Convert DocumentSet to serializable format
                results_data = []
                for doc in self.combined_results:
                    doc_data = {
                        'title': doc.title,
                        'authors': [author.name for author in doc.authors],
                        'publication_date': str(doc.publication_date) if doc.publication_date else None,
                        'abstract': doc.abstract,
                        'doi': doc.doi,
                        'venue': getattr(doc, 'venue', None),
                        'citations': getattr(doc, 'citations', None)
                    }
                    results_data.append(doc_data)
                
                json.dump(results_data, f, indent=2, ensure_ascii=False)
            logger.info("Results saved to %s", json_file)
        except (IOError, OSError, TypeError, ValueError) as e:
            logger.error("Error saving JSON results: %s", e)
        
        # Save analysis results
        analysis = self.analyze_results()
        analysis_file = os.path.join(output_dir, f"analysis_{timestamp}.json")
        try:
            with open(analysis_file, 'w', encoding='utf-8') as f:
                json.dump(analysis, f, indent=2, ensure_ascii=False)
            logger.info("Analysis saved to %s", analysis_file)
        except (IOError, OSError, TypeError, ValueError) as e:
            logger.error("Error saving analysis: %s", e)
        
        # Save as CSV (if possible)
        try:
            csv_file = os.path.join(output_dir, f"papers_{timestamp}.csv")
            papers_data = []
            for doc in self.combined_results:
                paper_data = {
                    'title': doc.title,
                    'authors': '; '.join([author.name for author in doc.authors]),
                    'publication_date': str(doc.publication_date) if doc.publication_date else '',
                    'abstract': doc.abstract or '',
                    'doi': doc.doi or '',
                    'venue': getattr(doc, 'venue', '') or '',
                    'citations': getattr(doc, 'citations', '') or ''
                }
                papers_data.append(paper_data)
            
            df = pd.DataFrame(papers_data)
            df.to_csv(csv_file, index=False, encoding='utf-8')
            logger.info("Results saved to %s", csv_file)
        except (IOError, OSError, pd.errors.EmptyDataError) as e:
            logger.error("Error saving CSV: %s", e)
    
    def generate_plots(self, output_dir: str = "lab7_output") -> None:
        """
        Generate visualization plots for the results.
        
        Args:
            output_dir: Directory to save plot files
        """
        if not self.combined_results:
            logger.warning("No results to plot. Run search first.")
            return
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        try:
            # Year distribution plot
            year_plot_file = os.path.join(output_dir, f"year_distribution_{timestamp}.png")
            plot_year_histogram(self.combined_results, save_path=year_plot_file)
            logger.info("Year distribution plot saved to %s", year_plot_file)
        except (IOError, OSError, ImportError) as e:
            logger.error("Error creating year distribution plot: %s", e)
        
        try:
            # Author distribution plot
            author_plot_file = os.path.join(output_dir, f"author_distribution_{timestamp}.png")
            plot_author_histogram(self.combined_results, save_path=author_plot_file)
            logger.info("Author distribution plot saved to %s", author_plot_file)
        except (IOError, OSError, ImportError) as e:
            logger.error("Error creating author distribution plot: %s", e)


def main():
    """
    Main function to run the literature search.
    """
    print("=" * 60)
    print("Lab 7: Literature Search using litstudy")
    print("=" * 60)
    
    # Configuration
    SEARCH_QUERIES = DEFAULT_QUERIES
    MAX_RESULTS_PER_DB = DEFAULT_MAX_RESULTS
    
    # Initialize search
    search = LiteratureSearch(
        scopus_api_key=CONFIG_SCOPUS_API_KEY,
        scopus_inst_token=CONFIG_SCOPUS_INST_TOKEN
    )
    
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
        total_papers = sum(len(doc_set) for doc_set in results.values())
        print(f"Total papers found: {total_papers}")
        for db_name, doc_set in results.items():
            print(f"  {db_name}: {len(doc_set)} papers")
        print()
    
    # Combine all results
    print("Combining all results...")
    search.combined_results = DocumentSet()
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
    
    if analysis.get('year_distribution'):
        print(f"  Publication years: {len(analysis['year_distribution'])} unique years")
    
    if analysis.get('top_authors'):
        print(f"  Top authors: {len(analysis['top_authors'])} identified")
    
    print()
    
    # Save results
    print("Saving results...")
    search.save_results()
    
    # Generate plots
    print("Generating plots...")
    search.generate_plots()
    
    print("=" * 60)
    print("Lab 7 completed successfully!")
    print("Check the 'lab7_output' directory for results.")
    print("=" * 60)


if __name__ == "__main__":
    main()
