#!/usr/bin/env python3
"""
Lab 8: Literature Study Analysis
Performs data cleaning, organization, and bibliometric analysis on Scopus data
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import json

# Add the litstudy library to the path
sys.path.append('/Users/simonwang/Documents/Usage/HKUworkshop/agent4hku/litstudy_explore/scripts/litstudy')

try:
    from litstudy import (
        load_scopus_csv, 
        compute_year_histogram,
        compute_author_histogram,
        compute_source_histogram,
        compute_affiliation_histogram,
        compute_country_histogram,
        plot_year_histogram,
        plot_author_histogram,
        plot_source_histogram,
        plot_affiliation_histogram,
        plot_country_histogram,
        build_corpus,
        compute_word_distribution,
        plot_word_distribution,
        plot_topic_clouds,
        build_coauthor_network,
        plot_coauthor_network
    )
    print("✅ Successfully imported litstudy library")
except ImportError as e:
    print(f"❌ Error importing litstudy: {e}")
    sys.exit(1)

def setup_output_directory():
    """Create output directory with timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"/Users/simonwang/Documents/Usage/HKUworkshop/agent4hku/litstudy_explore/practice/lab8_output/analysis_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    print(f"📁 Output directory: {output_dir}")
    return output_dir

def load_and_clean_data(input_file):
    """Load and clean the Scopus CSV data"""
    print(f"📊 Loading data from: {input_file}")
    
    try:
        # Load the Scopus CSV data
        documents = load_scopus_csv(input_file)
        print(f"✅ Loaded {len(documents)} documents")
        
        # Basic data cleaning and organization
        print("🧹 Performing data cleaning...")
        
        # Remove documents with missing essential fields
        original_count = len(documents)
        documents = [doc for doc in documents if doc.title and doc.title.strip()]
        print(f"📝 Filtered out {original_count - len(documents)} documents with missing titles")
        
        # Remove duplicates based on title similarity (basic approach)
        seen_titles = set()
        unique_documents = []
        for doc in documents:
            title_key = doc.title.lower().strip()
            if title_key not in seen_titles:
                seen_titles.add(title_key)
                unique_documents.append(doc)
        
        print(f"🔄 Removed {len(documents) - len(unique_documents)} duplicate documents")
        documents = unique_documents
        
        print(f"📊 Final dataset: {len(documents)} documents")
        return documents
        
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

def compute_bibliometric_stats(documents, output_dir):
    """Compute bibliometric statistics"""
    print("📈 Computing bibliometric statistics...")
    
    stats = {}
    
    try:
        # Year distribution
        print("  📅 Computing year histogram...")
        year_hist = compute_year_histogram(documents)
        stats['year_distribution'] = dict(year_hist)
        
        # Author distribution
        print("  👥 Computing author histogram...")
        author_hist = compute_author_histogram(documents)
        stats['top_authors'] = dict(list(author_hist.items())[:20])  # Top 20 authors
        
        # Source distribution
        print("  📚 Computing source histogram...")
        source_hist = compute_source_histogram(documents)
        stats['top_sources'] = dict(list(source_hist.items())[:20])  # Top 20 sources
        
        # Affiliation distribution
        print("  🏢 Computing affiliation histogram...")
        affiliation_hist = compute_affiliation_histogram(documents)
        stats['top_affiliations'] = dict(list(affiliation_hist.items())[:20])  # Top 20 affiliations
        
        # Country distribution
        print("  🌍 Computing country histogram...")
        country_hist = compute_country_histogram(documents)
        stats['top_countries'] = dict(list(country_hist.items())[:20])  # Top 20 countries
        
        # Basic statistics
        stats['total_documents'] = len(documents)
        stats['date_range'] = {
            'earliest': min([doc.year for doc in documents if doc.year]) if any(doc.year for doc in documents) else None,
            'latest': max([doc.year for doc in documents if doc.year]) if any(doc.year for doc in documents) else None
        }
        
        # Save statistics
        stats_file = os.path.join(output_dir, 'bibliometric_stats.json')
        with open(stats_file, 'w') as f:
            json.dump(stats, f, indent=2)
        print(f"💾 Saved statistics to: {stats_file}")
        
        return stats
        
    except Exception as e:
        print(f"❌ Error computing statistics: {e}")
        return {}

def create_visualizations(documents, output_dir):
    """Create bibliometric visualizations"""
    print("📊 Creating visualizations...")
    
    try:
        # Set up plotting style
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        
        # Year distribution plot
        print("  📅 Creating year distribution plot...")
        fig, ax = plot_year_histogram(documents)
        plt.title('Publication Timeline', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'publication_timeline.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        # Author distribution plot
        print("  👥 Creating author distribution plot...")
        fig, ax = plot_author_histogram(documents, top_n=20)
        plt.title('Top 20 Most Productive Authors', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'top_authors.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        # Source distribution plot
        print("  📚 Creating source distribution plot...")
        fig, ax = plot_source_histogram(documents, top_n=20)
        plt.title('Top 20 Publication Venues', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'top_venues.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        # Affiliation distribution plot
        print("  🏢 Creating affiliation distribution plot...")
        fig, ax = plot_affiliation_histogram(documents, top_n=20)
        plt.title('Top 20 Research Affiliations', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'top_affiliations.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        # Country distribution plot
        print("  🌍 Creating country distribution plot...")
        fig, ax = plot_country_histogram(documents, top_n=20)
        plt.title('Top 20 Countries by Publication Count', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'top_countries.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        print("✅ All visualizations created successfully")
        
    except Exception as e:
        print(f"❌ Error creating visualizations: {e}")

def perform_text_analysis(documents, output_dir):
    """Perform text analysis on abstracts"""
    print("📝 Performing text analysis...")
    
    try:
        # Build corpus from abstracts
        print("  📚 Building text corpus...")
        corpus = build_corpus(documents)
        
        # Word distribution
        print("  📊 Computing word distribution...")
        word_dist = compute_word_distribution(corpus)
        
        # Create word cloud
        print("  ☁️ Creating word cloud...")
        fig, ax = plot_word_distribution(corpus, top_n=50)
        plt.title('Most Frequent Words in Abstracts', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'word_distribution.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        # Topic clouds
        print("  🎯 Creating topic clouds...")
        fig, ax = plot_topic_clouds(corpus, n_topics=5)
        plt.title('Topic Analysis of Abstracts', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'topic_clouds.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        print("✅ Text analysis completed")
        
    except Exception as e:
        print(f"❌ Error in text analysis: {e}")

def create_network_analysis(documents, output_dir):
    """Create co-author network analysis"""
    print("🕸️ Creating network analysis...")
    
    try:
        # Build co-author network
        print("  👥 Building co-author network...")
        network = build_coauthor_network(documents)
        
        # Plot co-author network
        print("  📊 Creating co-author network visualization...")
        fig, ax = plot_coauthor_network(network)
        plt.title('Co-Author Collaboration Network', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'coauthor_network.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        print("✅ Network analysis completed")
        
    except Exception as e:
        print(f"❌ Error in network analysis: {e}")

def generate_summary_report(documents, stats, output_dir):
    """Generate a summary report"""
    print("📋 Generating summary report...")
    
    report = f"""
# Literature Study Analysis Report
Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Dataset Overview
- **Total Documents**: {len(documents)}
- **Date Range**: {stats.get('date_range', {}).get('earliest', 'N/A')} - {stats.get('date_range', {}).get('latest', 'N/A')}

## Key Findings

### Publication Timeline
The dataset shows publications from {stats.get('date_range', {}).get('earliest', 'N/A')} to {stats.get('date_range', {}).get('latest', 'N/A')}.

### Top Authors
{chr(10).join([f"- {author}: {count} publications" for author, count in list(stats.get('top_authors', {}).items())[:10]])}

### Top Publication Venues
{chr(10).join([f"- {venue}: {count} publications" for venue, count in list(stats.get('top_sources', {}).items())[:10]])}

### Top Research Affiliations
{chr(10).join([f"- {affiliation}: {count} publications" for affiliation, count in list(stats.get('top_affiliations', {}).items())[:10]])}

### Geographic Distribution
{chr(10).join([f"- {country}: {count} publications" for country, count in list(stats.get('top_countries', {}).items())[:10]])}

## Generated Files
- bibliometric_stats.json: Detailed statistics
- publication_timeline.png: Publication trends over time
- top_authors.png: Most productive authors
- top_venues.png: Most common publication venues
- top_affiliations.png: Most active research institutions
- top_countries.png: Geographic distribution
- word_distribution.png: Most frequent words in abstracts
- topic_clouds.png: Topic analysis of abstracts
- coauthor_network.png: Collaboration network

## Analysis Notes
This analysis was performed using the litstudy library with the following steps:
1. Data cleaning and deduplication
2. Bibliometric statistics computation
3. Visualization generation
4. Text analysis of abstracts
5. Network analysis of co-authorship
"""
    
    report_file = os.path.join(output_dir, 'analysis_report.md')
    with open(report_file, 'w') as f:
        f.write(report)
    
    print(f"📄 Summary report saved to: {report_file}")

def main():
    """Main analysis function"""
    print("🚀 Starting Lab 8: Literature Study Analysis")
    print("=" * 60)
    
    # Setup
    input_file = "/Users/simonwang/Documents/Usage/HKUworkshop/agent4hku/litstudy_explore/practice/lab7_scopus_output/papers_20251024_002037.csv"
    output_dir = setup_output_directory()
    
    # Step 1: Load and clean data
    print("\n📊 Step 1: Data Loading and Cleaning")
    print("-" * 40)
    documents = load_and_clean_data(input_file)
    
    if not documents:
        print("❌ Failed to load data. Exiting.")
        return
    
    # Step 2: Compute bibliometric statistics
    print("\n📈 Step 2: Bibliometric Analysis")
    print("-" * 40)
    stats = compute_bibliometric_stats(documents, output_dir)
    
    # Step 3: Create visualizations
    print("\n📊 Step 3: Visualization Generation")
    print("-" * 40)
    create_visualizations(documents, output_dir)
    
    # Step 4: Text analysis
    print("\n📝 Step 4: Text Analysis")
    print("-" * 40)
    perform_text_analysis(documents, output_dir)
    
    # Step 5: Network analysis
    print("\n🕸️ Step 5: Network Analysis")
    print("-" * 40)
    create_network_analysis(documents, output_dir)
    
    # Step 6: Generate summary report
    print("\n📋 Step 6: Report Generation")
    print("-" * 40)
    generate_summary_report(documents, stats, output_dir)
    
    print("\n✅ Lab 8 Analysis Complete!")
    print(f"📁 All outputs saved to: {output_dir}")
    print("=" * 60)

if __name__ == "__main__":
    main()
