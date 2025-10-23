# Secondary school students' mental models and attitudes regarding artificial intelligence - A scoping review

## Metadata
- **Author**: Erik Marx
- **Subject**: Computers and Education: Artificial Intelligence, 5 (2023) 100169. doi:10.1016/j.caeai.2023.100169
- **Creator**: Elsevier
- **Producer**: Acrobat Distiller 8.1.0 (Windows)
- **Creation Date**: D:20250102213905Z
- **Modification Date**: D:20250106114018Z
- **Source File**: Secondary-school-students--mental-models-and-atti_2023_Computers-and-Educati.pdf
- **Converted**: 2025-10-23 22:46:12

---

## Content

--- Page 1 ---

Computers and Education: Artificial Intelligence 5 (2023) 100169
Available online 4 October 2023
2666-920X/© 2025 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).
Secondary school students’ mental models and attitudes regarding artificial 
intelligence - A scoping review 
Erik Marx a,b,*, Thiemo Leonhardt a,b, Nadine Bergner c 
a TUD Dresden University of Technology, Professur für Didaktik der Informatik, N¨othnitzer Straße 46, 01187, Dresden, Germany 
b Center for Scalable Data Analytics and Artificial Intelligence (Sca DS.AI), Dresden, Leipzig, Germany 
c RWTH Aachen University, Professur für Didaktik der Informatik, Templergraben 55, 52062, Aachen, Germany   
A R T I C L E  I N F O   
Keywords: 
Artificial intelligence 
K-12 education 
Mental models 
Attitudes 
Conceptions 
Scoping review 
A B S T R A C T   
With the increasing relevance of Artificial Intelligence (AI) in society, AI literacy is increasingly being integrated 
into K-12 education. However, students already form conceptions about modern technologies (especially AI) 
from their interaction with their everyday environment. In this paper, we conduct a systematic scoping review on 
the emerging research field of secondary school students’ mental models and attitudes regarding AI. Our goal is 
to identify research approaches and uncover research gaps. To achieve this, we reviewed literature published 
within the timeframe of 2012–2022 found in the ACM, IEEE, ERIC, and Science Direct databases. In total, we 
identified 18 relevant papers, for which we collected and evaluated research objectives, approaches, results, and 
areas requiring further investigation. Our findings reveal that most of the literature examined focuses with 
students’ attitudes toward AI and moderating variables. Additionally, there is preliminary research on the types 
of mental models students possess about AI. Notable research gaps include the absence of development of 
research instruments for surveying mental models and insufficient research into the impact of learning in-
terventions on the construction of students’ mental models.   
1. Introduction 
Advancements in the field of artificial intelligence (AI), and specif-
ically machine learning (ML), have an increasing impact on our daily 
lives (Elliott, 2019) and in the way we work (Brynjolfsson & Mitchell, 
2017; Zhang & Dafoe, 2019). However, despite this growing influence, 
many individuals are still unfamiliar with terms such as ML and its 
underlying technology (Nader et al., 2022). Therefore, there is a 
growing belief that teaching AI, particularly ML, will be one of the next 
major frontiers in computer science education (CSE), as evidenced by 
the development of various AI literacy frameworks (Long & Magerko, 
2020; Michaeli et al., 2022; D. Touretzky et al., 2022). 
The objective of these frameworks is to cultivate AI competencies 
that will enable students to gain a comprehensive understanding of AI 
and its associated algorithms. Tedre et al. (2021) note that ML contra-
dicts some fundamental computational thinking (CT) concepts such as 
correctness, transparency, or problem-solving strategies. Consequently, 
a question arises regarding the extent to which students can tie AI 
competencies to existing CT competencies; this applies not only to 
overarching concepts, as emphasized by Tedre et al., but also to specific 
topics. For instance, Tedre et al. (2021) place significant emphasis on the 
role of neural networks, and the grade band progression chart of Tour-
etzky et al. (2022) introduces neural networks from grades 3 to 5 on-
wards. By contrast, other frameworks, like that proposed by Long and 
Magerko (2020), mention neural networks either not at all, or in passing 
as one among many possible ML models (Michaeli et al., 2022). 
Informed decision-making regarding the inclusion of concepts such as 
neural networks in specific grade levels is underpinned by research on 
students’ comprehension of individual concepts. This is supported in 
turn by Touretzky et al. (2022), who state the construction of appro-
priate mental models as a goal of their framework, making it imperative 
for future research to investigate the extent to which their framework 
fosters the development of these mental models. Moreover, insights 
gained from research on students’ conceptions of AI can help to devise 
educational materials that tie into their existing prior knowledge 
(Gentner, 2001; Greca & Moreira, 2000) and helps educators to identify 
and address their students’ conceptual errors (Hazzan et al., 2011). 
The importance of research on mental models in ML is also supported 
by Tedre et al. (2021), who identified research on mental models and 
notional machines as one of many emerging research trajectories. The 
* Corresponding author. TUD Dresden University of Technology, Germany. 
E-mail addresses: erik.marx@tu-dresden.de (E. Marx), thiemo.leonhardt@tu-dresden.de (T. Leonhardt), bergner@informatik.rwth-aachen.de (N. Bergner).  
Contents lists available at Science Direct 
Computers and Education: Artificial Intelligence 
journal homepage: www.sciencedirect.com/journal/computers-and-education-artificial-intelligence 
https://doi.org/10.1016/j.caeai.2023.100169 
Received 5 May 2023; Received in revised form 15 September 2023; Accepted 23 September 2023   

--- Page 2 ---

Computers and Education: Artificial Intelligence 5 (2023) 100169

objective of this paper is to shed further light on this novel research 
direction and to uncover existing research approaches, methods, and 
open research gaps by conducting a systematic literature review on 
research on secondary school students’ mental models and attitudes 
towards AI. We will use the scoping review method recommended by 
Peters et al. (2020), as it is particularly “appropriate in assessing and 
understanding the extent of knowledge in an emerging field” (p. 5) and 
to “explore the breadth/depth of the literature, inform future research, 
and identify/address knowledge gaps” (p. 4). For this study, we pose the 
following research questions. 
RQ 1: What are the research directions on students’ mental models 
and attitudes regarding AI to date? 
RQ 2: What open research gaps regarding students’ mental models 
and attitudes regarding AI can be identified? 
In the following sections, we will first clarify the theoretical foun-
dations leading us to focus on students’ mental models and attitudes. 
Then, we will present related works and describe the scoping review as 
our method of choice. We will then present and discuss the results, 
highlighting uncovered research areas. 
2. Theoretical background 
A key question in education research concerns the internal learning 
processes of students and how acquired information is retained and 
applied. One concept that explains how individuals explain the world, 
solve problems, or form hypotheses is that of mental models (Gentner, 
2001; Greca & Moreira, 2000; Rapp, 2005; Seel et al., 2000), a notion 
that has revolutionary implications for science education (Greca & 
Moreira, 2000). The fundamental premise of mental model theory lies in 
the theory of constructivist knowledge acquisition. According to 
constructivism, knowledge is not transmitted by reception and repeti-
tion of lectures and books but rather built up by the learner. Learning 
occurs when the learner’s prior knowledge and interest converge with 
new learning experiences (Sorva, 2013; Taber, 2017). While construc-
tivism affects learning processes at a meta-theoretical level (Seel et al., 
2000), in the following we will take a closer look at mental models 
which are founded on the constructivist principles. While the “term 
mental model” was popularized in the 1980s in cognitive psychology, 
the basic idea is commonly attributed to Craik (1943), who theorized 
that people translate external events into internal models (as cited in 
Staggers & Norcio, 1993). Craik described these models as “internal 
representations of the external world that allow for the generation of 
inferences” (as cited in Rapp, 2005, p. 45). Rapp further elaborated and 
defined mental models as “internalized, organized knowledge structures 
that are used to solve problems” (Rapp, 2005, p. 46). 
Starting from Craik’s fundamental idea, according to Greca and 
Moreira (2000), with the publications of Johnson-Laird (1983) and 
Gentner and Stevens (1983), two main understandings of mental models 
formed: the “theoretical approach” and the “instructional approach.” The 
goal of Johnson-Laird’s theoretical approach is to present a unified theory 
that can be used to explain various cognitive phenomena (e.g., deductive 
reasoning or text comprehension) (as cited in Greca & Moreira, 2000). 
According to Johnson-Laird, mental models are temporary constructs that 
help us perform tasks that take place in the present moment (as cited in 
Gentner, 2001) and are thus rooted in short-term memory (Jones et al., 
2011). Johnson-Laird’s fundamental innovation, in contrast to the pre-
vailing ideas about mental processes within cognitive psychology at the 
time, was to assume that thinking in mental models does not require 
knowing or forming causal rules; instead, humans create a mental replica, 
an analog representation, of the current situation, and reason by manip-
ulating this replica and observing the effects of their manipulation (Greca 
& Moreira, 2000; Nitz & Fechner, 2018). Mental models are thus a way of 
representing knowledge, and manipulating these mental models consti-
tutes reasoning (Staggers & Norcio, 1993). 
The instructional approach derived from Gentner and Stevens’ 
(1983) book aims to characterize the knowledge that people develop 
about physical or technological systems (Greca & Moreira, 2000). Here, 
mental models provide an explanation for how people understand or 
reason about things in knowledge-rich domains (Gentner, 2001). Thus, 
they are situated in long-term memory (Jones et al., 2011). In Gentner 
and Stevens’ book, mental models are characterized as potential or 
conceivable causal models for the systems they represent. Unlike in 
Johnson-Laird’s approach, these mental models represent the entities of 
the system and their properties, as well as relationships in a causal 
context, more precisely through explicit rules in the form of causal 
chains (Greca & Moreira, 2000). In contrast to the theoretical approach, 
these models are reduced to the information relevant to the task—that 
is, they are simplified representations (Nitz & Fechner, 2018). In this 
framework, “thinking” entails the execution of these models; a mental 
simulation takes place and the results of this simulation are used to draw 
conclusions and provide explanations (Greca & Moreira, 2000). 
While these two concepts exhibit differences (some quite substan-
tial), they are usually not explicitly separated in practice. Ultimately, the 
two approaches tend to represent opposite ends of a spectrum, with one 
leaning more toward cognitive psychology and the other toward 
instructional traditions (Nitz & Fechner, 2018). In the following, we 
therefore do not want to further distinguish the two approaches and 
refer to Johnson-Laird (1993), according to whom the different concepts 
on mental models go back to “the same underlying reality” (p. 469). We 
define mental models as cognitive representations of situations or do-
mains that help in understanding, learning, reasoning, or predicting 
(Gentner, 2001; Greca & Moreira, 2000). 
2.1. Construction of mental models 
For educational research, it is not only the existence of mental 
models and their use that is of interest, but above all how mental models 
are constructed (following the principles of constructivism) and how this 
construction process can be influenced. Just as a multitude of publica-
tions can be found in which mental models are theorized in a wide va-
riety of forms, various models can be found that explain the dynamics of 
model construction (Aliberas et al., 2021). These construction processes 
can be described for specific application domains—for example, John-
son-Laird (1993) expounds on how mental models are constructed for 
the tasks of discourse comprehension or syllogistic reasoning— but more 
interesting for education research are the construction processes of 
mental models as representations of knowledge, for which, following the 
instructional approach of Genter and Stevens, there is no universally 
applicable theory (Greca & Moreira, 2000). Fundamental ideas about 
the construction of mental models can already be traced back to Piaget’s 
equilibrium theory, which posits two main processes in the construction 
of mental structures: Firstly, cognitive structures are adapted in order to 
be able to deal with new information (accommodation). Secondly, new 
information can be modified during the assimilation process to align with 
existing cognitive structures (as cited in Aliberas et al., 2021). Adher-
ence to existing mental structures explains both why mental models are 
partly based on explicit or implicit analogies to what is already known, 
and why changing students’ conceptions is sometimes quite challenging 
(Gentner, 2001; Greca & Moreira, 2000; Staggers & Norcio, 1993). Some 
researchers propose that the accommodation of new knowledge employs 
analogies with fixed structural features. Conversely, others suggest the 
use of more open metaphors that consider not only structural similarities 
but also differences, enabling learners to derive new mental models. 
Accordingly, analogies and metaphors provide structural supports for 
applying mental models to structurally similar knowledge (Staggers & 
Norcio, 1993). 
The construction of mental models is of particular interest in edu-
cation research fields such as conceptual change theory. In this field, 
many models have emerged that describe how students form and adapt 
mental models. For example, Posner et al., Schwarz et al., and Gutierrez 
E. Marx et al.                                                                                                                                                                                                                                    

--- Page 3 ---

Computers and Education: Artificial Intelligence 5 (2023) 100169

and Ogborn (all cited in Aliberas et al., 2021) describe models according 
to which students construct mental models. This list is not exhaustive, 
but serves to show the range of theories on the formation of mental 
models. What they all have in common is that they address the question 
of how instruction can influence the formation of mental models. An 
important influencing factor, which at the same time provides links to 
more commonly used terms in education, such as students’ conceptions, 
is the term conceptual model. 
2.2. Mental models and students‘ conceptions 
Initially, “conceptual model” was used differently by different au-
thors; for example, it has been used synonymously with mental models 
(Staggers & Norcio, 1993). Nowadays, however, the notion, formulated 
by Norman (1983) seems to be established, who distinguished concep-
tual models from mental models. Norman understood conceptual 
models as a suitable representation of a target system that a user is 
supposed to learn or understand. While coined in the context of 
human-computer-interaction (HCI), the concept of a conceptual model 
is also relevant to education, as Norman himself pointed out. Greca and 
Moreira (2000) expanded on the term and defined conceptual models as 
precise and complete representations of the perceivable reality that are 
consistent with accepted scientific knowledge of a community. These 
external representations can take the form of mathematical formula-
tions, analogies, or material artifacts. Similarly, Seel et al. (2000) 
defined a conceptual model as “a specific kind of a representation which 
is constructed in accordance with didactic principles in order to illus-
trate the main components and relationships of a complex system with 
the help of graphical diagrams or object-based replica” (p. 134). Con-
ceptual models are therefore not only used by researchers but are also 
created by teachers or other educators (Greca & Moreira, 2000; Norman, 
1983). 
In educational research, however, in addition to the concepts of 
mental and conceptual models, there are other terms that deal with the 
sense-making of students, the most widely used being “students’ con-
ceptions.” Research on students’ conceptions in the context of concep-
tual change research has been significantly influenced by mental model 
research (Nitz & Fechner, 2018; Vosniadou & Brewer, 1994). Additional 
terms (e. g., alternative conceptions, intuitive theories, beliefs, ideas) are 
also used, but with little consistency as to how these terms relate to each 
other (Taber, 2017). Therefore, throughout this paper, we will use 
“students’ conceptions” as an umbrella term for the concepts presented 
in this chapter. Nevertheless, some terms can be classified by dis-
tinguishing conceptual model from mental model. To wit: Misconceptions 
are learners’ ideas that are incompatible with currently accepted sci-
entific knowledge (Qian & Lehman, 2017)—that is, ideas that result 
from the difference between the learner’s mental model and the con-
ceptual model—while preconceptions are mental models that were 
already formed before the instruction and were not influenced by con-
ceptual models or instruction (Seel et al., 2000). 
Of particular importance for CSE is the concept of the notional ma-
chine. According to du Boulay et al. (1981), a notional machine is an 
“idealized, conceptual computer whose properties are implied by the 
constructs in the programming language employed” (p.237). Du Boulay 
et al. introduced the term to develop instructional methods for learning 
programming, by designing programming languages that provide the 
learner insights into the states of the system through the notional ma-
chine; they did not discuss whether the notional machine refers to the 
mental representation of a machine in the student’s mind (mental 
model) or an abstract representation of how a programming language 
functions (conceptual model). Sorva (2013) is more explicit in his re-
view, and does not categorize notional machines as mental models or 
descriptions/visualizations of the computer. As expected, there are 
contributions in the literature that on one hand associate notional ma-
chines with mental models (Tedre, Toivonen et al., 2021; D. S. Tour-
etzky, 2017) and on the other hand understand them as a form of 
conceptual model (Fincher et al., 2020). Notional machines are also 
relevant in the field of machine learning. Tedre et al. (2021; 2021) 
argued that notional machines in ML fundamentally differ from those in 
traditional programming, which opens research potential in this area. 
2.3. Mental models in the learning process 
The integration of mental models into the general learning process, 
according to instructional theory, can be understood through the 
extensive framework proposed by Snow (1990). Within this framework, 
mental models are categorized as “conceptual structures” which 
encompass various types of declarative knowledge. According to Snow 
(1990), the construction of mental models follows a developmental 
progression, starting from initial preconceptions and culminating in 
desired causal models. Building upon this framework, Seel et al. (2000) 
emphasize the significance of conceptual models in shaping the learning 
process (see Fig. 1). 
According to Snow’s framework, the learning process is also influ-
enced by factors grouped under “motivational orientation,” which in-
cludes interest, motivation, self-concept, and self-efficacy; these are also 
named as main affective influencing factors by Fortus (2014). Further-
more, Fortus emphasizes the impact of attitudes on the learning process. 
While self-efficacy, self-concept, and motivation occur situationally or 
action-related and cannot be directly connected to a specific topic such 
as AI, attitudes and interest can be linked to a specific learning content 
or area. Hidi and Renninger (2006) describe situational interest as 
aiming to generate and sustain attention, thereby enabling the devel-
opment of individual interest as a relatively permanent disposition. 
Because interest is a permanent disposition in a person-object relation-
ship, and AI is only one topic area of CSE, we argue that interest research 
specifically for AI does not provide new aspects in the context of CSE 
research. However, this is different for the relationship between atti-
tudes and the learning process as it relates to the development of mental 
models in AI. From a psychological perspective, there exists no singular 
definition of attitude. Allport (1935), one of the co-founders of the field 
of personality psychology, defines attitude as an individuals’ mental 
readiness to adopt a particular position toward a given object or person. 
Eagly and Chaiken, in their standard work The Psychology of Attitudes 
(1993), define attitude as “a psychological tendency expressed by 
valuing a particular object with some degree of favor or disfavor” (p. 1). 
Ajzen (2001) lists examples for attribute dimensions such as good-bad, 
harmful-beneficial, pleasant-unpleasant, and likeable-unlikeable. Maio 
and Haddock (2023) list numerous definitions of attitudes and sum-
marizes that despite subtle differences among definitions, all involve the 
expression of an evaluative judgment about an object; inferring from 
this, they define an attitude as an “overall evaluation of an object that is 
based on cognitive, affective, and behavioral information” (p. 4). It is 
desirable in many fields to measure attitudes and know the degree of 
people’s attitude toward a given object or situation because attitudes 
significantly influence human behavior (Maio & Haddock, 2023). The 
topicality of the subject in the news, as well as the fictional treatment of 
AI in novels and movies, suggests a preconceptual attitude toward AI 
Fig. 1. Mental models in the learning process (adapted from Seel et al., 2000; 
authors’ extension highlighted in green). (For interpretation of the references to 
colour in this figure legend, the reader is referred to the Web version of 
this article.) 
E. Marx et al.                                                                                                                                                                                                                                    

--- Page 4 ---

Computers and Education: Artificial Intelligence 5 (2023) 100169

that is independent of mental models of how AI works. This, in turn, may 
influence the learning process and thus the development of mental 
models. To account for this, we extend the model of Seel et al. to include 
motivational influencing factors, especially attitudes, indicated in green 
(see Fig. 1). 
Finally, in addition to the aforementioned psychological constructs, 
the construction of mental models must be seen in the context of the 
learning situation: that is, mental models are shaped by the distinctive 
features of learning situations and the interactions of learners with them 
(Seel et al., 2000). Learning situations should be viewed in the context of 
instructional design, which encompasses any deliberate organization of 
environmental conditions to foster competence development. To un-
derscore the significance of learning situations in this context, we 
further consolidate them under the term learning interventions. 
2.4. Elicitation of mental models 
There is no universally applicable method for assessing mental 
models; because mental models are subjective, abstract, and dynamic 
constructs (Greca & Moreira, 2000; Rapp, 2005), they can only be 
assessed indirectly (Staggers & Norcio, 1993). Also, depending on how 
mental models are defined (that is, theoretically or instructionally), 
fundamentally different assessment methods are required. Additionally 
Staggers and Norcio (1993) raise the fundamental question of whether 
the assessment of mental models measures a process or a product. This is 
well illustrated by the model proposed by Seel et al. (2000), shown in 
Fig. 1; assessments at the start or endpoint of the learning process can be 
understood as assessments of mental models as a product, while as-
sessments focusing on the mental model progression can be understood 
as assessments of a process. 
How can mental models be determined? Classical assessment 
methods include interviews or questionnaires and the analysis of think- 
aloud protocols (Gentner, 2001); however, because individuals may not 
necessarily think in the mental models they articulate—for instance, 
even experts use individual mental models but formalize their thoughts 
into conceptual models (Greca & Moreira, 2000)—the collected mental 
models must be validated using other procedures. Once these rudi-
mentary mental models are known, materials can be developed to 
interact with these models, such as contradicting the mental model to 
trigger conceptual change (Gentner, 2001). 
3. Related work 
There are already some systematic literature reviews in the field of AI 
literacy and students’ conceptions conducted. Tedre et al. (2021) 
reviewed 63 articles dealing with ML education in K–12. The aim of the 
review was to explore what innovations the field of AI and especially ML 
brings to CSE and thus to identify emerging trajectories in educational 
practice, theory, and technology. In doing so, the researchers identified 
13 areas from which research on the construction of mental models in 
the field of ML is one of them; however, they did not elaborate on the 
current state of research, nor was this in the scope of the review. They 
concluded that the notional machines and mental models for ML in CSE 
are bound to be different and little research in the direction exists so far. 
Rather than review research approaches, we presented a summary of 
previous findings on students’ conceptions of AI, concluding that stu-
dents’ conceptions are influenced by (entertainment) media, science 
fiction, and the anthropomorphization of AI, and that the technical 
background of AI is mostly unknown to students. Furthermore, students 
perceive AI mainly as “autonomously acting systems whose actions are 
directly observable” (p. 2), which is reflected in their perception of 
applications such as facial recognition, voice assistants or autonomous 
cars as AI. However, we did not list an analysis of existing research 
approaches or methods used, as this was our initial exploratory research 
serving as a baseline for this scoping review (see also Section 4.1.; Marx 
et al., 2022). 
Based on a literature review, Long and Magerko (2020) developed an 
AI literacy framework in which they presented AI competencies and 
design considerations. To this end, they explored, among other things, 
what general misconceptions non-technical learners may have; in a 
digression, they examined young children’s preconceptions about AI. 
Based on their review, they offer design recommendations according to 
which AI curricula should be designed. However, the search terms 
used—“perceptions of AI,” “misconceptions AI,” “AI in the home,” “in-
teractions with AI,” and “AI in media” (p. 3)—were missing important 
terms relevant for the field, like “mental models,” and thus did not cover 
all potential literature. Further, the scope of the review was focused on 
adult non-technical learners and children. Furthermore, the goal of the 
study was to establish competency and design recommendations for AI 
literacy, not to review current research approaches to mental model 
research. Our research provides new insights by focusing on secondary 
school students (in contrast to non-technical learners of any age or 
children) and using more comprehensive search terms. 
A previous literature review by Li et al. (2022) examined the use and 
perception of AI technologies in education among children and adoles-
cents. The review identified five relevant articles and one research gap 
in children’s and adolescents’ use and perception of AI technologies in 
education. The selection of search terms was not comprehensive, but 
used, for example, “artificial intelligence” or “intelligent” as AI-related 
search terms; this may have missed systems or technologies, as the re-
searchers themselves noted as limitations of their study. 
Our review builds on the identified trajectory of mental model 
research by Tedre et al. (2021) as we review the current state of research 
and identify research approaches, along with gaps, by conducting a 
dedicated review on this issue specifically in contrast to the works of 
Tedre et al. (2021) and Long and Magerko (2020). In addition, our re-
view extends previous findings (Li et al., 2022; Marx et al., 2022) around 
research approaches and gaps through a systematic review with 
extended search terms. 
4. Methodology 
In this section, the scoping review methodology is presented. This 
review adapts the guidelines for scoping reviews (Peters et al., 2020) 
from the JBI organization with respect to the PRISMA-Sc R extension 
(Tricco et al., 2018). Though originating in health research, this 
approach is also used in CSE research (Su et al., 2022). Because the field 
of AI is complex and heterogeneous, a scoping review is particularly 
suited for this purpose (Peters et al., 2020). In the following, we present 
the inclusion criteria, search terms and data collection procedure. The 
scoping review process can be traced in Fig. 2. 
4.1. Search strategy 
Scoping reviews are an iterative process (Peters et al., 2020). As 
Tedre et al. (2021) noted through analysis of other systematic reviews 
on the topic of AI, initial exploratory research is suitable for the area of 
AI education research, due to ambiguity in terminology and different 
research approaches. In addition to the theoretical review presented in 
Section 2 we conducted initial exploratory research to identify 
commonly used terms and research approaches. This was done by first 
searching Google Scholar1 and Base Search2 for relevant literature. The 
citations used in the papers this found were searched for further suitable 
literature, continuing this systematically (Marx et al., 2022). 
By analyzing the results of the exploratory search and the theoretical 
background, the keywords for which the databases should be searched 
were defined. For the development of the search terms, we adapted the 
PCC mnemonic (population, concept, and context) recommended by 
1 https://scholar.google.de.  
2 https://www.base-search.net. 
E. Marx et al.                                                                                                                                                                                                                                    

--- Page 5 ---

Computers and Education: Artificial Intelligence 5 (2023) 100169

Peters et al. (2020). The keywords used for the first database searches 
are shown in Table 1. Note that this is only the formalized representation 
of the keywords and not the search query, as these differ in syntax for 
each database. The search queries used can be viewed in the Appendix. 
The exploratory preliminary research revealed that students also 
associate AI with robots (Ellis et al., 2007; Evangelista et al., 2018; 
Kreinsen & Schulz, 2021; Lindner et al., 2021; Mertala et al., 2022). It 
was therefore decided to include the terms robot and robotics. In order to 
account for edge cases in which papers examined several audiences (for 
example, children in an age range from primary to secondary educa-
tion), the terms primary school, university, and college were also included. 
Our data sources included the ACM,3 IEEE,4 ERIC,5 and Science 
Direct (SD6) databases. ACM focuses on computer science research, 
especially CSE research; IEEE extends the search area to engineering and 
technology education; ERIC broadens the scope to general education 
research; and SD includes even more general areas. Thus, the databases 
used cover the relevant search area from the specific consideration of 
CSE to related fields and general points of contact in research. In addi-
tion, each of these platforms offers open access. These databases were 
also used in other systematic reviews on AI (Gresse von Wangenheim 
et al., 2021; Li et al., 2022; Long & Magerko, 2020; Marques et al., 2020; 
Su et al., 2022). 
The ACM, IEEE, and ERIC databases were thus searched on 
December 1, 2022 by title and abstract. Queries were performed such 
that words independent of the singular/plural (conception/conceptions 
→ search term: conception+), as well as words containing part of the 
term (conception/pre-conception → search term: *conception), were 
matched if the databases did not already have these features. For our 
search of the IEEE database, the filter “Publication Topics” was used. 
Here the filters related to CSE or associated topics were selected. A 
detailed list of the filters used can be found in the Appendix. All records 
retrieved were then screened by title and abstract using the inclusion 
criteria described in Section 4.2. 
In a final step, a search of the Science Direct database was performed 
on January 4, 2023. Based on the findings of the exploratory investi-
gation in advance and the initial database search, it was found that the 
search terms for the supplementary search in SD could be adapted as 
shown in Table 2. Reasons for limiting the second search query are 
described in Section 6.1. These final records were screened by title and 
abstract as well. 
4.2. Inclusion criteria 
During the course of the research, the inclusion of records in the 
review was determined based on the inclusion criteria. The titles and 
abstracts of all entries were checked for the inclusion criteria. If these 
were not met, the entry was sorted out. For the development of the in-
clusion criteria, we again adapted the PCC mnemonic recommended by 
Peters et al. (2020). 
(1) Types of evidence sources: English papers in journals, confer-
ences, and reports were included for the study. We included both 
primary and secondary studies. Poster and extended abstracts 
were also collected but analyzed separately. 
(2) Target group: For the review, only papers dealing with second-
ary school students were considered, by which the age range of 
10–18 years was defined. Accordingly, papers dealing solely with 
primary or tertiary education were eliminated. If the target 
groups overlapped, as in studies on children aged 6–12 years, the 
study was included in the review.  
(3) Topic: Results were restricted to the topic of AI and associated 
terminology, including AI methods such as ML and specific ML 
models (e.g., neural networks). No restrictions were made ac-
cording to geographical locations or specific social, cultural, or 
gender-based factors.  
(4) Concept: Only records dealing with students’ conceptions in 
some form were considered. This means models implicitly formed 
by students, moderating variables such as attitudes, and learning 
Fig. 2. Adapted PRISMA flowchart (Tricco et al., 2018) showing the research process (rs = researcher, sa = student assistant).  
Table 1 
Keywords for database search 1 (ACM, IEEE, ERIC).  
Concept 
concept OR conception OR misconception OR mental model OR beliefs OR attitudes OR image OR views OR notional machines OR analogies OR perception 
AND 
Context 
artificial intelligence OR machine learning OR deep learning OR neural networks OR self-learning algorithms OR intelligent systems OR intelligent technologies OR 
agent learning OR intelligent agents OR robot OR robotics 
AND 
Population 
students OR pupils OR primary school OR secondary school OR college OR university  
Table 2 
Keywords for database search 2 (SD).  
Concept 
conceptions OR misconception OR mental models OR attitudes OR 
preconceptions OR pre-conceptions 
AND 
Context 
artificial intelligence OR machine learning 
AND 
Population 
students  
3 https://dl.acm.org/.  
4 https://ieeexplore.ieee.org/Xplore/home.jsp.  
5 https://eric.ed.gov/.  
6 https://www.sciencedirect.com/. 
E. Marx et al.                                                                                                                                                                                                                                    

--- Page 6 ---

Computers and Education: Artificial Intelligence 5 (2023) 100169

experiences whose effect on students’ conceptions were 
examined.  
(5) Age of sources: The range of AI methods and applications has 
expanded considerably over the past few years. In addition, AI is 
now discussed much differently in society and the media, and 
users now have direct experience with AI technologies. It is 
therefore to be expected that the conceptions of students have 
also changed significantly from several years ago. Therefore, only 
papers from the last ten years were considered. 
4.3. Evidence screening and selection 
The course of the search process can be traced in the flowchart (see 
Fig. 2), adapted from PRISMA. Entries obtained via the database query 
(n = 1813) were stored with title and abstract in a literature manage-
ment software and cleaned of duplicates (n = 13). Afterward, two re-
searchers (rs) and a student assistant (sa) independently screened all 
entries based on title and abstract according to the inclusion criteria. The 
results of each were then reunited (OR). A total of n = 44 papers were 
than analyzed by the researchers. First, 5 papers were selected and read 
independently by both researchers and analyzed according to the 
research questions. Based on this, a first charting table to record key 
findings was developed. Afterward, both researchers read half of the 
papers and filtered them by format (if the article was a poster or 
extended abstract) and by topic (if the content did not meet the inclusion 
criteria). This was followed by a joint exchange in which the charting 
table was adjusted. Subsequently, both researchers read all n = 44 pa-
pers again, recorded findings in the charting table, and confirmed the 
exclusion by format and content. Finally, papers that were sorted 
differently (n = 2) were discussed and included in agreement. This 
resulted in a total of n = 18 papers, which were then analyzed and 
discussed. 
4.4. Data analysis 
After all papers were screened and sorted, the remaining 18 papers 
were evaluated in relation to the research questions. As described in the 
JBI guidelines, the intention of a scoping review is not the synthesis of 
outcomes of the included sources, but descriptive analyses such as 
research approaches (Peters et al., 2020). For this purpose, we reread all 
papers and marked relevant passages, noting descriptive data such as the 
location of the studies, as well as the age and number of participants, and 
any learning interventions described. Additionally, the research ques-
tions and research gaps described in the papers were identified. Special 
attention was paid to analyzing the methodology and findings regarding 
the elicitation of mental models or attitudes. This involved evaluating 
questions in surveys or the presented results from audio and video re-
cordings and their discussions to determine the extent to which they 
explored mental models or attitudes. Since these points are central to the 
scoping review basic coding techniques were used, as recommended by 
Peters et al. (2020). The theoretical foundations described in Section 2 
served as the basis for this analysis. 
The two researchers analyzed the data independently and then dis-
cussed the results until a consensus was reached. Surveys were evaluated 
as attitudes research when respondents positioned themselves on or 
evaluated AI or aspects of it (Maio & Haddock, 2023). For example, 
survey questions such as “I think that AI should be taught in school” (Suh 
& Ahn, 2022, p. 8) or collected statements such as “Artificial intelligence 
is useful if used in the right way, and harmful if used in the wrong way” 
(Demir & Güraksin, 2022, p. 306) were assessed as attitudes research. 
Based on our definition of mental models as cognitive representa-
tions of situations or domains that help in understanding, learning, 
reasoning, or predicting, papers were assigned to mental model research 
either when students were asked directly about their mental models 
(“Describe how you think artificial intelligence works.” (Mertala et al., 
2022, p. 4) or the mental models had to be applied to perform tasks, e. g. 
“We gathered information [from the students] on what does learning 
mean for a computer.” (Evangelista et al., 2018, p. 2). In addition, we 
also counted self-assessments on these topics as mental model research 
(“I have general knowledge about how AI is being used today” (Chiu 
et al., 2022, p. 33). After collecting the necessary data in all papers as 
described, we discussed again and summarized the results. 
5. Results 
In this section, we present the results of the scoping review. We begin 
with findings from the review process itself. As was recognized in the 
preliminary considerations, many different terms are used both in the 
field of students’ conceptions and in the field of AI. Accordingly, the 
formulated search query was quite large. It soon became apparent that 
some keywords, such as image or perception, yielded many false positives, 
particularly in the form of papers on the topic of image recognition. 
Papers on adaptive response systems using AI technology were 
frequently mismatched, too. The keywords robotics and robot also 
returned many results dealing with the influence of robot programming 
on attitudes toward STEM. Overall, many keywords in the AI context 
failed to return papers corresponding to the research question. For 
example, only the terms AI and ML were used in papers dealing with 
students’ mental models. General characteristics of included studies are: 
Year of Publication: Most articles that met the selection criteria 
were published in 2021 and 2022 (67%). This is in line with the global 
trend of annually increasing publications on AI (Maslej et al., 2023). 
Fig. 3 shows the distribution of publication years of the analyzed papers 
and posters. 
Targeted age groups: In the papers we analyzed, overall, all age 
groups from 11 to 18 years are studied with a roughly equal distribution 
(see Fig. 4). As expected, there was a diminished focus on the age groups 
11, 17, and 18, which represent the lower and upper ends of the age 
spectrum. In the majority of papers, a wide age range was encompassed, 
with surveys conducted across four or more age groups. These studies 
were predominantly quantitative in nature, in contrast to a few papers 
that adopted a qualitative research approach, specifically targeting 
selected age groups. 
In some papers, only grade levels or general descriptors such as high 
school were provided, making it not possible to accurately determine the 
age groups studied. We added data from these papers by assuming 
school enrollment from the age 6 in Turkey (Demir & Güraksin, 2022) 
and China (Chai et al., 2021). Additionally, “high school” was assumed 
to include ages 15–18 for Poland (Bochniarz et al., 2022) and ages 15–17 
for Turkey (Korkmaz et al., 2014) respectively, based on an inquiry 
about the educational systems of the respective countries. Table 3 in-
cludes the reviewed papers and their surveyed age groups. 
Distribution by region: Studies of students’ conceptions are taking 
place in many different regions. We identified multiple studies in Asia 
(Chai et al., 2021; Chiu et al., 2022; Demir & Güraksin, 2022; Korkmaz 
et al., 2014; Sing et al., 2022; Sisman et al., 2019; Su et al., 2022; Suh & 
Ahn, 2022), Europe (Bochniarz et al., 2022; Conde et al., 2016; Mertala 
Fig. 3. Distribution of publication years.  
E. Marx et al.                                                                                                                                                                                                                                    

--- Page 7 ---

Computers and Education: Artificial Intelligence 5 (2023) 100169

et al., 2022; Voulgari et al., 2021), and North America (Dove & Fayard, 
2020; Druga & Ko, 2021; Van Brummelen et al., 2021), and one each in 
Africa (Sanusi & Olaleye, 2022), South America (Evangelista et al., 
2018), and Oceania (Ahmad et al., 2016), as shown in Fig. 5. This again 
demonstrates the global relevance of AI in CSE research. The biggest 
finding, however, is that most research on Students’ Conceptions of AI is 
carried out in Asia, even though we only examined English-language 
papers. This is further evidenced by the fact that the only meta-study 
in our review results focused specifically on the Asia-Pacific region 
(Su et al., 2022) (see Fig. 6). 
In the following sections, we will present the found papers according 
to their research foci. For this purpose, as introduced in Section 4.4, we 
analyzed the research questions, methodologies, and results of the pa-
pers and categorized them into groups: attitudes, mental models, and 
learning interventions. Beneath that, the research methods used to elicit 
the respective aspect are listed. The results can be traced in Table 4. It 
should be noted that a variety of papers appear in multiple categories. 
Some papers may touch on a category, but do not primarily focus on it; 
for example Druga and Ko (2021) use a survey with six items, three of 
which assess attitudes, but more extensively analyze video recordings, 
exploring the construction of mental models. This contrasts with the 
works of Sisman et al. (2019) and Suh and Ahn (2022), who each 
develop comprehensive attitude scales. To highlight these differences, 
we categorized the papers found into works with minor and major focus. 
5.1. Attitudes toward AI 
By far the most papers deal in some way with students’ attitudes 
toward AI. A total of 15 of the 18 papers deal with attitudes, with the 
majority using quantitative methods for data collection. Within these 
papers, different emphases on certain aspects of attitudes could be 
identified. For example, we have identified relevance, trustworthiness, 
and friendliness as perspectives on students’ attitudes. 
Attitudes are assessed both qualitatively and quantitatively. Quali-
tative studies either employ open-ended questions (Mertala et al., 2022), 
evaluate metaphors that students formulate about AI (Demir & Gür-
aksin, 2022) or robots (Korkmaz et al., 2014), or analyze video or audio 
recordings of how students make sense of machine intelligence (Druga & 
Ko, 2021) or how students perceive adaptive behavioral changes of ro-
bots (Ahmad et al., 2016). A common aspect across all data collection 
formats is that students are not explicitly queried about their attitudes. 
However, attitudes can still be inferred from the statements collected 
and related to the mentioned mental models. At the same time, this can 
sometimes mean that answers do not necessarily include attitudes, 
which makes an evaluation in this regard more difficult or not the focus 
(Druga & Ko, 2021; Korkmaz et al., 2014). 
Part of quantitative attitudes research aims to develop models to 
measure the interrelationships of different variables on students’ atti-
tudes. The influence of age (Conde et al., 2016) and cultural and ethical 
competencies (Sanusi & Olaleye, 2022) on the perception of AI were 
investigated, as well as the interrelationship with cynical hostility to-
ward AI (Bochniarz et al., 2022) and behavioral intentions toward 
learning AI (Chai et al., 2021). Additionally, general attitudes scales are 
also developed for AI (Suh & Ahn, 2022) and robots (Sisman et al., 
2019). 
Finally, surveys on students’ attitudes were used by three papers to 
evaluate learning interventions. Van Brummelen et al. (2021) designed a 
persona questionnaire, measuring the change in students’ attitudes to-
ward friendliness and trustworthiness of AI using a 7-point Likert scale. 
Similarly, Druga and Ko (2021) used questions on attitudes toward trust 
and friendliness to assess the effect of an learning interventions 
involving programming smart agents. Chiu et al. (2022) used a survey to 
test the effect of their AI curriculum, in part by assessing attitudes about 
Fig. 4. Distribution of the targeted age groups.  
Table 3 
Reviewed papers and researched age groups.  
age 
11–14 
(Ahmad et al., 2016; Chai et al., 2021; Chiu et al., 2022; Conde et al., 
2016; Demir & Güraksin, 2022; Druga & Ko, 2021; Evangelista et al., 
2018; Mertala et al., 2022; Sanusi & Olaleye, 2022; Sing et al., 2022;  
Sisman et al., 2019; Su et al., 2022; Suh & Ahn, 2022; Van Brummelen 
et al., 2021; Voulgari et al., 2021) 
age 
15–18 
(Bochniarz et al., 2022; Chiu et al., 2022; Conde et al., 2016;  
Evangelista et al., 2018; Korkmaz et al., 2014; Sanusi & Olaleye, 2022;  
Sing et al., 2022; Su et al., 2022; Suh & Ahn, 2022; Van Brummelen 
et al., 2021; Voulgari et al., 2021)  
Fig. 5. Distribution of studies by continent.  
E. Marx et al.                                                                                                                                                                                                                                    

--- Page 8 ---

Computers and Education: Artificial Intelligence 5 (2023) 100169

the relevance of AI. Further evidence on the effect of AI learning in-
terventions on students’ attitudes in the Asian region was collected by Su 
et al. (2022) in a systematic literature review on educational approaches 
for teaching AI at the K–12 levels showing the interest in attitude 
research in the field of AI. 
5.2. Mental models of AI 
In total, we identified 10 papers dealing with students’ mental 
models. While in the study of attitudes a tendency towards quantitative 
research was found, the same can be said here for qualitative (n = 3), 
quantitative (n = 6) and mixed (n = 1) approaches. However, a 
distinction must be made between studies with major and minor foci. 
Papers that focused on the elicitation of mental models assessed these 
almost exclusively qualitatively. Overall, two basic perspectives can be 
identified under which mental models have been studied. One 
perspective often studied is the question of how AI functions (function-
ality). Druga and Ko (2021) investigated how children make sense of 
machine intelligence by analyzing video recordings. In two papers 
metaphors were used to assess mental models. Demir and Güraksin 
(2022) examined the metaphors students used to describe AI and were 
able to identify several categories by which students assess the func-
tionality of AI. Korkmaz et al. (2014) also used metaphors to survey the 
change in students’ mental models after a learning interventions. Also 
qualitatively, Mertala et al. (2022) investigated not only students’ 
conceptions of functionality, but also what technologies students 
consider to be AI (application), as did Evangelista et al. (2018) 
quantitatively. 
The papers with minor focus are those concerned with attitudes and 
other influencing factors. Here, the aim was to investigate in-
terrelationships between AI literacy and other variables such as cynical 
hostility (Bochniarz et al., 2022) (see previous section). For this purpose, 
questionnaires with Likert scales were used, in which respondents were 
asked to rate certain statements (“Do you think that artificial intelli-
gence will reach the level of human thinking?” Bochniarz et al., 2022, p. 
2) or self-assessments (“I know that AI can be used to recognize images,” 
Chai et al., 2021, p. 94) thus providing a rudimentary insight into the 
underlying mental models. We also found three papers in which student 
self-assessments of their AI knowledge were employed to motivate the 
design of a learning intervention (Evangelista et al., 2018), to evaluate 
learning interventions (Chiu et al., 2022), and to investigate their 
interrelated relationship with other variables such as attitudes (Chai 
et al., 2021), respectively. 
5.3. Learning interventions 
Most of the work examining learning interventions in the context of 
mental models and attitudes has already been presented. Four studies in 
our review have assessed the change of attitudes and mental models 
through learning interventions. The emphasis of these studies was either 
on the evaluation of the proposed learning intervention (Chiu et al., 
2022) or the progression of mental models (Druga & Ko, 2021; Korkmaz 
et al., 2014; Van Brummelen et al., 2021). Other papers mentioned in-
terventions, but their influence on mental models or attitudes was not 
examined. To elaborate, in order for students in the studies of Chai et al. 
(2021) and Sing et al. (2022) to have the knowledge necessary for 
answering the survey, they took courses on AI beforehand. Similarly, 
Sisman et al. (2019) conducted a lesson with a robot and then surveyed 
students about their attitudes toward robots. Types of learning in-
terventions mentioned were workshops (Druga & Ko, 2021; Evangelista 
et al., 2018), lessons (Conde et al., 2016; Sisman et al., 2019) or 
curricula (Chiu et al., 2022; Korkmaz et al., 2014; Sing et al., 2022; Van 
Brummelen et al., 2021). 
Finally, we want to highlight the works of Dove and Fayard (2020), 
Evangelista et al. (2018), and Voulgari et al. (2021), who presented 
ideas for alternative conceptual models or learning interventions. For 
example, Dove and Fayard (2020) present a method using the AI-as--
monster metaphor, through which students can be taught important 
features of ML applications. Voulgari et al. (2021), by contrast, describe 
the design of an educational game that teaches various ML procedures in 
a playful way. Common to these works is that they present the devel-
opment of learning interventions that stimulate the formation of mental 
models in students, comparable to notional machines for program 
sequences. 
6. Discussion 
In the following, we first discuss the differences in terminology found 
in the papers and second the findings regarding the two research 
questions. 
6.1. Findings regarding terminology 
An important finding is that the terms used in the context of students’ 
conceptions are ambiguous and often used interchangeably. This can be 
well illustrated by the term perception, for example. Chai et al. (2021), 
Demir and Güraksin (2022), Druga and Ko (2021), Korkmaz et al. (2014) 
and Van Brummelen et al. (2021) all put this term at the center of their 
research and mentioned it in their titles, but none satisfactorily defined 
Table 4 
Research foci and approaches of the reviewed papers.  
categories 
attitudes 
mental models 
learning interventions 
Paper 
major focus 
Ahmad et al., 2016; Bochniarz et al., 2022; Chai et al., 
2021; Chiu et al., 2022; Conde et al., 2016; Demir & 
Güraksin, 2022; Mertala et al., 2022; Sanusi & Olaleye, 
2022; Sing et al., 2022; Sisman et al., 2019; Su et al., 
2022; Suh & Ahn, 2022; Van Brummelen et al., 2021 
Demir & Güraksin, 2022; Druga & Ko, 
2021; Korkmaz et al., 2014; Mertala et al., 
2022; Van Brummelen et al., 2021 
Chiu et al., 2022; Conde et al., 2016; Dove & Fayard, 
2020; Druga & Ko, 2021; Evangelista et al., 2018;  
Korkmaz et al., 2014; Van Brummelen et al., 2021;  
Voulgari et al., 2021 
minor focus 
Druga & Ko, 2021; Korkmaz et al., 2014 
Bochniarz et al., 2022; Chai et al., 2021;  
Chiu et al., 2022; Evangelista et al., 2018;  
Sing et al., 2022 
Chai et al., 2021; Sing et al., 2022; Sisman et al., 2019 
Research method 
qualitative 
Ahmad et al., 2016; Demir & Güraksin, 2022; Korkmaz 
et al., 2014; Mertala et al., 2022 
Demir & Güraksin, 2022; Korkmaz et al., 
2014; Mertala et al., 2022 
Korkmaz et al. (2014) 
quantitative 
Bochniarz et al., 2022; Chai et al., 2021; Chiu et al., 
2022; Conde et al., 2016; Druga & Ko, 2021; Sanusi & 
Olaleye, 2022; Sing et al., 2022; Sisman et al., 2019; Suh 
& Ahn, 2022; Van Brummelen et al., 2021 
Bochniarz et al., 2022; Chai et al., 2021;  
Chiu et al., 2022; Evangelista et al., 2018;  
Sing et al., 2022; Van Brummelen et al., 

Chai et al., 2021; Chiu et al., 2022; Conde et al., 2016;  
Evangelista et al., 2018; Sing et al., 2022; Sisman et al., 
2019; Van Brummelen et al., 2021 
mixed 
Druga and Ko (2021) 
Druga and Ko (2021) 
Druga and Ko (2021)  
E. Marx et al.                                                                                                                                                                                                                                    

--- Page 9 ---

Computers and Education: Artificial Intelligence 5 (2023) 100169

it. Substantial differences in the use of the term can be found; for 
example, Demir and Güraksin (2022) describe the goal of their study as 
“to reveal the students’ perceptions of… AI” (p. 300). Later they state 
that “This study… Investigated… attitudes of middle school students 
towards AI and to what extent the concept of AI affects children” (p. 
300). Perception is seen here as an umbrella term for, among other 
things, attitudes (as it is in Suh & Ahn, 2022). In Van Brummelen et al. 
(2021), perceptions were mentioned alongside feelings, and were linked 
to preconceptions and mental models without elaborating. Other con-
tradictions can be found in the literature we reviewed; our goal is not to 
engage in a debate about whether terms are used correctly, but to draw 
attention to how precisely defining terms used in the context of the 
paper supports comparability across different studies. 
This applies not only to the term perception. For example, Bochniarz 
et al. (2022) named the goal of their study “to examine how adoles-
cents… currently view AI and its development and what are their atti-
tudes towards it” (p. 2). However, according to our formulated 
definition in Section 2, we understood the corresponding items in their 
survey largely as asking superficially about mental models (e.g. “Do you 
think that artificial intelligence will reach the level of human thinking?” 
(Bochniarz et al., 2022, p. 2). 
Some papers set forth mixture of closed statements about or attri-
butes of AI. These attributes were mostly related to attitudes, as well as 
mental models. For example, in the persona questionnaire used by van 
Brummelen et al. (2021), aspects of students’ mental models (“Alexa is 
____” followed by “intelligent,” “alive,” “human-like,” and “smarter than 
me”), as well as attitudes (“Alexa is ___” “friendly,” “safe,” “trustworthy”) 
are investigated (p. 307). Future research should focus on individual 
concepts and investigate them in depth. 
6.2. Findings regarding research questions 
We begin with the open research questions that the studied papers 
themselves identify. Most of the papers examined note that research 
should be extended to a broad, heterogeneous audience. For example, 
Druga and Ko (2021), Sisman et al. (2019), and Van Brummelen et al. 
(2021) all recommend their research be extended to different age groups 
and (educational) environments. This includes research on the influence 
of background variables such as interest or socioeconomic status (Mer-
tala et al., 2022), perceived ease of use (Sing et al., 2022), and adverse 
psychological factors such as anxiety toward AI (Chai et al., 2021), as 
well as an expansion of audiences to different geographic (Suh & Ahn, 
2022) or cultural (Mertala et al., 2022; Suh & Ahn, 2022) areas. In that 
sense, Sanusi and Olaleye (2022) address this demand by examining the 
influence of cultural competence on students’ conceptions and in turn 
describe the need to extend their research to qualitative methods. 
This highlights the second class of often-mentioned research ques-
tions: the enhancement and development of new survey methods and 
research instruments (Suh & Ahn, 2022). Thus, the potential of 
long-term evaluations (Ahmad et al., 2016; Conde et al., 2016) or 
semi-structured interviews (Demir & Güraksin, 2022) was noted. Suh 
and Ahn (2022) summarized this by stating, “Future studies are needed 
to 
apply 
rigorous 
quantitative 
methods 
(e.g., 
correlational, 
quasi-experimental, factor analysis) and qualitative methods (e.g., 
content and thematic analysis, action research, dialogue analysis) to 
offer a fuller picture of AI learning” (p. 10). 
In the following, we present the research approaches and gaps we 
identified. For illustration purposes, we use the model formulated in 
Section 2 and assign the papers to the corresponding sections (see 
Fig. 6). To avoid clutter, we have assigned the papers to their main focus. 
It is noticeable that the majority of the papers concentrate on influencing 
factors, especially attitudes. Besides research on attitudes, there are also 
studies on motivation, interest, or self-efficacy. In some cases, new in-
struments were developed to measure attitudes; often, effects on other 
influencing factors or learning interventions were investigated. Almost 
all studies in this area were conducted using quantitative surveys. By 
contrast, there is a substantially smaller number of papers that investi-
gate mental models. Most studies conducted in this area focus on 
investigating preconceptions of AI, meaning conceptions that have been 
collected from students without any learning interventions having taken 
place. Surveys on the progression of mental models are even more 
scarce, with only three papers addressing them. To answer the question 
raised by Staggers and Norcio (1993): In the papers we analyzed, mental 
models were mostly studied as a product. This can be explained by the 
fact that not only are appropriate elicitation methods needed to elicit 
mental model progression, but these must also be applied to learning 
intervention designed for this purpose, which are themselves only in the 
process of development (Gresse von Wangenheim et al., 2021; Marques 
et al., 2020). In summary, we found that research on attitudes has often 
been conducted to assess their moderating effects on other variables or 
Fig. 6. Categorization of the analyzed papers by research foci. The two blocks under influencing factors refer to research on attitudes (left) and learning in-
terventions (right). 
E. Marx et al.                                                                                                                                                                                                                                    

--- Page 10 ---

Computers and Education: Artificial Intelligence 5 (2023) 100169

learning interventions. Assessments were mostly surveys with 
closed-ended questions about attributes or statements. This contrasts 
with the research on mental models, which has focused on the elicitation 
of this concept. This can be explained by the model we formulated, in 
which attitudes have a moderating effect and mental models are prod-
ucts of a process (Staggers & Norcio, 1993). There were generally two 
reasons for investigating learning interventions in the context of mental 
models and attitudes. Firstly, surveys were conducted to evaluate the 
effectiveness of designed learning interventions—for example, by 
measuring differences in attitudes through pre/post-tests. The second 
reason was to examine mental model progression through the learning 
interventions. Additionally, there are works that present learning in-
terventions specifically designed from the perspective of enabling stu-
dents to construct appropriate mental models of AI. 
This leaves several open research gaps. Students’ mental models 
have been studied only sparsely to date; not only are there few studies on 
this topic, but most of them only address students’ preconceptions 
without investigating their influence on the learning process. Further-
more, there is a lack of research on how students use their constructed 
models to complete tasks and what misconceptions are revealed thereby. 
There is also a lack of research on the development of conceptual models 
or notional machines with respect to their influence both on the learning 
process and the construction of mental models. For this purpose, 
research tools to collect students’ mental models need to be developed 
and validated. The method of qualitative interviews (Gentner, 2001), 
which is traditionally used in mental model research, especially in the 
form of the teachback technique (Aliberas et al., 2021; Seel et al., 2000), 
has not been applied yet. Moreover, Suh and Ahn (2022) see the need for 
future researchers to develop a scale that measures a learner’s concept of 
AI. In addition, it is noteworthy that research on mental models is still 
very general, and previous studies have solely taken a superficial look at 
the subject area of AI; thus, the extant body of literature has focused 
almost exclusively on the topics of AI and robots. However, the range of 
AI applications and technologies requires a differentiated examination. 
Future studies should therefore examine individual phenomena in depth 
and develop research tools designed for this purpose. This includes—for 
example, researching misconceptions about specific ML technologies 
that form during learning interventions (Voulgari et al., 2021). 
Research on influencing factors shows a greater variety. Research 
instruments are already being developed to assess attitudes, and their 
interaction with other factors such as motivation or interest is also being 
investigated. Nevertheless, Bochniarz et al. (2022) stated “it is likely 
that the way people conceptualize AI may considerably affect their 
attitude towards it” (p. 4). For future research, therefore, there is an 
opportunity to clarify what influence attitudes and other factors have on 
the learning process, and how learning about AI in turn influences at-
titudes. For example, conceptual models have shown an impact on the 
construction of mental models (Seel et al., 2000) that needs to be 
explored further in the field of AI education. Moreover, according to the 
social constructivism theory we do not learn alone but in social and 
cultural environments (Sorva, 2013); teachers and parents, in particular, 
may affect the learning process through their own conceptions. How-
ever, we did not find any work that examined the influence of social 
factors on the construction of mental models; thus, this influence also 
warrants investigation (see, for instance, Druga et al., 2018). In a similar 
vein, research on learning interventions involving mental models should 
also be expanded. While evaluating learning interventions is important, 
it is equally necessary to examine the effect of learning interventions on 
the formation of mental models. 
Another finding from the results presented here is that there are some 
research disciplines whose outcomes are also relevant to CSE. For 
example, research in the area of human-robot interaction (see Ahmad 
et al., 2016; Conde et al., 2016; Korkmaz et al., 2014; Sisman et al., 
2019) can provide insights for further research into students’ concep-
tions of AI. Similarly, results from HCI research (Druga & Ko, 2021; Van 
Brummelen et al., 2021) can be relevant which is explained by the fact 
that research on the influence of conceptual models on comprehension 
originates from the field of HCI (Norman, 1983). Also, by incorporating 
psychological concepts and models into research design (Bochniarz 
et al., 2022; Chai et al., 2021; Sing et al., 2022), learning outcomes in AI 
education can be interpreted in a more nuanced way. 
Our research has shown that there is a growing body of research on 
secondary school students’ conceptions of AI. While research on stu-
dents’ mental models and attitudes are important for successful AI ed-
ucation, we also found research on other moderating variables (e. g. self- 
efficacy, motivation, and interest) although these were not present in the 
search terms. This shows the close interconnectedness of these concepts 
and the variety of perspectives from which students’ conceptions of AI 
can be studied. Overall, we found that initial groundwork has been laid 
for research on mental models of AI, but there are a number of research 
gaps that need to be explored in more detail in the future. 
7. Limitations and future research 
The present study has some limitations. Given that the topic of stu-
dents’ mental models and attitudes regarding AI is still evolving—and, 
as we have seen, there is not yet an established standard vocab-
ulary—we cannot guarantee that we have found all relevant papers. We 
also did not look at concepts such as self-efficacy or motivation. Another 
limitation is the selection of the databases searched. There were only 25 
duplicates, which suggests that we only found an isolated selection of all 
possible papers. 
As pointers for future research, we examined the posters and 
extended abstracts we found in the course of our review. The poster 
abstracts focused largely on the influence of learning interventions on 
students’ mental models and attitudes. Broll et al. (2022) developed 
interactive tools and program activities to build intuition for complex 
ML concepts. Other researchers developed AI courses designed to correct 
misconceptions about AI (Mahon et al., 2022) and to measure the 
change in high school students’ sense-making with regard to AI (Tatar 
et al., 2022). Additionally, Young and Ringenberg (2019) measured how 
their introductory unit changed students’ attitudes toward AI. Chandra 
et al. (2017) also conducted research on students’ attitudes toward ro-
bots by investigating the impact of robots’ learning ability. Lastly, 
Kreinsen and Schulz (2021) conducted interviews to survey students’ 
pre-conceptions of AI. It is expected that more work will be published on 
this topic. Future reviews are invited to extend the scope of their studies 
by incorporating other moderating variables as well as to use papers 
from other sources using other methods of data collection such as 
snowballing (Wohlin, 2014). Furthermore, the research results for one 
of the research directions identified here can be synthesized in another 
systematic literature review. 
Declaration of competing interest 
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.  
E. Marx et al.                                                                                                                                                                                                                                    

--- Page 11 ---

Computers and Education: Artificial Intelligence 5 (2023) 100169

Appendix 
10.1. Review Protocol  
Scoping Review Protocol 
Title 
Secondary School Students’ Mental Models and Attitudes Regarding Artificial Intelligence — A Scoping Review 
First reviewer 
Erik Marx 
Team of reviewers 
Erik Marx 
Thiemo Leonhardt 
Julius Edelmann (student assistent) 
Research Questions: 
RQ 1: What are the research directions on students’ mental models and attitudes regarding AI to date? 
RQ 2: What open research gaps regarding students’ mental models and attitudes regarding AI can be identified?  
Inclusion criteria 
Inclusion 
Exclusion 
Concept  
• students’ mental models and conceptions  
• students’ attitudes  
• interventions in relation to students’ mental models and 
attitudes 
•use of AI in educational settings (e. g. adaptive response systems 
or image recognition) 
Context 
•artificial intelligence and robots in general 
•technology in AI (e.g., machine learning, artificial neural 
networks) 
•AI applications (e.g., recommender systems, chatbots) 
•science or technology in general 
•technology unrelated to AI (e.g., internet) 
Population 
•secondary school students (age range of 11–18 years) 
•overlapping target groups (e.g., ages 6–12 years) were 
included 
•studies on primary or tertiary education (age range outside 11–18 
years) 
Eligibility criteria 
•Age of publication: January 2012–January 2023 
•Language: English 
•Publication status: Published 
•Types of evidence sources: Peer reviewed journals, 
conferences, and reports 
•Age of publication older than January 2012 
•Language: Not English 
•publication status: Preprints, self-published 
Search strategy 
Preliminary research 
•Exploratory research to get familiar with literature and used terms 
•Search engines used:  
o Google Scholar (https://scholar.google.de)  
o Base-Search (https://www.base-search.net) 
Data sources 
•ACM (https://dl.acm.org/) 
•IEEE (https://ieeexplore.ieee.org/Xplore/home.jsp) 
•ERIC (https://eric.ed.gov/) 
•Science Direct (https://www.sciencedirect.com/) 
Date of search 
•December 01, 2022 (ACM, IEEE, ERIC) 
•January 04, 2023 (Science Direct) 
Search terms 
ACM 
(Title: (conception? OR misconception? OR “Mental model” OR “Mental models” OR belief? OR attitude OR image OR view OR 
“notional machine” OR “notional machines” OR analog* OR perception) OR Abstract: (conception? OR misconception? OR “Mental 
model” OR “Mental models” OR belief? OR attitude OR image OR view OR “notional machine” OR “notional machines” OR analog* 
OR perception)) AND (Title: (“artificial intelligence” OR “machine learning” OR “Deep Learning” OR “Neural Network?” OR 
“Neural Networks” OR “self-learning algorithm” OR “self-learning algorithms” OR “intelligent system” OR “intelligent systems” OR 
“intelligent technology” OR “intelligent technologies” OR “agent learning” OR “intelligent agent” OR “intelligent agents” OR 
robot*) OR Abstract: (“artificial intelligence” OR “machine learning” OR “Deep Learning” OR “Neural Network?” OR “Neural 
Networks” OR “self-learning algorithm” OR “self-learning algorithms” OR “intelligent system” OR “intelligent systems” OR 
“intelligent technology” OR “intelligent technologies” OR “agent learning” OR “intelligent agent” OR “intelligent agents” OR 
robot*)) AND (Title: (student? OR pupil? OR school OR college OR university) OR Abstract: (student? OR pupil? OR school OR 
college OR university)) 
IEEE 
((“Abstract”:“conception?” OR “Abstract”:“misconception?” OR “Abstract”:“mental model?” OR “Abstract”:“belief?” OR 
“Abstract”:“attitude” OR “Abstract”:“image” OR “Abstract”:“view” OR “Abstract”:“notional machine?” OR “Abstract”:“analog*” 
OR “Abstract”:“perception”) OR (“Publication Title”:“conception?” OR “Publication Title”:“misconception?” OR “Publication 
Title”:“mental model?” OR “Publication Title”:“belief?” OR “Publication Title”:“attitude” OR “Publication Title”:“image” OR 
“Publication Title”:“view” OR “Publication Title”:“notional machine?” OR “Publication Title”:“analog*” OR “Publication 
Title”:“perception”)) AND ((“Abstract”:“artificial intelligence” OR “Abstract”:“machine learning” OR “Abstract”:“deep learning” 
OR “Abstract”:“neural network?” OR “Abstract”:“self-learning algorithm?” OR “Abstract”:“intelligent system?” OR 
“Abstract”:“intelligent technolog*” OR “Abstract”:“agent learning” OR “Abstract”:“intelligent agent?” OR “Abstract”:“robot*”) OR 
(“Publication Title”:“artificial intelligence” OR “Publication Title”:“machine learning” OR “Publication Title”:“deep learning” OR 
“Publication Title”:“neural network?” OR “Publication Title”:“self-learning algorithm?” OR Publication Title:“intelligent system?” 
OR “Publication Title”:“intelligent technolog*” OR “Publication Title”:“agent learning” OR “Publication Title”:“intelligent agent?” 
OR “Publication Title”:“robot*”)) AND ((“Abstract”:“student?” OR “Abstract”:“pupil?” OR “Abstract”:“school” OR 
“Abstract”:“college” OR “Abstract”:“university”) OR (“Publication Title”:“student?” OR “Publication Title”:“pupil?” OR 
“Publication Title”:“school” OR “Publication Title”:“college” OR “Publication Title”:“university”)) 
Publication Topics (before filtering for year of publication):  
•“Computer Science Education” (76), 
•“learning (Artificial Intelligence)” (523), 
•“teaching” (202), 
•“educational courses” (163) 
•“educational institutions“ (165) 
•“further education“ (79) 
(continued on next page) 
E. Marx et al.                                                                                                                                                                                                                                    

--- Page 12 ---

Computers and Education: Artificial Intelligence 5 (2023) 100169

(continued) 
Inclusion criteria 
Inclusion 
Exclusion 
ERIC 
((abstract:“conception” OR abstract:“misconception” OR abstract:“mental model” OR abstract:“belief” OR abstract:“attitude” OR 
abstract:“image” OR abstract:“view” OR abstract:“notional machine” OR abstract:“analogy” OR abstract:“perception”) OR 
(title:“conception” OR title:“misconception” OR title:“mental model” OR title:“belief” OR title:“attitude” OR title:“image” OR 
title:“view” OR title:“notional machine” OR title:“analogy” OR title:“perception”)) AND ((abstract:“artificial intelligence” OR 
abstract:“machine learning” OR abstract:“deep learning” OR abstract:“neural network” OR abstract:“self-learning algorithm” OR 
abstract:“intelligent system” OR abstract:“intelligent technology” OR abstract:“agent learning” OR abstract:“intelligent agent” OR 
abstract:“robot” OR abstract:“robotics”) OR (title:“artificial intelligence” OR title:“machine learning” OR title:“deep learning” OR 
title:“neural network” OR title:“self-learning algorithm” OR title:“intelligent system” OR title:“intelligent technology” OR 
title:“agent learning” OR title:“intelligent agent” OR title:“robot” OR title:“robotics”)) AND ((abstract:“student” OR 
abstract:“pupil” OR abstract:“school” OR abstract:“college” OR abstract:“university”) OR (title:“student” OR title:“pupil” OR 
title:“school” OR title:“college” OR title:“university”)) 
Science Direct 
(conceptions OR misconception OR “Mental models” OR attitudes OR preconceptions OR pre-conceptions) AND (“artificial 
intelligence” OR “machine learning”) AND students 
Number of found 
entries 
•ACM (n = 466) 
•IEEE (n = 762) 
•ERIC (n = 560) 
•SD (n = 25) 
Record selection 
•Duplicates removed (n = 13) 
•Screening based on abstract and title (removed n = 1756) 
•Full text screening (removed n = 26) 
•Records included in review (n = 18) 
Analysis 
Data charting 
Data Collected 
•Authors 
•Year of publication 
•Country of origin 
•Research goals 
•Targeted age groups and sample size (if applicable) 
•Methodology 
•Type of learning interventions (if applicable). 
•Key findings that relate to the scoping review questions  
References 
Ahmad, M. I., Mubin, O., & Orlando, J. (2016). Children views’ on social robot’s 
adaptations in education. In H. Duh, & C. Lueg (Eds.), Oz CHI ‘16: Proceedings of the 
28th Australian conference on computer-human interaction (pp. 145–149). https://doi. 
org/10.1145/3010915.3010977. Association for Computing Machinery. 
Ajzen, I. (2001). Nature and operation of attitudes. Annual Review of Psychology, 52, 
27–58. https://doi.org/10.1146/annurev.psych.52.1.27 
Aliberas, J., Guti´errez, R., & Izquierdo, M. (2021). Identifying changes in a student’s 
mental models and stimulating intrinsic motivation for learning during a dialogue 
regulated by the teachback technique: A case study. Research in Science Education, 51, 
617–645. https://doi.org/10.1007/s11165-018-9810-z 
Allport, G. W. (1935). Attitudes. In C. Murchison (Ed.), Handbook of social psychology (pp. 
798–844). Clark University Press.  
Bochniarz, K. T., Czerwi´nski, S. K., Sawicki, A., & Atroszko, P. A. (2022). Attitudes to AI 
among high school students: Understanding distrust towards humans will not help us 
understand distrust towards AI. Personality and Individual Differences, 185, Article 
111299. https://doi.org/10.1016/j.paid.2021.111299 
du Boulay, B., O’Shea, T., & Monk, J. (1981). The black box inside the glass box: 
Presenting computing concepts to novices. International Journal of Man-Machine 
Studies, 14(3), 237–249. https://doi.org/10.1016/S0020-7373(81)80056-9 
Broll, B., Grover, S., & Babb, D. (2022). Beyond black-boxing: Building intuitions of 
complex machine learning ideas through interactives and levels of abstraction. In 
J. Vahrenhold, K. Fisler, M. Hauswirth, & D. Franklin (Eds.), Icer ‘22: Proceedings of 
the 2022 ACM conference on international computing education research (Vol. 2, pp. 
21–23). Association for Computing Machinery, 10/grdctg[. 
Brynjolfsson, E., & Mitchell, T. (2017). What can machine learning do? Workforce 
implications. Science, 358(6370), 1530–1534. https://doi.org/10.1126/science. 
aap8062 
Chai, C. S., Lin, P.-Y., Jong, M. S.-Y., Dai, Y., Chiu, T. K. F., & Qin, J. (2021). Perceptions 
of and behavioral intentions towards learning artificial intelligence in primary 
school students. Educational Technology & Society, 24(3), 89–101. 
Chandra, S., Paradeda, R., Yin, H., Dillenbourg, P., Prada, R., & Paiva, A. (2017). Affect 
of robot’s competencies on children’s perception. In K. Larson, & M. WInikoff (Eds.), 
Aamas ‘17: Proceedings of the 16th conference on autonomous agents and Multi Agent 
systems (pp. 1490–1492). International Foundation for Autonomous Agents and 
Multiagent Systems.  
Chiu, T. K. F., Meng, H., Chai, C.-S., King, I., Wong, S., & Yam, Y. (2022). Creation and 
evaluation of a pretertiary artificial intelligence (AI) curriculum. IEEE Transactions 
on Education, 65(1), 30–39. https://doi.org/10.1109/TE.2021.3085878 
Conde, M.´A., Fern´andez, C., Rodríguez-Lera, F. J., Rodríguez-Sedano, F. J., Matell´an, V., 
& García-Pe˜nalvo, F. J. (2016). Analysing the attitude of students towards robots 
when lectured on programming by robotic or human teachers. In F. J. García- 
Pe˜nalvo (Ed.), Teem ‘16: Proceedings of the fourth international conference on 
technological ecosystems for enhancing multiculturality (pp. 59–65). Association for 
Computing Machinery. https://doi.org/10.1145/3012430.3012497.  
Demir, K., & Güraksin, G. E. (2022). Determining middle school students’ perceptions of 
the concept of artificial intelligence: A metaphor analysis. Participatory Educational 
Research, 9(2), 297–312. https://doi.org/10.17275/per.22.41.9.2 
Dove, G., & Fayard, A.-L. (2020). Monsters, metaphors, and machine learning. In CHI ‘20: 
Proceedings of the 2020 CHI conference on human factors in computing systems (pp. 
1–17). Association for Computing Machinery. https://doi.org/10.1145/ 
3313831.3376275.  
Druga, S., & Ko, A. J. (2021). How do children’s perceptions of machine intelligence 
change when training and coding smart programs? In M. Roussou, & S. Shahid 
(Eds.), IDC ‘21: Proceedings of the 20th annual ACM interaction design and children 
conference (pp. 49–61). Association for Computing Machinery. https://doi.org/ 
10.1145/3459990.3460712.  
Druga, S., Williams, R., Park, H. W., & Breazeal, C. (2018). How smart are the smart toys? 
Children and parents’ agent interaction and intelligence attribution. In 
M. N. Giannakos, L. Jaccheri, & M. Divitini (Eds.), IDC ‘18: Proceedings of the 17th 
ACM conference on interaction design and children (pp. 231–240). Association for 
Computing Machinery. https://doi.org/10.1145/3202185.3202741.  
Eagly, A. H., & Chaiken, S. (1993). The psychology of attitudes. Harcourt Brace 
Jovanovich.  
Elliott, A. (2019). The culture of AI: Everyday life and the digital revolution. London: 
Routledge.  
Ellis, G., Lauer, J., Silva, K., & Nina, N. (2007). Assessing high school girls’ 
preconceptions about artificial intelligence to improve learning. In 2007 annual 
conference & exposition (p. 12). American Society for Engineering Education. https:// 
doi.org/10.18260/1-2–2044, 267.1–12.267.15. 
Evangelista, I., Blesio, G., & Benatti, E. (2018). Why are we not teaching machine 
learning at high school? A proposal. In 2018 world engineering education forum - global 
engineering deans council (WEEF-GEDC) (pp. 1–6). Institute of Electrical and 
Electronics Engineers (IEEE). https://doi.org/10.1109/WEEF-GEDC.2018.8629750.  
Fincher, S., Jeuring, J., Miller, C. S., Donaldson, P., du Boulay, B., Hauswirth, M., 
Hellas, A., Hermans, F., Lewis, C., Mühling, A., Pearce, J. L., & Petersen, A. (2020). 
Notional machines in computing education: The education of attention. In 
G. R¨oßling, & B. R. Krogstie (Eds.), ITi CSE-WGR ‘20: Proceedings of the working group 
reports on innovation and technology in computer science education (pp. 21–50). https:// 
doi.org/10.1145/3437800.3439202. Association for Computing Machinery. 
Fortus, D. (2014). Attending to affect. Journal of Research in Science Teaching, 51(7), 
821–835, 10/ghgbwc. 
E. Marx et al.                                                                                                                                                                                                                                    

--- Page 13 ---

Computers and Education: Artificial Intelligence 5 (2023) 100169

Gentner, D. (2001). Mental models, psychology of. In N. J. Smelser, & P. B. Baltes (Eds.), 
International encyclopedia of the social & behavioral sciences (pp. 9683–9687). Elsevier. 
https://doi.org/10.1016/B0-08-043076-7/01487-X.  
Gentner, D., & Stevens, A. L. (Eds.). (1983). Mental models. Psychology Press. https://doi. 
org/10.4324/9781315802725.  
Greca, I. M., & Moreira, M. A. (2000). Mental models, conceptual models, and modelling. 
International Journal of Science Education, 22(1), 1–11, 10/btgzg6. 
Gresse von Wangenheim, C., Hauck, J. C. R., Pacheco, F. S., & Bertonceli Bueno, M. F. 
(2021). Visual tools for teaching machine learning in K–12: A ten-year systematic 
mapping. Education and Information Technologies, 26, 5733–5778. https://doi.org/ 
10.1007/s10639-021-10570-8 
Hazzan, O., Lapidot, T., & Ragonis, N. (2011). Guide to teaching computer science. 
Springer. https://doi.org/10.1007/978-0-85729-443-2_6 
Hidi, S., & Renninger, K. A. (2006). The four-phase model of interest development. 
Educational Psychologist, 41(2), 111–127, 10/db3dp.6. 
Johnson-Laird, P. N. (1983). Mental Models: Towards a Cognitive Science of Language, 
Inference, and Consciousness. Harvard University Press.  
Johnson-Laird, P. N. (1993). Mental models. In M. Posner (Ed.), The foundations of 
cognitive science (pp. 469–499). The MIT Press.  
Jones, N. A., Ross, H., Lynam, T., Perez, P., & Leitch, A. (2011). Mental models: An 
interdisciplinary synthesis of theory and methods. Ecology and Society, 16(1), 45–57. 
Korkmaz, O., Altun, H., Usta, E., & Ozkaya, A. (2014). The effect of activities in robotic 
applications on students’ perception on the nature of science and students’ 
metaphors related to the concept of robot. International Journal on New Trends in 
Education and Their Implications, 5(2), 44–62. 
Kreinsen, M., & Schulz, S. (2021). Students’ conceptions of artificial intelligence. In 
M. Berges, A. Mühling, & M. Armoni (Eds.), Wi PSCE ‘21: The 16th Workshop in 
Primary and secondary computing education (pp. 1–2). Association for Computing 
Machinery, 10/gqjsqq. 
Li, E., Li, S., & Yuan, X. (2022). Adoption and perception of artificial intelligence 
technologies by children and teens in education. In H. Degen, & S. Ntoa (Eds.), 
Artificial intelligence in HCI, lecture notes in computer science (pp. 69–79). Springer 
International, 10/grpcns. 
Lindner, A., Berges, M., & Lechner, M. (2021). KI im toaster? Schüler:innenvorstellungen 
zu künstlicher intelligenz [AI in the toaster? Students’ conceptions of artificial 
intelligence]. In L. Humbert (Ed.), Proceedings: INFOS 2021 – GI-Fachtagung 
Informatik und Schule (pp. 133–142). https://doi.org/10.18420/infos2021_f199 
Long, D., & Magerko, B. (2020). What is AI literacy? Competencies and design 
considerations. In CHI ‘20: Proceedings of the 2020 CHI conference on human factors in 
computing systems (pp. 1–16). Association for Computing Machinery, 10/ghbz2q. 
Mahon, J., Quille, K., Mac Namee, B., & Becker, B. A. (2022). A novel machine learning 
and artificial intelligence course for secondary school students. In L. Metkle, & 
M. Doyle (Eds.), Sigcse 2022: Proceedings of the 53rd ACM technical symposium on 
computer science education (Vol. 2, p. 1155). Association for Computing Machinery, 
10/gqgt3q. 
Maio, G., & Haddock, G. (2023). The psychology of attitudes and attitude change. SAGE 
Publications Ltd. https://doi.org/10.4135/9781446214299 
Marques, L. S., Gresse Von Wangenheim, C., & Hauck, J. C. R. (2020). Teaching machine 
learning in school: A systematic mapping of the state of the art. Informatics in 
Education, 19(2), 283–321. https://doi.org/10.15388/infedu.2020.14 
Marx, E., Leonhardt, T., & Bergner, N. (2022). Brief summary of existing research on 
students’ conceptions of AI. In M. Grillenberger, & M. Berges (Eds.), Wi PSCE ‘22: 
Proceedings of the 17th workshop in primary and secondary computing education (pp. 
1–2). Association for Computing Machinery, 10/gq2p2n. 
Maslej, N., Fattorini, L., Brynjolfsson, E., Etchemendy, J., Ligett, K., Lyons, T., 
Manyika, J., Ngo, H., Niebles, J. C., Parli, V., Shoham, Y., Wald, R., Clark, J., & 
Perrault, R. (2023). Artificial intelligence index report 2023. Institute for Human- 
Centered AI, Stanford University [PDF] https://aiindex.stanford.edu/wp-content 
/uploads/2023/04/HAI_AI-Index-Report_2023.pdf. 
Mertala, P., Fagerlund, J., & Calderon, O. (2022). Finnish 5th and 6th grade students’ 
pre-instructional conceptions of artificial intelligence (AI) and their implications for 
AI literacy education. Computers and Education: Artificial Intelligence, 3, Article 
100095. https://doi.org/10.1016/j.caeai.2022.100095 
Michaeli, T., Romeike, R., & Seegerer, S. (2022). What students can learn about artificial 
intelligence: Recommendations for K–12 computing education. In T. Saito, & 
T. Kakeshita (Eds.), Proceedings of IFIP WCCE 2022: World conference on computers in 
education. Information Processing Society of Japan.  
Nader, K., Toprac, P., Scott, S., & Baker, S. (2022). Public understanding of artificial 
intelligence through entertainment media. AI & Society.  
Nitz, S., & Fechner, S. (2018). Mentale modelle [Mental models]. In D. Krüger, 
I. Parchmann, & H. Schecker (Eds.), Theorien in der naturwissenschaftsdidaktischen 
Forschung (pp. 69–86). Springer. https://doi.org/10.1007/978-3-662-56320-5_5.  
Norman, D. A. (1983). Some observations on mental models. In D. Gentner, & 
A. L. Stevens (Eds.), Mental models (pp. 15–22). Psychology Press. https://doi.org/ 
10.4324/9781315802725-5, 15–22. 
Peters, M. D. J., Marnie, C., Tricco, A. C., Pollock, D., Munn, Z., Alexander, L., 
Mc Inerney, P., Godfrey, C. M., & Khalil, H. (2020). Updated methodological 
guidance for the conduct of scoping reviews. JBI Evidence Synthesis, 18(10), 
2119–2126. https://doi.org/10.11124/JBIES-20-00167 
Qian, Y., & Lehman, J. (2017). Students’ misconceptions and other difficulties in 
introductory programming: A literature review. ACM Transactions on Computing 
Education, 18(1), 1–24. https://doi.org/10.1145/3077618 
Rapp, D. N. (2005). Mental models: Theoretical issues for visualizations in science 
education. In J. K. Gilbert (Ed.), Visualization in science education (pp. 43–60). 
Springer Netherlands. https://doi.org/10.1007/1-4020-3613-2_4.  
Sanusi, I. T., & Olaleye, S. A. (2022). An insight into cultural competence and ethics in K- 
12 artificial intelligence education. In I. Kallel, H. M. Kammoun, & L. Hsairi (Eds.), 
Proceedings of the IEEE global engineering education conference (EDUCON 2022) (pp. 
790–794). https://doi.org/10.1109/EDUCON52537.2022.9766818 
Seel, N. M., Al-Diban, S., & Blumschein, P. (2000). Mental models and instructional 
planning. In J. M. Spector, & T. M. Anderson (Eds.), Integrated and holistic perspectives 
on learning, instruction and technology: Understanding complexity (pp. 129–158). 
Springer Netherlands. https://doi.org/10.1007/0-306-47584-7_8.  
Sing, C. C., Teo, T., Huang, F., Chiu, T. K. F., & Xing wei, W. (2022). Secondary School 
students’ intentions to learn AI: Testing Moderation effects of readiness, social good 
and optimism. Educational Technology Research & Development, 70, 765–782. https:// 
doi.org/10.1007/s11423-022-10111-1 
Sisman, B., Gunay, D., & Kucuk, S. (2019). Development and validation of an educational 
robot attitude scale (ERAS) for secondary school students. Interactive Learning 
Environments, 27(3), 377–388. https://doi.org/10.1080/10494820.2018.1474234 
Snow, R. E. (1990). New approaches to cognitive and conative assessment in education. 
International Journal of Educational Research, 14(5), 455–473. https://doi.org/ 
10.1016/0883-0355(90)90028-7 
Sorva, J. (2013). Notional machines and introductory programming education. ACM 
Transactions on Computing Education, 13(2), 1–31, 10/gfzwz9. 
Staggers, N., & Norcio, A. F. (1993). Mental models: Concepts for human-computer 
interaction research. International Journal of Man-Machine Studies, 38, 587–605. 
https://doi.org/10.1006/imms.1993.1028 
Suh, W., & Ahn, S. (2022). Development and validation of a scale measuring student 
attitudes toward artificial intelligence. Sage Open, 12(2). https://doi.org/10.1177/ 

Su, J., Zhong, Y., & Ng, D. T. K. (2022). A meta-review of literature on educational 
approaches for teaching AI at the K–12 levels in the Asia-Pacific region. Computers 
and Education: Artificial Intelligence, 3, Article 100065. https://doi.org/10.1016/j. 
caeai.2022.100065 
Taber, K. S. (2017). The nature of student conceptions in science. In K. S. Taber, & 
B. Akpan (Eds.), Science education: New directions in mathematics and science education 
(pp. 119–131). https://doi.org/10.1007/978-94-6300-749-8_9. Sense Publishers. 
Tatar, C., Culbreth, D., Jiang, S., Rose, C., Chao, J., Ellis, R., Jiang, S., & Wiedemann, K. 
(2022). High school students’ sense-making of artificial intelligence and machine 
learning. In I. Jormanainen, & A. Petersen (Eds.), Koli calling ‘22: Proceedings of the 
22nd koli calling international conference on computing education research (pp. 1–2). 
Association for Computing Machinery, 10/grdb6j. 
Tedre, M., Denning, P., & Toivonen, T. (2021a). CT 2.0. In O. Sepp¨al¨a, & A. Petersen 
(Eds.), Koli calling ‘21: Proceedings of the 21st koli calling international conference on 
computing education research (pp. 1–8). Association for Computing Machinery, 10/ 
gnqv9f. 
Tedre, M., Toivonen, T., Kahila, J., Vartiainen, H., Valtonen, T., Jormanainen, I., & 
Pears, A. (2021b). Teaching machine learning in K–12 classroom: Pedagogical and 
technological trajectories for artificial intelligence education. IEEE Access, 9, 
110558–110572, 10/gmnrt9. 
Touretzky, D. S. (2017). Computational thinking and mental models: From Kodu to 
Calypso, 2017. In F. Turbak, J. Gray, C. Kelleher, & M. Sherman (Eds.), 2017 IEEE 
blocks and beyond workshop (B&B) (pp. 71–78). https://doi.org/10.1109/ 
BLOCKS.2017.8120416. 
Touretzky, D., Gardner-Mc Cune, C., & Seehorn, D. (2022). Machine learning and the five 
big ideas in AI. International Journal of Artificial Intelligence in Education, 33, 233–266. 
https://doi.org/10.1007/s40593-022-00314-1 
Tricco, A. C., Lillie, E., Zarin, W., O’Brien, K. K., Colquhoun, H., Levac, D., Moher, D., 
Peters, M. D. J., Horsley, T., Weeks, L., Hempel, S., Akl, E. A., Chang, C., 
Mc Gowan, J., Stewart, L., Hartling, L., Aldcroft, A., Wilson, M. G., Garritty, C., & 
Straus, S. E. (2018). PRISMA extension for scoping reviews (PRISMA-Sc R): Checklist 
and explanation. Annals of Internal Medicine, 169, 467–473, 10/gfd8vk. 
Van Brummelen, J., Tabunshchyk, V., & Heng, T. (2021). “Alexa, can I program you?”: 
Student perceptions of conversational artificial intelligence before and after 
programming Alexa. In M. Roussou, & S. Shahid (Eds.), IDC ‘21: Proceedings of the 
20th annual ACM interaction design and children conference (pp. 305–313). Association 
for Computing Machinery. https://doi.org/10.1145/3459990.3460730.  
Vosniadou, S., & Brewer, W. F. (1994). Mental models of the day/night cycle. Cognitive 
Science, 18, 123–183. https://doi.org/10.1207/s15516709cog1801_4 
Voulgari, I., Zammit, M., Stouraitis, E., Liapis, A., & Yannakakis, G. (2021). Learn to 
machine learn: Designing a game based approach for teaching machine learning to 
primary and secondary education students. In M. Roussou, & S. Shahid (Eds.), IDC 
‘21: Proceedings of the 20th annual ACM interaction design and children conference (pp. 
593–598). https://doi.org/10.1145/3459990.3465176 
Wohlin, C. (2014). Guidelines for snowballing in systematic literature studies and a 
replication in software engineering. In M. Shepperd (Ed.), EASE ‘14: Proceedings of 
the 18th international conference on evaluation and assessment in software engineering 
(pp. 1–10). Association for Computing Machinery. https://doi.org/10.1145/ 
2601248.2601268.  
Young, R., & Ringenberg, J. (2019). Machine learning: An introductory unit of study for 
secondary education. In E. K. Hawthorne, & M. A. P´erez-Qui˜nones (Eds.), SIGCSE 
‘19: Proceedings of the 50th ACM technical symposium on computer science education (p. 
1274). Association for Computing Machinery, 10/grdb59. 
Zhang, B., & Dafoe, A. (2019). Artificial intelligence: American attitudes and trends. 
https://doi.org/10.2139/ssrn.3312874. 
E. Marx et al.
