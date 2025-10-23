# A framework for inclusive AI learning design for diverse learners

## Metadata
- **Author**: Yukyeong Song
- **Subject**: Computers and Education: Artificial Intelligence, 6 (2024) 100212. doi:10.1016/j.caeai.2024.100212
- **Creator**: Elsevier
- **Producer**: Acrobat Distiller 8.1.0 (Windows)
- **Creation Date**: D:20240615094315Z
- **Modification Date**: D:20240615152359Z
- **Source File**: A-framework-for-inclusive-AI-learning-des_2024_Computers-and-Education--Arti.pdf
- **Converted**: 2025-10-23 22:46:13

---

## Content

--- Page 1 ---

Computers and Education: Artificial Intelligence 6 (2024) 100212
Available online 28 February 2024
2666-920X/© 2024 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-
nc-nd/4.0/).
Contents lists available at Science Direct
Computers and Education: Artiﬁcial Intelligence
journal homepage: www.sciencedirect.com/journal/computers-and-education-artiﬁcial-intelligence
A framework for inclusive AI learning design for diverse learners
Yukyeong Song a,∗, Lauren R. Weisberg a, Shan Zhang a, Xiaoyi Tian b, Kristy Elizabeth Boyer b, 
Maya Israel a
a School of Teaching & Learning, College of Education, University of Florida, Gainesville, FL 32611, USA
b Department of Computer and Information Science and Engineering, University of Florida, Gainesville, FL 32611, USA
A R T I C L E 
I N F O
A B S T R A C T
Keywords:
K-12 AI education
AI learning design
Inclusive learning design
Universal Design for Learning (UDL)
As artiﬁcial intelligence (AI) becomes more prominent in children’s lives, an increasing number of researchers 
and practitioners have underscored the importance of integrating AI as learning content in K-12. Despite the 
recent eﬀorts in developing AI curricula and guiding frameworks in AI education, the educational opportunities 
often do not provide equally engaging and inclusive learning experiences for all learners. To promote equality 
and equity in society and increase competitiveness in the AI workforce, it is essential to broaden participation in 
AI education. However, a framework that guides teachers and learning designers in designing inclusive learning 
opportunities tailored for AI education is lacking. Universal Design for Learning (UDL) provides guidelines 
for making learning more inclusive across disciplines. Based on the principles of UDL, this paper proposes a 
framework to guide the design of inclusive AI learning. We conducted a systematic literature review to identify 
AI learning design-related frameworks and synthesized them into our proposed framework, which includes the 
core component of AI learning content (i.e., ﬁve big ideas), anchored by the three UDL principles (the “why,” 
“what,” and “how” of learning), and six praxes with pedagogical examples of AI instruction. Alongside this, we 
present an illustrative example of the application of our proposed framework in the context of a middle school 
AI summer camp. We hope this paper will guide researchers and practitioners in designing more inclusive AI 
learning experiences.
1. Introduction
Artiﬁcial intelligence (AI) was ﬁrst deﬁned in 1956 as “the science 
and engineering of making intelligent machines” (Mc Carthy, 2007). 
Ever since, many other deﬁnitions have arisen, such as the “science 
and technology of research and development of theories, methods, tech-
niques, and application systems for simulating and extending human 
intelligence” (Wang, 2019) or “a branch of Computer Science com-
bining Machine Learning, Algorithm development, Natural Language 
Processing” (Akgun & Greenhow, 2022). Recently, AI has progressively 
advanced and permeated all parts of our society, such as business, art, 
education, and medical ﬁelds, beyond the computing industry (Ng et al., 
2021a), such as the ubiquity of AI in society has created a pervasive and 
profound impact on children’s daily lives. According to the Childwise 
Monitor report, one in four children ages 5 to 16 live in households with 
a virtual assistant (Childwise, 2019). Children begin to engage with AI 
at a young age for many reasons, such as education, entertainment, and 
* Corresponding author.
E-mail addresses: y.song1@uﬂ.edu (Y. Song), lweisberg@uﬂ.edu (L.R. Weisberg), zhangshan@uﬂ.edu (S. Zhang), tianx@uﬂ.edu (X. Tian), keboyer@uﬂ.edu
(K.E. Boyer), misrael@coe.uﬂ.edu (M. Israel).
socialization. Children’s perceptions of AI have evolved towards per-
ceiving robots as sentient beings whom they can interact with, and are 
smarter than humans (Williams et al., 2019). For instance, one study 
found that children perceive a strong sense of social connection with a 
chatbot, viewing AI not only as a tool but also as a learning companion 
(Liu et al., 2022).
Despite their daily exposure to AI applications, young children are 
rarely aware of the concepts and mechanisms behind AI technology and 
potential ethical issues related to AI (Ghallab, 2019, Burgsteiner et al., 
2016). Studies suggest that early exposure to AI learning enhances self-
eﬃcacy and the willingness to persist in AI learning (Song et al., 2023) 
and prepares them for future AI-related careers (Kim et al., 2023). On 
the other hand, a lack of AI literacy may prevent children from devel-
oping as creators, designers, and producers of future AI technologies 
(Ghallab, 2019, Burgsteiner et al., 2016), and may result in misconcep-
tions or naive conceptions about AI, such as perceiving AI as a cure-all 
solution (Kim et al., 2023) or being overly fearful of AI (Cave et al., 
https://doi.org/10.1016/j.caeai.2024.100212
Received 2 November 2023; Received in revised form 19 February 2024; Accepted 20 February 2024

--- Page 2 ---

Computers and Education: Artificial Intelligence 6 (2024) 100212

Y. Song, L.R. Weisberg, S. Zhang et al.
2019). The latter misconception may prevent young people from con-
sidering AI-related careers (Bewersdorﬀ et al., 2023).
Acknowledging the importance of AI literacy, governmental and 
non-governmental educational initiatives and research centers around 
the world have begun developing curriculum guidelines for K-12 AI ed-
ucation (i.e., teaching AI as a subject matter)1 (Su et al., 2022, UNESCO, 
2022). As an early eﬀort, the AI4K12 initiative has organized its frame-
work for K-12 AI learning based on the “Five AI Big Ideas” (Touretzky et 
al., 2019). While the Five Big Ideas framework outlines the foundational 
knowledge of K-12 AI education, more guidance is needed regarding 
how to eﬀectively design and implement AI learning experiences that 
are both meaningful and inclusive (Yang, 2022, Gibellini et al., 2023).
The rapid and substantial transformation of the workforce driven by 
AI innovation (Ng et al., 2021a) underscores the importance of AI lit-
eracy as an essential competency for future citizens (Long & Magerko, 
2020). Taking into account that today’s learners are the future work-
force (Vought, 2018), making AI learning more inclusive and accessible 
at the K-12 level is an essential step for broadening participation in 
AI careers, promoting diversity (Gibellini et al., 2023), and support-
ing economic advancement in related sectors of the workforce (Vought, 
2018). This objective is supported by a growing body of research sug-
gesting that diverse groups, encompassing various genders, races, and 
cultural backgrounds (among other variables), excel in conﬂict man-
agement within organizations (Lee et al., 2018) and are more likely to 
consider a multitude of perspectives in their decision-making processes, 
thus avoiding the pitfalls of group thinking (Gaither et al., 2018). In 
light of such research, there is a pressing societal call for more atten-
tion to equity and inclusion in K-12 AI education (Vought, 2018).
Despite the call for increasing diversity in AI-related disciplines 
(Vought, 2018), a lack of guidance exists at the K-12 level for design-
ing inclusive AI learning experiences (Gibellini et al., 2023). Relevant 
to this gap in the literature, the aim of this paper is to propose a frame-
work to guide the design and implementation of inclusive AI learning 
grounded in the principles of Universal Design for Learning (UDL). UDL 
is an interdisciplinary educational framework that centers on the cre-
ation of ﬂexible and inclusive learning environments (CAST, 2018). It 
prioritizes catering to the diverse needs and abilities of all learners, 
regardless of their individual diﬀerences, thereby promoting equitable 
learning. In the context of K-12 education, UDL emphasizes the de-
velopment of curricular materials, teaching methods, and assessment 
strategies that are accessible to all students, including those with dis-
abilities and various learning preferences. While research on UDL in 
STEM contexts (e.g., computing education) has shown promise for re-
ducing barriers to participation for diverse learners (Strickland et al., 
2023, Israel, Ray, et al., 2017), scholars have yet to leverage UDL in 
support of inclusive AI learning design. Given that the application of 
the UDL principles should be carefully contextualized in speciﬁc do-
main areas (Almeqdad et al., 2023), there is a pressing need for a 
UDL-based framework speciﬁcally tailored for AI learning. To ﬁll this 
gap, we propose a novel framework by synthesizing existing AI learning 
design frameworks and integrating them with UDL to make AI learning 
design more inclusive. To maximize our framework’s practicality, we 
provide an example illustrating its application in the design of learning 
experiences within a conversational AI summer camp for middle school 
students.
2. Background
2.1. Universal Design for Learning (UDL)
UDL is a pedagogical framework that aims to make learning more 
inclusive for all students by proactively planning for the diversity in 
1 AI education is often compared with the concept of “AI in Education,” which 
is often used to refer to utilizing AI as a learning tool (e.g., recommendation 
system). This paper focuses on teaching AI as a subject matter.
today’s classrooms, including the range of backgrounds, abilities, and 
learning preferences (CAST, 2018). At its core, UDL recognizes that a 
one-size-ﬁts-all approach to education is inherently limiting, and alter-
natively promotes the proactive design of tailored educational experi-
ences (CAST, 2018). Speciﬁcally, UDL places a premium on honoring 
ﬂexibility with the goal of dismantling barriers to learning and attend-
ing to the distinct learning needs of students with disabilities (Israel et 
al., 2020, Israel, Ray, et al., 2017). UDL also focuses on accessibility 
and leverages the use of assistive technologies to support these individ-
uals’ learning needs (Basham et al., 2010). As a framework for designing 
instruction, UDL promotes adaptable activities and assessments that em-
power learners to assume control over their learning. UDL-IRN (2011)
underscores the importance of four critical elements in a UDL-based 
instructional environment: clear goals, ﬂexible methods and materials, in-
tentional planning for learner variability, and timely progress monitoring.
UDL draws its roots from architectural and product design ﬁelds. 
Alongside the passage of the Americans with Disabilities Act of 1990 
(Public Law 101-336, 1990), the “universal design” movement captured 
the attention of architects and designers aspiring to create environ-
ments and products that were accessible to individuals with disabilities. 
This wave of inclusivity extended its reach into the education realm, 
aligning with the evolution of inclusive policies intended to enhance 
instructional accessibility (Israel et al., 2023). As such, this juncture 
marked the emergence of UDL as a pivotal force in fostering equi-
table learning and addressing the diverse learning needs of all students 
(Burgstahler, 2020). UDL’s evolution is also linked with research in the 
ﬁeld of cognitive neuroscience (CAST, 2018), which has made substan-
tial advancements in unraveling the intricacies of how our brains pro-
cess information. These strides include the identiﬁcation of key neural 
networks responsible for various aspects of learning, such as attention, 
memory, and executive functioning. Notably, cognitive neuroscientists 
have elucidated the variability in individual learning proﬁles, shedding 
light on the diverse ways that learners absorb, process, and retain infor-
mation (Yuan et al., 2017).
Informed by these insights, the Center for Applied Special Technol-
ogy (CAST) developed a framework for UDL that has become promi-
nently used in educational research and practices (CAST, 2023). The 
UDL framework is rooted in the following three guiding principles, 
which align with the key brain networks responsible for learning: Mul-
tiple means of representation (recognition networks; the “what” of 
learning), engagement (aﬀective networks; the “why” of learning), and 
action and expression (strategic networks; the “how” of learning). Each 
principle plays a crucial role in fostering learning, prompting educa-
tors to provide multiple pathways for students to access information, 
engage with content, and express their knowledge and understanding. 
For instance, “multiple means of engagement” underscores the impor-
tance of providing diverse and motivating avenues for learning, focus-
ing on students’ varied interests, preferences, and backgrounds to help 
them sustain eﬀort and persistence through self-regulation when learn-
ing becomes diﬃcult. “Multiple means of representation” emphasizes 
the signiﬁcance of providing content in a variety of formats and me-
dia, making the content accessible and comprehensible for all students. 
“Multiple means of action/expression” highlights the need to oﬀer di-
verse options for students to express their knowledge, understanding, 
and skills, recognizing that learners diﬀer in their abilities, preferences, 
and limitations when it comes to demonstrating what they have learned. 
Fig. 1 shows the CAST (2018) framework in its entirety.
These three interconnected principles collectively help educators 
create a dynamic and inclusive learning environment where learners are 
empowered to engage with, comprehend, and express their knowledge 
in ways that suit their individual needs and strengths. In honoring the 
inherent variability of learners by promoting ﬂexibility, the UDL frame-
work has established a common terminology and shared understand-
ing regarding the design of inclusive instruction (Mc Mahon & Walker, 
2019). Numerous K-12 education policy initiatives in the United States 
have endorsed UDL, including the Every Student Succeeds Act (U.S. De-

--- Page 3 ---

Computers and Education: Artificial Intelligence 6 (2024) 100212

Y. Song, L.R. Weisberg, S. Zhang et al.
Fig. 1. Universal Design for Learning guidelines (CAST, 2018).
partment of Education, 2015), which requires that assessments align 
with UDL principles, the United States Higher Education Opportunity 
Act (U.S. Department of Education, 2008), which describes UDL as a 
“scientiﬁcally valid framework for guiding educational practices” (p. 
110), and the National Education Technology Plan (U.S. Department 
of Education, 2017), which recommends applying UDL to promote ac-
cessible learning with technology. UDL has also gained international 
support for research and implementation, with European countries such 
as Belgium, Norway, and Spain engaging in UDL implementation eﬀorts 
beginning in 2015, and New Zealand’s Ministry of Education following 
suit in 2018 (Mc Mahon & Walker, 2019).
2.2. UDL for inclusive AI learning design
UDL and technology have a symbiotic relationship in the literature. 
Technology has become a formidable ally in implementing UDL princi-
ples by enabling the creation of customizable and inclusive learning ex-
periences (Israel et al., 2014, Rose et al., 2010). From adaptive software 
and online resources to interactive multimedia content, technology can 
serve as a facilitator of personalized learning, a cornerstone of UDL. 
Furthermore, the ubiquity of digital devices has expanded access to 
educational opportunities and materials, helping individuals with dis-
abilities transcend physical barriers to learning. Although technology 
has been consistently harnessed to deliver UDL-enhanced instruction, 
the implementation of UDL in Science, Technology, Engineering, and 
Mathematics (STEM) education contexts has been limited. Furthermore, 
although scholars have advocated for adopting AI tools to support UDL 
implementation in the curriculum (Banes & Behnke, 2019, Bray et al., 
2023, Mc Mahon & Walker, 2019), limited attention has been paid to 
leveraging UDL to reduce barriers to participation and expand interest 
in AI-related subjects.
Our eﬀorts to design inclusive AI instruction were largely inﬂu-
enced by the literature on UDL integration in computer science (CS) 
education. UDL’s potential for increasing access and representation in 
CS at the K-12 and post-secondary levels is strongly supported by an 
emerging body of research (Hutchison & Evmenova, 2022, Lechelt et 
al., 2018, Marino et al., 2014, Wille et al., 2017). Central to these ef-
forts, Israel, Lash, et al. (2017) developed a curricular crosswalk by 
adapting CAST (2011)’s framework to provide actionable guidance for 
addressing the “what,” “why,” and “how” of making CS education more 
inclusive. Their recommendations include representing information for 
learners using multiple modalities, symbols, and languages (“what”), 
recruiting learner interest by providing choices of projects or software 
(“why”), and facilitating learner action/expression using unplugged ac-
tivities to physically represent abstract computing concepts (“how”). 
The disciplines of CS and AI education are intricately interwoven, as CS 
provides foundational framing, tools, and competencies necessary for 
developing and advancing AI technologies. However, AI education in-
volves distinct knowledge and competencies that diﬀer from traditional 
CS education (Long & Magerko, 2020). Supporting scholars’ assertions 
that the application of UDL should be carefully contextualized within 
a domain area (Almeqdad et al., 2023), we are proposing a UDL-based 
framework speciﬁcally tailored for designing inclusive AI learning ex-
periences.

--- Page 4 ---

Computers and Education: Artificial Intelligence 6 (2024) 100212

Y. Song, L.R. Weisberg, S. Zhang et al.
3. Methods
3.1. Systematic literature review for AI education frameworks
We chose to conduct a systematic literature review to ﬁnd, analyze, 
and synthesize existing literature on AI education in order to develop 
our novel framework. This decision was driven by the notion that 
there is no single dominant framework for AI learning design, whereas 
UDL’s CAST framework has become widely applied across disciplines to 
guide inclusive learning (CAST, 2018). Our review was guided by the 
Preferred Reporting Items for Systematic Reviews and Meta-Analyses 
(PRISMA) framework (Liberati et al., 2009). We conducted an ini-
tial search of research papers from the following relevant academic 
databases: Pro Quest (encompassing ERIC, Education Database), EB-
SCO (encompassing Education Source, Academic Search Premier, APA 
Psyc INFO, Teacher Reference Center), ACM Digital Library, Web of 
Science, Scopus, and IEEE Xplore. In addition, we hand-searched the 
following three journals that were recommended by two AI education 
experts serving as faculty at a Research 1 institution in the United 
States: Computers and Education, Computers and Education: Artiﬁcial 
Intelligence, and Tech Trends.
We limited the time period of publications to the past 10 years (from 
2014 to September 21, 2023) to broadly include recent educational re-
search in the ﬁeld of AI education, which began gaining researchers’ 
interest after the emergence of Google’s Alpha Go (Silver et al., 2016). 
We sought to identify peer-reviewed articles and conference proceed-
ings broadly related to AI learning frameworks in the context of K-12 
or general AI literacy for the public. Our search strategy consisted of 
the following keyword combinations: (AI OR “Artiﬁcial Intelligence”) 
AND (education OR learning OR curriculum OR teaching) AND (K-12 
OR K12 OR “AI literacy” OR “high school” OR “elementary school” OR 
child*) AND (framework OR “conceptual model”). The search string 
was reviewed and approved by the two aforementioned AI education 
experts.
We identiﬁed 521 potential articles for inclusion, which we down-
loaded and imported into the web-based software platform Covidence 
to manage the literature review process. After 157 duplicates were re-
moved, 364 abstracts were screened for relevance using the following 
inclusion criteria.
1. Articles should present frameworks for AI learning design or ap-
proaches to AI education or AI literacy.
2. Studies should focus on AI learning in K-12 contexts or general AI 
literacy education for the public.
3. AI should be seen as the learning content (i.e., teaching AI).
Records were excluded based on the following criteria.
1. Papers included neither frameworks for AI learning design nor ap-
proaches to AI education or AI literacy.
2. Studies focused on higher education contexts or specialized AI ed-
ucation for experts.
3. AI was applied as a methodology (e.g., learning analytics) or used 
as a learning tool (e.g., recommendation system) in educational 
settings, rather than being the focus of the instruction.
4. Articles were not related to education (e.g., deep learning).
5. The presented frameworks are not novel (i.e., they are borrowed 
from previous literature).2
6. Papers were written in languages other than English, with no trans-
lation provided.
7. Conference posters or keynotes.
2 In this case, we searched the original article and included that.
Fig. 2. PRISMA ﬂowchart of the search and screening process.
Through the screening process, we speciﬁcally aimed to identify 
novel frameworks for AI learning design or approaches related to AI 
education. By “frameworks,” we mean a visual representation (i.e., ﬁg-
ure) that identiﬁes key components (i.e., competencies, skills, beliefs) 
related to AI literacy or AI learning. By “approaches,” we mean prelim-
inary ideas to guide AI learning that may be valuable to include in our 
proposed framework (typically represented in the form of a table). The 
initial screening process involved a full-text scan to identify whether the 
articles included related ﬁgures or tables. To establish inter-rater relia-
bility, two researchers independently engaged in full-text scans of 20% 
of papers. Inter-rater reliability was calculated using Cohen’s Kappa, 
resulting in a coeﬃcient of 0.90, indicating almost perfect agreement 
(Sim & Wright, 2005). The remaining conﬂicts were resolved through 
discussion. One of the researchers then proceeded to screen the remain-
ing articles. Twenty records met all inclusion criteria and were assessed 
for eligibility with a full-text review conducted by both researchers. 
A snowball technique was used to include relevant articles that re-
currently appeared in references within the relevant articles (Jalali & 
Wohlin, 2012). At the conclusion of this process, ten articles were iden-
tiﬁed as relevant and were thus included in our review. Fig. 2 visualizes 
the search and screening process.
3.2. Synthesizing multiple frameworks into a new framework
To develop our framework for inclusive AI learning design, we en-
gaged in a synthesis of key components within the AI learning design 
frameworks and approaches drawn from the 10 relevant articles. Then, 
we organized these components into the “why,” “what,” and “how” 
of AI learning, in alignment with CAST (2018)’s UDL framework. The 
“why” of AI learning involves eliciting learner interest in AI, the “what” 
of AI learning encompasses the content related to building knowledge 
of AI, and the “how” of AI learning involves pedagogical strategies re-
lated to teaching AI.
4. Synthesis of literature
We identiﬁed ten articles related to AI learning through the sys-
tematic literature review. Below, we summarize each framework and 

--- Page 5 ---

Computers and Education: Artificial Intelligence 6 (2024) 100212

Y. Song, L.R. Weisberg, S. Zhang et al.
approach from our review and describe how the components informed 
our novel framework by identifying the “why,” “what,” and “how” of 
learning from each framework and approach.
The “Five Big Ideas” framework is amongst the most frequently cited 
frameworks designed to guide educators in choosing “what” AI con-
tent to teach (Touretzky et al., 2019). The Five Big Ideas of AI are 
#1. computers perceive the world using sensors, #2. agents maintain 
models/representations of the world and use them for reasoning, #3. 
computers can learn from data, #4. making agents interact comfortably 
with humans is a substantial challenge for AI developers, and #5. AI ap-
plications can impact society in both positive and negative ways. These 
ﬁve ideas serve as a core content knowledge of K-12 AI education, driv-
ing AI learning across other frameworks, such as Ng et al. (2021b), Sun 
et al. (2023) and Su et al. (2022).
Chiu (2021) proposes a holistic model for AI curriculum design for 
K-12 schools based on interviews with 24 K-12 teachers. The model 
consists of the three main “content components” of AI education (i.e., 
knowledge in AI, process in AI, and impact of AI) and “praxes” (i.e., stu-
dent relevance, teacher-student communication, and ﬂexibility), with some 
example ideas (e.g., authenticity and local understanding with a global 
perspective under the praxis of student relevance). In addition to the 
“what” of AI learning (e.g., knowledge, process, and impact of AI), this 
framework attempts to provide a holistic view of the “why” of AI learn-
ing (e.g., relevance, authenticity) and the “how” of AI learning (e.g., 
teacher-student communication, ﬂexibility).
Sanusi et al. (2022) proposes a conceptual framework of the fol-
lowing key components of AI learning: knowledge (i.e., skill, cultural), 
learning (i.e., cognitive, self-learning), and team competency (i.e., team-
work, human-tool collaboration). They also emphasize the importance 
of ethics of AI by situating it in the center of the framework. The com-
ponents of this framework can be categorized into the “why” of AI 
learning (i.e., teamwork, self-learning), the “what” of AI learning (i.e., 
skill, cultural knowledge, ethics of AI), and the “how” of AI learning (i.e., 
human-tool collaboration).
Two frameworks (Ng et al., 2021b, Sun et al., 2023) in our re-
view are rooted in the Technological Pedagogical Content Knowledge 
(TPACK) model, which highlights key competencies involved in eﬀec-
tive teaching with technology (Mishra & Koehler, 2006). In the con-
text of AI learning, “Technological Knowledge” involves understanding 
of learning artifacts, such as hardware and software, AI-related agents, 
unplugged artifacts, and gamiﬁed elements. “Pedagogical Knowledge” 
involves understanding of approaches like discovery, inquiry-based learn-
ing, collaborative learning, constructionism, project/problem-based learning, 
unplugged activities, and hands-on/playful learning. “Content Knowledge” 
involves an understanding of AI-related concepts such as AI awareness, 
use of AI ethics, AI syllabus (Russell & Norvig, 2010), and Five Big Ideas 
about AI (Touretzky et al., 2019).
Yang (2022)’s framework is potentially the most relevant to the no-
tion of inclusive AI learning. Inﬂuenced by culturally responsive teach-
ing, their framework emphasizes the “why” of AI learning by establishing 
inclusion (i.e., promoting collaborative and welcoming learning environ-
ments), developing a positive attitude (i.e., connecting AI activities with 
students’ prior knowledge and familiar culture), and enhancing mean-
ing (i.e. solving real-world problems using AI). It also addresses the 
“how” of AI learning by proposing engendering competence (i.e., pro-
viding various authentic assessments, such as artifacts, portfolios, and 
self-assessments). Built upon this work, our framework intends to pro-
vide a more holistic understanding of AI learning design encompassing 
the UDL principles and examples of AI pedagogy.
The following three articles include “approaches” to AI literacy and 
AI education with key components that are worth referring to when 
developing our framework. Yi (2021) conceptualizes AI literacy by sug-
gesting three components: functional literacy, including 3Rs (Reading, 
w Riting, and a Rithmetic); social literacy, including social practice and 
critical thinking; and technological literacy, including technological in-
timacy and designing social future. Next, Su and Zhong (2022) proposed 
an outline of AI curriculum design in the early childhood education 
context, with components like AI knowledge, AI skills, and AI attitudes.
The components under each category are related to the “what,” “how,” 
and “why” of AI learning; AI knowledge addresses of “what” of learning, 
while AI skills is related to “how” and AI attitudes is connected to “why” 
of learning. Last, Casal-Otero et al. (2023) conducted a systematic liter-
ature review of AI literacy in K-12 education and generated a taxonomy 
of approaches to K-12 AI education. Casal-Otero et al. (2023)’s taxon-
omy includes “why” (i.e., learning for life with AI), “what” (i.e., learning 
about how AI works), and “how” (i.e., learning tools for AI) of learning.
Lastly, Long and Magerko (2020) presented AI literacy competencies 
and design principles. The competencies include learners’ capability to 
answer the following essential questions: what is AI?, what can AI do?,
and how does AI work?. While the competencies address the “what” of 
AI learning, the design principles address the “why” and “how” of AI 
learning. For instance, a design principle like “embodied interactions,” 
meaning allowing learners to put themselves “in the agent’s shoes” and 
experience embodied simulations of algorithms and hands-on experi-
ments with AI technology, is closely related to the “how” of AI learning. 
Another design principle of “promote transparency,” meaning to elimi-
nate black-boxed functionality and improve documentation, also guides 
how AI should be taught.
Table 1 illuminates the synthesis process of literature on the above-
summarized AI learning-related frameworks and CAST (2018) frame-
work. We categorized the components in the alignment of the “why,” 
“what,” and “how” of learning, and the “selected components for our 
framework” in the last row of this table show the common components 
that we chose to include in our novel framework.
5. A new framework for inclusive AI learning design
Figure 3 features our novel framework for inclusive AI learning 
design. At its core lies the “AI Five Big Ideas” (i.e., Perception, Represen-
tation & Reasoning, Learning, Natural Interaction, and Societal Impact) 
(Touretzky et al., 2019), signifying their prominence as the key tenets 
of teaching AI in K-12 education. To facilitate inclusive pedagogy, the 
framework is anchored by the three UDL principles: multiple means 
of engagement (the “why” of learning), representation (the “what” of 
learning), and action & expression (the “how” of learning). Each prin-
ciple is complemented by three corresponding praxes that draw their 
inspiration from UDL’s guidelines and are visually distinguished by the 
predominant colors in CAST’s (2018) framework of green, blue, and 
purple.
The outermost layer, which features examples of each principle’s 
praxes within K-12 AI education contexts, was informed by our syn-
thesis of AI learning design frameworks (see Table 1). These examples 
may relate to multiple praxes aligned with the same UDL principle, ac-
knowledging the nuanced, multifaceted nature of AI pedagogy. For in-
stance, within the “engagement” category, project-based learning may 
be closely associated both with the “Authenticity & Relevance” and 
“Collaboration & Community” praxes, contingent upon the contextual 
approaches adopted. Notably, the dashed circle enclosing the entire 
framework represents our intention for these examples to serve as start-
ing points for AI learning design rather than conﬁnements, as the ﬁeld 
of AI continues to rapidly evolve. Below, we describe the praxes in our 
framework that align with each UDL principle.
5.1. The “engagement” praxes
The following praxes align with multiple means of engagement (the 
“why” of AI learning): “Authenticity & Relevance,” “Collaboration & 
Communication,” and “Self-regulation & Autonomy.” These praxes pro-
vide diverse motivating avenues for AI learning to leverage students’ 
varied interests, preferences, and backgrounds in order to help them 
sustain eﬀort and persistence when learning becomes diﬃcult.

--- Page 6 ---

Computers and Education: Artificial Intelligence 6 (2024) 100212

Y. Song, L.R. Weisberg, S. Zhang et al.
Table 1
Synthesis of the UDL framework and AI education frameworks.
Framework & Approaches
Why
What
How
UDL
The UDL Guidelines
(CAST, 2018)
Provide multiple means of
“Engagement”
- Recruiting interest
- Sustaining eﬀort
& Persistence
- Self-regulation
Provide multiple means of
“Representation”
- Perception
- Language & Symbols
- Comprehension
Provide multiple means of
“Action & Expression”
- Physical Action
- Expression
& Communication
- Executive Functions
AI Education
the Five Big Ideas
(AI4K12, 2020)
-
Five big ideas: perception,
representation & reasoning,
learning, natural interaction,
societal impact
-
Holistic model to
design AI curriculum
for K-12 schools
(Chiu, 2021)
Relevance;
Authenticity
Knowledge in AI;
Process in AI;
Impact of AI;
Graphical representation
Teacher-student
Communication;
Flexibility
Framework for
competencies for
AI education
(Sanusi et al., 2022)
Teamwork, Self-learning
Skill, cultural knowledge;
Ethics of AI
Human-tool collaboration
AI literacy TPACK
Framework
(Ng et al., 2021b)
Pedagogical knowledge
(e.g., inquiry-based
learning,
collaborative
learning, project/
problem-based learning)
Content knowledge
(e.g., AI awareness,
Use AI ethics,
Five big ideas about AI)
Technological knowledge
(e.g., hardware-/
software
-based artifacts, AI-related
agents, unplugged artifact,
gamiﬁed elements)
TPACK-based PD Framework
(Sun et al., 2023)
Pedagogical knowledge:
(e.g., project/problem
-based learning)
Content knowledge
(e.g., Five Big Ideas,
Application of AI,
AI ethics)
Technical knowledge
(e.g., digital software,
physical hardware
to learn AI);
Pedagogical knowledge
(e.g., game-based learning,
unplugged activities);
Technical pedagogical
knowledge
(e.g., tools for teaching AI)
The culturally responsive
approach to AI education
(Yang, 2022)
Establish inclusion
(e.g., collaborative
learning);
Develop positive attitude
(e.g., using cultural events);
Enhance meaning
(e.g., real-world issues,
design project)
-
Engender competence
(e.g., authentic
assessment, timely
feedback)
Foundation of AI literacy
(Yi, 2021)
Social literacy
(e.g., Social practice)
Functional literacy
(e.g., reading,
writing, arithmetic)
Technological literacy
(e.g., technological intimacy)
AI curriculum design in
early childhood education
(Su & Zhong, 2022)
AI attitude
(e.g., Collaborate with AI)
AI knowledge
(e.g., Deﬁnitions & examples
of AI; The Five Big Ideas of AI)
AI skills
(e.g., Using AI tools,
problem solving)
Taxonomy of approach
to AI learning in K-12
(Casal-Otero et al., 2023)
Learning for
life with AI
Learning about
how AI works
Learning
tools for AI
AI literacy competencies
and design considerations
(Long & Magerko, 2020)
-
What is AI?;
What can AI do?;
How does AI work?;
How should AI be used?
-
Contextualizing data
Graphical visualizations,
simulations, explanations,
interactive demonstrations
Embodied interactions,
Unveil gradually,
Promote transparency
Selected components 
for our framework
- Project/
problem-based learning
- Personally-relevant
project design
- Collaborative learning
- Self- and peer-evaluation
- Graphical visualizations
- Simulations
- Interactive demonstrations
- Explainability
- AI ﬁve big ideas
(learning content)
- AI unplugged activities
- Developing artifacts
using AI tools
(digitally and physically)
- Authentic assessment
- Individualized facilitation
- AI project documentation

--- Page 7 ---

Computers and Education: Artificial Intelligence 6 (2024) 100212

Y. Song, L.R. Weisberg, S. Zhang et al.
Fig. 3. New framework for inclusive AI learning design.
5.1.1. Authenticity & Relevance
Optimizing relevance and authenticity is an eﬀective way to re-
cruit learners’ interest (CAST, 2018). To best engage learners, learning 
activities should be personalized and authentic to learners’ lives. For 
example, they should be appropriate for learners’ age, race, gender, 
ability, and cultural background. For instance, utilizing A. project-based 
learning or problem-based learning (PBL) can promote authentic AI learn-
ing, especially when learners devise ways to use AI technologies to solve 
a real-world problem (Ng et al., 2021b, Sun et al., 2023). While leverag-
ing PBL, it is also important to support learners in B. personally relevant 
project design to maximize the relevance of instruction and allow learn-
ers to use their imagination to solve relevant problems in creative ways 
(CAST, 2018).
5.1.2. Collaboration & Community
Supporting collaboration and community is a recommended strat-
egy to sustain learning eﬀorts and persistence (CAST, 2018). Students 
can develop AI literacy by forming diﬀerent types of relationships with 
their peers in the classroom. For instance, constructing AI-focused learn-
ing communities and providing C. collaborative learning opportunities 
geared towards AI literacy with peers who share common interests 
could be eﬀective ways to foster engagement in AI learning.
5.1.3. Self-regulation & Autonomy
Self-regulation is one of the critical constructs to sustain learning 
and a deliberately designed level of autonomy is one of the important 
foundations for developing self-regulation. In AI education, students 
can have an opportunity to foster self-regulation and autonomy by con-
ducting D. self and peer evaluations of their learning artifacts. After the 
evaluation, learners would have time to reﬂect on their learning and set 
the next goal or adjust their goals.
5.2. The “representation” praxes
The following praxes align with multiple means of representation 
(the “what” of AI learning): “Perception,” “Language & Symbols,” and 
“Connections & Comprehension.” These praxes emphasize providing 
content related to AI literacy in a variety of formats and media, making 
it accessible and comprehensible for all students.
5.2.1. Perception
Eﬀective learning happens when the information is easily perceived. 
Because AI is a new topic for most learners, it is important to present in-
formation in diﬀerent modalities (e.g., text, sound, images) and ﬂexible 
pathways (e.g., adjusting the text size). In AI education, it is often essen-
tial to present how technology works in eﬀective and varied ways, such 
as A. graphical visualization, B. simulations, and C. interactive demonstra-
tions. For example, learning technologies, such as Teachable Machine3
can be useful in supporting learners’ perceptions of how AI works.
5.2.2. Language & Symbols
For learning to be accessible and comprehensible for all learners, 
learners’ language and cultural backgrounds must be considered. In AI 
learning contexts, there may be many essential terms or phrases that 
young learners are not familiar with in their daily lives, such as “ma-
chine learning,” or “training data.” Therefore, it is important to scaﬀold 
instruction by explaining these terms right away, before transitioning 
towards higher-level learning activities. In addition, using A. graphical 
visualization, B. simulations, and C. interactive demonstrations can also 
support learners’ understanding of AI-relevant languages and symbols.
3 https://teachablemachine .withgoogle .com/.

--- Page 8 ---

Computers and Education: Artificial Intelligence 6 (2024) 100212

Y. Song, L.R. Weisberg, S. Zhang et al.
5.2.3. Connections & Comprehension
To support learners in constructing usable knowledge, it is important 
to provide ways for them to connect with prior knowledge and guide 
their information processing. One of the barriers to AI learning and 
comprehension derives from black-box models of AI (Khosravi et al., 
2022), which prevents learners from fully understanding the underlying 
mechanism of an AI model’s decision-making. Therefore, it is important 
to prioritize the D. explainability of AI, such as visualizing the decision-
making processes of AI models within learning technologies.
5.3. The “action & expression” praxes
The following praxes align with multiple means of action and ex-
pression (the “how” of AI learning): “Physical Action,” “Expression & 
Communication,” and “Executive Function.” These praxes oﬀer diverse 
options for students to express their knowledge, understanding, and 
skills related to AI literacy.
5.3.1. Physical Action
Interactive learning activities involving dynamic physical actions 
provide more joyful learning experiences (CAST, 2018). For instance, 
in CS education, “unplugged” activities have been used to introduce CS 
concepts to novice learners using various physical actions without us-
ing computers (Bell et al., 2005). The AI education community is also 
taking advantage of this strategy by developing AI-unplugged activi-
ties (Ma et al., 2023, Long et al., 2021). A. AI unplugged activities help 
learners who do not feel comfortable with computers have easy and 
formidable access to AI education. In addition, B. developing artifacts us-
ing AI tools is another way to engage learners in physical action. When 
designing these activities and tools, it is important to make sure they are 
accessible to learners with diﬀerent physical abilities and preferences.
5.3.2. Expression & Communication
Individual learners hold strengths and weaknesses in diﬀerent 
modalities to express their knowledge and communicate (CAST, 2018). 
Thus, learners should be provided with alternative modalities for ex-
pression, especially in the context of assessment, where in progressive 
C. authentic assessment is prioritized over traditional paper-and-pencil 
tests. In AI education, authentic assessment could include the summa-
tive evaluation of students’ AI artifacts (e.g., chatbots), or formative 
approaches, such as cognitive interviews where students can express 
their knowledge and gamiﬁed assessments of AI knowledge using tools 
like Kahoot!.4
5.3.3. Executive Function
Executive function refers to the ability to set long-term goals, mon-
itor one’s own behaviors, and enact strategies to obtain goals (CAST, 
2018). In contexts where students engage in long-term AI development 
projects, well-designed scaﬀolding, and individualized facilitation are 
necessary to support the successful planning, managing resources, and 
monitoring processes. Relevant to this notion, we suggest providing 
tools for D. AI project documentation, which helps learners document 
their long-term goals, step-by-step strategies, and reﬂections during the 
AI project activities. In addition, E. individualized facilitation is essential 
to provide learners with timely feedback and scaﬀolding.
6. Illustrative example: “Camp Dialogs” learning experiences
In this section, we provide an illustrative example of how our novel 
framework can support inclusive AI learning within the context of 
an AI summer camp for middle school students called Camp Dialogs. 
Camp Dialogs aims to engage rising 7th and 8th graders in AI learn-
ing by empowering them to create personally relevant AI artifacts (i.e., 
4 https://kahoot .it/.
chatbots), which have become increasingly common in the lives of to-
day’s tech-savvy youth, using custom-designed development software 
called “AMBY (AI Made By You)” (Tian et al., 2023). The idea behind 
this instructional approach is to anchor AI learning within familiar ex-
periences for students. It has become commonplace for children and 
teens to engage with AI chatbots in everyday tasks, such as seeking 
assistance from Alexa for their homework or requesting their favorite 
tunes (Garg & Sengupta, 2020). By learning how to design this form 
of conversational AI, learners are introduced to foundational AI con-
cepts that underpin the Five Big Ideas (Touretzky et al., 2019), such as 
understanding computers’ perception of natural language, the need for 
training data sets, and AI-human interaction design (Song et al., 2023). 
Through three years of iterative design and implementation process, 
the camp experience was universally designed to increase accessibil-
ity and relevance for learners from diverse backgrounds, irrespective of 
their prior knowledge, skills, interests, or experiences. The outcomes of 
the camp, involving 32 participants, demonstrate signiﬁcant improve-
ments in learners’ ability, beliefs, willingness to share their knowledge, 
and persistence about AI learning from pre-to-post surveys (Song et al., 
2023).5 In the following sections, we describe how the camp’s learning 
activities and the software interface design utilized in this camp align 
with aspects of our proposed framework.
Fig. 4 illustrates an exemplary application of the inclusive AI learn-
ing design framework in the context of the “Camp Dialogs” program 
learning design. While the camp lessons and activities are designed 
to cover several of the AI Five Big Ideas (e.g., # 2. representation & 
reasoning, #3 learning), the main learning activities around the con-
versational app development project focus on the big idea #4. natural 
interaction (placed at the core of Fig. 4). The newly added outer circle 
with light colors represents the learning activities in Camp Dialogs that 
align with our inclusive framework.
6.1. “Engagement” (WHY)
In the Camp Dialogs program, students engage in the conversational 
app development project. This project activity promotes authenticity 
and relevance to the students by leveraging project-based learning (1.1. 
Authenticity & Relevance - A. Project-based Learning). Prior to the project 
development, learners participate in a chatbot brainstorming session 
(Fig. 5.a), where they generate ideas based on their interests. During 
the project, students engage in pair programming where students and 
the work on the same computer and switch roles between the driver
(who types) navigator (who observes and suggests) periodically during 
the task (Campe et al., 2020) (Fig. 5.b). Pair programming is a popular 
collaborative learning approach in CS education that has demonstrated 
mostly positive outcomes, such as increased project quality and en-
gagement (Bowman et al., 2020). In the context of our framework, 
pair programming fosters collaborative learning (1.2. Collaboration & 
Community - C. Collaborative Learning), enriching communication and 
knowledge sharing. Learners collaborated with peers who shared sim-
ilar interests to develop personally relevant and meaningful ideas for 
their chatbot (1.1. Authenticity & Relevance - B. Personally-relevant Project 
Design). For example, a pair of Black students developed a chatbot that 
teaches about Black history, while a pair of students who were twins 
collaborated to create a chatbot that provides facts about twins. At the 
culmination of the development process, learners engaged in self and 
peer evaluations (1.3. Self-regulation & Autonomy - D. Self and Peer Eval-
uation) of each other’s projects in small groups based on a provided 
checklist (Fig. 5.c).
5 For more information about the iterative design and evaluation of the out-
come of the summer camp, please refer to Song et al. (2023), Katuka et al. 
(2023).

--- Page 9 ---

Computers and Education: Artificial Intelligence 6 (2024) 100212

Y. Song, L.R. Weisberg, S. Zhang et al.
Fig. 4. Application of the framework to “Camp Dialogs” program.
Fig. 5. Conversational app development activities during the summer camp (Photo release has been obtained from the participants.) a) Learners brainstorm about 
chatbot ideas using sticky notes; b) Learners work collaboratively on developing a chatbot; c) A learner engages in project testing and gives peers feedback.
6.2. “Representation” (WHAT)
To provide an engaging and accessible learning experience, a tech-
nology called AMBY that supports students’ development of their chat-
bots was devised, aligns with our framework by providing a set of AMBY 
a set of sample projects that students can use as interactive demonstra-
tions (2.1. Perception - C. Interactive Demonstrations) to test and tinker 
with before they start their own projects. When the students create their 
own chatbots, they can customize the name and avatar that represent 
their agent. The main development page utilizes graphic visualization 
to represent the dialogue structure of the conversational agent (2.1. 
- Perception - A. Graphic Visualization). For example, Fig. 6 shows the 
aforementioned project created by twins called “twinnem.” In the con-
versation tree of the “development panel,” the colored boxes represent 
user intents, which are created by the developer (i.e., learner) to capture 
the intention of various user expressions (e.g., “greeting,” “asking for 
help,” “learning about facts”). Intents are colored diﬀerently (in yellow, 
purple, and green) to represent their unique properties and to ensure 
optimal visibility through emphasized color contrast (2.1. - Perception 
- A. Graphic Visualization). This design consideration not only aids in 
distinguishing between diﬀerent types of intents but also enhances the 
user experience, especially for those with visual impairments. The size 
of the conversation tree and text in the box is adjustable to support 
accessibility.
On the “chat simulations panel” (right), learners can test the agent 
instantly while editing the intents (2.2. Language & Symbols- B. Simu-
lations). In the user text entry box, there is a microphone button that 
enables voice-based interaction. By turning on the speaker, the agent’s 
utterances are presented with sounds, allowing learners to have a ver-
bal interaction with the agent (2.2. Language & Symbols). AMBY also 
oﬀers the AI model’s explainability (2.3. - Connection & Comprehension 
- C. Explainability); By clicking the “debug” button, learners can enter 

--- Page 10 ---

Computers and Education: Artificial Intelligence 6 (2024) 100212

Y. Song, L.R. Weisberg, S. Zhang et al.
Fig. 6. AMBY’s development page. Bordered boxes are annotations of the interface, light green boxes indicate the functionality of diﬀerent panels, and yellow boxes 
indicate its direct connection with our proposed framework.
Fig. 7. a) Learners engage in an Unplugged activity; b) Conversational app design log.
a debugging mode (shown in the right ﬁgure). Within this mode, they 
can examine the intent classiﬁcation results and the conﬁdence levels 
associated with each user expression generated by the AI model. Fig. 6
presents AMBY’s interface with an annotation of how each component 
is aligned with the proposed framework.
6.3. “Action & Expression” (HOW)
Camp Dialogs’ program deploys a variety of activities that encour-
age learners to express their knowledge, understanding, and skills in 
AI. First, before delving into the AI lessons, students are introduced 
to basic AI and conversational AI concepts through unplugged activ-
ities. Stemming from CS education, unplugged activities are designed 
to teach CS concepts to novice learners without using computers (i.e., 
“unplugged.”) (Bell et al., 2005). In the Camp Dialogs program, a series 
of AI-unplugged activities were devised to engage learners in diﬀer-
ent physical activities, such as playing with Lego, yoga, and acting 
(Fig. 7.a).6 These unplugged activities were designed to reﬂect the prin-
ciples of 3.1. Physical Action - B. Developing Artifacts Using AI Tools. 
In addition, as mentioned above, the main conversational app devel-
opment project activity supports 3.1. Physical Action - B. Developing 
Artifacts Using AI Tools. In addition, to support the conversational app 
development activity, AMBY oﬀers voice-to-text as an input modality to 
reduce the barrier of typing (3.1. Physical actions, 3.2. Expression & Com-
munication through multi-media). During the project’s development, a 
facilitator was assigned to each pair of students to provide individu-
6 For more information and detailed instruction of AI-unplugged activities, 
please refer to Song et al. (2024).

--- Page 11 ---

Computers and Education: Artificial Intelligence 6 (2024) 100212

Y. Song, L.R. Weisberg, S. Zhang et al.
alized feedback and optimized scaﬀolding (3.3. Executive Function - E. 
Individualized facilitation). To support their chatbot development pro-
cesses, we provided a design log that guided learners through the stages 
of Design Thinking (i.e., Empathize, Deﬁne, Ideate, Prototype, Test) 
(Thoring et al., 2011, Arık & Topçu, 2020) (Fig. 7.a). This document 
was devised based on the UDL principle of 3.3. Executive Function - D. 
AI Project Documentation. The ﬁnal learning artifact (e.g., the chatbots) 
was holistically evaluated based on a rubric (3.2. - Expression & Com-
munication - C. Authentic assessment).
7. Conclusion
In a society where AI is becoming increasingly prevalent (Ng et al., 
2021a), making AI learning more inclusive and accessible for all learn-
ers is an important step for the advancement of the AI ﬁeld and pro-
moting equity in society (Vought, 2018). Toward this goal, this paper 
proposes a novel framework for inclusive AI learning design grounded 
in recent literature on AI learning and the principles of UDL. The pro-
posed framework has “AI Five Big Ideas” at its core and emphasizes 
inclusivity by grounding itself in the three UDL principles (i.e., en-
gagement (“why”), representation (“what”), and action & expression 
(“how”). Under each of related AI pedagogy UDL principle are three 
praxes with multiple examples of AI pedagogy. In addition, this paper 
provides an illustrative example of the framework’s application in the 
context of K-12 AI education.
The proposed framework highlights the following three points of 
signiﬁcance. First, the framework is created based on the systematic re-
view of recent literature on AI education. As pressing as it is to design 
and implement AI learning experiences and curricula in K-12 education, 
there have not been many frameworks that guide learning designers and 
teachers in the design of inclusive AI instruction (Gibellini et al., 2023). 
Relevant to this gap, this paper synthesized the existing frameworks and 
approaches into one framework. Second, this framework showcases an 
example of an application of UDL in AI education. The CAST (2018)
framework guides making learning more inclusive across disciplines. 
However, for practical usage, it is important to contextualize the UDL 
principles in speciﬁc domains (Almeqdad et al., 2023). This paper is 
an attempt to support the application of the UDL in K-12 AI education. 
Lastly, this paper intends to maximize the practicality of the proposed 
framework by providing example pedagogies (i.e., the outermost layer 
of the framework in Fig. 3) and an illustrative example of AI summer 
camp design. The Camp Dialogs example illustrates the real-world ap-
plication of our framework in terms of the activity design and learning 
technology interface design.
Because AI is an emerging ﬁeld and teaching AI has recently be-
gun to be discussed in the education community, there was a relatively 
small number of articles included in our review. At this point, this 
framework serves as an entry into inclusive AI learning design that 
we expect will evolve alongside rapid changes within the ﬁeld of AI. 
As we mentioned, the outermost circle of the framework (Fig. 3) has a 
dashed line with the intention to imply that these examples are not ﬁxed 
and rather expected to be changing and evolving. Second, there could 
be some logistical hardships or burdens for the teachers to implement 
the suggested guidelines of the framework. The illustrative example in 
section 6 is situated in an informal learning setting, where learning 
designers could have more autonomy to control the learning environ-
ment. For instance, individualized facilitation could be less realistic for 
a formal classroom setting with limited resources where one teacher 
needs to lead the whole class. Third, while this framework targets K-12 
learners broadly, teachers or learning designers would need to make ad-
justments to each component and its relative importance to best serve 
their learners. For example, for younger learners who have not devel-
oped abstract thinking skills (i.e., concrete operational stage; ages 7-11, 
according to Piaget (1955)’s theory), more emphasis should be placed 
on components such as interactive demonstrations and unplugged activities. 
Following the idea of UDL, this framework does not intend to provide a 
cure-all solution to inclusive AI learning and requires users to be ﬂexible 
when applying this. Lastly, our illustrative example (section 6) provides 
only a use case with a certain situation (e.g., geographical location). 
More empirical studies are needed to utilize the proposed framework 
to design AI learning experiences (e.g., curriculum, learning technology 
interfaces) to evaluate its applicability and gain insights to improve it. 
We hope that this framework will be applicable to diverse learners in 
broad grade levels and geographical locations.
List of acronyms
AI
Artiﬁcial Intelligence
UDL
Universal Design for Learning
CAST
Center for Applied Special Technology
STEM
Science, Technology, Engineering, and Mathematics
CS
Computer Science
TPACK
Technological Pedagogical Content Knowledge
PBL
Project-Based Learning or Problem-Based Learning
Statements on open data and ethics
The data supporting the ﬁndings of this paper are available from the 
corresponding author upon reasonable request. Regarding the example 
case presented in the paper, the study was approved by the [Author’s in-
stitute’s] Institutional Review Board (IRB202100031, IRB202300786). 
No personal identiﬁers were reported in this paper.
CRedi T authorship contribution statement
Yukyeong Song: Writing – review & editing, Writing – original 
draft, Visualization, Project administration, Methodology, Data cura-
tion, Conceptualization. Lauren R. Weisberg: Writing – review & 
editing, Writing – original draft, Visualization, Methodology, Concep-
tualization. Shan Zhang: Methodology, Data curation. Xiaoyi Tian:
Writing – original draft. Kristy Elizabeth Boyer: Writing – review & 
editing, Supervision. Maya Israel: Writing – review & editing, Supervi-
sion, Conceptualization.
Declaration of competing interest
The authors declare that they have no known competing ﬁnancial 
interests or personal relationships that could have appeared to inﬂuence 
the work reported in this paper.
References
AI4K12. https://ai4k12 .org/.
Akgun, S., & Greenhow, C. (2022). Artiﬁcial intelligence in education: Addressing ethical 
challenges in k-12 settings. AI and Ethics, 2, 431–440.
Almeqdad, Q. I., Alodat, A. M., Alquraan, M. F., Mohaidat, M. A., & Al-Makhzoomy, A. K. 
(2023). The eﬀectiveness of universal design for learning: A systematic review of the 
literature and meta-analysis. Cogent Education, 10, Article 2218191.
Arık, M., & Topçu, M. S. (2020). Implementation of engineering design process in the 
k-12 science classrooms: Trends and issues. Research in Science Education, 21–43.
Banes, D., & Behnke, K. (2019). The potential evolution of universal design for learning 
(udl) through the lens of technology innovation. In Universal access through inclusive 
instructional design (pp. 323–331).
Basham, J. D., Israel, M., Graden, J., Poth, R., & Winston, M. (2010). A comprehensive 
approach to rti: Embedding universal design for learning and technology. Learning 
Disability Quarterly, 33, 243–255.
Bell, T., Witten, I. H., Fellows, M., Adams, R., & Mc Kenzie, J. (2005). Computer science 
unplugged: An enrichment and extension programme for primary-aged children.
Bewersdorﬀ, A., Zhai, X., Roberts, J., & Nerdel, C. (2023). Myths, mis- and preconceptions 
of artiﬁcial intelligence: A review of the literature. Computers and Education: Artiﬁcial 
Intelligence, Article 100143.
Bowman, N. A., Jarratt, L., Culver, K., & Segre, A. M. (2020). Pair programming in per-
spective: Eﬀects on persistence, achievement, and equity in computer science. Journal 
of Research on Educational Eﬀectiveness, 13, 731–758.
Bray, A., Devitt, A., Banks, J., Sanchez Fuentes, S., Sandoval, M., Riviou, K., Byrne, D., 
Flood, M., Reale, J., & Terrenzio, S. (2023). What next for universal design for learn-
ing? A systematic literature review of technology in udl implementations at second 
level. British Journal of Educational Technology.

--- Page 12 ---

Computers and Education: Artificial Intelligence 6 (2024) 100212

Y. Song, L.R. Weisberg, S. Zhang et al.
Burgstahler, S. (2020). Equal access: Universal design of instruction. https://
www .washington .edu /doit /equal -access -universal -design -instruction. (Accessed 29 
September 2023).
Burgsteiner, H., Kandlhofer, M., & Steinbauer, G. (2016). Irobot: Teaching the basics of 
artiﬁcial intelligence in high schools. In Proceedings of the AAAI conference on artiﬁcial 
intelligence.
Campe, S., Denner, J., Green, E., & Torres, D. (2020). Pair programming in middle school: 
Variations in interactions and behaviors. Computer Science Education, 30, 22–46.
Casal-Otero, L., Catala, A., Fernández-Morante, C., Taboada, M., Cebreiro, B., & Barro, 
S. (2023). Ai literacy in k-12: A systematic literature review. International Journal of 
STEM Education, 10, 29.
CAST (2011). Universal design for learning guidelines version 2.0. Wakeﬁeld, MA: CAST.
CAST (2018). Udl & the learning brain. https://www .cast .org /products -services /
resources /2018 /udl -learning -brain -neuroscience. (Accessed 29 September 2023).
CAST (2023). Udl in public policy. https://www .cast .org /impact /udl -public -policy. (Ac-
cessed 29 September 2023).
Cave, S., Coughlan, K., & Dihal, K. (2019). “scary robots” examining public responses 
to ai. In Proceedings of the 2019 AAAI/ACM conference on AI, ethics, and society
(pp. 331–337).
Childwise (2019). Monitor report: A comprehensive annual report focused on children and 
young people’s media consumption, purchasing habits, attitudes and activities.
Chiu, T. K. (2021). A holistic approach to the design of artiﬁcial intelligence (ai) education 
for k-12 schools. Tech Trends, 65, 796–807.
Gaither, S. E., Apfelbaum, E. P., Birnbaum, H. J., Babbitt, L. G., & Sommers, S. R. (2018). 
Mere membership in racially diverse groups reduces conformity. Social Psychological 
and Personality Science, 9, 402–410.
Garg, R., & Sengupta, S. (2020). Conversational technologies for in-home learning: Using 
co-design to understand children’s and parents’ perspectives. In Proceedings of the 
2020 CHI conference on human factors in computing systems (pp. 1–13).
Ghallab, M. (2019). Responsible ai: Requirements and challenges. AI Perspectives, 1, 1–7.
Gibellini, G., Fabretti, V., & Schiavo, G. (2023). Ai education from the educator’s per-
spective: Best practices for an inclusive ai curriculum for middle school. In Extended 
abstracts of the 2023 CHI conference on human factors in computing systems (pp. 1–6).
Hutchison, A., & Evmenova, A. S. (2022). Planning computer science instruction for stu-
dents with high-incidence disabilities. Intervention in School and Clinic, 57, 262–267.
Israel, M., Lash, T., & Ray, M. (2017). Universal design for learning within computer science 
education. Creative Technology Research Lab, University of Florida.
Israel, M., Ray, M., & Lash, T. (2017). Universal design for learning guidelines + computer 
science computational thinking. https://ctrl .education .uﬂ .edu /wp -content /uploads /
sites /5 /2020 /05 /Copy -of -UDL -and -CS _CT -remix .pdf.
Israel, M., Ribuﬀo, C., & Smith, S. (2014). Universal design for learning: Recommen-
dations for teacher preparation and professional development. Document No. IC-
7 CEEDAR Centre. Available online: http://ceedar .education .uﬂ .edu /wp -content /
uploads /2014 /08 /IC -7 _FINAL _08 -27 -14 .pdf. (Accessed 22 March 2018).
Israel, M., Jeong, G., Ray, M., & Lash, T. (2020). Teaching elementary computer science 
through universal design for learning. In Proceedings of the 51st ACM technical sympo-
sium on computer science education (pp. 1220–1226).
Israel, M., Chandler, L., Cobo, A., & Weisberg, L. (2023). Increasing access, participation 
and inclusion within k–12 cs education through universal design for learning and high 
leverage practices. Computer Science Education: Perspectives on Teaching and Learning 
in School, 115.
Jalali, S., & Wohlin, C. (2012). Systematic literature studies: Database searches vs. back-
ward snowballing. In Proceedings of the ACM-IEEE international symposium on empirical 
software engineering and measurement (pp. 29–38).
Katuka, G. A., Auguste, Y., Song, Y., Tian, X., Kumar, A., Celepkolu, M., Boyer, K. E., Bar-
ret, J., Israel, M., & Mc Klin, T. (2023). A summer camp experience to engage middle 
school learners in AI through conversational app development. In Proceedings of the 
54th ACM Technical Symposium on Computer Science Education V. 1 (pp. 813–819).
Khosravi, H., Shum, S. B., Chen, G., Conati, C., Tsai, Y. S., Kay, J., Knight, S., Martinez-
Maldonado, R., Sadiq, S., & Gaševi´c, D. (2022). Explainable artiﬁcial intelligence in 
education. Computers and Education: Artiﬁcial Intelligence, 3, Article 100074.
Kim, K., Kwon, K., Ottenbreit-Leftwich, A., Bae, H., & Glazewski, K. (2023). Exploring 
middle school students’ common naive conceptions of artiﬁcial intelligence concepts, 
and the evolution of these ideas. Education and Information Technologies, 1–28.
Lechelt, Z., Rogers, Y., Yuill, N., Nagl, L., Ragone, G., & Marquardt, N. (2018). Inclusive 
computing in special needs classrooms: Designing for all. In Proceedings of the 2018 
CHI conference on human factors in computing systems (pp. 1–12).
Lee, H. W., Choi, J. N., & Kim, S. (2018). Does gender diversity help teams construc-
tively manage status conﬂict? An evolutionary perspective of status conﬂict, team 
psychological safety, and team creativity. Organizational Behavior and Human Decision 
Processes, 144, 187–199.
Liberati, A., Altman, D. G., Tetzlaﬀ, J., Mulrow, C., Gøtzsche, P. C., Ioannidis, J. P., Clarke, 
M., Devereaux, P. J., Kleijnen, J., & Moher, D. (2009). The prisma statement for 
reporting systematic reviews and meta-analyses of studies that evaluate health care 
interventions: Explanation and elaboration. Annals of Internal Medicine, 151, 65–94.
Liu, C. C., Liao, M. G., Chang, C. H., & Lin, H. M. (2022). An analysis of children’ inter-
action with an ai chatbot and its impact on their interest in reading. Computers and 
Education, 189, Article 104576.
Long, D., & Magerko, B. (2020). What is ai literacy? Competencies and design considera-
tions. In Proceedings of the 2020 CHI conference on human factors in computing systems
(pp. 1–16).
Long, D., Moon, J., & Magerko, B. (2021). Unplugged assignments for k-12 ai education. 
AI Matters, 7, 10–12.
Ma, R., Sanusi, I. T., Mahipal, V., Gonzales, J. E., & Martin, F. G. (2023). Developing 
machine learning algorithm literacy with novel plugged and unplugged approaches.
In Proceedings of the 54th ACM technical symposium on computer science education: Vol. 1
(pp. 298–304).
Marino, M. T., Gotch, C. M., Israel, M., Vasquez III, E., Basham, J. D., & Becht, K. (2014). 
Udl in the middle school science classroom: Can video games and alternative text 
heighten engagement and learning for students with learning disabilities? Learning 
Disability Quarterly, 37, 87–99.
Mc Carthy, J. (2007). From here to human-level ai. Artiﬁcial Intelligence, 171, 1174–1182.
Mc Mahon, D. D., & Walker, Z. (2019). Leveraging emerging technology to design an 
inclusive future with universal design for learning. CEPS Journal, 9, 75–93.
Mishra, P., & Koehler, M. J. (2006). Technological pedagogical content knowledge: A 
framework for teacher knowledge. Teachers College Record, 108, 1017–1054.
Ng, D. T. K., Leung, J. K. L., Chu, K. W. S., & Qiao, M. S. (2021a). Ai literacy: Deﬁnition, 
teaching, evaluation and ethical issues. Proceedings of the Association for Information 
Science and Technology, 58, 504–509.
Ng, D. T. K., Leung, J. K. L., Chu, S. K. W., & Qiao, M. S. (2021b). Conceptualizing 
ai literacy: An exploratory review. Computers and Education: Artiﬁcial Intelligence, 2, 
Article 100041.
Piaget, J. (1955). The child’s construction of reality. London: Routledge & Kegan Paul.
Public Law 101-336 (1990). Americans with disabilities act of 1990. https://www .
govinfo .gov /app /details /STATUTE -104 /STATUTE -104 -Pg327. (Accessed 29 Septem-
ber 2023).
Rose, D., Gravel, J., & Domings, Y. (2010). Udl unplugged: The role of technology 
in udl. https://www .cast .org /products -services /resources /2012 /udl -unplugged -role -
technology. (Accessed 29 September 2023).
Russell, S. J., & Norvig, P. (2010). Artiﬁcial intelligence a modern approach. London: Pren-
tice Hall.
Sanusi, I. T., Olaleye, S. A., Agbo, F. J., & Chiu, T. K. (2022). The role of learners’ 
competencies in artiﬁcial intelligence education. Computers and Education: Artiﬁcial 
Intelligence, 3, Article 100098.
Silver, D., Huang, A., Maddison, C. J., Guez, A., Sifre, L., Van Den Driessche, G., Schrit-
twieser, J., Antonoglou, I., Panneershelvam, V., Lanctot, M., et al. (2016). Mastering 
the game of go with deep neural networks and tree search. Nature, 529, 484–489.
Sim, J., & Wright, C. C. (2005). The kappa statistic in reliability studies: Use, interpreta-
tion, and sample size requirements. Physical Therapy, 85, 257–268.
Song, Y., Katuka, G. A., Barrett, J., Tian, X., Kumar, A., Mc Klin, T., Celepkolu, M., Boyer, 
K. E., & Israel, M. (2023). Ai made by youth: A conversational ai curriculum for 
middle school summer camps. In Proceedings of the thirty-seventh AAAI conference on 
artiﬁcial intelligence and thirty-ﬁfth innovative applications of artiﬁcial intelligence con-
ference and thirteenth AAAI symposium on educational advances in artiﬁcial intelligence: 
Vol. 37 (pp. 15851–15859).
Song, Y., Tian, X., Regatti, N., Katuka, G. A., Boyer, K. E., & Israel, M. (2024). Artiﬁcial 
intelligence unplugged: Designing unplugged activities for a conversational ai sum-
mer camp. In Proceedings of the 55th ACM technical symposium on computer science 
education.
Strickland, C., Ramírez-Salgado, A., Weisberg, L., Chandler, L., Di Domenico, J., Lehman, 
E. M., & Israel, M. (2023). Designing an equity-centered framework and crosswalk for 
integrated elementary computer science curriculum and instruction.
Su, J., & Zhong, Y. (2022). Artiﬁcial intelligence (ai) in early childhood education: Cur-
riculum design and future directions. Computers and Education: Artiﬁcial Intelligence, 
3, Article 100072.
Su, J., Zhong, Y., & Ng, D. T. K. (2022). A meta-review of literature on educational ap-
proaches for teaching ai at the k-12 levels in the Asia-Paciﬁc region. Computers and 
Education: Artiﬁcial Intelligence, 3, Article 100065.
Sun, J., Ma, H., Zeng, Y., Han, D., & Jin, Y. (2023). Promoting the ai teaching competency 
of k-12 computer science teachers: A tpack-based professional development approach. 
Education and Information Technologies, 28, 1509–1533.
Tian, X., Kumar, A., Solomon, C. E., Calder, K. D., Katuka, G. A., Song, Y., Celepkolu, 
M., Pezzullo, L., Barret, J., Boyer, K. E., et al. (2023). AMBY: A development environ-
ment for youth to create conversational agents. International Journal of Child-Computer 
Interaction, 38, Article 100618.
Thoring, K., Müller, R. M., et al. (2011). Understanding design thinking: A process model 
based on method engineering. In DS 69: Proceedings of e&PDE 2011, the 13th interna-
tional conference on engineering and product design education (pp. 493–498).
Touretzky, D., Gardner-Mc Cune, C., Martin, F., & Seehorn, D. (2019). Envisioning ai for 
k-12: What should every child know about ai? In Proceedings of the AAAI conference 
on artiﬁcial intelligence (pp. 9795–9799).
U.S. Department of Education (2008). Higher education opportunity act. https://www2 .
ed .gov /policy /highered /leg /hea08 /index .html. (Accessed 29 September 2023).
U.S. Department of Education (2015). Every student succeeds act (essa). https://www .ed .
gov /essa ?src =rn. (Accessed 29 September 2023).
U.S. Department of Education (2017). Reimagining the role of technology in education. 
https://tech .ed .gov /netp/. (Accessed 29 September 2023).
UDL-IRN (2011). Critical elements of udl in instruction (version 1.2). http://mits .cenmi .
org/.
UNESCO (2022). A mapping of government-endorsed ai curricula 2022. https://
gcedclearinghouse .org /resources /k -12 -ai -curricula -mapping -government -endorsed -
ai -curricula.

--- Page 13 ---

Computers and Education: Artificial Intelligence 6 (2024) 100212

Y. Song, L.R. Weisberg, S. Zhang et al.
Vought, R. T. (2018). Charting a course for success: America’s strategy for stem education.
Wang, P. (2019). On deﬁning artiﬁcial intelligence. Journal of Artiﬁcial General Intelligence, 
10, 1–37.
Wille, S., Century, J., & Pike, M. (2017). Exploratory research to expand opportunities 
in computer science for students with learning diﬀerences. Computing in Science & 
Engineering, 19, 40–50.
Williams, R., Park, H. W., & Breazeal, C. (2019). A is for artiﬁcial intelligence: The impact 
of artiﬁcial intelligence activities on young children’s perceptions of robots. In Pro-
ceedings of the 2019 CHI conference on human factors in computing systems (pp. 1–11).
Yang, W. (2022). Artiﬁcial intelligence education for young children: Why, what, and 
how in curriculum design and implementation. Computers and Education: Artiﬁcial 
Intelligence, 3, Article 100061.
Yi, Y. (2021). Establishing the concept of ai literacy. Jahr–European Journal of Bioethics, 
12, 353–368.
Yuan, H., Rippetoe, J., Ding, L., Kang, Z., Shehab, R. L., & West, S. G. (2017). 
Universal design for learning in the framework of neuroscience-based education 
and neuroimaging-based assessment. In 2017 2nd international conference on bio-
engineering for smart technologies (Bio SMART) (pp. 1–4). IEEE.
