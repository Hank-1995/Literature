#!/usr/bin/env python3
"""
Lab 8: Literature Study Analysis (Simplified Version)
Performs data cleaning, organization, and bibliometric analysis on Scopus data
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import json
from collections import Counter
import re

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
        # Load the CSV data
        df = pd.read_csv(input_file)
        print(f"✅ Loaded {len(df)} documents")
        
        # Basic data cleaning and organization
        print("🧹 Performing data cleaning...")
        
        # Remove documents with missing essential fields
        original_count = len(df)
        df = df.dropna(subset=['title'])
        df = df[df['title'].str.strip() != '']
        print(f"📝 Filtered out {original_count - len(df)} documents with missing titles")
        
        # Remove duplicates based on title similarity
        df['title_clean'] = df['title'].str.lower().str.strip()
        df = df.drop_duplicates(subset=['title_clean'], keep='first')
        df = df.drop('title_clean', axis=1)
        
        print(f"🔄 Removed {original_count - len(df)} duplicate documents")
        print(f"📊 Final dataset: {len(df)} documents")
        
        return df
        
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

def extract_year_from_date(date_str):
    """Extract year from date string"""
    if pd.isna(date_str):
        return None
    try:
        # Handle different date formats
        if 'T' in str(date_str):
            return int(str(date_str).split('T')[0].split('-')[0])
        else:
            return int(str(date_str).split('-')[0])
    except:
        return None

def compute_bibliometric_stats(df, output_dir):
    """Compute bibliometric statistics"""
    print("📈 Computing bibliometric statistics...")
    
    stats = {}
    
    try:
        # Extract years
        df['year'] = df['published'].apply(extract_year_from_date)
        valid_years = df['year'].dropna()
        
        # Year distribution
        print("  📅 Computing year histogram...")
        year_counts = valid_years.value_counts().sort_index()
        stats['year_distribution'] = year_counts.to_dict()
        
        # Author distribution
        print("  👥 Computing author histogram...")
        all_authors = []
        for authors_str in df['authors'].dropna():
            if isinstance(authors_str, str):
                # Split by semicolon and clean
                authors = [author.strip() for author in authors_str.split(';')]
                all_authors.extend(authors)
        
        author_counts = Counter(all_authors)
        stats['top_authors'] = dict(author_counts.most_common(20))
        
        # Source distribution
        print("  📚 Computing source histogram...")
        source_counts = df['venue'].value_counts()
        stats['top_sources'] = dict(source_counts.head(20))
        
        # Basic statistics
        stats['total_documents'] = len(df)
        if not valid_years.empty:
            stats['date_range'] = {
                'earliest': int(valid_years.min()),
                'latest': int(valid_years.max())
            }
        else:
            stats['date_range'] = {'earliest': None, 'latest': None}
        
        # Save statistics
        stats_file = os.path.join(output_dir, 'bibliometric_stats.json')
        with open(stats_file, 'w') as f:
            json.dump(stats, f, indent=2, default=str)
        print(f"💾 Saved statistics to: {stats_file}")
        
        return stats
        
    except Exception as e:
        print(f"❌ Error computing statistics: {e}")
        return {}

def create_visualizations(df, output_dir):
    """Create bibliometric visualizations"""
    print("📊 Creating visualizations...")
    
    try:
        # Set up plotting style
        plt.style.use('default')
        sns.set_palette("husl")
        
        # Extract years for plotting
        df['year'] = df['published'].apply(extract_year_from_date)
        valid_years = df['year'].dropna()
        
        # Year distribution plot
        print("  📅 Creating year distribution plot...")
        plt.figure(figsize=(12, 6))
        year_counts = valid_years.value_counts().sort_index()
        plt.bar(year_counts.index, year_counts.values, alpha=0.7)
        plt.title('Publication Timeline', fontsize=16, fontweight='bold')
        plt.xlabel('Year')
        plt.ylabel('Number of Publications')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'publication_timeline.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        # Author distribution plot
        print("  👥 Creating author distribution plot...")
        all_authors = []
        for authors_str in df['authors'].dropna():
            if isinstance(authors_str, str):
                authors = [author.strip() for author in authors_str.split(';')]
                all_authors.extend(authors)
        
        author_counts = Counter(all_authors)
        top_authors = author_counts.most_common(20)
        
        plt.figure(figsize=(12, 8))
        authors, counts = zip(*top_authors)
        plt.barh(range(len(authors)), counts, alpha=0.7)
        plt.yticks(range(len(authors)), authors)
        plt.title('Top 20 Most Productive Authors', fontsize=16, fontweight='bold')
        plt.xlabel('Number of Publications')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'top_authors.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        # Source distribution plot
        print("  📚 Creating source distribution plot...")
        source_counts = df['venue'].value_counts().head(20)
        
        plt.figure(figsize=(12, 8))
        plt.barh(range(len(source_counts)), source_counts.values, alpha=0.7)
        plt.yticks(range(len(source_counts)), source_counts.index)
        plt.title('Top 20 Publication Venues', fontsize=16, fontweight='bold')
        plt.xlabel('Number of Publications')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'top_venues.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        print("✅ All visualizations created successfully")
        
    except Exception as e:
        print(f"❌ Error creating visualizations: {e}")

def perform_text_analysis(df, output_dir):
    """Perform text analysis on abstracts"""
    print("📝 Performing text analysis...")
    
    try:
        # Combine all abstracts
        abstracts = df['abstract'].dropna()
        all_text = ' '.join(abstracts.astype(str))
        
        # Simple word frequency analysis
        print("  📊 Computing word frequency...")
        # Remove common words and clean text
        words = re.findall(r'\b[a-zA-Z]{4,}\b', all_text.lower())
        
        # Remove common stopwords
        stopwords = {'this', 'that', 'with', 'from', 'they', 'been', 'have', 'were', 'said', 'each', 'which', 'their', 'time', 'will', 'about', 'there', 'could', 'other', 'after', 'first', 'well', 'also', 'where', 'much', 'some', 'these', 'into', 'more', 'than', 'then', 'them', 'can', 'only', 'its', 'now', 'find', 'any', 'new', 'work', 'part', 'take', 'made', 'over', 'think', 'help', 'just', 'like', 'know', 'people', 'year', 'way', 'day', 'get', 'come', 'made', 'may', 'say', 'use', 'man', 'new', 'our', 'out', 'no', 'time', 'very', 'when', 'much', 'then', 'them', 'can', 'only', 'its', 'now', 'find', 'long', 'down', 'day', 'did', 'get', 'has', 'had', 'his', 'how', 'its', 'may', 'not', 'now', 'old', 'see', 'two', 'way', 'who', 'boy', 'did', 'its', 'let', 'put', 'say', 'she', 'too', 'use'}
        
        words = [word for word in words if word not in stopwords and len(word) > 3]
        word_counts = Counter(words)
        
        # Create word frequency plot
        print("  📊 Creating word frequency plot...")
        top_words = word_counts.most_common(30)
        
        plt.figure(figsize=(12, 8))
        words, counts = zip(*top_words)
        plt.barh(range(len(words)), counts, alpha=0.7)
        plt.yticks(range(len(words)), words)
        plt.title('Most Frequent Words in Abstracts', fontsize=16, fontweight='bold')
        plt.xlabel('Frequency')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'word_frequency.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        print("✅ Text analysis completed")
        
    except Exception as e:
        print(f"❌ Error in text analysis: {e}")

def generate_summary_report(df, stats, output_dir):
    """Generate a summary report"""
    print("📋 Generating summary report...")
    
    report = f"""
# Literature Study Analysis Report
Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Dataset Overview
- **Total Documents**: {len(df)}
- **Date Range**: {stats.get('date_range', {}).get('earliest', 'N/A')} - {stats.get('date_range', {}).get('latest', 'N/A')}

## Key Findings

### Publication Timeline
The dataset shows publications from {stats.get('date_range', {}).get('earliest', 'N/A')} to {stats.get('date_range', {}).get('latest', 'N/A')}.

### Top Authors
{chr(10).join([f"- {author}: {count} publications" for author, count in list(stats.get('top_authors', {}).items())[:10]])}

### Top Publication Venues
{chr(10).join([f"- {venue}: {count} publications" for venue, count in list(stats.get('top_sources', {}).items())[:10]])}

## Generated Files
- bibliometric_stats.json: Detailed statistics
- publication_timeline.png: Publication trends over time
- top_authors.png: Most productive authors
- top_venues.png: Most common publication venues
- word_frequency.png: Most frequent words in abstracts

## Analysis Notes
This analysis was performed with the following steps:
1. Data cleaning and deduplication
2. Bibliometric statistics computation
3. Visualization generation
4. Text analysis of abstracts

## Data Quality Notes
- Original dataset: {len(df)} documents after cleaning
- Date extraction: {len([y for y in df['published'].apply(extract_year_from_date) if y is not None])} documents with valid years
- Authors: {len([a for authors_str in df['authors'].dropna() for a in authors_str.split(';') if isinstance(authors_str, str)])} total author mentions
"""
    
    report_file = os.path.join(output_dir, 'analysis_report.md')
    with open(report_file, 'w') as f:
        f.write(report)
    
    print(f"📄 Summary report saved to: {report_file}")

def main():
    """Main analysis function"""
    print("🚀 Starting Lab 8: Literature Study Analysis (Simplified)")
    print("=" * 60)
    
    # Setup
    input_file = "/Users/simonwang/Documents/Usage/HKUworkshop/agent4hku/litstudy_explore/practice/lab7_scopus_output/papers_20251024_002037.csv"
    output_dir = setup_output_directory()
    
    # Step 1: Load and clean data
    print("\n📊 Step 1: Data Loading and Cleaning")
    print("-" * 40)
    df = load_and_clean_data(input_file)
    
    if df is None:
        print("❌ Failed to load data. Exiting.")
        return
    
    # Step 2: Compute bibliometric statistics
    print("\n📈 Step 2: Bibliometric Analysis")
    print("-" * 40)
    stats = compute_bibliometric_stats(df, output_dir)
    
    # Step 3: Create visualizations
    print("\n📊 Step 3: Visualization Generation")
    print("-" * 40)
    create_visualizations(df, output_dir)
    
    # Step 4: Text analysis
    print("\n📝 Step 4: Text Analysis")
    print("-" * 40)
    perform_text_analysis(df, output_dir)
    
    # Step 5: Generate summary report
    print("\n📋 Step 5: Report Generation")
    print("-" * 40)
    generate_summary_report(df, stats, output_dir)
    
    print("\n✅ Lab 8 Analysis Complete!")
    print(f"📁 All outputs saved to: {output_dir}")
    print("=" * 60)

if __name__ == "__main__":
    main()
