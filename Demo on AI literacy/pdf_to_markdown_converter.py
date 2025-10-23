#!/usr/bin/env python3
"""
PDF to Markdown Converter
Converts PDF files to markdown format while preserving all content including text, formatting, and structure.
"""

import sys
import os
import re
from pathlib import Path

try:
    import PyPDF2
    import pdfplumber
    from pdfminer.high_level import extract_text
    from pdfminer.layout import LAParams
except ImportError as e:
    print(f"Missing required libraries. Please install them with:")
    print(f"pip install PyPDF2 pdfplumber pdfminer.six")
    print(f"Error: {e}")
    sys.exit(1)


class PDFToMarkdownConverter:
    def __init__(self, pdf_path, output_path=None):
        self.pdf_path = Path(pdf_path)
        if not self.pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        if output_path is None:
            self.output_path = self.pdf_path.with_suffix('.md')
        else:
            self.output_path = Path(output_path)
    
    def extract_text_with_pdfplumber(self):
        """Extract text using pdfplumber for better formatting preservation"""
        text_content = []
        
        with pdfplumber.open(self.pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                print(f"Processing page {page_num}/{len(pdf.pages)}...")
                
                # Extract text with layout information
                text = page.extract_text()
                if text:
                    # Add page break marker
                    text_content.append(f"\n---\n**Page {page_num}**\n---\n")
                    text_content.append(text)
                
                # Extract tables if any
                tables = page.extract_tables()
                if tables:
                    for table_num, table in enumerate(tables, 1):
                        text_content.append(f"\n**Table {table_num} on Page {page_num}:**\n")
                        text_content.append(self._format_table_as_markdown(table))
        
        return '\n'.join(text_content)
    
    def extract_text_with_pdfminer(self):
        """Extract text using pdfminer for comprehensive text extraction"""
        try:
            # Use layout parameters for better text extraction
            laparams = LAParams(
                word_margin=0.1,
                char_margin=2.0,
                line_margin=0.5,
                boxes_flow=0.5
            )
            
            text = extract_text(str(self.pdf_path), laparams=laparams)
            return text
        except Exception as e:
            print(f"Error with pdfminer extraction: {e}")
            return ""
    
    def extract_text_with_pypdf2(self):
        """Extract text using PyPDF2 as fallback"""
        text_content = []
        
        try:
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                
                for page_num, page in enumerate(pdf_reader.pages, 1):
                    print(f"Processing page {page_num}/{len(pdf_reader.pages)}...")
                    text = page.extract_text()
                    if text.strip():
                        text_content.append(f"\n---\n**Page {page_num}**\n---\n")
                        text_content.append(text)
        except Exception as e:
            print(f"Error with PyPDF2 extraction: {e}")
        
        return '\n'.join(text_content)
    
    def _format_table_as_markdown(self, table):
        """Convert table data to markdown table format"""
        if not table or not table[0]:
            return ""
        
        markdown_table = []
        
        # Header row
        header = "| " + " | ".join(str(cell) if cell else "" for cell in table[0]) + " |"
        markdown_table.append(header)
        
        # Separator row
        separator = "| " + " | ".join("---" for _ in table[0]) + " |"
        markdown_table.append(separator)
        
        # Data rows
        for row in table[1:]:
            if row:  # Skip empty rows
                data_row = "| " + " | ".join(str(cell) if cell else "" for cell in row) + " |"
                markdown_table.append(data_row)
        
        return '\n'.join(markdown_table)
    
    def clean_and_format_text(self, text):
        """Clean and format the extracted text for better markdown output"""
        if not text:
            return ""
        
        # Split into lines for processing
        lines = text.split('\n')
        processed_lines = []
        
        for line in lines:
            line = line.strip()
            if not line:
                processed_lines.append("")
                continue
            
            # Detect potential headers (lines that are all caps or start with numbers)
            if self._is_likely_header(line):
                processed_lines.append(f"## {line}")
            else:
                processed_lines.append(line)
        
        # Join lines and clean up multiple empty lines
        formatted_text = '\n'.join(processed_lines)
        formatted_text = re.sub(r'\n\s*\n\s*\n', '\n\n', formatted_text)  # Max 2 consecutive newlines
        
        return formatted_text
    
    def _is_likely_header(self, line):
        """Determine if a line is likely a header"""
        # Check for common header patterns
        header_patterns = [
            r'^[A-Z\s]{10,}$',  # All caps, at least 10 chars
            r'^\d+\.?\s+[A-Z]',  # Numbered headers
            r'^[IVX]+\.?\s+[A-Z]',  # Roman numeral headers
            r'^[A-Z][a-z]+\s+[A-Z]',  # Title case patterns
        ]
        
        for pattern in header_patterns:
            if re.match(pattern, line):
                return True
        
        return False
    
    def convert(self):
        """Main conversion method"""
        print(f"Converting PDF: {self.pdf_path}")
        print(f"Output will be saved to: {self.output_path}")
        
        # Try multiple extraction methods for best results
        text_content = ""
        
        print("\n1. Trying pdfplumber extraction (best for formatting)...")
        try:
            text_content = self.extract_text_with_pdfplumber()
            if text_content and len(text_content.strip()) > 100:
                print("✓ pdfplumber extraction successful")
            else:
                raise Exception("Insufficient content extracted")
        except Exception as e:
            print(f"✗ pdfplumber failed: {e}")
            text_content = ""
        
        if not text_content or len(text_content.strip()) < 100:
            print("\n2. Trying pdfminer extraction...")
            try:
                text_content = self.extract_text_with_pdfminer()
                if text_content and len(text_content.strip()) > 100:
                    print("✓ pdfminer extraction successful")
                else:
                    raise Exception("Insufficient content extracted")
            except Exception as e:
                print(f"✗ pdfminer failed: {e}")
                text_content = ""
        
        if not text_content or len(text_content.strip()) < 100:
            print("\n3. Trying PyPDF2 extraction (fallback)...")
            try:
                text_content = self.extract_text_with_pypdf2()
                if text_content and len(text_content.strip()) > 100:
                    print("✓ PyPDF2 extraction successful")
                else:
                    raise Exception("Insufficient content extracted")
            except Exception as e:
                print(f"✗ PyPDF2 failed: {e}")
                text_content = ""
        
        if not text_content or len(text_content.strip()) < 100:
            raise Exception("All extraction methods failed or produced insufficient content")
        
        # Clean and format the text
        print("\n4. Formatting text for markdown...")
        formatted_text = self.clean_and_format_text(text_content)
        
        # Add metadata header
        markdown_content = f"""# {self.pdf_path.stem}

*Converted from PDF: {self.pdf_path.name}*
*Conversion date: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

---

{formatted_text}
"""
        
        # Write to output file
        print(f"\n5. Writing to markdown file...")
        with open(self.output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"✓ Conversion completed successfully!")
        print(f"✓ Output saved to: {self.output_path}")
        print(f"✓ Content length: {len(formatted_text)} characters")
        
        return self.output_path


def main():
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_markdown_converter.py <pdf_file> [output_file]")
        print("Example: python pdf_to_markdown_converter.py document.pdf document.md")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        converter = PDFToMarkdownConverter(pdf_file, output_file)
        output_path = converter.convert()
        print(f"\n🎉 Successfully converted {pdf_file} to {output_path}")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
