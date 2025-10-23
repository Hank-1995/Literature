# Lab 7: Literature Search using litstudy

This lab demonstrates how to use the `litstudy` module to search academic databases for literature related to AI literacy frameworks and academic writing.

## Overview

The program searches multiple academic databases:
- **arXiv**: Open access repository for preprints
- **CrossRef**: DOI registration agency with metadata
- **Scopus**: Commercial database (requires API credentials)

## Files

- `lab7_literature_search.py` - Main program with LiteratureSearch class
- `run_lab7.py` - Simple runner script with command-line options
- `requirements_lab7.txt` - Required Python packages
- `README_Lab7.md` - This documentation

## Installation

1. Install required packages:
```bash
pip install -r requirements_lab7.txt
```

2. Ensure the litstudy module is available in the path (it should be in the scripts directory).

## Usage

### Basic Usage

Run with default settings:
```bash
python run_lab7.py
```

### Custom Queries

Search for specific topics:
```bash
python run_lab7.py --queries "machine learning education" "AI in higher education"
```

### Adjust Results

Limit results per database:
```bash
python run_lab7.py --max-results 50
```

### Skip Scopus (No API Key Required)

If you don't have Scopus API credentials:
```bash
python run_lab7.py --no-scopus
```

### Custom Output Directory

Specify where to save results:
```bash
python run_lab7.py --output-dir my_results
```

### Verbose Logging

Enable detailed logging:
```bash
python run_lab7.py --verbose
```

## API Credentials

**IMPORTANT: For security, API credentials are no longer hardcoded.**

### Option 1: Environment Variables (Recommended)
```bash
export SCOPUS_API_KEY="your_api_key"
export SCOPUS_INST_TOKEN="your_institutional_token"
```

### Option 2: Interactive Setup
```bash
python setup_credentials.py
```

### Option 3: Command Line Arguments
```bash
python run_lab7.py --scopus-key YOUR_KEY --scopus-token YOUR_TOKEN
```

## Output Files

The program generates several output files in the specified directory:

### Data Files
- `combined_results_TIMESTAMP.json` - All papers in JSON format
- `papers_TIMESTAMP.csv` - Papers in CSV format for Excel
- `analysis_TIMESTAMP.json` - Statistical analysis results

### Visualization Files
- `year_distribution_TIMESTAMP.png` - Publication year distribution
- `author_distribution_TIMESTAMP.png` - Author frequency distribution

### Log Files
- `lab7_search.log` - Detailed execution log

## Program Structure

### LiteratureSearch Class

The main class provides these methods:

- `search_arxiv_papers(query, max_results)` - Search arXiv
- `search_crossref_papers(query, max_results)` - Search CrossRef  
- `search_scopus_papers(query, max_results)` - Search Scopus
- `search_all_databases(query, max_results)` - Search all databases
- `combine_results()` - Merge results from all sources
- `analyze_results()` - Perform statistical analysis
- `save_results(output_dir)` - Save to multiple formats
- `generate_plots(output_dir)` - Create visualizations

### Error Handling

The program includes comprehensive error handling:
- Database connection failures
- API rate limiting
- Missing credentials
- Data processing errors

### Logging

All operations are logged with timestamps:
- Search progress
- Results summary
- Error messages
- Performance metrics

## Example Output

```
Lab 7 Literature Search Runner
========================================
Queries: ['AI literacy framework', 'academic writing']
Max results per DB: 30
Output directory: lab7_output
Scopus search: Enabled
========================================

Search 1/2: 'AI literacy framework'
----------------------------------------
Total papers found: 45
  arxiv: 15 papers
  crossref: 20 papers
  scopus: 10 papers

Search 2/2: 'academic writing'
----------------------------------------
Total papers found: 38
  arxiv: 12 papers
  crossref: 18 papers
  scopus: 8 papers

Combining all results...
Total combined papers: 83

Analyzing results...

Analysis Summary:
  Total papers: 83
  Databases used: arxiv, crossref, scopus
  Papers per database: {'arxiv': 27, 'crossref': 38, 'scopus': 18}
  Publication years: 12 unique years
  Top authors: 156 identified

Saving results to lab7_output...
Generating plots...

============================================================
Lab 7 completed successfully!
Results saved to: lab7_output
============================================================
```

## Troubleshooting

### Common Issues

1. **Import Error**: Ensure litstudy module is in the Python path
2. **API Errors**: Check Scopus credentials if using Scopus search
3. **Network Issues**: Some databases may be temporarily unavailable
4. **Memory Issues**: Reduce max_results if processing large datasets

### Debug Mode

Run with verbose logging to see detailed error messages:
```bash
python run_lab7.py --verbose
```

## Advanced Usage

### Programmatic Usage

You can also use the LiteratureSearch class directly in your own code:

```python
from lab7_literature_search import LiteratureSearch

# Initialize with credentials
search = LiteratureSearch(
    scopus_api_key="your_key",
    scopus_inst_token="your_token"
)

# Search specific query
results = search.search_all_databases("your query", max_results=50)

# Combine and analyze
search.combine_results()
analysis = search.analyze_results()

# Save results
search.save_results("output_directory")
```

## Next Steps

After running the search, you can:
1. Review the generated CSV file in Excel
2. Analyze the JSON data programmatically
3. Use the plots for presentations
4. Import results into other analysis tools

## Support

For issues or questions:
1. Check the log file for detailed error messages
2. Ensure all dependencies are installed
3. Verify API credentials are correct
4. Try running with `--no-scopus` to test without Scopus
