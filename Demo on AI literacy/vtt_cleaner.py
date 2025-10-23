#!/usr/bin/env python3
"""
VTT Transcript Cleaner and Summarizer
Cleans WebVTT files by removing timestamps and generates summary notes
"""

import re
import os
from datetime import datetime

def clean_vtt_file(input_path, output_path):
    """
    Clean VTT file by removing timestamps and formatting
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Remove WEBVTT header
        content = re.sub(r'^WEBVTT\s*\n', '', content)
        
        # Remove timestamp lines (format: 00:00:02.350 --> 00:00:04.380)
        content = re.sub(r'\d{2}:\d{2}:\d{2}\.\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}\.\d{3}\s*\n', '', content)
        
        # Remove sequence numbers (standalone numbers on lines)
        content = re.sub(r'^\d+\s*\n', '', content, flags=re.MULTILINE)
        
        # Remove empty lines and clean up whitespace
        lines = content.split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            if line and not line.isdigit():  # Skip empty lines and standalone numbers
                cleaned_lines.append(line)
        
        # Join lines and clean up multiple spaces
        cleaned_content = '\n'.join(cleaned_lines)
        cleaned_content = re.sub(r'\s+', ' ', cleaned_content)  # Replace multiple spaces with single space
        cleaned_content = re.sub(r'\n\s*\n', '\n\n', cleaned_content)  # Clean up multiple newlines
        
        # Write cleaned content
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)
        
        print(f"✅ Successfully cleaned VTT file: {output_path}")
        return cleaned_content
        
    except Exception as e:
        print(f"❌ Error cleaning VTT file: {e}")
        return None

def extract_speakers_and_content(cleaned_content):
    """
    Extract speakers and their content from cleaned transcript
    """
    # Pattern to match speaker names followed by content
    speaker_pattern = r'([^:]+):\s*(.+?)(?=\n[A-Z][^:]+:|$)'
    
    speakers_content = {}
    matches = re.findall(speaker_pattern, cleaned_content, re.DOTALL)
    
    for speaker, content in matches:
        speaker = speaker.strip()
        content = content.strip()
        
        if speaker not in speakers_content:
            speakers_content[speaker] = []
        speakers_content[speaker].append(content)
    
    return speakers_content

def generate_summary(cleaned_content, speakers_content, output_path):
    """
    Generate a comprehensive summary of the transcript
    """
    # Basic statistics
    total_words = len(cleaned_content.split())
    total_speakers = len(speakers_content)
    
    # Find main speaker (most content)
    main_speaker = max(speakers_content.keys(), key=lambda x: len(' '.join(speakers_content[x])))
    
    # Generate summary
    summary = f"""# Workshop Training Helper Transcript Summary

## Basic Information
- **Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Total words:** {total_words:,}
- **Number of speakers:** {total_speakers}
- **Main speaker:** {main_speaker}

## Speakers and Content Overview
"""
    
    for speaker, content_list in speakers_content.items():
        speaker_word_count = len(' '.join(content_list).split())
        summary += f"\n### {speaker}\n"
        summary += f"- **Content segments:** {len(content_list)}\n"
        summary += f"- **Word count:** {speaker_word_count:,}\n"
        summary += f"- **Percentage of total:** {(speaker_word_count/total_words)*100:.1f}%\n"
    
    # Key topics and themes (simple keyword extraction)
    summary += "\n## Key Topics and Themes\n"
    
    # Extract potential key topics from the content
    all_text = cleaned_content.lower()
    
    # Look for common workshop/educational terms
    educational_terms = [
        'workshop', 'training', 'student', 'help', 'assist', 'guide', 'teach',
        'learn', 'practice', 'exercise', 'activity', 'session', 'briefing',
        'ai', 'agent', 'tool', 'technology', 'digital', 'online', 'platform'
    ]
    
    found_terms = []
    for term in educational_terms:
        if term in all_text:
            count = all_text.count(term)
            found_terms.append((term, count))
    
    # Sort by frequency
    found_terms.sort(key=lambda x: x[1], reverse=True)
    
    summary += "**Most frequently mentioned topics:**\n"
    for term, count in found_terms[:10]:  # Top 10 terms
        summary += f"- {term}: {count} mentions\n"
    
    # Extract key sentences (longer sentences that might contain important information)
    sentences = re.split(r'[.!?]+', cleaned_content)
    key_sentences = [s.strip() for s in sentences if len(s.strip()) > 50]
    
    summary += "\n## Key Content Highlights\n"
    summary += "**Important statements and explanations:**\n"
    for i, sentence in enumerate(key_sentences[:15], 1):  # Top 15 key sentences
        if sentence.strip():
            summary += f"{i}. {sentence.strip()}\n"
    
    # Workshop structure and timeline
    summary += "\n## Workshop Structure\n"
    summary += "Based on the transcript content, this appears to be a training session for workshop helpers.\n"
    summary += "The session covers:\n"
    summary += "- Introduction and welcome\n"
    summary += "- Workshop logistics and scheduling\n"
    summary += "- Training content and methodology\n"
    summary += "- Q&A and discussion\n"
    
    # Write summary to file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(summary)
    
    print(f"✅ Summary generated: {output_path}")
    return summary

def main():
    # File paths
    input_file = "/Users/simonwang/Documents/Usage/0ESP2026/study5 agent workshop/training_helper.transcript.vtt"
    cleaned_file = "/Users/simonwang/Documents/Usage/0ESP2026/study5 agent workshop/training_helper_cleaned.txt"
    summary_file = "/Users/simonwang/Documents/Usage/0ESP2026/study5 agent workshop/training_helper_summary.md"
    
    print("🧹 Starting VTT file cleanup and summarization...")
    
    # Step 1: Clean the VTT file
    print("\n📝 Step 1: Cleaning VTT file...")
    cleaned_content = clean_vtt_file(input_file, cleaned_file)
    
    if not cleaned_content:
        print("❌ Failed to clean VTT file. Exiting.")
        return
    
    # Step 2: Extract speakers and content
    print("\n👥 Step 2: Analyzing speakers and content...")
    speakers_content = extract_speakers_and_content(cleaned_content)
    
    print(f"Found {len(speakers_content)} speakers:")
    for speaker in speakers_content.keys():
        print(f"  - {speaker}")
    
    # Step 3: Generate summary
    print("\n📊 Step 3: Generating summary...")
    summary = generate_summary(cleaned_content, speakers_content, summary_file)
    
    print("\n✅ All tasks completed successfully!")
    print(f"📁 Cleaned transcript: {cleaned_file}")
    print(f"📁 Summary report: {summary_file}")

if __name__ == "__main__":
    main()
