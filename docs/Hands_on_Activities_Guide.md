# Hands-on AI Agent Activities
**Part 2 of HKU AI Agents in Education Workshop**

## 🎯 Activity Overview
**Duration**: 45 minutes  
**Format**: Interactive hands-on exercises  
**Participants**: Individual or pairs

## 📋 Pre-Activity Setup

### Technical Requirements:
- Laptop with internet connection
- AI agent access (GitHub Copilot, ChatGPT, or similar)
- Text editor or IDE (VS Code recommended)
- Sample research materials (provided)

### Workspace Setup:
```bash
# Create workshop directory
mkdir hku_ai_workshop
cd hku_ai_workshop

# Create subdirectories
mkdir research_papers
mkdir analysis_outputs
mkdir code_examples
```

## 🛠️ Activity 1: File Management and Document Processing (15 minutes)

### Objective:
Learn to use AI agents for file operations and document analysis

### Tasks:

#### Task 1.1: Create Research Folder Structure (5 minutes)
**Instructions**:
1. Ask AI agent to create a research project folder structure
2. Include subfolders for: papers, data, analysis, outputs
3. Generate a project README with your research goals

**AI Agent Prompt Example**:
```
"Create a research project folder structure for my study on AI in education. 
Include subfolders for literature, data, analysis, and outputs. 
Generate a README file with my research objectives."
```

**Expected Output**:
```
hku_ai_workshop/
├── literature/
├── data/
├── analysis/
├── outputs/
└── README.md
```

#### Task 1.2: Document Analysis (10 minutes)
**Instructions**:
1. Upload a sample research paper (provided)
2. Ask AI agent to extract key information
3. Generate structured summary

**AI Agent Prompt Example**:
```
"Analyze this research paper on AI in education. Extract:
- Research questions and objectives
- Methodology used
- Key findings
- Limitations and future work
- Generate a structured summary"
```

**Expected Output**:
- Structured analysis report
- Key findings extraction
- Methodology summary
- Research gaps identification

## 💻 Activity 2: Code Generation and Data Analysis (15 minutes)

### Objective:
Experience AI agent code generation and execution capabilities

### Tasks:

#### Task 2.1: Generate Data Analysis Code (10 minutes)
**Instructions**:
1. Describe your research data needs
2. Ask AI agent to generate analysis code
3. Execute and modify the code

**Sample Data Scenario**:
```
"I have survey data from 200 students about their experience with AI tools in education. 
The data includes: age, major, AI tool usage, satisfaction ratings, and learning outcomes. 
I want to analyze the relationship between AI tool usage and learning outcomes."
```

**AI Agent Prompt Example**:
```
"Generate Python code to analyze survey data about AI tool usage in education. 
Include data loading, descriptive statistics, correlation analysis, and visualizations. 
The data has columns: age, major, ai_usage, satisfaction, learning_outcomes."
```

**Expected Output**:
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data
df = pd.read_csv('survey_data.csv')

# Descriptive statistics
print(df.describe())

# Correlation analysis
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.title('Correlation Matrix: AI Usage and Learning Outcomes')
plt.show()

# AI usage vs learning outcomes
plt.scatter(df['ai_usage'], df['learning_outcomes'])
plt.xlabel('AI Tool Usage')
plt.ylabel('Learning Outcomes')
plt.title('AI Usage vs Learning Outcomes')
plt.show()
```

#### Task 2.2: Debug and Modify Code (5 minutes)
**Instructions**:
1. Introduce an error in the generated code
2. Ask AI agent to debug and fix
3. Modify code for additional analysis

**AI Agent Prompt Example**:
```
"The code has an error when loading the data. The file is actually an Excel file, 
not CSV. Also, I want to add a regression analysis to predict learning outcomes 
based on AI usage and other factors."
```

## 🔍 Activity 3: Web Search and Information Gathering (15 minutes)

### Objective:
Learn to use AI agents for research information gathering

### Tasks:

#### Task 3.1: Literature Search (10 minutes)
**Instructions**:
1. Define your research topic
2. Ask AI agent to search for relevant papers
3. Analyze and synthesize findings

**Research Topic Example**:
```
"Find recent research (2023-2024) on the impact of AI tools on student learning outcomes in higher education. 
Focus on empirical studies with quantitative data."
```

**AI Agent Prompt Example**:
```
"Search for recent empirical studies on AI tools in higher education. 
Look for papers published in 2023-2024 that include quantitative data on learning outcomes. 
Extract key findings, methodologies, and research gaps."
```

**Expected Output**:
- List of relevant papers with abstracts
- Key findings summary
- Methodology analysis
- Research gaps identification

#### Task 3.2: Information Synthesis (5 minutes)
**Instructions**:
1. Review the gathered information
2. Ask AI agent to synthesize findings
3. Identify research opportunities

**AI Agent Prompt Example**:
```
"Based on the literature I found, synthesize the key findings about AI tools in higher education. 
Identify common themes, conflicting results, and underexplored areas for future research."
```

## 📊 Activity 4: Research Planning and Organization (15 minutes)

### Objective:
Use AI agents for research project planning and organization

### Tasks:

#### Task 4.1: Research Question Development (5 minutes)
**Instructions**:
1. Describe your research interests
2. Ask AI agent to help develop research questions
3. Refine and prioritize questions

**AI Agent Prompt Example**:
```
"I'm interested in studying how AI tools affect student learning in higher education. 
Help me develop specific, researchable questions. Consider different aspects like 
learning outcomes, student engagement, and pedagogical approaches."
```

#### Task 4.2: Research Methodology Planning (10 minutes)
**Instructions**:
1. Select a research question
2. Ask AI agent to suggest methodologies
3. Create a research plan

**AI Agent Prompt Example**:
```
"For my research question about AI tools and learning outcomes, suggest appropriate 
research methodologies. Include data collection methods, analysis approaches, and 
ethical considerations."
```

**Expected Output**:
- Research methodology framework
- Data collection plan
- Analysis strategy
- Timeline and resources needed

## 🎯 Activity Reflection and Discussion

### Group Discussion Questions:
1. **What surprised you most about AI agent capabilities?**
2. **How might AI agents change your research workflow?**
3. **What challenges did you encounter?**
4. **What would you like to explore further?**

### Individual Reflection:
- **Write down 3 ways you could use AI agents in your research**
- **Identify 1 specific research task you'd like to try with AI agents**
- **Note any questions or concerns about AI agent use**

## 📝 Activity Checklist

### Completion Checklist:
- [ ] Created research folder structure
- [ ] Analyzed sample research paper
- [ ] Generated and executed data analysis code
- [ ] Performed web search for literature
- [ ] Synthesized research findings
- [ ] Developed research questions
- [ ] Created research methodology plan
- [ ] Participated in group discussion
- [ ] Completed individual reflection

### Troubleshooting Support:
- **Technical Issues**: AI agent access problems
- **Code Errors**: Debugging assistance
- **Research Questions**: Methodology guidance
- **Time Management**: Activity prioritization

## 🚀 Next Steps

### Immediate Follow-up:
- **Practice**: Try AI agents with your own research
- **Explore**: Experiment with different AI agent capabilities
- **Share**: Discuss experiences with peers

### Advanced Activities:
- **Literature Review**: Systematic review using AI agents
- **Data Analysis**: Complex statistical analysis
- **Writing Support**: Research paper drafting and editing
- **Collaboration**: Team research with AI agents

---

**Duration**: 45 minutes  
**Format**: Hands-on exercises with instructor support  
**Materials**: Sample research papers, data files, code templates
