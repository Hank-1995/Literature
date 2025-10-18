# Litstudy Demonstration and Hands-on Activities
**Part 4 of HKU AI Agents in Education Workshop**

## 🎯 Learning Objectives
- Understand litstudy as a systematic literature review tool
- Experience automated literature analysis capabilities
- Learn to use litstudy for research project planning
- Apply litstudy to your own research interests

## 📚 What is Litstudy?

### Overview:
**Litstudy** is an open-source Python package for systematic literature reviews that automates:
- **Citation Network Analysis**: Visualize research connections
- **Author Collaboration Networks**: Identify research communities
- **Topic Modeling**: Discover research themes using NLP
- **Trend Analysis**: Track research evolution over time
- **Bibliometric Analysis**: Quantitative research metrics

### Key Features:
- **Automated Data Collection**: From multiple academic databases
- **Network Analysis**: Citation and collaboration networks
- **Text Mining**: Topic modeling and keyword analysis
- **Visualization**: Interactive charts and network diagrams
- **Export Capabilities**: Multiple output formats

## 🛠️ Technical Setup

### Prerequisites:
```bash
# Python 3.7+ required
python --version

# Install litstudy
pip install litstudy

# Additional dependencies
pip install pandas matplotlib networkx scikit-learn
```

### Installation Verification:
```python
import litstudy
print("Litstudy version:", litstudy.__version__)
```

## 🎬 Live Demonstration (10 minutes)

### Demo 1: Citation Network Analysis (3 minutes)

#### Scenario:
"Analyze the citation network for AI in education research"

#### AI Agent + Litstudy Workflow:
```python
import litstudy
import matplotlib.pyplot as plt

# AI Agent generates litstudy code
# 1. Load literature collection
papers = litstudy.load_collection("ai_education_papers.csv")

# 2. Create citation network
network = litstudy.create_citation_network(papers)

# 3. Visualize network
plt.figure(figsize=(12, 8))
litstudy.plot_network(network, node_size=50, edge_width=0.5)
plt.title("Citation Network: AI in Education Research")
plt.show()

# 4. Analyze network properties
print("Network density:", network.density())
print("Number of components:", network.number_of_components())
```

#### Expected Output:
- **Network Visualization**: Interactive citation network
- **Network Metrics**: Density, clustering, centrality
- **Key Papers**: Highly cited and influential papers
- **Research Clusters**: Thematic groupings

### Demo 2: Author Collaboration Networks (3 minutes)

#### Scenario:
"Identify research communities and collaboration patterns"

#### AI Agent + Litstudy Workflow:
```python
# AI Agent generates collaboration analysis
# 1. Extract author information
authors = litstudy.extract_authors(papers)

# 2. Create collaboration network
collab_network = litstudy.create_collaboration_network(authors)

# 3. Visualize collaboration
plt.figure(figsize=(10, 8))
litstudy.plot_collaboration_network(collab_network)
plt.title("Author Collaboration Network")
plt.show()

# 4. Identify research communities
communities = litstudy.detect_communities(collab_network)
print("Number of research communities:", len(communities))
```

#### Expected Output:
- **Collaboration Network**: Author co-authorship patterns
- **Research Communities**: Thematic author groups
- **Key Collaborators**: Central authors in networks
- **Collaboration Patterns**: Cross-institutional partnerships

### Demo 3: Topic Modeling and Trend Analysis (4 minutes)

#### Scenario:
"Discover research themes and track evolution over time"

#### AI Agent + Litstudy Workflow:
```python
# AI Agent generates topic analysis
# 1. Extract and preprocess text
texts = litstudy.extract_abstracts(papers)
processed_texts = litstudy.preprocess_text(texts)

# 2. Perform topic modeling
topics = litstudy.topic_modeling(processed_texts, n_topics=10)

# 3. Visualize topics
plt.figure(figsize=(12, 6))
litstudy.plot_topic_distribution(topics)
plt.title("Research Topics in AI Education")
plt.show()

# 4. Analyze trends over time
trends = litstudy.analyze_trends(papers, topics)
litstudy.plot_trends(trends)
plt.title("Research Trends Over Time")
plt.show()
```

#### Expected Output:
- **Topic Distribution**: Main research themes
- **Trend Analysis**: Evolution of topics over time
- **Keyword Analysis**: Most frequent and important terms
- **Temporal Patterns**: Research focus changes

## 🎯 Hands-on Activity: Litstudy for Your Research (15 minutes)

### Activity Setup:
**Duration**: 15 minutes  
**Format**: Individual or pairs  
**Materials**: Sample literature collections, litstudy access

### Activity Tasks:

#### Task 1: Literature Collection Setup (5 minutes)

##### AI Agent Prompt:
```
"Help me set up a literature collection for my research on [your topic]. 
I want to analyze recent papers (2020-2024) from major education journals. 
Create a litstudy collection and provide analysis options."
```

##### Expected Actions:
1. **Define Research Scope**: Topic, time range, journals
2. **Create Collection**: Set up litstudy data structure
3. **Data Validation**: Check collection quality
4. **Analysis Planning**: Identify analysis options

#### Task 2: Network Analysis (5 minutes)

##### AI Agent Prompt:
```
"Analyze the citation and collaboration networks in my literature collection. 
Identify key papers, influential authors, and research communities. 
Generate visualizations and provide insights."
```

##### Expected Output:
- **Citation Network**: Paper citation relationships
- **Collaboration Network**: Author co-authorship patterns
- **Key Insights**: Influential papers and authors
- **Research Communities**: Thematic groupings

#### Task 3: Topic Analysis (5 minutes)

##### AI Agent Prompt:
```
"Perform topic modeling on my literature collection. 
Identify main research themes, track trends over time, 
and suggest underexplored areas for future research."
```

##### Expected Output:
- **Topic Model**: Main research themes
- **Trend Analysis**: Evolution over time
- **Research Gaps**: Underexplored areas
- **Future Directions**: Research opportunities

### Sample Research Topics for Activity:

1. **AI-Powered Personalized Learning**
   - Focus: Adaptive learning systems
   - Time Range: 2020-2024
   - Journals: Computers & Education, Educational Technology Research

2. **AI in Assessment and Evaluation**
   - Focus: Automated grading and feedback
   - Time Range: 2020-2024
   - Journals: Assessment & Evaluation in Higher Education, Educational Assessment

3. **AI Ethics in Education**
   - Focus: Privacy, bias, and ethical considerations
   - Time Range: 2020-2024
   - Journals: AI & Society, Ethics and Information Technology

4. **AI for Student Support Services**
   - Focus: Chatbots, tutoring, academic assistance
   - Time Range: 2020-2024
   - Journals: Higher Education, Student Success

5. **AI in Curriculum Development**
   - Focus: Content creation and course design
   - Time Range: 2020-2024
   - Journals: Curriculum Journal, Teaching and Teacher Education

## 📊 Expected Outcomes

### Technical Skills:
- **Litstudy Proficiency**: Basic to intermediate usage
- **Network Analysis**: Understanding citation and collaboration patterns
- **Topic Modeling**: Identifying research themes
- **Visualization**: Creating effective research visualizations

### Research Skills:
- **Literature Review**: Systematic approach to literature analysis
- **Research Planning**: Identifying research opportunities
- **Collaboration**: Understanding research networks
- **Trend Analysis**: Tracking research evolution

### AI Agent Integration:
- **Automated Analysis**: Using AI agents with litstudy
- **Code Generation**: AI agent assistance with litstudy code
- **Interpretation**: AI agent help with results analysis
- **Documentation**: AI agent support for research documentation

## 🔄 Discussion and Reflection

### Group Discussion Questions:
1. **What patterns did you identify in your literature analysis?**
2. **How might litstudy change your literature review process?**
3. **What research opportunities did you discover?**
4. **How can AI agents enhance litstudy usage?**

### Individual Reflection:
- **Research Interests**: What topics interest you most?
- **Methodological Preferences**: What analysis approaches appeal to you?
- **Research Networks**: What collaboration opportunities exist?
- **Future Research**: What areas need more investigation?

## 📝 Assessment and Feedback

### Formative Assessment:
- **Progress Monitoring**: Check understanding throughout
- **Technical Support**: Address litstudy usage questions
- **Peer Feedback**: Share insights and learn from others
- **Skill Development**: Track improvement in litstudy usage

### Summative Assessment:
- **Analysis Quality**: Depth and accuracy of literature analysis
- **Technical Proficiency**: Effective use of litstudy tools
- **Research Planning**: Identification of research opportunities
- **Collaboration**: Understanding of research networks

## 🚀 Next Steps

### Immediate Applications:
- **Your Research**: Apply litstudy to your own literature review
- **Collaboration**: Work with peers on joint research projects
- **Skill Development**: Practice advanced litstudy techniques
- **Knowledge Sharing**: Share insights with research community

### Advanced Topics:
- **Systematic Reviews**: Comprehensive literature analysis
- **Meta-Analysis**: Quantitative synthesis of findings
- **Research Networks**: Collaboration and knowledge sharing
- **Publication Support**: Writing and publishing assistance

## 📚 Additional Resources

### Litstudy Documentation:
- **Official Repository**: https://github.com/nlesc/litstudy
- **Documentation**: https://nlesc.github.io/litstudy/
- **Examples**: Sample notebooks and tutorials
- **Community**: Discussion forum and support

### AI Agent Integration:
- **Code Generation**: AI agent assistance with litstudy
- **Analysis Support**: AI agent help with interpretation
- **Documentation**: AI agent support for research documentation
- **Collaboration**: AI agent assistance with team research

---

**Duration**: 15 minutes  
**Format**: Live demonstration and hands-on activity  
**Materials**: Litstudy access, sample literature collections, AI agent support
