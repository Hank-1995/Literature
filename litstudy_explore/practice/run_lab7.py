#!/usr/bin/env python3
"""
Simple runner script for Lab 7 Literature Search
===============================================

This script provides an easy way to run the literature search with different configurations.
"""

import sys
import os
import argparse
from datetime import datetime

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    parser = argparse.ArgumentParser(description='Run Lab 7 Literature Search')
    parser.add_argument('--queries', nargs='+', 
                       default=['AI literacy framework', 'academic writing'],
                       help='Search queries (default: AI literacy framework, academic writing)')
    parser.add_argument('--max-results', type=int, default=30,
                       help='Maximum results per database (default: 30)')
    parser.add_argument('--output-dir', default='lab7_output',
                       help='Output directory (default: lab7_output)')
    parser.add_argument('--scopus-key', 
                       default=os.getenv('SCOPUS_API_KEY', ''),
                       help='Scopus API key')
    parser.add_argument('--scopus-token',
                       default=os.getenv('SCOPUS_INST_TOKEN', ''), 
                       help='Scopus institutional token')
    parser.add_argument('--no-scopus', action='store_true',
                       help='Skip Scopus search (no API credentials needed)')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose logging')
    
    args = parser.parse_args()
    
    print("Lab 7 Literature Search Runner")
    print("=" * 40)
    print(f"Queries: {args.queries}")
    print(f"Max results per DB: {args.max_results}")
    print(f"Output directory: {args.output_dir}")
    print(f"Scopus search: {'Disabled' if args.no_scopus else 'Enabled'}")
    print("=" * 40)
    
    try:
        # Import and run the main search
        from lab7_literature_search import LiteratureSearch
        
        # Initialize search with or without Scopus credentials
        if args.no_scopus:
            search = LiteratureSearch()
        else:
            search = LiteratureSearch(
                scopus_api_key=args.scopus_key,
                scopus_inst_token=args.scopus_token
            )
        
        # Perform searches for all queries
        all_results = {}
        for i, query in enumerate(args.queries, 1):
            print(f"\nSearch {i}/{len(args.queries)}: '{query}'")
            print("-" * 40)
            
            results = search.search_all_databases(query, args.max_results)
            all_results[query] = results
            
            # Print summary
            total_papers = sum(len(doc_set) for doc_set in results.values())
            print(f"Total papers found: {total_papers}")
            for db_name, doc_set in results.items():
                print(f"  {db_name}: {len(doc_set)} papers")
        
        # Combine all results
        print(f"\nCombining all results...")
        search.combined_results = search.combined_results.__class__()
        for query_results in all_results.values():
            for db_results in query_results.values():
                search.combined_results.extend(db_results)
        
        print(f"Total combined papers: {len(search.combined_results)}")
        
        # Analyze and save results
        print(f"\nAnalyzing results...")
        analysis = search.analyze_results()
        
        print(f"\nAnalysis Summary:")
        print(f"  Total papers: {analysis.get('total_papers', 0)}")
        print(f"  Databases used: {', '.join(analysis.get('databases_used', []))}")
        print(f"  Papers per database: {analysis.get('papers_per_database', {})}")
        
        if analysis.get('year_distribution'):
            print(f"  Publication years: {len(analysis['year_distribution'])} unique years")
        
        if analysis.get('top_authors'):
            print(f"  Top authors: {len(analysis['top_authors'])} identified")
        
        # Save results
        print(f"\nSaving results to {args.output_dir}...")
        search.save_results(args.output_dir)
        
        # Generate plots
        print(f"Generating plots...")
        search.generate_plots(args.output_dir)
        
        print(f"\n{'='*60}")
        print(f"Lab 7 completed successfully!")
        print(f"Results saved to: {args.output_dir}")
        print(f"{'='*60}")
        
    except ImportError as e:
        print(f"Error: Could not import required modules: {e}")
        print("Please ensure all dependencies are installed:")
        print("pip install -r requirements_lab7.txt")
        sys.exit(1)
    except Exception as e:
        print(f"Error running Lab 7: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
