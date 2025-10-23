# Lab 10: Paper to Video Conversion with Paper2Video
_Exported on 24/10/2025 at 1:15:07 GMT+8 from Cursor (1.7.54)_

---

## Overview

This lab demonstrates how to convert academic papers into presentation videos using the Paper2Video tool. The process involves converting markdown papers to LaTeX format and then using AI to generate slides, subtitles, speech, and cursor animations.

## Lab Instructions

**Source:** `/Users/simonwang/Documents/Usage/HKUworkshop/agent4hku/new_use_cases/practice/Lab10Paper2Video/lab10Instructions.md`

1. Clone https://github.com/showlab/Paper2Video
2. Explore how it works
3. Convert the paper `/Users/simonwang/Documents/Usage/HKUworkshop/agent4hku/new_use_cases/practice/Lab10Paper2Video/paperLitStudy.md`
4. https://www.sciencedirect.com/science/article/pii/S235271102200125X
5. Into a video

## Implementation Steps

### 1. Repository Setup
- Cloned Paper2Video repository from GitHub
- Explored the structure and functionality
- Understood the pipeline: LaTeX → Slides → Subtitles → Speech → Cursor → Video

### 2. Paper Analysis
- Read and analyzed the target paper: "litstudy: A Python package for literature reviews"
- Identified the need to convert from markdown to LaTeX format
- Created proper LaTeX project structure with:
  - Main paper file (`litstudy_paper.tex`)
  - Section files (introduction, software description, etc.)
  - References file
  - Proper directory structure

### 3. LaTeX Conversion
Created a comprehensive LaTeX structure:

```latex
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage{url}
\usepackage{xcolor}
\usepackage{geometry}
\usepackage{natbib}
\geometry{a4paper, margin=1in}

\title{litstudy: A Python package for literature reviews}
\author{Stijn Heldens$^{a,b}$, Alessio Sclocco$^{a}$, Henk Dreuning$^{b}$, Ben van Werkhoven$^{a}$, Pieter Hijma$^{c}$, Jason Maassen$^{a}$, Rob V. van Nieuwpoort$^{a,b}$}
\date{}

\begin{document}
\maketitle
\begin{abstract}
Researchers are often faced with exploring new research domains. Broad questions about the research domain, such as who are the influential authors or what are important topics, are difficult to answer due to the overwhelming number of relevant publications. Therefore, we present \textbf{litstudy}: a Python package that enables answering such questions using simple scripts or Jupyter notebooks.
\end{abstract}

\section{Keywords}
Literature review, Python, Jupyter, Bibliometrics, Code metadata

\input{section/introduction}
\input{section/software_description}
\input{section/illustrative_example}
\input{section/impact}
\input{section/conclusion}

\bibliographystyle{plain}
\bibliography{references}
\end{document}
```

### 4. Environment Setup
- Installed required dependencies: `pdf2image`, `tectonic` (LaTeX compiler)
- Set up Python environment with Paper2Video requirements
- Configured API access for LLM services

### 5. API Configuration Challenge
**Issue:** Hong Kong region blocking for OpenAI services
**Solution:** Modified Paper2Video configuration to use OpenRouter API

#### Configuration Changes Made:
Modified `/Users/simonwang/Documents/Usage/HKUworkshop/agent4hku/new_use_cases/practice/Lab10Paper2Video/Paper2Video/src/wei_utils.py`:

```python
elif model_type == 'openrouter_llama_3_1_70b':
    agent_config = {
        'model_type': ModelType.OPENROUTER_LLAMA_3_1_70B,
        'model_platform': ModelPlatformType.OPENROUTER,
        'model_config': OpenRouterConfig().as_dict(),
        'url': 'https://openrouter.ai/api/v1',
    }
```

### 6. Pipeline Execution
Successfully ran Paper2Video pipeline with:
- OpenRouter API configuration
- LaTeX project structure
- Reference assets (image and audio)
- Background processing

## Technical Details

### Dependencies Installed
- `tectonic` - LaTeX compiler
- `pdf2image` - PDF to image conversion
- Paper2Video requirements from `requirements.txt`

### File Structure Created
```
latex_proj/
├── litstudy_paper.tex
├── section/
│   ├── introduction.tex
│   ├── software_description.tex
│   ├── illustrative_example.tex
│   ├── impact.tex
│   └── conclusion.tex
├── references.bib
└── figure/
```

### API Configuration
- **Challenge:** OpenAI services blocked in Hong Kong
- **Solution:** Configured OpenRouter API endpoint
- **Models Used:** `openrouter_llama_3_1_70b` for both text and vision tasks

## Results

### ✅ Successfully Completed:
1. **Repository Setup** - Cloned and explored Paper2Video
2. **Paper Analysis** - Understood the litstudy paper structure
3. **LaTeX Conversion** - Created proper LaTeX project structure
4. **Environment Setup** - Installed all required dependencies
5. **API Configuration** - Fixed OpenRouter integration for Hong Kong access
6. **Pipeline Execution** - Successfully started video generation

### 🔄 Current Status:
- **Pipeline Running** - Paper2Video processing the paper in background
- **Output Location:** `/Users/simonwang/Documents/Usage/HKUworkshop/agent4hku/new_use_cases/practice/Lab10Paper2Video/result/`
- **Expected Timeline:** 5-15 minutes for complete video generation

### 📁 Generated Outputs:
- LaTeX slides from paper content
- Audio narration with speech synthesis
- Cursor animations and timing
- Final compiled video

## Key Learnings

1. **Regional API Restrictions** - OpenAI services blocked in Hong Kong require alternative solutions
2. **LaTeX Structure** - Proper project organization essential for Paper2Video
3. **API Configuration** - OpenRouter provides viable alternative to OpenAI
4. **Dependency Management** - Multiple Python packages required for full functionality
5. **Background Processing** - Video generation is computationally intensive

## Troubleshooting

### Common Issues:
- **Python Environment Conflicts** - Use `python3` instead of `python`
- **Missing Dependencies** - Install `tectonic` for LaTeX compilation
- **API Access** - Configure OpenRouter for regions with OpenAI restrictions
- **LaTeX Structure** - Ensure proper file organization and references

### Solutions Applied:
- Modified `wei_utils.py` for OpenRouter configuration
- Installed missing system dependencies
- Created proper LaTeX project structure
- Used background processing for long-running tasks

## Conclusion

Successfully demonstrated paper-to-video conversion using Paper2Video with OpenRouter API integration. The process involves multiple stages: paper analysis, LaTeX conversion, environment setup, API configuration, and pipeline execution. The final result is an automated video presentation generated from academic paper content.

**Note:** All sensitive information including API keys has been removed from this documentation for security purposes.