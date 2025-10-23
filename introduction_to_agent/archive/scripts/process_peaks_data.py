#!/usr/bin/env python3
"""
Process Genomic Peaks CSV Data and Generate Charts
Author: Dr Simon Wang, HKBU
Workshop: AI Agents for HKU Research Students
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

def load_peaks_data(csv_path):
    """Load the genomic peaks CSV data"""
    try:
        df = pd.read_csv(csv_path)
        print(f"✅ Successfully loaded {len(df)} peaks from {csv_path}")
        return df
    except FileNotFoundError:
        print(f"❌ Error: Could not find file {csv_path}")
        return None
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

def basic_data_analysis(df):
    """Perform basic data analysis and print summary statistics"""
    print("\n📊 DATA SUMMARY")
    print("=" * 50)
    print(f"Total number of peaks: {len(df)}")
    print(f"Chromosomes represented: {df['chr'].nunique()}")
    print(f"Unique chromosomes: {sorted(df['chr'].unique())}")
    print(f"Annotation types: {df['annotation'].value_counts().to_dict()}")
    print(f"Score range: {df['score'].min()} - {df['score'].max()}")
    print(f"Average score: {df['score'].mean():.2f}")
    
    # Peak length analysis
    df['peak_length'] = df['end'] - df['start']
    print(f"Peak length range: {df['peak_length'].min()} - {df['peak_length'].max()} bp")
    print(f"Average peak length: {df['peak_length'].mean():.0f} bp")

def create_score_distribution_chart(df, output_dir):
    """Create a score distribution histogram"""
    plt.figure(figsize=(10, 6))
    plt.hist(df['score'], bins=15, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title('Distribution of Peak Scores', fontsize=14, fontweight='bold')
    plt.xlabel('Peak Score', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Add mean line
    mean_score = df['score'].mean()
    plt.axvline(mean_score, color='red', linestyle='--', linewidth=2, 
                label=f'Mean: {mean_score:.1f}')
    plt.legend()
    
    plt.tight_layout()
    output_path = output_dir / 'score_distribution.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"📈 Score distribution chart saved to: {output_path}")

def create_annotation_pie_chart(df, output_dir):
    """Create a pie chart showing annotation distribution"""
    annotation_counts = df['annotation'].value_counts()
    
    plt.figure(figsize=(8, 8))
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    wedges, texts, autotexts = plt.pie(annotation_counts.values, 
                                       labels=annotation_counts.index,
                                       autopct='%1.1f%%',
                                       colors=colors[:len(annotation_counts)],
                                       startangle=90)
    
    plt.title('Distribution of Peak Annotations', fontsize=14, fontweight='bold')
    
    # Improve text appearance
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    plt.tight_layout()
    output_path = output_dir / 'annotation_distribution.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"🥧 Annotation pie chart saved to: {output_path}")

def create_chromosome_bar_chart(df, output_dir):
    """Create a bar chart showing peaks per chromosome"""
    chr_counts = df['chr'].value_counts().sort_index()
    
    plt.figure(figsize=(12, 6))
    bars = plt.bar(chr_counts.index, chr_counts.values, 
                   color='lightcoral', alpha=0.8, edgecolor='black')
    
    plt.title('Number of Peaks per Chromosome', fontsize=14, fontweight='bold')
    plt.xlabel('Chromosome', fontsize=12)
    plt.ylabel('Number of Peaks', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{int(height)}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    output_path = output_dir / 'chromosome_peaks.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"📊 Chromosome bar chart saved to: {output_path}")

def create_score_vs_annotation_boxplot(df, output_dir):
    """Create a boxplot comparing scores by annotation type"""
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='annotation', y='score', palette='Set2')
    plt.title('Peak Scores by Annotation Type', fontsize=14, fontweight='bold')
    plt.xlabel('Annotation Type', fontsize=12)
    plt.ylabel('Peak Score', fontsize=12)
    plt.grid(True, alpha=0.3, axis='y')
    
    # Add mean points
    for i, annotation in enumerate(df['annotation'].unique()):
        mean_score = df[df['annotation'] == annotation]['score'].mean()
        plt.scatter(i, mean_score, color='red', s=100, marker='D', 
                   label='Mean' if i == 0 else "", zorder=5)
    
    plt.legend()
    plt.tight_layout()
    output_path = output_dir / 'score_by_annotation.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"📦 Score by annotation boxplot saved to: {output_path}")

def create_genomic_position_plot(df, output_dir):
    """Create a scatter plot showing genomic positions"""
    plt.figure(figsize=(14, 8))
    
    # Color by annotation type
    colors = {'promoter': 'red', 'enhancer': 'blue'}
    for annotation in df['annotation'].unique():
        subset = df[df['annotation'] == annotation]
        plt.scatter(subset['start'], subset['chr'], 
                   c=colors.get(annotation, 'gray'), 
                   label=annotation, alpha=0.7, s=subset['score']*2)
    
    plt.title('Genomic Positions of Peaks (Size = Score)', fontsize=14, fontweight='bold')
    plt.xlabel('Genomic Position (bp)', fontsize=12)
    plt.ylabel('Chromosome', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Add a note about point sizes
    plt.text(0.02, 0.98, 'Point size represents peak score', 
             transform=plt.gca().transAxes, fontsize=10, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7),
             verticalalignment='top')
    
    plt.tight_layout()
    output_path = output_dir / 'genomic_positions.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"🗺️ Genomic positions plot saved to: {output_path}")

def generate_summary_report(df, output_dir):
    """Generate a text summary report"""
    report_path = output_dir / 'peaks_analysis_report.txt'
    
    with open(report_path, 'w') as f:
        f.write("GENOMIC PEAKS ANALYSIS REPORT\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Analysis Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Peaks Analyzed: {len(df)}\n\n")
        
        f.write("CHROMOSOME DISTRIBUTION:\n")
        f.write("-" * 30 + "\n")
        for chr_name, count in df['chr'].value_counts().sort_index().items():
            f.write(f"{chr_name}: {count} peaks\n")
        
        f.write(f"\nANNOTATION DISTRIBUTION:\n")
        f.write("-" * 30 + "\n")
        for annotation, count in df['annotation'].value_counts().items():
            f.write(f"{annotation}: {count} peaks ({count/len(df)*100:.1f}%)\n")
        
        f.write(f"\nSCORE STATISTICS:\n")
        f.write("-" * 30 + "\n")
        f.write(f"Mean Score: {df['score'].mean():.2f}\n")
        f.write(f"Median Score: {df['score'].median():.2f}\n")
        f.write(f"Standard Deviation: {df['score'].std():.2f}\n")
        f.write(f"Min Score: {df['score'].min()}\n")
        f.write(f"Max Score: {df['score'].max()}\n")
        
        f.write(f"\nPEAK LENGTH STATISTICS:\n")
        f.write("-" * 30 + "\n")
        df['peak_length'] = df['end'] - df['start']
        f.write(f"Mean Length: {df['peak_length'].mean():.0f} bp\n")
        f.write(f"Median Length: {df['peak_length'].median():.0f} bp\n")
        f.write(f"Min Length: {df['peak_length'].min()} bp\n")
        f.write(f"Max Length: {df['peak_length'].max()} bp\n")
    
    print(f"📄 Summary report saved to: {report_path}")

def main():
    """Main function to process peaks data and generate all charts"""
    print("🧬 GENOMIC PEAKS DATA ANALYSIS")
    print("=" * 50)
    
    # Set up paths
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent / 'data'
    output_dir = script_dir.parent / 'outputs'
    output_dir.mkdir(exist_ok=True)
    
    csv_path = data_dir / 'example_peaks.csv'
    
    # Load data
    df = load_peaks_data(csv_path)
    if df is None:
        return
    
    # Perform analysis
    basic_data_analysis(df)
    
    # Generate charts
    print("\n📊 GENERATING CHARTS")
    print("=" * 30)
    
    create_score_distribution_chart(df, output_dir)
    create_annotation_pie_chart(df, output_dir)
    create_chromosome_bar_chart(df, output_dir)
    create_score_vs_annotation_boxplot(df, output_dir)
    create_genomic_position_plot(df, output_dir)
    
    # Generate summary report
    generate_summary_report(df, output_dir)
    
    print(f"\n✅ Analysis complete! All outputs saved to: {output_dir}")
    print("\nGenerated files:")
    for file in output_dir.glob('*'):
        print(f"  📁 {file.name}")

if __name__ == "__main__":
    main()
