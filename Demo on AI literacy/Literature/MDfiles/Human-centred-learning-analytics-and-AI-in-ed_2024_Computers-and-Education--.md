# Human-centred learning analytics and AI in education: A systematic literature review

## Metadata
- **Author**: Riordan Alfredo
- **Subject**: Computers and Education: Artificial Intelligence, 6 (2024) 100215. doi:10.1016/j.caeai.2024.100215
- **Creator**: Elsevier
- **Producer**: Acrobat Distiller 8.1.0 (Windows)
- **Creation Date**: D:20240615072722Z
- **Modification Date**: D:20240615150226Z
- **Source File**: Human-centred-learning-analytics-and-AI-in-ed_2024_Computers-and-Education--.pdf
- **Converted**: 2025-10-23 22:46:10

---

## Content

--- Page 1 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215
Available online 13 March 2024
2666-920X/© 2024 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY-NC license (http://creativecommons.org/licenses/by-
nc/4.0/).
Contents lists available at Science Direct
Computers and Education: Artiﬁcial Intelligence
journal homepage: www.sciencedirect.com/journal/computers-and-education-artiﬁcial-intelligence
Human-centred learning analytics and AI in education: A systematic 
literature review
Riordan Alfredo a,∗, Vanessa Echeverria a,b, Yueqiao Jin a, Lixiang Yan a, Zachari Swiecki a, 
Dragan Gaševi´c a, Roberto Martinez-Maldonado a
a Centre for Learning Analytics Monash (Co LAM), Monash University, Clayton, 3800, Victoria, Australia
b Escuela Superior Politécnica del Litoral, 30.5 Via Perimetral, Guayaquil, Ecuador
A R T I C L E 
I N F O
A B S T R A C T
Keywords:
Human-centered AI
Human-centered learning analytics
AI in education
Stakeholders involvement
Education technology
Ethical considerations
The rapid expansion of Learning Analytics (LA) and Artiﬁcial Intelligence in Education (AIED) oﬀers new 
scalable, data-intensive systems but raises concerns about data privacy and agency. Excluding stakeholders—
like students and teachers—from the design process can potentially lead to mistrust and inadequately aligned 
tools. Despite a shift towards human-centred design in recent LA and AIED research, there remain gaps in our 
understanding of the importance of human control, safety, reliability, and trustworthiness in the design and 
implementation of these systems. We conducted a systematic literature review to explore these concerns and 
gaps. We analysed 108 papers to provide insights about i) the current state of human-centred LA/AIED research; 
ii) the extent to which educational stakeholders have contributed to the design process of human-centred 
LA/AIED systems; iii) the current balance between human control and computer automation of such systems; 
and iv) the extent to which safety, reliability and trustworthiness have been considered in the literature. Results 
indicate some consideration of human control in LA/AIED system design, but limited end-user involvement 
in actual design. Based on these ﬁndings, we recommend: 1) carefully balancing stakeholders’ involvement in 
designing and deploying LA/AIED systems throughout all design phases 2) actively involving target end-users, 
especially students, to delineate the balance between human control and automation, and 3) exploring safety, 
reliability, and trustworthiness as principles in future human-centred LA/AIED systems.
1. Introduction
Artiﬁcial Intelligence (AI) advancements are rapidly changing how 
we carry out our daily activities (Chakraborty et al., 2022). In educa-
tional contexts, AI and LA innovations are prompting a signiﬁcant trans-
formation by both enabling innovative teaching and learning strategies 
(Markauskaite et al., 2022) and, at the same time, challenging current 
assessment practices (Swiecki et al., 2022). Emerging Learning Analyt-
ics and AI in education (LA/AIED) systems oﬀer novel data-intensive 
solutions that promise to enable adaptive and personalised teaching 
and learning experiences at scale (Buckingham Shum & Luckin, 2019). 
For instance, various intelligent tutoring systems and LA solutions pro-
vide personalised learning support and automated feedback (e.g. Maier 
& Klotz, 2022, Cavalcanti et al., 2021). LA dashboards are providing 
educators with new means to track student progress and oﬀer tar-
geted support, potentially leading to improved student outcomes (e.g. 
* Corresponding author.
E-mail address: riordan.alfredo@monash.edu (R. Alfredo).
Williamson & Kizilcec, 2022, Fernandez Nieto et al., 2022). LA/AIED 
systems, paired with novel interaction innovations, such as gamiﬁca-
tion and mixed reality (e.g. Carter & Egliston, 2023), are also enabling 
new pedagogical strategies that can potentially make learning more 
engaging and interactive for students. In sum, educational providers 
are increasingly adopting LA/AIED systems because data-intensive tech-
nologies hold the promise of making learning more accessible, scalable, 
eﬀective, and personalised for students (Macfadyen, 2022) by provid-
ing various forms of teacher-facing and student-facing user interfaces 
(Mavrikis & Cukurova, 2021, Buckingham Shum & Luckin, 2019).
Yet, the proliferation of LA/AIED systems raises key concerns about 
the privacy of students and security of educational data (Viberg et 
al., 2022), as well as the potential for algorithms to perpetuate bi-
ases and discrimination (Uttamchandani & Quick, 2022). The lack of 
involvement of students and teachers in the design and development of 
LA/AIED systems can potentially lead to a lack of understanding and 
https://doi.org/10.1016/j.caeai.2024.100215
Received 20 December 2023; Received in revised form 2 March 2024; Accepted 7 March 2024

--- Page 2 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
trust in the technology (Shibani et al., 2022, Dollinger et al., 2019, 
Sarmiento & Wise, 2022, Alzahrani et al., 2023). This lack of involve-
ment also raises questions about the accountability and transparency 
of AI in education (Tsai et al., 2020). Furthermore, increased student 
adoption of generative AI systems may recurrently challenge existing 
assessment practices and blur the lines of academic integrity (Moya et 
al., 2023). It is thus essential to address these concerns and incorporate 
the perspectives and authentic needs of students and teachers in design-
ing and implementing LA/AIED systems. This can potentially contribute 
to creating ethical, eﬀective, and inclusive ways to adopt LA/AIED sys-
tems (Williamson & Kizilcec, 2021, 2022).
In response to the above challenges, there has been a growing inter-
est in adopting human-centred design (HCD) approaches that prioritise 
human needs, values, and perspectives in the design and deployment of 
LA/AIED systems (Lang & Davis, 2023, Viberg et al., 2023, Luckin et al., 
2006, Buckingham Shum et al., 2019). Beyond education, there is also 
a growing interest in applying similar human-centred principles in the 
emerging discipline of Human-Centred AI (HCAI). An HCAI approach 
views AI as systems aimed at serving human interests rather than as 
a means of achieving technical goals or replacing humans (Shneider-
man, 2022, Usmani et al., 2023). Thus, the design of HCAI systems is to 
be guided by a set of ethical principles and design guidelines that em-
power end-users. The aim is to ensure that technologies providing high 
automation capabilities are created in ways that guarantee their trust-
worthiness, transparency, and beneﬁt to society (Usmani et al., 2023, 
Shneiderman, 2020a, Ozmen Garibay et al., 2023).
In recent years, the concept of HCAI has gained signiﬁcant attention 
in LA/AIED with a growing recognition of the importance of consid-
ering educational stakeholders’ needs and perspectives in the design 
and deployment of data-intensive innovations (Buckingham Shum et 
al., 2019, Yang et al., 2021, Sarmiento & Wise, 2022, Holmes et al., 
2022, Kloos et al., 2022). This includes, for example, the use of partici-
patory design and co-design methods to involve teachers (e.g. Ahn et al., 
2021, Holstein et al., 2019), students (e.g. Prieto-Alvarez et al., 2018, 
Sarmiento et al., 2020), and other educational stakeholders (such as 
educational decision-makers, learning designers, IT developers and edu-
cational researchers) (e.g. Prieto et al., 2019, Schmitz et al., 2022) in the 
co-creation of LA/AIED systems, the development of ethical frameworks 
particularly tailored to LA/AIED (e.g. Dollinger et al., 2019, Holmes et 
al., 2022, Brossi et al., 2022), the exploration of new methods for incor-
porating teachers perspectives and experiences into machine learning 
algorithms and end-user LA interface designs (Luckin et al., 2006, Wise 
et al., 2021), and ways to open the AI algorithmic “black box” to pro-
vide insight to teachers and students into the analytics or communicate 
analysis outputs to them in ways they can easily understand (Khosravi 
et al., 2022).
Given the rapidly growing interest in applying human-centred de-
sign principles in LA/AIED research and practice, a timely systematic 
literature review (SLR) in this area oﬀers a crucial opportunity to syn-
thesise and evaluate the existing body of research. This can inform the 
direction of future research and ensure that new work is building upon 
the foundations established by previous studies. The closest work to 
ours was presented by Sarmiento and Wise (2022), who conducted an 
initial, non-systematic review of the literature in participatory and co-
design of LA. The authors surveyed the design systems and techniques 
used in the participatory design of learning analytics. To the best of our 
knowledge, no previous research has conducted comprehensive and sys-
tematic review of the body of work focused on applying human-centred 
design and HCAI principles in LA/AIED literature.
This paper presents an SLR that goes beyond previous works and 
aims to address the knowledge gap about the state of the art of human-
centredness in LA/AIED systems. We used the HCAI framework (Shnei-
derman, 2022) as a lens to motivate and structure our review. This 
framework helped us to focus on key themes of HCD, balance human 
control and computer automation, safety, reliability, and trustworthi-
ness, and to identify relevant studies that address these themes in the 
context of stakeholder involvement in LA/AIED. The ﬁndings of this SLR 
contribute insights into gaps in the existing research, highlighting areas 
where further investigation is needed and methodological challenges 
that need to be addressed for human-centred LA/AIED data-intensive 
systems to remain relevant and potentially become part of the main-
stream practices in the foreseeable future.
2. Background
2.1. Foundations of human-centred AI and learning analytics in education
While AI and analytics technologies exhibit potential for augmenting 
human decision-making, concerns over transparency, accountability, 
algorithmic bias, discrimination, and potential threats to human auton-
omy and agency can mitigate their beneﬁts (van Berkel et al., 2022). 
Consequently, governments – such as the G20 members (Jelinek et al., 
2021) – and large tech companies (e.g., see review by Jobin et al., 
2019) have proposed guidelines for AI application design centred on 
human values (e.g., safety, reliability, and trustworthiness). In this con-
text, HCAI is emerging as a new research discipline that can be broadly 
deﬁned as an approach to creating “software designs that give users high 
levels of understanding and control over their AI-enabled systems to pre-
serve human agency” (Shneiderman, 2021, p.56). HCAI has its roots in 
ﬁelds such as human-computer interaction, HCD, and human factors 
engineering (Chignell et al., 2022), which focus on understanding and 
incorporating human perspectives and experiences into technology de-
sign (Grudin, 2009). HCAI aims to extend human-computer interaction 
and HCD principles to address unique issues and unforeseen impacts of 
AI autonomy (Xu et al., 2023).
Echoing Engelbart’s (1962) seminal research on augmenting intelli-
gence, an HCAI approach emphasises the complementarity of humans 
and machines, aiming to design AI systems that amplify, augment, 
and empower individuals by considering safety, reliability, and trust-
worthiness principles (Shneiderman, 2022). In educational contexts, 
Buckingham Shum et al. (2019) and Luckin et al. (2006) were among 
the pioneers advocating for the integration of human-computer interac-
tion, and HCD approaches (Giacomin, 2014) in the ﬁelds of LA and 
AIED, respectively. They emphasised the need to fully comprehend 
educational stakeholders’ needs, preferences and challenges, often ne-
cessitating their inclusion in some stages of the design process using 
HCD methods. This reinforces the relevance of HCAI and HCD methods 
in designing the technical, social, and data-related aspects of LA/AIED, 
mitigating potential social harms related to the spectrum of analytics 
use, from rule-based and descriptive to AI and machine learning-driven 
predictive and prescriptive forms (Davenport, 2018).
2.1.1. Human and computer automation complementarity
To articulate the balance between humans and AI, Shneiderman 
(2022) developed a two-dimensional framework. This framework, de-
signed for a broad audience, distinguishes between varying levels of
human control and computer automation. These factors are not con-
sidered mutually exclusive.
The notion of human control is closely related to the sense of agency. 
This subjective experience stems from perceived control over one’s ac-
tions to make decisions and inﬂuence events (Moore, 2016). Viewed 
through the HCD lens, a sense of agency is crucial in designing inter-
faces that support an internal locus of control (i.e., individuals’ percep-
tions of controlling their outcomes). In an educational setting, human 
control can range widely, from learners or teachers exercising a high 
level of agency over the outcomes of LA/AIED systems to simply receiv-
ing and understanding information (Hooshyar et al., 2023). A high level 
of human control may involve learners using their expertise to strate-
gically make informed decisions and take appropriate actions in their 
learning environment. In contrast, a low level of control might occur 
when individuals receive and understand information but lack auton-
omy in their learning or teaching environment. This notion of human 

--- Page 3 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
control encompasses key elements of intentional, purposeful, and mean-
ingful learning (Jääskelä et al., 2021) and teaching (Biesta et al., 2015).
The notion of computer automation in an HCAI context refers to 
the characteristics of systems that use computer technology or algo-
rithms to perform tasks automatically, streamlining and expediting op-
erations that were previously completed by human actors (e.g., teachers 
or students) (Parasuraman et al., 2000). The level of automation is 
determined by its complexity (e.g., ranging from simple rule-based al-
gorithms to complex machine learning and AI models) and the number
of information process stages the automation supports (i.e., acquiring 
information, information analysis, decision-making, or action imple-
mentation) in the decision-making process (Onnasch et al., 2014). In 
educational setting, a high level of automation commonly refers to 
LA/AIED system capabilities that can automatically capture learner data 
and make predictions, commonly achieved using multiple algorithms 
or AI techniques, such as machine learning, computer vision, natu-
ral language processing, or intelligent agents (e.g. Dogan et al., 2023, 
Jamalova et al., 2022). On the other hand, a low level of computer 
automation typically involves a system where information is manu-
ally prepared or a system follows a ﬁxed set of rules strictly deter-
ministically. Examples can include non-data-intensive solutions (e.g., 
presentation slide decks) and manually pre-conﬁgured visualisations in 
LA dashboards (Fernandez Nieto et al., 2022). Such systems often lack 
autonomy and adaptability when faced with situations beyond their pro-
grammed capabilities.
In turn, a single LA/AIED system can provide various features that 
combine diﬀerent levels of human control and computer automation, 
catering to diﬀerent tasks and intended users (Holstein et al., 2020). 
This results in the following four quadrants (two-dimensional HCAI 
framework) contextualised for LA/AIED systems, each representing a 
diﬀerent combination of human control and computer automation:
Q1: LOW human control & LOW computer automation. This quad-
rant represents systems with limited user control or conﬁguration 
and minimal or no automation. After receiving information from 
the system, end-users can only comprehend it but cannot person-
alise or modify it. Some examples in this quadrant include learning 
resources in the learning management system; student-facing report-
ing systems that generate reports for awareness or reﬂection in an 
asynchronous manner (e.g., Bodily & Verbert, 2017); and rule-based 
visual data stories (e.g., Echeverria et al., 2018, 2024), which pro-
vide feedback to students about their collaboration process and task 
completion after a learning activity.
Q2: HIGH human control & LOW computer automation. This quad-
rant represents systems where end-users can personalise and con-
ﬁgure aspects of the information process and maintain a sense of 
agency over the learning environment. In contrast, the system fa-
cilitates exploration through manual operation with minimal or no 
automation. Examples include personalised visualisation dashboards
(e.g., Muslim et al., 2016), which allow end-users to control or co-
conﬁgure the descriptive analytics that learners can use to reﬂect 
on the achievement of learning goals; and educator-driven data ana-
lytics systems (e.g., Fernandez Nieto et al., 2022), which may rely on 
educators’ experience, intuition, and informal observations for ed-
ucators themselves to make decisions about instructional strategies 
and feedback.
Q3: LOW human control & HIGH computer automation. This quad-
rant represents systems that heavily rely on automation with min-
imal end-user control. Here, automated processes and algorithms 
handle decision-making and action-taking processes. Examples in-
clude systems that capture interactions of students or teachers and 
utilise them in predictive analytics components to provide fully au-
tomated feedback (e.g., Ochoa et al., 2018, Maier & Klotz, 2022) 
and automated grading systems (e.g., Shetty et al., 2022), which may 
fully or partly replace the teacher’s role in speciﬁc assessment tasks.
Q4: HIGH human control & HIGH computer automation. This quad-
rant represents systems that enable manual operation while bene-
ﬁting from automated assistance to enhance the decision-making 
process in the learning environment for teachers or learners. Ex-
amples in this quadrant include intelligent teaching assistants that 
support classroom orchestration (e.g., Lawrence et al., 2023)), rec-
ommender systems that promote the development of metacognitive 
skills (e.g., Khosravi et al., 2019, Darvishi et al., 2024), and sophis-
ticated modelling/predictive features in analytics reports or dash-
boards that provide guidance and support (e.g., Khachatryan et al., 
2014). Here, teachers or students can utilise the highly automated 
features of the tool to perceive and make sense of learning data 
and make informed pedagogical decisions about the next course of 
action (Holstein et al., 2019).
2.1.2. The HCAI principles of safety, reliability, and trustworthiness
In addition to deﬁning these levels of control, designing any 
LA/AIED systems that oﬀer a signiﬁcant level of human control and 
computer automation must consider the fundamental principles of 
safety, reliability, and trustworthiness to ensure ethical practices and 
reduce the risk of data misuse (Cavalcante Siebert et al., 2023, Shneider-
man, 2022). In educational contexts, LA/AIED systems should embrace 
a safety culture, which implies that researchers, designers, and system 
operators should establish strong relationships with end-users and rele-
vant educational stakeholders, as well as implement strict data privacy 
measures (Holmes et al., 2022). These may include involving stakehold-
ers in data-sharing decisions, ensuring data collection transparency, and 
granting data access only to speciﬁc users (Drachsler & Greller, 2016).
An LA/AIED system is deemed reliable when it delivers accurate
information as anticipated by the user while interacting with it (Shnei-
derman, 2022). However, no predictive model can achieve such perfec-
tion (Baker, 2016). Therefore, LA/AIED systems designers may beneﬁt 
from accepting the existence of imperfection by studying how users val-
idate and respond to whether such systems may adversely aﬀect their 
learning (Kitto et al., 2018). This can potentially be done by educating 
humans about AI capabilities and human biases, allowing for a balanced 
delegation of automation tasks while incorporating elements of human 
oversight (Pinski et al., 2023). Finally, an LA/AIED system is considered 
trustworthy when users have conﬁdence (and, therefore, it is regarded as 
‘trusted’ by users). Aiming to foster greater trust and conﬁdence among 
users, the system could actively seek feedback from users, learn from 
its mistakes, and adapt to improve its performance while aligning with 
user expectations (Usmani et al., 2023). Designers ought to adopt a 
practical approach that prioritises transparency (Nazaretsky, Ariely et 
al., 2022, Nazaretsky, Cukurova et al., 2022) and accountability (Pardo 
& Siemens, 2014) and aim to understand the features of a system that 
would increase users’ trust in it.
2.1.3. Human-centred design in LA/AIED
An HCAI approach strongly advocates for the participation of per-
tinent stakeholders, such as end-users with lived experience, potential 
future users, policymakers, and experts in ethics and human values, in 
the design and deployment of AI systems (Usmani et al., 2023, Shnei-
derman, 2020b). HCD thus plays a crucial role in HCAI as it focuses 
on the needs and requirements of the people for whom the system is 
intended, rather than the designer’s creative process or the technology 
capabilities (Giacomin, 2014). As a participatory practice, HCD involves 
an iterative process of understanding the context, identifying end-user 
requirements, and involving stakeholders with lived experiences in the 
design and evaluation of the system, ideally engaging with stakeholders 
as equal partners (Xu et al., 2023, Bødker et al., 2022). From Hanington 
and Martin’s (2012) perspective, the HCD process includes ﬁve multi-
faceted phases: (1) planning, scoping, and deﬁnition – clearly deﬁning the 
parameters of the project; (2) exploration, synthesis, and design implica-
tions – conducting immersive research and design ethnography to gather 
information and derive insights that will guide design choices; (3) con-

--- Page 4 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
cept generation and early prototype iteration – generating ideas, concepts, 
or creating an early version of prototypes with stakeholders; (4) evalu-
ation, reﬁnement, and production – testing and gathering feedback from 
stakeholders to reﬁne designs, ensuring they meet the desired standards 
in the production; and (5) launch and monitor – conducting quality as-
surance testing of the design to ensure readiness for public use, and 
ongoing analysis to make necessary adjustments if needed.
Numerous HCD techniques are available to assist designers and 
researchers in the aforementioned phases (Giacomin, 2014, Maguire, 
2001). These techniques can enable interaction with stakeholders and 
aid in the identiﬁcation of their meanings, desires, and needs, which 
can be achieved through verbal techniques (e.g., ethnographic inter-
views, questionnaires, cognitive tasks, think-aloud, persona crafting, 
and brainstorming) or non-verbal techniques (e.g., design probes, ob-
servations, body language analysis, and physiological analysis). Design 
probes involve designed artifacts, such as photography or diaries, doc-
umented by participants to elicit observable responses (Bødker et al., 
2022). A growing set of more speculative techniques (e.g., real ﬁc-
tion, role-playing, para-functional prototypes, what-if scenarios and 
fabulation) are used for simulating opportunities and envisaging pos-
sible futures for designing future-looking features. Nowadays, some of 
these HCD techniques are starting to be used to design contemporary 
LA/AIED systems or to envisage potential future scenarios of AI appli-
cation in education (e.g., Prestigiacomo et al., 2020, Holstein et al., 
2019, Echeverria et al., 2023).
Regarding stakeholder involvement, Sarmiento and Wise (2022)
conducted an initial review of HCD methods in the LA literature, par-
ticularly in participatory design and co-design. They pointed out the 
increased use of these two methods in higher education and highlighted 
detailed descriptions of research techniques that were often lacking. 
From this point of view, the extent of stakeholders’ involvement can be 
categorised into active or passive. Active involvement refers to possess-
ing agency in shaping the outcomes that arise from the design processes 
(Dollinger et al., 2019). Stakeholders engage in conversations that con-
tribute to creating designs, assisting in testing, evaluating, and provid-
ing feedback on designs, or being actively involved in decision-making 
processes that shape the design of LA/AIED systems. On the other hand,
passive involvement refers to stakeholders playing a role as more 
consultative or advisory in the design activities (Edelenbos & Klijn, 
2006). They provide input, feedback, or opinions but may have lim-
ited decision-making authority or direct inﬂuence over the outcomes.
2.2. Related works and research gaps
To better understand how human-centredness has been considered 
in the design of LA/AIED systems, it is crucial to examine the key char-
acteristics of current research in this area. These include the education 
levels mainly targeted, the types of research methods used (such as 
qualitative, quantitative, or mixed), and the most commonly applied 
HCD techniques like co-design, focus groups, and prototyping. For in-
stance, previous reviews of LA/AIED generally have focused on higher 
education (e.g., Williamson & Kizilcec, 2022, Leitner et al., 2017, Do-
gan et al., 2023), K-12 (Zhang & Aslan, 2021, Grani´c, 2022, Lin et 
al., 2023), or informal learning (Grani´c, 2022). However, it remains 
unclear which education level has most thoroughly considered human-
centredness. Moreover, there is a gap in current research regarding the 
diverse research methodologies used in human-centred LA/AIED re-
search and the speciﬁc design phases (listed in Section 2.1.3) where 
they have been applied. At the same time, previous non-systematic re-
views that initially explored human-centredness in LA (e.g., Sarmiento 
& Wise, 2022) and AIED (e.g., Khosravi et al., 2022) literature have 
not identiﬁed the speciﬁc HCD techniques employed at diﬀerent design 
stages. Together, these issues motivate our ﬁrst research question:
RQ1. What is the current state of human-centred LA/AIED research, 
speciﬁcally through the lens of education levels targeted, research 
methodologies employed, design phases covered, and HCD tech-
niques utilised?
Arguably (Lang & Davis, 2023), the involvement of educational 
stakeholders is paramount in the HCD process, as highlighted in recent 
human-centred LA (e.g., Sarmiento & Wise, 2022, Barreiros et al., 2023) 
and AIED (e.g., Li & Gu, 2023, Lin et al., 2023) works. However, this 
involvement can take various forms (Lang & Davis, 2023). It remains 
unclear to what extent educational stakeholders’ involvement, whether 
active or passive (see Section 2.1.3), has been considered in the vari-
ous phases of the design process, from inception to implementation and 
evaluation of existing human-centred LA/AIED systems. Additionally, 
none of these works have discussed how extensively the perspectives 
of each educational stakeholder (i.e., teachers, students, and experts) 
have been incorporated at the various design phases. This highlights a 
pressing need to explore the extent of each educational stakeholder’s 
contribution to the design process of current human-centred LA/AIED 
systems. This motivates our second research question:
RQ2: To what extent have educational stakeholders contributed to 
the design process (phases) of current human-centred LA/AIED sys-
tems?
Although the involvement of stakeholders in the design of LA/AIED 
systems has received signiﬁcant attention (e.g., Lawrence et al., 2023, 
Holstein et al., 2019, Kaliisa et al., 2023) other key aspects of human-
centredness, such as balancing system features for end-users against 
fully automated features focused on technical goals or replacing hu-
man activity, are also important (Lang & Davis, 2023, Usmani et al., 
2023). LA/AIED researchers have suggested various ways to empower 
users, such as oﬀering control over automated recommendations (e.g., 
Ma et al., 2022, Lawrence et al., 2023) or enhancing the explainability 
of AI outcomes (e.g., Khosravi et al., 2022, Kloos et al., 2022). How-
ever, the balance between human control and computer automation in 
existing human-centred LA/AIED systems remains underexplored. Ad-
ditionally, the importance of empowering stakeholders in light of rapid 
AI advancements was emphasised in a systematic review by Dogan et al. 
(2023), which focused on the implementation of AI in online learning 
but not in other LA/AIED system types like visualisation/dashboards, 
intelligent tutoring systems, and recommender systems (Kaliisa et al., 
2023, Williamson & Kizilcec, 2022, Lin et al., 2023, da Silva et al., 
2023). To our knowledge, no studies have examined the level of human 
control and computer automation in designing existing human-centred 
LA/AIED systems. The two-dimensional HCAI framework proposed by 
Shneiderman (2020b) (see Section 2.1.1) provides a frame of reference 
to analyse the human control/automation balance. This motivates our 
third research question:
RQ3: What levels of human control and computer automation have 
been considered in various types of human-centred LA/AIED systems 
designed with the involvement of stakeholders?
As mentioned above, some researchers have increasingly recog-
nised the importance and potential of HCAI in the current LA/AIED 
literature landscape (e.g., Renz & Vladova, 2021, Zhao et al., 2023). 
One critical aspect that has garnered considerable attention within the 
HCAI domain is the assurance of safety, reliability, and trustworthiness 
in such systems. For example, Renz and Vladova (2021) highlighted 
the importance of incorporating human values and ethical considera-
tions while developing AI systems for personalised learning environ-
ments. The authors visualised the applications of AIED systems (Renz 
& Vladova, 2021, ﬁg. 4, p.12) in an adapted Shneiderman’s (2020b)
two-dimensional HCAI framework, by adding a trustworthiness dimen-
sion perpendicular to human-AI augmentation and types of machine 
learning. In a more recent LA study, Zhao et al. (2023) proposed a 
framework based on HCAI to identify the most eﬀective learning strate-

--- Page 5 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
gies highlighting the signiﬁcance of reliability of the AI algorithms. In 
AIED literature, Yang et al. (2021) argued that AI systems should be 
designed to be transparent, explainable, and accountable to reduce the 
risk of algorithmic bias and misuse of AI. While these examples recog-
nise the critical role of investigating safety, reliability, and trustworthiness
principles, there is a lack of understanding of how these principles have 
been considered when designing human-centred LA/AIED systems. This 
motivates our fourth research question:
RQ4: How and to what extent have the HCAI principles of safety, 
reliability, and trustworthiness been discussed in existing human-
centred LA/AIED systems?
3. Method
3.1. Review procedures
To conduct the systematic literature review, we followed the Pre-
ferred Reporting Items for Systematic Reviews and Meta-Analyses 
(PRISMA) protocol (Page et al., 2021), which has four phases and aims 
to promote transparent reporting. We searched four reputable biblio-
graphic databases, including Scopus, ACM Digital Library, IEEE Xplore, 
and Web of Science, to ﬁnd high-quality peer-reviewed publications on 
HCAI in LA, and where the relevant LA/AIED (e.g., Learning Analytics 
and Knowledge – LAK and Artiﬁcial Intelligence in Education – AIED) con-
ferences are commonly published (i.e., ACM and Scopus, respectively). 
The initial query that was used for the title, abstract, and keyword 
search of peer-reviewed publications included the following groups of 
keywords:
• (human-cent*red OR user-cent*redness OR “value-sensitive design” OR 
“co-design” OR “participatory design” OR “co-creation” OR design pro-
cess) AND
• (“learning analytics” OR education* OR student* OR teacher* OR 
classroom) AND
• (“artiﬁcial intelligence” OR “intelligent augmentation” OR tool* OR 
system OR automation OR AI OR analytic* OR algorithm* OR visu-
ali*ation OR “dashboard” OR “interface”).
To focus on studies published in the established research ﬁeld of LA and 
AIED in the last decade, a publication year constraint was used to search 
for relevant publications from January 1, 2012 to November 1, 2023. 
By focusing on the past 10 years, this SLR captures the most recent ad-
vancements in LA/AI technologies and their educational applications, 
providing an up-to-date understanding of the ﬁeld’s current state. The 
database search initially yielded 1,678 articles with 511 duplicates re-
moved (14 duplicates were identiﬁed and merged manually), leaving 
1167 articles for the title and abstract screening process (see Fig. 1). To 
ensure a thorough and accurate screening, three researchers indepen-
dently reviewed the titles and abstracts of eligible articles according to 
three predetermined inclusion and exclusion criteria, as follows:
1. First, we included articles that reported empirical studies for de-
veloping LA/AIED systems (long papers). These included studies 
proposing a design framework that may use tools/interfaces for il-
lustration/explanation in practice. We excluded non-empirical stud-
ies, such as theoretical, opinion/positioning, dataset, literature re-
view, and short papers.
2. Second, we included articles that reported on the studies that aimed 
to design or develop data-intensive education systems/tools/in-
terfaces for end-users and excluded studies that only mentioned 
“education”, “learning”, “LA”, or “AI” as an example of other more 
general topics.
3. Third, we only included articles that involved stakeholders (e.g., 
teachers, students, administrative staﬀ, and designers) in the study 
and excluded studies that focus merely on advancing technical 
aspects of the technology (e.g., improving the accuracy of AI al-
gorithms) without directly studying the implications for human 
learning.
At least two researchers reviewed each article (R1–R2), and a third 
researcher (R3) resolved the conﬂicts through in-depth simultaneous 
discussions until a consensus was reached. After the title and abstract 
screening, a total of 272 articles (as seen in Fig. 1) were identiﬁed 
as candidates for full-text review. The inter-rater reliability among the 
three researchers was 0.80 (R1&R2), 0.88 (R1&R3), and 0.74 (R2&R3), 
as measured by Cohen’s kappa, indicating a substantial to high agree-
ment among the reviewers (Page et al., 2021).
After the full-text review, 164 articles were excluded following our 
exclusion criteria (detailed above), consisting of not aiming to design 
or develop LA/AIED systems for end-users (n=81), non-empirical study
(n=53), merely mentioned “education”/”learning”/”AI”/”LA” as exam-
ples (n=15), focused on advancing algorithms/technologies without learn-
ing implications (n=9), lack of full-text access (n=6). This means that 
108 articles were chosen for data extraction, and the inter-rater reli-
ability (Cohen’s kappa) for the full-text screening was 0.71 (R1&R2), 
0.67 (R1&R3), and 0.93 (R2&R3) indicating a substantial agreement 
between the researchers. Conﬂicting decisions were resolved through 
in-depth discussions among researchers (R1–R3) or consulting a fourth 
researcher to reach a consensus (Yan et al., 2022). The following sub-
sections describe the data extraction and analysis processes to address 
each research question.
3.2. Data extraction and analysis
To address RQ1, we collected the study characteristics, including 
targeted educational levels (i.e., K-12, middle school, high school, and 
university/college) and employed research methodologies (i.e., qualita-
tive, quantitative, or mixed). Next, we employed the ﬁve multifaceted 
design phases by Hanington and Martin (2012, see Section 2.1.3) to 
identify in which phase(s) stakeholders’ views or inputs were consid-
ered in the studies included in the review. We also collected information 
about what HCD techniques were utilised in the study (e.g., co-design, 
prototyping, interviews, and storyboards). It is important to note that 
each study could employ multiple HCD research techniques through-
out diﬀerent design phases. We presented our ﬁndings in the form of 
a Sankey Diagram to inductively analyse relationships between charac-
teristics, design phases, and HCD techniques.
To address RQ2, we extracted the information on stakeholders’ in-
volvement as active or passive, aligning with their deﬁnitions presented 
above (in Section 2.1.3). We further identiﬁed the level of involvement 
based on stakeholders’ roles, such as students, teachers, subject experts, 
and administrators. To ascertain the impact of stakeholder involvement 
on the design of the LA/AIED system, we mapped their active or passive 
involvement status in each of ﬁve multifaceted design phases proposed 
by Hanington and Martin (2012, see Section 2.1.3). For example, Hol-
stein et al. (2019) actively involved teachers in developing a classroom 
orchestration system for their use, representing active involvement. On 
the other hand, Fernandez Nieto et al. (2022) consulted teachers in de-
signing a system for student use, in which students who would be the 
intended users were not involved in any of the phases of the design 
process. All this information was subjected to quantitative analysis by 
comparing and employing descriptive statistics as the primary analyt-
ical approach for reporting results. The percentages presented in the 
next section were calculated based on the total of the included studies 
(n=108).
To address RQ3, ﬁrst, the proposed human-centred LA/AIED sys-
tem described in each article was categorised based on the deﬁnition 
of the two-dimensional HCAI framework (Shneiderman, 2022), which 
included the four quadrants of human control and computer automa-
tion outlined in Section 2.1.1. Then, we further mapped these systems 
with the aforementioned stakeholder involvement (active or passive, 

--- Page 6 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
Fig. 1. The PRISMA protocol as applied in the current systematic literature review.
see 2.1.3). We also collected the type of LA/AIED system (i.e., visu-
alisation/dashboard, intelligent tutoring system, learning design tool, 
recommender system, prediction system, information retrieval assis-
tant, and evaluation of course essay system) presented in each article 
(Zhang & Aslan, 2021, Grani´c, 2022, da Silva et al., 2023). This gath-
ered information underwent inductive analysis through a comparative 
approach, incorporating descriptive statistics and supported by illustra-
tive examples.
Lastly, regarding RQ4, any discussion about HCAI principles within 
the scope of safety, reliability and trustworthiness was extracted with a 
question “How did authors discuss safety, reliability, or trustworthiness?”. 
We qualitatively analysed these discussions using inductive thematic 
analysis (Braun & Clarke, 2012). We prepared and applied an initial 
coding scheme that pertained to safety, reliability and trustworthi-
ness (as deﬁned in Section 2.1.2). In this case, data safety included 
the subcodes: data privacy, data sharing, and transparency in data 
collection. Reliability encompassed the subcodes: data accuracy, com-
pleteness, bias, validity, and consistency. Trustworthiness included the 
subcodes: trust, transparency, and accountability. The coded data was 
cross-checked between two researchers concurrently, and any emerging 
codes or conﬂicts were jointly agreed upon in iterative discussion ses-
sions until a consensus was reached. Lastly, the emerging themes were 
reported by classifying them into the context of safety, reliability and 
trustworthiness.
4. Results
4.1. Current research on human-centred LA/AIED systems (RQ1)
Most studies were reported at a University/college level (53%), fol-
lowed by K-12 (34%) and informal learning (13%). The type of research 
method reported in these studies was distributed as follows: qualitative 
(44%), mixed-methods (43%), and quantitative (13%). Regarding the 
design phases of the HCD process, we found that 18% of the studies 
addressed Phase 1 (planning, scoping, and deﬁnition). Phase 2 (explo-
ration, synthesis, design implications) was addressed in 53% of the stud-
ies, while Phase 3 (concept generation and early prototype iteration) 
accounted for 51%. Phase 4 (evaluation, reﬁnement, and production) 
received the highest attention at 56%. However, only a small minority, 
9% of the studies, considered Phase 5 (launch and monitor).
Next, common HCD techniques used in the design process include 
interviews (52%), questionnaires (47%), co-design (28%), prototype 
validation (26%), focus groups (10%), observations (10%), and surveys 
(8%). Less used techniques included workshops (5%), storyboards (4%), 
personas (4%), and card sorting (3%). Very few studies used other tech-
niques that are common in wider HCD research, such as Wizard-of-Oz 
(Schulz et al., 2022, Vinella et al., 2022, Echeverria et al., 2023), speed 
dating (Holstein et al., 2019, Tenório et al., 2022), think-aloud (Conijn, 
Van Waes et al., 2020, Ahn et al., 2021), eye tracking (Lallé et al., 2017, 
Mangaroska et al., 2018), and user journeys (Weigand & Kindsmüller, 
2021).
Fig. 2 illustrates the characteristics of current research focused on 
human-centred LA/AIED systems. In summary, we found that most 
studies have been conducted at the university level, and studies have 
mostly involved qualitative or mixed-method research. More attention 
has been given to Phases 2, 3, and 4 of the HCD process, while Phases 
1 and 5 received less attention. There was a shift from a more qualita-
tive methodology approach in Phase 2 to a more mixed methodology 
in Phase 4 as the design tended to mature. Quantitative research has 
not been employed in Phase 1. Yet, some quantitative methods are used 
at later stages of the design process (phases 4 and 5), particularly in 
the form of evaluation questionnaires. Last but not least, interviews 
have been the most commonly used HCD technique (20%) in most de-
sign phases, except for Phase 4 (5%), where questionnaires were more 
prevalent (7%).
4.2. The extent of stakeholder involvement in design (RQ2)
Concerning stakeholder involvement in the design process, stake-
holders were classiﬁed into active and passive roles (see deﬁnitions in 
Section 2.1.3). Fig. 3 depicts each design phase with the percentage of 
included studies covering stakeholders’ active/passive involvement.
Overall, lower (both active and passive together) stakeholder in-
volvement has been observed in Phases 1 (18% – 4% passive and 14% 
active) and 5 (11% – 5% passive and 6% active), while there has been 
more stakeholder involvement in other design phases (Phase 2 – 51%, 
Phase 3 – 51%, and Phase 4 – 56%). Our ﬁndings also indicated a 
higher active stakeholder involvement in Phase 2 (32%) and Phase 
3 (33%) compared to the passive involvement. Notably, the design
Phase 4 – evaluation, reﬁnement, and production – was the only phase 
that had higher passive (31%) compared to active (25%) stakeholder 
involvement. This ﬁnding suggests that while most of the works are 
concentrated on evaluating the design of their LA/AIED systems, there 
is a tendency for the outcomes produced by stakeholders not to be fur-
ther considered for improving these designs. For example, Khosravi et 
al.’s (2019) study illustrates this passive stakeholder involvement, where 
the authors only reported on students’ evaluation of a system through 
surveys and lab experiments. In contrast, Wiley et al.’s (2023) work il-
lustrates active involvement in which teachers participated in several 
iterative evaluation sessions to re-design an LA dashboard based on 
their continuous input and feedback.
Furthermore, our analysis revealed that students and teachers were 
involved in 71% and 59%, respectively of the total number of included 
studies (see Fig. 4). Subject experts made up 17%, administrators 8%, 
and educational designers 4%. The remaining 9% included professionals 
such as software developers (e.g., Wiley et al., 2023), evaluators (e.g., 
Ocumpaugh et al., 2017), and counsellors (e.g., Cukurova et al., 2017).
Students exhibited the highest representation of passive involvement 
at 52%. For instance, students are often involved in the evaluation of 
the system (e.g., Ochoa & Dominguez, 2020, Lim et al., 2021), or be-
ing observed on their behaviours during a learning activity while using 
the system (e.g., Khosravi et al., 2019) but this does not necessarily 
means they are actively involved in the design of such systems. The 
active student involvement can be observed, for example, in the form 
of participating in ideas generation design activities (e.g., de Quincey 
et al., 2019, Wang et al., 2022). Conversely, despite students being 
the most involved stakeholders, their active involvement was compara-
tively lower than that of teachers (39%). In these studies, teachers were 
involved in co-design activities, from inception to evaluation, where 
the systems were designed to meet their teaching needs and prefer-
ences (e.g., Lawrence et al., 2023, Rodríguez-Triana et al., 2021, Olsen 
et al., 2021). An example of passive involvement of teachers (20%) 

--- Page 7 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
Fig. 2. The distribution of key characteristics in the current research state of human-centred LA/AIED systems, depicted through a Sankey diagram. Categories are 
sorted by frequency. The diagram illustrates the distribution of education levels, the utilisation of research methodologies (qualitative, quantitative, or mixed), the 
progression through ﬁve multifaceted design phases, and the application of HCD techniques. The varying thickness of the ﬂow path represents the signiﬁcance of 
each transition.
Fig. 3. Distribution of stakeholder involvement varies across various design phases. The data demonstrates shifts in passive (black) and active (green) involvement 
throughout design phases, with more passive stakeholders in Phase 4.
Fig. 4. Distribution of stakeholder involvement in the design of human-centred LA/AIED systems. The green bar represents the percentage of stakeholders actively 
contributing to and inﬂuencing the design. In contrast, the black bar represents the percentage of stakeholders participating in the study with limited inﬂuence on 
design outcomes.

--- Page 8 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
Fig. 5. Distribution of human-centred LA/AIED systems categorised into the human control and computer automation quadrants of the HCAI framework (Q1-Q4, 
see deﬁnitions in Section 2.1.1). The green bars represent studies where the stakeholders actively engaged and contributed to the design of the tools. The black bars 
represent studies where stakeholders merely participated as test subjects, oﬀering limited input during the design phase of LA/AIED systems.
is when they are invited to explore the system, thereby oﬀering re-
searchers valuable insights into the sensemaking process without clar-
ifying whether such insights are further considered in the design or 
re-design of the system (e.g., Fernandez-Nieto et al., 2022, Alfredo et 
al., 2023).
Subject experts (e.g., Eradze et al., 2020) and educational designers 
(e.g., Tsai et al., 2022), 14% and 4% respectively, were more actively 
involved through participatory design. Administrators and others had 
almost equal proportions of active roles at 5% (e.g., De Silva et al., 
2022, Bonnat & Sanchez, 2022). In summary, students and teachers 
were the most involved education stakeholders, with students having 
the highest representation of passive involvement and teachers having 
the highest representation of active involvement.
4.3. The levels of human control and computer automation (RQ3)
We examined the distribution of LA/AIED systems across the four 
quadrants of the HCAI framework (see Section 2.1.1). This distribution 
is summarised in Fig. 5 and the details are in the Appendix (see Table 2).
Notably, a higher proportion of human-centred LA/AIED systems 
have already considered substantial human control features in their 
design, with a more signiﬁcant percentage of systems categorised in 
Q4 at 47% (e.g., Pozdniakov et al., 2022, Alfredo et al., 2023) and in 
Q2 at 32% (e.g., Hu et al., 2022, Jeong et al., 2023). In contrast, a 
smaller proportion is found in Q1 at 12% (e.g., Kivimäki et al., 2019, 
Fernandez-Nieto et al., 2021) and in Q3 at 10% (e.g., Ochoa et al., 2018, 
Ocumpaugh et al., 2017). Next, we present the ﬁndings of Q4 and Q2, 
as these were the most frequent categories, followed by Q1 and Q3, 
which were the least represented categories.
LA/AIED systems in Q4 have had more active stakeholder involve-
ment (28%) compared to systems in other quadrants, where stake-
holders have often been passively involved. One example for Q4 is 
illustrated in Lawrence et al. (2023)’s work, in which teachers were 
actively involved in several design phases during a multi-year study 
to build an AI-powered classroom orchestration system that explicitly 
considers teachers’ agency (i.e., giving the control to teachers to accept 
or reject recommendations coming from the AI). In contrast, passive 
stakeholder involvement in Q4 (19%) include studies where researchers 
documented observations and behavioural multimodal data (eye track-
ing data, interaction log ﬁles, and other physiological sensors) from 
students interacting with an AI-powered system (i.e., intelligent tutor-
ing system) (e.g., Lallé et al., 2017).
Next, systems in Q2 had less active stakeholder involvement in 
their design processes (13%) compared to a higher passive involvement 
(19%). In this quadrant, active stakeholder involvement includes par-
ticipatory design activities to understand how stakeholders use systems 
that require customisation (i.e., manually selecting options to gener-
ate visualisations) on exploratory tasks, for example, how teachers use 
a data visualisation inquiry tool that requires them to control and 
customise visualisations (e.g., Shreiner & Guzdial, 2022). In contrast, 
passive involvement may be observed in the form of usability studies 
where participants are asked to evaluate systems through surveys or 
questionnaires, such as in the work by Muslim et al. (2016), where stu-
dents and teachers were asked to rate the usefulness of a rule-based 
system to support ﬂexible deﬁnition and dynamic generation of indi-
cators to meet the needs of diﬀerent stakeholders with diverse goals 
and questions (i.e., exploratory tasks using LA dashboards). This can be 
considered an indirect inﬂuence on design outcomes.
Regarding systems in Q3 which feature high automation and low 
human control, we found less active stakeholder involvement in their 
design process (4%) compared to passive involvement (6%). For Q3, 
active involvement can be illustrated through co-design sessions aimed 
at identifying features that could be included in intelligent systems, 
for example, by including teachers’ perspectives in the design of two 
modalities of a robot to support social interactions (as a social actor) or 
knowledge acquisition (as a didactic tool), and that would run fully au-
tomated during authentic classroom use (e.g., Ekstrom & Pareto, 2022). 
As for passive stakeholder involvement, these studies have commonly 
collected diverse log data and usability questionnaires to understand 
users’ attitudes towards the use of automated intelligent support, such 
as the work presented by Wilson et al. (2021), in which teachers and 
students were asked to evaluate a fully-automated writing score system 
using usability and attitude questionnaires.
Lastly, systems in Q1 that feature low human control and automa-
tion had an equal proportion of active and passive involvement, at 
6%. An active involvement is exempliﬁed in Garcia-Ruiz et al.’s (2022)
study, in which participatory design activities were conducted with 
students (e.g., initial exploration, focus group discovery, and collab-
orative prototyping with experts) to design a novel visualisation tool 
with a limited conﬁguration setting. In contrast, Fernandez-Nieto et 
al.’s (2021) work reﬂects passive involvement, as teachers participated 
in interviews to share their sensemaking on a low-ﬁdelity dashboard 
prototype, in which the prototype was manually generated, and the 
outcomes were not part of further studies. In summary, education stake-
holders were more involved in Q4 than in other quadrants, indicating 
active stakeholder involvement in inﬂuencing design outcomes on sys-

--- Page 9 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
Fig. 6. Distribution of human-centred LA/AIED systems on the two-dimensional HCAI framework by type of system. Each colour represents diﬀerent quadrants in 
the HCAI framework (Q1–Q4, see Section 2.1.1).
tems considering end-user agency and using AI or advanced computer 
automation.
Concerning the diﬀerent types of LA/AIED systems, as depicted in 
Fig. 6, we found that the most prevalent type is visualisation or dash-
boards, accounting for 53% of the total of the included studies.
The most prominent quadrant in this type is Q4, which comprises 
24% of the total included studies. This type involves a high level of hu-
man control and computer automation, such as educators actively util-
ising and interpreting the visualised data generated by an AI-powered 
system which automatically make inferences by analysing complex and 
large amount of students’ learning data (e.g., Alfredo et al., 2023, 
Nazaretsky, Bar et al., 2022, Conijn, Van Waes et al., 2020). The next 
most represented category is intelligent tutoring systems at a total of 
31% (e.g., Holstein et al., 2019, Gerdes et al., 2017, Ngoon et al., 2023). 
Q4 also represents the largest quadrant for this type (25%), where high 
human control is given to users, such as overseeing learning activities 
(e.g., Tissenbaum & Slotta, 2019), accepting or rejecting automated in-
terventions or recommendations from the system (e.g., Di Mitri et al., 
2022), and making real-time adjustments (e.g., Lawrence et al., 2023).
Next, learning design support for teachers is represented by a total 
of 11%. The most prominent quadrant for this type is Q2 at 6% (e.g., 
Michos et al., 2020, Vezzoli et al., 2020, Pishtari et al., 2021), which 
favours high human control, and Q4 is the second highest at 3% (e.g., 
Rodríguez-Triana et al., 2021, Albó et al., 2022, Kaliisa et al., 2020), 
which may indicate learning design systems have lacked computer-
automation. Learning design systems commonly consider high human 
control, as exempliﬁed by the agency of learning designers in applying 
the inquiry process where they possess the autonomy to actively shape 
and reﬁne learning experiences (e.g., Pishtari et al., 2021, Rodríguez-
Triana et al., 2021).
The prediction system type accounts for a total of 8% and only has 
high computer automation (Q3 at 3% and Q4 at 5%). An example of 
Q3 of this type is in Ocumpaugh et al.’s (2017) study, where the system 
was trained on historical students’ data to identify patterns, make pre-
dictions on students’ engagement, and produce non-conﬁgurable early 
warning reports for educators to interpret, without having any further 
control on the system. On the other hand, an example in Q4 can be 
seen in Duan et al.’s (2023) study, where the teachers have more con-
trol over conﬁguring the model and representation of prediction results 
to identify at-risk students, which ensures predictions are trustworthy 
and can support proper interventions. Evidently, no prediction systems 
are at low-level computer automation, as evidenced by no studies found 
in Q1 and Q2, since all prediction systems require a high level of com-
puter automation (i.e., AI models) to operate.
The remaining three types—recommender system, information re-
trieval assistant, and evaluation of course essays—have Q4 as the most 
prominent quadrant. Recommender systems are represented by total of 
7%, with 5% in Q4, that includes course recommender system (e.g., 
Chang et al., 2023), learning resources recommender (e.g., Ruiz-Calleja 
et al., 2019), and personalised learning recommendations (e.g., Khos-
ravi et al., 2019). Information retrieval assistant comprises total of 
6%, with 4% in Q4 (e.g., Bonnat & Sanchez, 2022) and evaluation of 
course essay 4%, with 3% in Q4 (e.g., Lee et al., 2023). Systems in Q4 
across these three types have similarities where automation or an in-
telligent system relies on teachers’ or students’ oversight to interpret, 
make judgements, and contextualise the information from the provided 
interface to take actions in their teaching or learning environment close 
to real-time.
The other types of educational technologies accounted for smaller 
percentages, ranging from 1% to 5% of the total studies, adding up 
to 33%. These include game-based learning system (e.g., Tenório et 
al., 2022, Shute et al., 2021), online learning system (e.g., Martinez et 
al., 2020), mixed-reality systems such as augmented-reality and virtual-
reality (Bonnat & Sanchez, 2022, Zwolinski et al., 2022, Kang et al., 
2020), and social robots (e.g., Ekstrom & Pareto, 2022, Muldner et al., 
2013). In studies about social robots, such as in Ekstrom and Pareto’s 
(2022) study, Wizard of Oz tended to be employed in which the sys-
tem was manually controlled by researchers in the background, but 
students still had full control of the interaction, such as having a ﬂexi-
ble conversation with a robot to develop empathy and communication 

--- Page 10 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
skills. Among these, the most notable quadrant when aggregated was 
Q2 (14%), in which students had full control when interacting with the 
system (i.e., playing learning games (Wang et al., 2019) or interacting 
with peers in online learning (Cukurova et al., 2017)), which was man-
ually prepared with a pre-deﬁned set of rules towards intended learning 
outcomes, without requiring advanced automation.
In summary, regardless of the level of computer automation, each 
type of LA/AIED system has already considered a high level of human 
control, indicated by a higher percentage of studies categorised in Q2 
or Q4 for each type. These ﬁndings suggest that most reviewed human-
centred LA/AIED systems have been designed to empower users with 
the support of human oversight.
4.4. Safety, reliability, and trustworthiness discussion (RQ4)
Of the total number of human-centred LA/AIED systems’ studies re-
viewed, 54% contained a discussion or consideration of the HCAI prin-
ciples of safety, reliability, and trustworthiness to some extent. The 
individual proportions were 35%, 37%, and 25%, respectively. Next, 
we describe the topics that emerged from each principle as a result of 
our thematic analysis.
4.4.1. Safety
Data privacy emerged as the much-discussed topic (18%), empha-
sising its signiﬁcance when designing and implementing safe LA/AIED 
systems. Data privacy refers to the protection and control of personal 
and sensitive information of students, teachers, or any other individ-
uals involved in the learning process. These studies involved discus-
sions about safeguarding data related to personal identiﬁcation (e.g., 
Kivimäki et al., 2019, Ngoon et al., 2023), academic performance (e.g., 
Echeverria et al., 2019), learning progress (e.g., Ma et al., 2022), 
and other sensitive details collected and processed by human-centred 
LA/AIED systems (e.g., Santos et al., 2012). Notably, discussion about 
privacy could inﬂuence stakeholders’ willingness to adopt these systems 
in practice (e.g., Ma et al., 2022, Garcia-Ruiz et al., 2022).
The discussion of data sharing primarily focused on strategies to 
overcome privacy concerns (7%). Four studies advocated for anonymity 
features when sharing data as measures to protect participants’ identi-
ties from others, promoting a more open discussion of learning activities 
(e.g., Echeverria et al., 2019, Conijn, Van Waes et al., 2020, Sato et al., 
2023, Barreiros et al., 2023). These anonymity features could also help 
students recall and discuss performed actions without feeling judged by 
their peers (i.e., Echeverria et al., 2019). Moreover, six studies discussed 
safety strategies for data sharing as part of their design methodologies. 
Two of them incorporated design principles such as “Privacy by Design” 
criteria (i.e., Bonnat & Sanchez, 2022), allowing privacy and design 
to co-exist, and “Risk Communication Principles” (i.e., Ocumpaugh et 
al., 2017), allowing communicating the risk involved and the certainty 
when presenting data in a way that both experts and non-experts (i.e., 
students) can easily understand during design activity. Other studies 
leveraged co-design methods with teachers (e.g., Ngoon et al., 2023, 
Pishtari et al., 2021) and students (e.g., Lee et al., 2022, Garcia-Ruiz 
et al., 2022), to explore the type of data that can be shared with other 
users without breaching their privacy.
We found some discussions about data collection impact and pro-
cedures (10%). Two studies reported conﬂicting opinions from partic-
ipants regarding the beneﬁts and concerns associated with collecting 
and utilising student data (i.e., Wang et al., 2022, Kivimäki et al., 
2019). For example, Wang et al. (2022) reported that several students 
expressed worries about potential privacy breaches and discomfort in 
asking questions in an online forum (due to being tracked and con-
tinuous data collection), but they wanted to have a more personalised 
learning experience from the system. It exempliﬁes how students may 
want something beneﬁcial for their learning with an intelligent system 
but are unaware that such a system requires data collection. It might 
be necessary to establish clear communication between researchers and 
participants through informed consent. Five studies highlighted the im-
portance of informed consent procedures to ensure transparent data 
collection (i.e., Conijn, Martinez-Maldonado et al., 2020, Khosravi et al., 
2019, Wang et al., 2022, de Quincey et al., 2019, Ngoon et al., 2023). By 
acquiring explicit consent from students (e.g., opt-in/out process) and 
allowing users to control data access and explaining how the system 
operates (i.e., Bonnat & Sanchez, 2022, Wang et al., 2022), human-
centred LA/AIED systems could potentially deliver a sense of safety to 
users. Yet, de Quincey et al. (2019) argued that some participants may 
overlook the privacy policy of the informed consent process because 
they may not have read the information thoroughly.
Moreover, monitoring and surveillance based on student data 
were discussed in four studies (i.e., Pozdniakov et al., 2022, Zhou et 
al., 2021, Alfredo et al., 2023, Tsai et al., 2020). For instance, Zhou 
et al. (2021) reported the experiences, privacy concerns, and impacts 
of providing students awareness for using monitoring tools in a collab-
orative learning setting (i.e., remote group meetings). They reported 
changes in students’ behaviours, such as half of students feeling more 
motivated to engage and be more productive in the group conversa-
tions, while half of students still felt intense pressure and uncomfortable 
being monitored. In another study, Alfredo et al. (2023) further ad-
vised against using physiological data modelling and visualisation for 
surveillance purposes, including scenarios like exams and regular class-
rooms, as well as measuring students’ performance. Another study by 
Ngoon et al. (2023) suggested that institutions that plan to adopt smart 
classroom systems with continuous monitoring features should conduct 
regular evaluations with both students and teachers, such as addressing 
privacy concerns through an iterative co-design process. Finally, a small 
number of studies (3%) proposed strategies to ensure secured data ac-
cess (data security), such as two-factor authentication (i.e., Wang et 
al., 2022), using third-party software to establish privacy and security 
policies (Santos et al., 2012), and allowing limited data accessibility 
and visibility to relevant stakeholders (i.e., students) intended only for 
academic purposes (Martinez et al., 2020).
4.4.2. Reliability
In terms of reliability, we found that this principle is often addressed 
in terms of the accuracy of the system, the potential bias of these sys-
tems, and strategies to produce reliable data. We describe each of these 
topics below.
From the set of studies, we found accuracy (14%) as a key aspect 
to evaluate the system’s reliability. These studies often consider two 
factors that could impact the accuracy and perception of the system’s 
reliability: machine algorithm (3%) and human interpretation (11%). Ac-
curacy in machine algorithm refers to the ability of the system to provide 
correct/accurate outcomes. Two studies discussed approaches to evalu-
ate AI model accuracy that can lead to reliable outcomes (e.g., Chang et 
al., 2023, Khosravi et al., 2019). For example, Chang et al. (2023) used 
a mixed-method approach that integrated students’ survey data to eval-
uate the accuracy of their proposed machine-learning model. Similarly, 
in a study on recommender systems, Khosravi et al. (2022) reported ini-
tial results about incorporating both students’ subjective opinions and 
machine-learning algorithms, which can potentially improve the accu-
racy of the system in determining learning resource quality. On the 
other hand, accuracy in human interpretation refers to the signiﬁcance 
of how end-users (teachers/students) correctly interpret and understand 
indicators presented by the LA/AIED systems.
Six studies reported stakeholders’ responses about receiving inaccu-
rate information or conclusions from a system that can introduce unre-
liability due to misinformation (i.e., Liaqat et al., 2021, Pozdniakov et 
al., 2022, Shreiner & Guzdial, 2022, Sato et al., 2023, Fernandez-Nieto 
et al., 2021, Kang et al., 2020). For example, in Shreiner and Guzdial’s 
(2022) study, teachers critically analysed data visualisations to sup-
port students in learning data visualisations creation with a computer. 
Teachers discovered many diﬀerent ways in which data visualisation 
generated by computers can be misleading. Speciﬁcally, teachers felt 

--- Page 11 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
less conﬁdent in their own abilities to identify ﬂaws and inaccuracies in 
computer-generated data visualisations. In their further exploration, au-
thors reported teachers felt more conﬁdent creating data visualisations 
with paper and pencil over using computers. As a result, only a small 
number of the teachers who were supposed to use this system have ac-
tually incorporated them into their classrooms. Moreover, seven studies 
reported how stakeholders questioned the accuracy of the results from 
LA/AIED systems (i.e., Ahn et al., 2021, Zhou et al., 2021, Shreiner & 
Guzdial, 2022, Barreiros et al., 2023), speciﬁcally in addressing social 
needs to promote social learning development (i.e., Wang et al., 2022), 
emotional support needs (i.e., Liaqat et al., 2021), and stress (i.e., Al-
fredo et al., 2023). For instance, in a couple of studies (i.e., Ahn et al., 
2021, Zhou et al., 2021), study participants doubted whether the data 
they saw in the system’s interface reﬂected what occurred in the learn-
ing activity. An example from Kang et al.’s (2020) study addresses this 
unreliability issue by providing students with control to correct the mis-
takes made by AI (i.e., incorrectly assigned labels to an interface). At 
the same time, it promotes students’ agency over the tool to acknowl-
edge that the system can be unreliable and corrections may be needed 
during use.
Another topic was human bias (4%), which refers to systematic 
and unfair preferences inﬂuencing the outcomes, decisions, or interpre-
tations generated by systems (e.g. Fernandez-Nieto et al., 2022, Crain 
et al., 2022, Pozdniakov et al., 2022, Alfredo et al., 2023). Two stud-
ies highlighted the possibility of bias risk in LA/AIED systems due to 
the perceptions and preferences of users who have control over them 
(e.g. Fernandez-Nieto et al., 2022, Crain et al., 2022), arguing that ex-
cessive human control could lead to over-interpretation of data. The 
other three studies reported that insights formulated based on inaccu-
rate visual analytics might be prone to interpretive bias (Pozdniakov et 
al., 2022, Alfredo et al., 2023, Fernandez Nieto et al., 2022). We also 
gathered several discussions about human bias in the design process, 
as examined by four studies (4%). Two studies explicitly discussed the 
risk of bias in the HCD process (i.e., Vinella et al., 2022, Di Mitri et 
al., 2022). For instance, Vinella et al. (2022) noted that the monetary 
incentive given to participants when employing HCD techniques (e.g., 
crowdsourcing in this study) could stir and bias stakeholders from the 
study’s intended purpose. Participants who are more focused on imme-
diate rewards may not necessarily invest the necessary time and eﬀort 
to provide insights that contribute to the long-term reliability of the 
system. However, two studies discussed the importance of balancing 
researchers’ bias with stakeholders’ needs in the design process (i.e., 
Vannaprathip et al., 2022, Fernandez Nieto et al., 2022). For instance, 
Fernandez Nieto et al. (2022) highlighted that ‘end-users’ (teachers/stu-
dents) should be actively involved in design and evaluation processes to 
perceive their real needs in order to minimise researchers’ bias. When 
researchers or designers work in isolation, they may unintentionally 
introduce their own assumptions and biases into the system. Diverse 
perspectives are considered when involving end-users, leading to a bet-
ter alignment with challenges found in authentic educational settings 
that can be more reliable for end-users use.
Furthermore, another topic that emerged is related to the strategies 
to produce reliable data (5%). Three studies discussed how they en-
sured the reliability of the data from their studies (i.e., Martinez et al., 
2020, Lee et al., 2023, Ocumpaugh et al., 2017). For instance, Martinez 
et al. (2020) ensured the reliability of their results by applying criteria 
such as data security and conﬁdentiality in data collection, triangulating 
data from multiple sources, and reviewing the analysis process for each 
design phase. Two studies reported that the methodological reliability 
for involving stakeholders in the design process could be inﬂuenced by 
the quality of evaluations from stakeholders (i.e., Ahn et al., 2019, Zhou 
et al., 2021). For instance, Ahn et al. (2019) highlighted that method-
ological reliability from a study might be inﬂuenced by how well the 
involved stakeholders understand the system’s validity in an educational 
setting. Validity refers to how well the expectations of those involved 
match the intended purpose of the system, which promotes consistency 
and relevancy in evaluating the system to produce reliable data. More-
over, three studies addressed the issue of system validity, noting that 
while these systems may function eﬀectively in laboratory settings, their 
sustainability in real-world scenarios remains uncertain (i.e., Zhang et 
al., 2022, Gibson et al., 2017, Hu et al., 2022). They suggested the need 
for ecological validity (the extent to which the systems and ﬁndings from 
studies can be generalised and applied to authentic educational settings) 
by incorporating intended stakeholders’ perspectives to design a more 
reliable system.
4.4.3. Trustworthiness
Three emerging topics were identiﬁed in relation to the trustworthi-
ness principle, such as trust (14%), transparency (9%), and accountability
(3%) in LA/AIED systems.
Trust was discussed in several studies (14%). This concept was con-
textualised in how the stakeholders perceive trustworthiness when using 
or designing LA/AIED systems (e.g., Duan et al., 2023, Ngoon et al., 
2023, Fernandez-Nieto et al., 2022, Ekstrom & Pareto, 2022, Barreiros 
et al., 2023, Ooge et al., 2023). In terms of evaluating trust of such 
LA/AIED systems, we have mixed ﬁndings on stakeholders’ perceived 
sense of trust. Four studies reported that stakeholders trusted the out-
comes of AI or computer automation (i.e., Liaqat et al., 2021, Gibson 
et al., 2017, Khosravi et al., 2019, Ma et al., 2022). For instance, Li-
aqat et al. (2021) reported that learners trusted automated feedback 
more than peer feedback, and Ma et al. (2022) noted that teachers were 
inclined to trust the system when the displayed data matched their ex-
pectations. On the other hand, four studies reported stakeholders were 
less trusting of outcomes from automation (i.e., Nazaretsky, Cukurova 
et al., 2022, Wang et al., 2022, Ooge et al., 2023), especially when the 
systems utilised emotion or stress data (i.e., Alfredo et al., 2023). For in-
stance, Nazaretsky, Cukurova et al. (2022) reported that teachers were 
less trusting of the AI-powered system compared to receiving advice 
from peer teachers or experts. In another study, Alfredo et al. (2023)
reported teachers doubted the system’s ability to infer students’ phys-
iological states accurately due the inherent complexity in modelling 
aﬀective constructs. They suggested additional contextual information 
(e.g., explainable data) that could support making inferences and ex-
plaining this data back to students, especially if the intention is to use 
these systems in authentic settings. Interestingly, Ooge et al. (2023)
argued that plainly giving learners a mechanism to control a recom-
mender system, such as an ability to reveal the number and detail of 
recommendations during a learning activity, does not necessarily in-
crease their trust in using the system. Instead, the authors highlighted 
this kind of human control could promote awareness of the algorithm 
behind computer automation, encouraging learners to reﬂect on their 
actions which may foster long-term trust in the system. Together, these 
results provide important insights into further investigating the nuanced 
dynamics of trust between stakeholders and the system, which may vary 
depending on who the end-user is (e.g., teachers or students).
Moreover, four studies discussed several approaches to cultivate 
stakeholders’ trust in the system (i.e., Ahn et al., 2021, Wilson et al., 
2021, Suleman et al., 2016, Gibson et al., 2017). For instance, Wil-
son et al. (2021) reported that balancing the presented information’s 
accuracy with explainable information could foster learners’ trust in 
the system. The authors ensured that the system is available to pro-
vide output whenever a learner requests feedback, but the output may 
be less accurate. This drawback was balanced by providing learners 
with an explanation that is more connected to the intended pedagog-
ical component (i.e., formative feedback). It exempliﬁes an approach 
to improving trustworthiness when using human-centred LA/AIED sys-
tems by improving interpretability through explainability and system 
availability. Gibson et al. (2017) emphasised that stakeholders’ trust in 
LA systems can be developed through reciprocity, meaning there ex-
ist continuous design processes that involve active evaluation and the 
ability to inﬂuence the programming code inside the system. The study 

--- Page 12 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
highlights the importance of cultivating trust between stakeholders and 
systems to foster trust in using them in the authentic learning context.
Transparency (9%) was the second most discussed topic in the 
trustworthiness principle. Transparency refers to the clear and under-
standable way the system gathers and manages information to build 
trust among stakeholders who use or contribute to the LA/AIED sys-
tem’s design. Five studies discussed the transparency strategies that 
could foster trust, built around the user’s perceptions and control (i.e., 
Shute et al., 2021, Ahn et al., 2021, Khosravi et al., 2022, Suleman et 
al., 2016, Dollinger et al., 2019). Shute et al. (2021) highlighted the im-
portance of users’ perceptions and their signiﬁcant role in designing and 
testing the LA/AIED system impacting trust and engagement. Khosravi 
et al. (2019) reported that educating students on how their knowledge 
status is computed by AI and giving them access to the learning model 
(i.e., opening up the black-box AI models) could ultimately increase 
their trust and motivation to learn. Ahn et al. (2021) suggested that 
communicating the perception and intention of data use can foster trust 
through ongoing interpersonal interactions. Similarly, Dollinger et al. 
(2019) emphasised that transparent communication and clear research 
documentation are fundamental for building trust between stakehold-
ers and establishing trustworthiness. This ﬁnding highlights that trust 
and engagement in LA/AIED systems can be positively inﬂuenced when 
users perceive transparency in knowledge computation and transparent 
communication between stakeholders and researchers is encouraged.
The concept of accountability refers to individuals or systems be-
ing responsible for their decisions and the consequences of their actions. 
This is discussed in only four studies, taking a perspective from sys-
tem usage (i.e., Zhou et al., 2021, Duan et al., 2023, Lawrence et al., 
2023) and design (i.e., Gibson et al., 2017). The study by Zhou et al. 
(2021) sees accountability from a system usage perspective. For them, 
accountability is not just about the teachers overseeing the system; it 
also involves students taking responsibility for adjusting their learning 
strategies based on the feedback they receive from the AI-powered sys-
tem. This suggests that the accountability of the AI-powered system 
usage is not solely dependent on teachers but also on the students’ 
willingness to use the information provided by the system in their 
learning. The importance of accountable use of an AI-powered system 
is also investigated in Duan et al.’ (2023) study, where authors high-
lighted the need for trustworthy and transparent AI algorithms that 
align with the needs of stakeholders involvement in real educational 
settings. The authors recommended exploring explainable AI technolo-
gies capable of dynamically incorporating subject-matter experts’ (i.e., 
teachers’) contextual insights during the learning process for generating 
more accountable interventions aimed at helping students accomplish 
their learning goals. This kind of teachers’ interventions are discussed 
in Lawrence et al.’s (2023) study. Authors highlighted that teachers felt 
responsible for classroom orchestration decisions made with the assis-
tance of the AI-powered system, thus suggesting that teachers should 
be encouraged to trust their own judgement and decision-making abil-
ity over the AI. Teachers explained they tended to override the system’s 
recommendations with their own judgement, indicating teachers may 
still hesitate to trust and follow AI suggestions completely. This study 
may suggest that when teachers have control over the system, the con-
trol features force them to be responsible for the system’s eﬀectiveness 
since they are accountable for their decisions, which may give them an 
extra burden to use in practice.
In contrast, Gibson et al. (2017) deﬁne accountability from a de-
sign standpoint study. The expectation was for teachers to exhibit a 
higher level of accountability, implying that they should be more crit-
ical during the evaluation phase of the design process. However, it 
was observed that the teachers did not meet this expectation and their 
evaluations were not as critical as anticipated. This highlights a need 
to minimise assumptions about stakeholders’ accountability in the de-
sign process. In summary, eﬀective exploration of accountable usage 
in human-centred LA/AIED systems requires active participation from 
both teachers and students. However, the limited literature from a de-
sign perspective shows a gap in our understanding of the accountability 
of stakeholders when involved in the design process. Each study inter-
prets its meaning diﬀerently, primarily focusing on accountability in 
system usage.
5. Discussion
5.1. Current state of human-centred LA/AIED systems
The results from RQ1 indicate that a high number of university/col-
lege studies align with other LA/AIED reviews (Sarmiento & Wise, 
2022, Grani´c, 2022). Yet, there are still opportunities to explore human-
centred LA/AIED systems in supporting informal learning (e.g. Zhang 
et al., 2022, Head et al., 2014), as noted by Buckingham Shum et al. 
(2019). Moreover, the HCD techniques most commonly used in design-
ing human-centred LA/AIED systems that have considered stakeholders’ 
voices include interviews, co-design sessions, and prototype validation, 
with few studies using other techniques such as surveys, workshops, 
and personas. Despite traditional techniques (interviews and question-
naires) being helpful, this area requires more innovative HCD tech-
niques to leverage AI’s potential challenges and beneﬁts. For example, 
other techniques and methods that mimic human-AI interaction (i.e., 
Wizard of Oz (Vinella et al., 2022) or technology probes (Sato et al., 
2023)) could be helpful to investigate how users interact with systems 
features that require complex automation without the burden of full 
implementation (Lawrence et al., 2023, Echeverria et al., 2023). How-
ever, researchers should consider the trade-oﬀ between high-ﬁdelity 
interaction and resources needed, as these techniques and methods 
may require more resources and expertise than low-ﬁdelity prototypes 
(Muldner et al., 2013).
The lack of human-centred LA/AIED systems in Phase 1 (18%) and 
Phase 5 (9%) highlights a need for greater attention to the inception and 
monitoring phases. Engaging stakeholders at the earliest and latest de-
sign phase can provide valuable perspectives that ensure the designed 
system aligns with real-world learning needs and concerns (Bucking-
ham Shum et al., 2019) and becomes sustainable solutions (Yan et al., 
2022). A closer look at the planning, scoping, and deﬁnition design 
phase (Phase 1) indicates quantitative methodologies are scarce. Inte-
grating quantitative methodologies, such as surveys or crowdsourcing, 
could oﬀer an objective, systematic approach to gathering and inter-
preting data that could capture ideas at a large scale for subsequent 
design phases. For example, researchers can conduct surveys on end-
users (teachers/students) to assess potential risks or feasibility, which 
can be cost-eﬀective and scalable; otherwise, it may require more ef-
fort and resources when stakeholders are involved in subsequent design 
phases (Lang & Davis, 2023). Researchers may also consider analysing 
historical or public data to develop relevant AI-powered features or 
models depending on the research objectives (i.e., by following data-
driven design approaches, Gorkovenko et al., 2020). Moreover, the 
limited literature in the launch and monitoring design phase (Phase 5) 
could suggest a gap in reporting practices about LA/AIED systems post-
deployment in authentic learning environments (Martinez-Maldonado, 
2023) or a lack of longitudinal studies that manage to deploy human-
centred LA/AIED systems sustainably.
Therefore, evidenced by our ﬁndings, we recommend:
• Research Scope: Expand human-centred LA/AIED research be-
yond the university and K-12 levels to include vocational educa-
tion, workplace training, and informal learning.
• Inception & Deployment Phases: Pay greater attention to Phases 
1 and 5 of the design process to balance stakeholder involvement, 
pedagogical focus, and research objectives at both inception (phase 
1) and monitoring (phase 5) stages.
• Quantitative Approaches: Employ quantitative methods in the 
planning phase to help reach stakeholder consensus and be 
resource-eﬀective. Consider large-scale surveys, crowdsourcing, 

--- Page 13 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
quantiﬁed risk analysis, or leveraging public datasets on AI-
powered features.
• In-the-Wild Studies: Report more in-the-wild studies during Phase 
5 to understand the impact of human-centred LA/AIED systems on 
teaching or learning experiences in real-world practices. Combine 
this with existing human-centred approaches and design method-
ologies (e.g., design-based research by Reimann, 2016).
• Innovative HCD Techniques: Use innovative HCD techniques be-
yond interviews and questionnaires to leverage AI’s potential chal-
lenges and beneﬁts. Consider techniques that mimic human-AI in-
teraction, such as Wizard of Oz.
5.2. Stakeholder involvement in design phases
Regarding RQ2, lower active stakeholder involvement in evaluat-
ing and reﬁning human-centred LA/AIED systems can overlook design 
ﬂaws that may persist in authentic educational scenarios (see Phase 
4). Including their voices in the reﬁnement process, such as conduct-
ing post-hoc reﬂection interviews to capture their experiences for us-
ing a system after pilot studies (Martinez-Maldonado et al., 2015), 
can provide an opportunity for end-users to reﬂect and re-align sys-
tems’ features with their values, preferences, and needs (Chen & Zhu, 
2019) before the system is ﬁnalised and deployed in real-world set-
tings. This active stakeholder involvement should be considered in all 
design phases, which have currently been considered in Phases 1, 2, 
3, and 5. Incorporating a “human-in-the-loop” practice in all design 
phases can be an approach to tap into education stakeholders’ expertise, 
ensuring a nuanced grasp of context, end-user needs, and ethical con-
siderations (Duan et al., 2023). Allowing end-users to share their voices 
can also foster a sense of ownership, which aligns with the main goal of 
human-centred LA/AIED systems to empower end-users (Usmani et al., 
2023, Barreiros et al., 2023). Ultimately, this active involvement will 
foster adaptive and human-centric designs that align more eﬀectively 
with real-world complexities and requirements (Buckingham Shum et 
al., 2019, Martinez-Maldonado, 2023). Indeed, it is crucial to acknowl-
edge that a balanced combination of HCD techniques and design phases 
for involving stakeholders in educational settings, such as availabili-
ties, policies, and resources, remains an open question that requires 
further exploration. Considering these beneﬁts, this ﬁnding highlights 
the need for stakeholder involvement in all design phases of human-
centred LA/AIED systems to co-create systems that can meet real-world 
educational needs (Dollinger et al., 2019).
The extent of stakeholder involvement indicates that students and 
teachers play a pivotal role in the design process as the most frequently 
engaged stakeholders (see Fig. 4). Despite students having the highest 
representation in the overall participant count (71%), the data high-
lighted their active involvement in the design process was relatively 
low (19%). Teachers may have expertise and pedagogy knowledge (e.g., 
how students learn, eﬀective instructional strategies, and a supportive 
learning environment). In contrast, students may be just consumers of 
these systems or partake in another role in the design, such as being 
observed when exploring the system or participating in experiments 
to test the newly developed system without giving input or voice to 
the design. It could be caused by several challenges, such as com-
munication, students’ narrowed perspectives or knowledge, monetary 
incentives (Vinella et al., 2022) and privacy concerns, especially in K-12 
education (Bond et al., 2023, see Section 4.4). This may lead to a heavy 
reliance on teachers and other experts, which invites further investiga-
tion. Same teachers or experts may be more available to contribute to 
the design process from the beginning until the end of the project than 
students, which commonly occurs in the longitudinal study (e.g., Hutt 
et al., 2021).
The challenges above show that students’ contributions tend to oc-
cur as one time-oﬀ and sporadic (happening occasionally and inconsis-
tently). These uncertainties signal a need for a more inclusive approach 
to the design process due to the underutilisation of students’ expertise 
and voices in the design process of human-centred LA/AIED systems. 
To break this pattern, eﬀorts should focus on recognising the value 
of students’ unique insights (Dollinger et al., 2019), empowering them 
through agency (Hooshyar et al., 2023), and addressing communication 
problems, such as by clearly stating the research outcomes and bene-
ﬁts of participating in the design activities (Slade & Prinsloo, 2013). It 
is also essential to encourage collaboration among students, teachers, 
researchers, and other stakeholders (e.g., developers, designers, and 
administrators) while establishing transparent communication about 
the purpose and beneﬁts of student involvement (Martinez-Maldonado, 
2023). This multifaceted approach aims to collaboratively create a more 
inclusive and eﬀective system (Dollinger et al., 2019).
Overall, we found a gap in which students’ active involvement is 
still limited, implying students can be considered as underrepresented 
stakeholders (Martinez-Maldonado, 2023). Martinez-Maldonado rec-
ommended building robust relationships with these underrepresented 
stakeholders, oﬀering compensation for their time in contributing to 
design activities and employing inclusive design toolkits that promote 
inclusivity and diversity. It urges researchers to be more proactive in 
including students’ voices because their learning experiences will be 
the most impacted by these technologies (Kitto et al., 2018). We fur-
ther argue that ensuring meaningful student engagement in the design 
process can enhance the relevance and eﬀectiveness of adopting human-
centred LA/AIED systems, promoting a more student-centred approach 
(de Quincey et al., 2019).
Therefore, we recommend:
• Active Stakeholder Involvement: Employ co-creation practices 
such as co-design, participatory design, and value-sensitive design. 
Emphasise active collaboration in all design phases and the cen-
tral role of end-users and directly aﬀected stakeholders (including 
students) in shaping outcomes.
• End-User Needs and Preferences: Ensure the system’s outcomes 
meet the needs and preferences of the end-users, particularly teach-
ers and students.
• Student Involvement: Address students’ passive involvement in 
the design process. Recognise that human-centred LA/AIED sys-
tems can signiﬁcantly impact students’ learning experiences and 
outcomes.
• Clear Communication: Ensure all stakeholders are well-informed 
about the beneﬁts and challenges of involving students in the de-
sign process.
5.3. Human control and computer automation
Regarding RQ3, by employing the two-dimensional HCAI frame-
work (Shneiderman, 2022) as an analysis lens, the current SLR revealed 
that current human-centred LA/AIED systems have already prioritised 
human control with a signiﬁcant percentage falling in this category 
(Q2=32% and Q4=47%). Human control is prioritised so students and 
teachers can be responsible for their learning and teaching practices. 
With AI-powered systems’ help and high human control (Q4), students 
can have personalised learning experiences, and teachers can provide 
guidance and support (Dogan et al., 2023). This ﬁnding also indicates 
the need for further exploration of frameworks for collaboration be-
tween humans and AI in the LA/AIED systems (Holstein et al., 2020). 
This approach stands in line with the objectives of HCAI (Shneiderman, 
2020b, Usmani et al., 2023, Renz & Vladova, 2021).
Regarding stakeholder involvement in the HCAI framework, no-
tably, Q3 (low human control and high computer automation) has 
shown more passive stakeholder involvement (6%). The possible rea-
son for this passive involvement, as highlighted by Nazaretsky, Ariely 
et al. (2022), could be a lack of technical expertise among the stake-
holders. Systems in Q3 often have simpler interfaces, resulting in lower 

--- Page 14 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
human control but it can be more complex behind the interface. It may 
require a certain understanding of technical knowledge, such as com-
puter science or AI literacy, to understand its automation. If teachers 
and students lack this expertise, they might ﬁnd it challenging to pro-
vide meaningful input in the design process, resulting in them taking 
a more passive role. Yet, stakeholders’ involvement should not only be 
considered for human-centred LA/AIED systems that oﬀer some sort 
of end-user interface but also in the design of systems that fully au-
tomate educational actions. For systems with low human control and 
high computer automation, it is important to ensure they are transpar-
ent, trustworthy, and user-friendly, as explored in (Duan et al., 2023)’s 
study (Q4) to balance it with giving more human control. Another ex-
ample is a Zoom Sense system with high computer automation in Zhou 
et al.’s (2021) and Pozdniakov et al.’s (2022) studies. Initially, Pozd-
niakov et al.’s (2022) study focused on computer automation with AI 
but had limited control (Q3). It was later updated by creating a query-
driven dashboard that allows teachers to control the online classroom 
in Pozdniakov et al. (2022)’s study (Q4).
Nonetheless, we also found that systems in quadrant Q2 had more 
passive stakeholder involvement (19%). Since systems in Q2 are in-
tended to provide an end-user interface that allows teachers or students 
to take control and make meaningful decisions about their teaching 
or learning process, it can be seen as short-sighted to neglect active 
stakeholder involvement just because AI or computer automation is un-
available. Buckingham Shum and Luckin (2019) and Dollinger et al. 
(2019) argued that designing human-centred LA/AIED systems requires 
a well-thought-out stakeholder engagement strategy that considers the 
diverse needs and values regardless of their level of computer automa-
tion.
In intelligent tutoring systems, the control is usually given to end-
users to a limited extent since these systems commonly provide a set 
of problems to students, adapting to their prior and current knowledge 
(Lawrence et al., 2023, Schulz et al., 2022). While teachers often do not 
have control to choose problems for students, they are likely to take ac-
tion based on those problems, such as providing additional instruction, 
oﬀering feedback, or adjusting the course material in response to the 
problems and how students are handling them (Holstein et al., 2019). 
Hence, it could be that the system’s control may often be attributed to 
teachers rather than students. This requires further exploration to de-
termine how much the teacher’s agency has been balanced with the 
student’s agency (Echeverria et al., 2023, Lawrence et al., 2023). Over-
all, most existing human-centred LA/AIED systems have been designed 
with a high degree of human control, as indicated by the larger pro-
portion of systems categorised into Q2 or Q4. It further suggests that 
these systems are already designed to empower end-users, supported 
by human oversight. This aligns with the notion of striking a balance 
between human control and computer automation, as too much of ei-
ther can lead to users being overwhelmed with options to control or 
mistrust since it may operate in a ‘black-box’ manner, respectively (Oz-
men Garibay et al., 2023).
Therefore, we recommend:
• Deﬁne End-Users: Clearly deﬁne the intended end-users to avoid 
ambiguity in agency between teachers and students in highly au-
tomated systems. Develop distinct interfaces for teachers and stu-
dents to enhance system usability and eﬀectiveness.
• Involve Stakeholders: Actively engage stakeholders in the devel-
opment process regardless of the system’s level of automation or 
AI. Consider the inﬂuence of stakeholders’ technical expertise on 
their preference for human control and computer automation.
• Maintain Control: In high computer automation systems (Q3 and 
Q4), allow teachers and students to adjust system parameters to 
suit dynamic changes in use. This ensures system ﬂexibility and 
adaptability according to the changing dynamics of the classrooms 
or learning environments.
• HCAI Framework as a Design Tool: Utilise the HCAI two-
dimensional framework as a design tool to assess and balance 
features that oﬀer human control and computer automation in the 
system (update sequentially from Q1 to Q4), empowering end-users 
and supporting self-eﬃcacy.
5.4. Exploring safety, reliability, and trustworthiness in human-centred 
LA/AIED systems
Lastly, regarding RQ4, we summarised how researchers address 
safety, reliability, and trustworthiness principles in human-centred 
LA/AIED systems. Finding reveals that reliability (37%) emerges as the 
most prominent principle, closely followed by safety (35%), with trust-
worthiness trailing at 25%. This distribution of principles is reﬂected in 
the design and evaluation of human-centred LA/AIED systems. While 
these principles are addressed to a certain degree, our review under-
scores the need for more robust evidence and methodological mecha-
nisms to thoroughly understand and evaluate them. This is particularly 
true for trustworthiness, which is less represented in the current re-
search. However, the importance of trustworthiness in the context of 
LA/AIED systems cannot be overstated. As highlighted by Shneiderman 
(2020b), the perceived trustworthiness of our systems can directly im-
pact their adoption in real-world practices. If end-users (i.e., teachers 
or students) deem these smart systems untrustworthy, it could sig-
niﬁcantly hinder their widespread acceptance and use. Investigating 
further on trustworthiness, interestingly, we identiﬁed various perspec-
tives on accountability; on one hand, there are several discussions about 
the accountability of teachers and students when using the system (i.e., 
Zhou et al., 2021, Duan et al., 2023, Lawrence et al., 2023), and on the 
other hand, one study refers to the accountability of teachers in provid-
ing design inputs during system evaluation to be trusted stakeholders. 
These ﬁndings underscore the complexity of accountability in the con-
text of human-centred LA/AIED systems (i.e., Gibson et al., 2017). It is 
a shared responsibility involving teachers, students, and the system it-
self. Each plays a crucial role in ensuring the system’s eﬀectiveness and 
in building trust among stakeholders. It extends beyond the traditional 
notion of individuals or systems being responsible for their actions and 
their consequences in use. Further investigation is required as this in-
sight could have signiﬁcant implications for the design of AI-powered 
systems in education.
From our ﬁndings, the principles of safety, reliability, and trustwor-
thiness are not isolated; rather, they are interconnected and mutually 
reinforcing in the context of human-centred LA/AIED systems. Safety is 
a fundamental aspect that can signiﬁcantly contribute to building trust. 
When users, especially students, feel that their data is protected and that 
the system operates within safe parameters, their trust in the system will 
likely increase (Drachsler & Greller, 2016). It can empower users by giv-
ing them the conﬁdence to use the system without fear of data breaches 
or misuse. For instance, robust data privacy measures (e.g., Kivimäki 
et al., 2019, Ngoon et al., 2023) and transparent data collection proce-
dures (e.g., Conijn, Martinez-Maldonado et al., 2020, Wang et al., 2022) 
can enhance the perceived safety of the system, thereby fostering trust 
among users. Reliability, on the other hand, refers to the consistent 
performance of the system. Interestingly, a system that is reliable and 
consistent, even if less accurate, can often be perceived as more trust-
worthy (Duan et al., 2023). It may happen because users (i.e., teachers) 
can predict the system’s behaviour and adjust their expectations accord-
ingly, increasing trust. This reliable system is important in empowering 
users by providing consistent and predictable results, enabling them to 
make informed decisions. Moreover, trustworthiness is closely linked to 
both safety and reliability. A system that consistently protects user data 
(safety) and performs as expected (reliability) is likely to be deemed 
trustworthy. A trustworthy system empowers users by fostering conﬁ-
dence in the system’s outputs, which in turn encourages its adoption 
and use (Khosravi et al., 2022).

--- Page 15 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
In conclusion, these principles are intertwined, and improvements 
in one area can positively impact the others (Ozmen Garibay et al., 
2023, Shneiderman, 2020b). The interconnected principles of safety, 
reliability, and trustworthiness, coupled with a balance of human con-
trol and computer automation, can signiﬁcantly empower stakeholders 
in the context of human-centred LA/AIED systems. Therefore, future 
research and development eﬀorts should enhance these principles col-
lectively to foster user trust and promote the acceptance and eﬀec-
tiveness of human-centred LA/AIED systems in real-world practices, 
accompanied by the aforementioned HCD practices above. Notably, be-
yond stakeholders’ perspectives, we could not ﬁnd studies exploring 
external mechanisms to ensure a human-centred LA/AIED system is 
safe, trustworthy or reliable. These mechanisms can involve, for ex-
ample, subjecting the systems to independent audits and assessments 
by third parties to verify their actual trustworthiness, to move beyond 
perceived trust, or ensure adherence to relevant legal and regulatory 
requirements, as well as industry standards (Shneiderman, 2020b).
Therefore, we recommend:
• Safety Procedures: Report safety procedures, including risk assess-
ment, stakeholders’ perspectives, and informed consent procedures.
• Data Privacy: Ensure data privacy of stakeholders when involving 
them in the design process. Include secure data storage procedures 
and risk assessments for safety in the educational environment.
• Reliability & Collaboration: Foster collaboration with end-users 
and employ system explainability. Educate end-users on system 
capabilities and limitations to improve privacy awareness and ef-
fective technology use.
• Trustworthiness: Report stakeholders’ trust perceptions, ensure 
transparency of data outcomes and algorithms, and measure trust-
worthiness using human control and computer automation dimen-
sions.
• Accountability: Explore stakeholder accountability in the design 
process, focusing on how teachers or students can be held account-
able for their inputs in human-centred LA/AIED systems.
5.5. Limitations
This SLR is subject to limitations that should be considered in inter-
preting results and discussions. First, despite the comprehensive search 
strategy employed, there is always a possibility of missing relevant stud-
ies due to limitations in the search terms, databases searched, or the 
exclusion of grey literature (e.g., unpublished works) and groundbreak-
ing results in short articles or posters. Although we took many studies to 
reduce bias, it is possible that the study selection process could be inﬂu-
enced by the reviewers’ judgement or subjective criteria, which could 
introduce some selection bias. However, this is a known possibility and 
has been addressed through transparency and open communication be-
tween researchers. We further acknowledge that LA and AIED come 
from two diﬀerent research communities and potentially diﬀerent ways 
of reporting their research (Rienties et al., 2020). Nonetheless, we found 
a clear overlap between these two communities. This SLR attempted 
to comprehensively view these overlaps through a human-centred per-
spective, allowing future work to explore and advance this avenue.
6. Concluding remarks
The ﬁndings of this SLR indicate a growing interest in human-
centred LA/AIED research. The review highlights the importance of 
safety, reliability, and trustworthiness in the design and implementa-
tion of these data-intensive systems, as well as the need for transparent, 
eﬀective communication and user control. The review also identiﬁes 
gaps in the existing research and methodological challenges that need 
to be addressed for human-centred LA/AIED to remain relevant and po-
tentially become part of mainstream practices in the foreseeable future. 
Overall, this review provides valuable insights into the current state of 
Table 1
Acronyms used in this paper.
Acronym
Description
AI
Artiﬁcial Intelligence
AIED
Artiﬁcial Intelligence in Education
HCAI
Human-centred Artiﬁcial Intelligence
HCD
Human-centred Design
HCLA
Human-centred Learning Analytics
LA
Learning Analytics
LA/AIED
Learning Analytics and AI in Education
PRISMA
Preferred Reporting Items for Systematic Reviews and Meta-Analyses
Q1,Q2,Q3,Q4
Quadrant 1,2,3 and 4 in two-dimensional HCAI framework
R1, R2, R3
Researcher 1, 2 and 3
SLR
Systematic Literature Review
human-centredness in LA/AIED studies with support HCAI framework 
as a lens, and underscores the importance of ongoing research and de-
velopment. (See Table 1.)
Ethics
This review does not involve any human participants. This review 
followed the PRISMA guidelines for transparency and comprehensive 
reporting and respected all copyrights and intellectual property rights 
associated with the studies.
CRedi T authorship contribution statement
Riordan Alfredo: Writing – review & editing, Writing – origi-
nal draft, Visualization, Resources, Project administration, Methodol-
ogy, Investigation, Formal analysis, Data curation, Conceptualization.
Vanessa Echeverria: Writing – review & editing, Validation, Supervi-
sion, Investigation, Formal analysis, Data curation, Conceptualization.
Yueqiao Jin: Validation, Investigation, Formal analysis, Conceptual-
ization. Lixiang Yan: Visualization, Resources, Methodology. Zachari 
Swiecki: Writing – review & editing, Supervision, Conceptualization.
Dragan Gaševi´c: Writing – review & editing, Supervision, Funding ac-
quisition, Conceptualization. Roberto Martinez-Maldonado: Writing 
– review & editing, Writing – original draft, Validation, Supervision, 
Methodology, Conceptualization.
Declaration of competing interest
The authors declare that they have no known competing ﬁnancial 
interests or personal relationships that could have appeared to inﬂuence 
the work reported in this paper.
Data availability
The data from this review is accessible to all interested parties 
upon reasonable request while respecting the privacy and conﬁdential-
ity agreements of the original studies.
Acknowledgement
Riordan Alfredo gratefully acknowledges Monash University for his 
Ph D scholarship. This research was funded partially by the Australian 
Government through the Australian Research Council (project number 
DP210100060, DP220101209, DP240100069), Jacobs Foundation (Re-
search Fellowship and Centre for Learning and Leaving with AI), and 
Digital Health Cooperative Research Centre.
Appendix A. HCAI two-dimensional quadrants in LA/AIED 
references

--- Page 16 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
Table 2
A comprehensive reference list of included articles in the two-dimensional HCAI framework quadrants (Q1–Q4).
No.
Quadrant
Reference

Q2
Ahn, J., Campos, F., Hays, M., & Digiacomo, D. (2019). Designing in context: Reaching beyond usability in learning analytics dashboard design. Journal of 
Learning Analytics, 6(2), 70–85. https://doi .org /10 .18608 /jla .2019 .62 .5

Q2
Al-Doulat, A., Nur, N., Karduni, A., Benedict, A., Al-Hossami, E., Maher, M. L., Dou, W., Dorodchi, M., & Niu, X. (2020). Making Sense of Student Success and 
Risk Through Unsupervised Machine Learning and Interactive Storytelling. In Artiﬁcial Intelligence in Education (Vol. 12163, pp. 3–15). Springer 
International Publishing. http://link .springer .com /10 .1007 /978 -3 -030 -52237 -7 _1

Q4
Albó, L., Barria-Pineda, J., Brusilovsky, P., & Hernández-Leo, D. (2022). Knowledge-Based Design Analytics for Authoring Courses with Smart Learning 
Content. Int. J. Artif. Intell. Educ., 32(1), 4–27. https://doi .org /10 .1007 /s40593 -021 -00253 -3

Q4
Aleven, V., Blankestijn, J., Lawrence, L., Nagashima, T., & Taatgen, N. (2022). A Dashboard to Support Teachers During Students’ Self-paced AI-Supported 
Problem-Solving Practice. 16–30.

Q4
Alfredo, R. D., Nie, L., Kennedy, P., Power, T., Hayes, C., Chen, H., Mc Gregor, C., Swiecki, Z., Gaševi´c, D., & Martinez-Maldonado, R. (2023). “That Student 
Should Be a Lion Tamer!” Stress Viz: Designing a stress analytics dashboard for teachers. LAK23: 13th International Learning Analytics and Knowledge 
Conference, 57–67. https://doi .org /10 .1145 /3576050 .3576058

Q3
Assim, M., Al-Bahri, H., Zafar, Q., Shahada, M., & Al-Ammary, J. (2021). Remote Teaching during COVID-19 pandemic in Higher Education Institutions in the 
Kingdom of Bahrain: Challenges and Innovative Solutions. 2021-January. https://doi .org /10 .1109 /SLAE54202 .2021 .9788084

Q2
Barreiros, C., Leitner, P., Ebner, M., Veas, E., & Lindstaedt, S. (2023). Students in Focus – Moving Towards Human-Centred Learning Analytics. In O. Viberg & 
Å. Grönlund (Eds.), Practicable Learning Analytics (pp. 77–94). Springer International Publishing. https://doi .org /10 .1007 /978 -3 -031 -27646 -0 _5

Q1
Bishop, E., Allington, D., Ringrose, T., Martin, C., Aldea, A., Garcia-Jaramillo, M., Leon-Vargas, F., Leal, Y., Henao, D., & Gomez, A. M. (2022). Design and 
Usability of an Avatar-Based Learning Program to Support Diabetes Education: Quality Improvement Study in Colombia. Journal of Diabetes Science and 
Technology, 19322968221136140–19322968221136140. https://doi .org /10 .1177 /19322968221136141

Q1
Boateng, S., Alex, J. K., Adelabu, F. M., Sihele, T., & Momoti, V. (2022). Pre-Service Teachers’ Perspectives towards the Use of Gamma Tutor in Teaching 
Physical Sciences in South African Secondary Schools. International Journal of Learning, Teaching and Educational Research, 21(6), 304–323. https://
doi .org /10 .26803 /ijlter .21 .6 .18

Q4
Bonnat, C., & Sanchez, E. (2022). Toward a Digital Companion to Monitor a Mixed Reality Game. International Journal of Serious Games, 9(3), 5–21. https://
doi .org /10 .17083 /ijsg .v9i3 .504

Q4
Borjigin, A., Miao, C., Lim, S. F., Li, S., & Shen, Z. (2015). Teachable Agents with Intrinsic Motivation. In Artiﬁcial Intelligence in Education (Vol. 9112, pp. 
34–43). Springer International Publishing. http://link .springer .com /10 .1007 /978 -3 -319 -19773 -9 _4

Q2
Camara Olim, S. M., Nisi, V., & Rubegni, E. (2023). “Periodic fable discovery” using tangible interactions and augmented reality to promote STEM subjects. 
Proceedings of the Seventeenth International Conference on Tangible, Embedded, and Embodied Interaction. https://doi .org /10 .1145 /3569009 .3572804

Q1
Challco, G. C., Bittencourt, I. I., & Isotani, S. (2020). Can Ontologies Support the Gamiﬁcation of Scripted Collaborative Learning Sessions? In Artiﬁcial 
Intelligence in Education (Vol. 12163, pp. 79–91). Springer International Publishing. http://link .springer .com /10 .1007 /978 -3 -030 -52237 -7 _7

Q4
Chang, H.-T., Lin, C.-Y., Jheng, W.-B., Chen, S.-H., Wu, H.-H., Tseng, F.-C., & Wang, L.-C. (2023). AI, Please Help Me Choose a Course: Building a Personalized 
Hybrid Course Recommendation System to Assist Students in Choosing Courses Adaptively. EDUCATIONAL TECHNOLOGY & SOCIETY, 26(1), 203–217. 
https://doi .org /10 .30191 /ETS .202301 _26(1 ).0015

Q2
Chatti, M. A., Muslim, A., Guesmi, M., Richtscheid, F., Nasimi, D., Shahin, A., & Damera, R. (2020). How to design eﬀective learning analytics indicators? A 
human-centered design approach. In Lecture Notes in Computer Science (including subseries Lecture Notes in Artiﬁcial Intelligence and Lecture Notes in 
Bioinformatics): Vol. 12315 LNCS (p. 317). https://doi .org /10 .1007 /978 -3 -030 -57717 -9 _22

Q4
Chavan, P., & Mitra, R. (2022). Tcherly: A Teacher-Facing Dashboard for Online Video Lectures. J. Learn. Anal., 9(3), 125–151. https://
doi .org /10 .18608 /jla .2022 .7555

Q4
Conijn, R., Martinez-Maldonado, R., Knight, S., Shum, S., Van Waes, L., & van Zaanen, M. (2022). How to provide automated feedback on the writing process? 
A participatory approach to design writing analytics tools. COMPUTER ASSISTED LANGUAGE LEARNING. https://doi .org /10 .1080 /09588221 .2020 .1839503

Q4
Conijn, R., Van Waes, L., & van Zaanen, M. (2020). Human-centered design of a dashboard on students’ revisions during writing. In Lecture Notes in Computer 
Science (including subseries Lecture Notes in Artiﬁcial Intelligence and Lecture Notes in Bioinformatics): Vol. 12315 LNCS (p. 44). https://
doi .org /10 .1007 /978 -3 -030 -57717 -9 _3

Q2
Crain, P., Lee, J., Yen, Y.-C. (Grace), Kim, J., Aiello, A., & Bailey, B. (2022). Visualizing topics and opinions helps students interpret large collections of peer 
feedback for creative projects. ACM Trans. Comput.-Hum. Interact. https://doi .org /10 .1145 /3571817

Q2
Cukurova, M., Mavrikis, M., Luckin, R., Clark, J., & Crawford, C. (2017). Interaction Analysis in Online Maths Human Tutoring: The Case of Third Space 
Learning. In Artiﬁcial Intelligence in Education (Vol. 10331, pp. 636–643). Springer International Publishing. http://
link .springer .com /10 .1007 /978 -3 -319 -61425 -0 _80

Q4
de Quincey, E., Briggs, C., Kyriacou, T., & Waller, R. (2019). Student Centred Design of a Learning Analytics System. 353–362. https://
doi .org /10 .1145 /3303772 .3303793

Q2
De Silva, L. M. H., Chounta, I.-A., Rodríguez-Triana, M. J., Roa, E. R., Gramberg, A., & Valk, A. (2022). Toward an Institutional Analytics Agenda for 
Addressing Student Dropout in Higher Education: An Academic Stakeholders’ Perspective. J. Learn. Anal., 9(2), 179–201. https://
doi .org /10 .18608 /jla .2022 .7507

Q4
Di Mitri, D., Schneider, J., & Drachsler, H. (2022). Keep Me in the Loop: Real-Time Feedback with Multimodal Data. Int J Artif Intell Educ, 32(4), 1093–1118. 
https://doi .org /10 .1007 /s40593 -021 -00281 -z

Q4
Dollinger, M., Liu, D., Arthars, N., & Lodge, J. M. (2019). Working together in learning analytics towards the co-creation of value. Journal of Learning 
Analytics, 6(2), 10–26. https://doi .org /10 .18608 /jla .2019 .62 .2

Q4
Duan, X., Pei, B., Ambrose, G. A., Hershkovitz, A., Cheng, Y., & Wang, C. (2023). Towards transparent and trustworthy prediction of student learning 
achievement by including instructors as co-designers: A case study. EDUCATION AND INFORMATION TECHNOLOGIES. https://
doi .org /10 .1007 /s10639 -023 -11954 -8

Q2
Easterday, M. W., Rees Lewis, D., & Gerber, E. M. (2017). Designing Crowdcritique Systems for Formative Feedback. Int. J. Artif. Intell. Educ., 27(3), 623–663. 
https://doi .org /10 .1007 /s40593 -016 -0125 -9

Q1
Echeverria, V., Martinez-Maldonado, R., & Buckingham Shum, S. (2019). Towards collaboration translucence: Giving meaning to multimodal group data. 
Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems, 1–16. https://doi .org /10 .1145 /3290605 .3300269

Q3
Ekstrom, S., & Pareto, L. (2022). The dual role of humanoid robots in education: As didactic tools and social actors. EDUCATION AND INFORMATION 
TECHNOLOGIES. https://doi .org /10 .1007 /s10639 -022 -11132 -2

Q1
Eradze, M., Rodríguez-Triana, M. J., Milikic, N., Laanpere, M., & Tammets, K. (2020). Contextualising Learning Analytics with Classroom Observations: A Case 
Study. Interaction Design and Architecture(s), 44, 71–95.

Q1
Fernandez Nieto, G. M., Kitto, K., Buckingham Shum, S., & Martinez-Maldonado, R. (2022). Beyond the Learning Analytics Dashboard: Alternative Ways to 
Communicate Student Data Insights Combining Visualisation, Narrative and Storytelling. 219–229. https://doi .org /10 .1145 /3506860 .3506895

Q2
Fernandez-Nieto, G., An, P., Zhao, J., Buckingham Shum, S., & Martinez-Maldonado, R. (2022). Classroom Dandelions: Visualising Participant Position, 
Trajectory and Body Orientation Augments Teachers’ Sensemaking. 1–17. https://doi .org /10 .1145 /3491102 .3517736

Q4
Fernandez-Nieto, G. M., Martinez-Maldonado, R., Kitto, K., & Buckingham Shum, S. (2021). Modelling Spatial Behaviours in Clinical Team Simulations using 
Epistemic Network Analysis: Methodology and Teacher Evaluation. 386–396. https://doi .org /10 .1145 /3448139 .3448176

--- Page 17 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
Table 2 (continued)
No.
Quadrant
Reference

Q1
Garcia-Ruiz, M., Santana-Mancilla, P. C., Gaytan-Lugo, L. S., & Iniguez-Carrillo, A. (2022). Participatory Design of Soniﬁcation Development for Learning 
about Molecular Structures in Virtual Reality. Multimodal Technologies and Interaction, 6(10). https://doi .org /10 .3390 /mti6100089

Q4
Gerdes, A., Heeren, B., Jeuring, J., & van Binsbergen, L. T. (2017). Ask-Elle: An Adaptable Programming Tutor for Haskell Giving Automated Feedback. Int. J. 
Artif. Intell. Educ., 27(1), 65–100. https://doi .org /10 .1007 /s40593 -015 -0080 -x

Q4
Gibson, A., Aitken, A., Sándor, Á., Buckingham Shum, S., Tsingos-Lucas, C., & Knight, S. (2017). Reﬂective Writing Analytics for Actionable Feedback. 
153–162. https://doi .org /10 .1145 /3027385 .3027436

Q4
Han, S., Liu, M., Pan, Z., Cai, Y., & Shao, P. (2022). Making FAQ Chatbots More Inclusive: An Examination of Non-Native English Users’ Interactions with New 
Technology in Massive Open Online Courses. Int. J. Artif. Intell. Educ. https://doi .org /10 .1007 /s40593 -022 -00311 -4

Q4
Head, A., Xu, Y., & Wang, J. (2014). Tone Wars: Connecting Language Learners and Native Speakers through Collaborative Mobile Games. In Intelligent 
Tutoring Systems (Vol. 8474, pp. 368–377). Springer International Publishing. http://link .springer .com /10 .1007 /978 -3 -319 -07221 -0 _46

Q4
Holstein, K., Mc Laren, B. M., & Aleven, V. (2019). Co-Designing a Real-Time Classroom Orchestration Tool to Support Teacher-AI Complementarity. Journal of 
Learning Analytics, 6(2), 27_52.

Q2
Hosseini, R., Akhuseyinoglu, K., Brusilovsky, P., Malmi, L., Pollari-Malmi, K., Schunn, C., & Sirkiä, T. (2020). Improving Engagement in Program Construction 
Examples for Learning Python Programming. Int. J. Artif. Intell. Educ., 30(2), 299–336. https://doi .org /10 .1007 /s40593 -020 -00197 -0

Q2
Hu, L., Wu, J., & Chen, G. (2022). i Talk–i See: A participatory visual learning analytical tool for productive peer talk. International Journal of 
Computer-Supported Collaborative Learning, 17(3), 397–425. https://doi .org /10 .1007 /s11412 -022 -09374 -w

Q4
Hutchins, N., & Biswas, G. (2023). Using Teacher Dashboards to Customize Lesson Plans for a Problem-Based, Middle School STEM Curriculum. 324–332. 
https://doi .org /10 .1145 /3576050 .3576100

Q3
Hutt, S., Krasich, K., Brockmole, J., & D’Mello, S. (2021). Breaking out of the Lab: Mitigating Mind Wandering with Gaze-Based Attention-Aware Technology 
in Classrooms (WOS:000758168003023). CHI ‘21: PROCEEDINGS OF THE 2021 CHI CONFERENCE ON HUMAN FACTORS IN COMPUTING SYSTEMS. 
https://doi .org /10 .1145 /3411764 .3445269

Q2
Jeong, Y., Cho, H., Kim, T., & Nam, T.-J. (2023). Automata Stage: An AR-Mediated creativity support tool for hands-on multidisciplinary learning. Proceedings 
of the 2023 CHI Conference on Human Factors in Computing Systems. https://doi .org /10 .1145 /3544548 .3581408

Q4
Kaliisa, R., Kluge, A., & Mørch, A. I. (2020). Combining checkpoint and process learning analytics to support learning design decisions in blended learning 
environments. J. Learn. Anal., 7(3), 33–47. https://doi .org /10 .18608 /JLA .2020 .73 .4

Q4
Kang, S., Shokeen, E., Byrne, V., Norooz, L., Bonsignore, E., Williams-Pierce, C., & Froehlich, J. (2020). ARMath: Augmenting Everyday Life with Math 
Learning (WOS:000695432500125). PROCEEDINGS OF THE 2020 CHI CONFERENCE ON HUMAN FACTORS IN COMPUTING SYSTEMS (CHI’20). https://
doi .org /10 .1145 /3313831 .3376252

Q4
Khachatryan, G. A., Romashov, A. V., Khachatryan, A. R., Gaudino, S. J., Khachatryan, J. M., Guarian, K. R., & Yufa, N. V. (2014). Reasoning mind genie 2: An 
intelligent tutoring system as a vehicle for international transfer of instructional methods in mathematics. Int. J. Artif. Intell. Educ., 24(3), 333–382. https://
doi .org /10 .1007 /s40593 -014 -0019 -7

Q4
Khosravi, H., Kitto, K., & Williams, J. J. (2019). Ri PPLE: A crowdsourced adaptive platform for recommendation of learning activities. J. Learn. Anal., 6(3), 
91–105. https://doi .org /10 .18608 /jla .2019 .63 .12

Q3
Kim, G., Kim, J., & Kim, Y.-S. (2023). “Explain what a treemap is”: Exploratory investigation of strategies for explaining unfamiliar chart to blind and low 
vision users. Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems. https://doi .org /10 .1145 /3544548 .3581139

Q1
Kivimäki, V., Pesonen, J., Romanoﬀ, J., Remes, H., & Ihantola, P. (2019). Curricular concept maps as structured learning diaries: Collecting data on 
self-regulated learning and conceptual thinking for learning analytics applications. J. Learn. Anal., 6(3), 106–121. https://doi .org /10 .18608 /jla .2019 .63 .13

Q4
Labonte-Le Moyne, E., Leger, P., Robert, J., Babin, G., Charland, P., & Michon, J. (2017). Business intelligence serious game participatory development: Lessons 
from ERPsim for big data. BUSINESS PROCESS MANAGEMENT JOURNAL, 23(3), 493–505. https://doi .org /10 .1108 /BPMJ -12 -2015 -0177

Q4
Lallé, S., Taub, M., Mudrick, N. V., Conati, C., & Azevedo, R. (2017). The Impact of Student Individual Diﬀerences and Visual Attention to Pedagogical Agents 
During Learning with Meta Tutor. In Artiﬁcial Intelligence in Education (Vol. 10331, pp. 149–161). Springer International Publishing. http://
link .springer .com /10 .1007 /978 -3 -319 -61425 -0 _13

Q4
Lawrence, L., Echeverria, V., Yang, K., Aleven, V., & Rummel, N. (2023). How teachers conceptualise shared control with an AI co-orchestration tool: A 
multiyear teacher-centred design process. British Journal of Educational Technology. https://doi .org /10 .1111 /bjet .13372

Q4
Lee, A. V. Y., Luco, A. C., & Tan, S. C. (2023). A Human-Centric Automated Essay Scoring and Feedback System for the Development of Ethical Reasoning. 
Educational Technology and Society, 26(1), 147–159. https://doi .org /10 .30191 /ETS .202301 _26(1 ).0011

Q4
Lee, E., Kamat, M., Temor, L., Schiafone, C., Fan, L., Liu, J., Coppin, P., Uribe-Quevedo, A., Ingino, R., Syed, A. R., Rojas, D., Lee, T., Perera, S., Dubrowski, A., 
& Sukhai, M. (2022). Prototyping a Spatial Skills AR Authoring Tool for Partially Sighted, Blind, and Sighted Individuals. 2022 IEEE Games, Entertainment, 
Media Conference, GEM 2022. https://doi .org /10 .1109 /GEM56474 .2022 .10017454

Q4
Liaqat, A., Munteanu, C., & Demmans Epp, C. (2021). Collaborating with Mature English Language Learners to Combine Peer and Automated Feedback: A 
User-Centered Approach to Designing Writing Support. International Journal of Artiﬁcial Intelligence in Education, 31(4), 638–679.

Q4
Lim, L.-A., Gasevic, D., Matcha, W., Ahmad Uzir, N., & Dawson, S. (2021). Impact of Learning Analytics Feedback on Self-Regulated Learning: Triangulating 
Behavioural Logs with Students’ Recall. 364–374. https://doi .org /10 .1145 /3448139 .3448174

Q2
Long, Y., Aman, Z., & Aleven, V. (2015). Motivational Design in an Intelligent Tutoring System that Helps Students Make Good Task Selection Decisions. In 
Artiﬁcial Intelligence in Education (Vol. 9112, pp. 226–236). Springer International Publishing. http://link .springer .com /10 .1007 /978 -3 -319 -19773 -9 _23

Q4
Luo, J., & Zhang, S. (2022). Research on the design of project-based teaching & learning mode assisted by educational robot. Proceedings of the 4th World 
Symposium on Software Engineering, 148–154. https://doi .org /10 .1145 /3568364 .3568387

Q4
Ma, S., Zhou, T., Nie, F., & Ma, X. (2022). Glancee: An adaptable system for instructors to grasp student learning status in synchronous online classes. 1–25.

Q2
Mangaroska, K., Sharma, K., Giannakos, M., Trætteberg, H., & Dillenbourg, P. (2018). Gaze Insights into Debugging Behaviour Using Learner-Centred Analysis. 
350–359. https://doi .org /10 .1145 /3170358 .3170386

Q2
Martinez, J., Catasus, M., & Fontanillas, T. (2020). Impact of using learning analytics in asynchronous online discussions in higher education. 
INTERNATIONAL JOURNAL OF EDUCATIONAL TECHNOLOGY IN HIGHER EDUCATION, 17(1). https://doi .org /10 .1186 /s41239 -020 -00217 -y

Q4
Martinez-Maldonado, R., Pardo, A., Mirriahi, N., Yacef, K., Kay, J., & Clayphan, A. (2015). The LATUX Workﬂow: Designing and Deploying Awareness Tools in 
Technology-Enabled Learning Settings. 1–10. https://doi .org /10 .1145 /2723576 .2723583

Q2
Mcneill, G., Sondag, M., Powell, S., Asplin, P., Turkay, C., Moller, F., & Archambault, D. (2023). From asymptomatics to zombies: Visualization-based 
education of disease modelling for children. Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems. https://
doi .org /10 .1145 /3544548 .3581573

Q2
Michos, K., Lang, C., Hernandez-Leo, D., & Price-Dennis, D. (2020). Involving teachers in learning analytics design: Lessons learned from two case studies 
(WOS:000558753800013). 94–99. https://doi .org /10 .1145 /3375462 .3375507

Q2
Muldner, K., Lozano, C., Girotto, V., Burleson, W., & Walker, E. (2013). Designing a Tangible Learning Environment with a Teachable Agent. In Artiﬁcial 
Intelligence in Education (Vol. 7926, pp. 299–308). Springer Berlin Heidelberg. http://link .springer .com /10 .1007 /978 -3 -642 -39112 -5 _31

Q2
Muslim, A., Chatti, M. A., Mahapatra, T., & Schroeder, U. (2016). A Rule-Based Indicator Deﬁnition Tool for Personalized Learning Analytics. 264–273. 
https://doi .org /10 .1145 /2883851 .2883921

Q4
Nazaretsky, T., Bar, C., Walter, M., & Alexandron, G. (2022). Empowering Teachers with AI: Co-Designing a Learning Analytics Tool for Personalized 
Instruction in the Science Classroom. 1–12. https://doi .org /10 .1145 /3506860 .3506861
(continued on next page)

--- Page 18 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
Table 2 (continued)
No.
Quadrant
Reference

Q4
Ngoon, T. J., Kovalev, D., Patidar, P., Harrison, C., Agarwal, Y., Zimmerman, J., & Ogan, A. (2023). ‘An Instructor is [already] able to keep track of 30 
students’: Students’ Perceptions of Smart Classrooms for Improving Teaching & Their Emergent Understandings of Teaching and Learning. Proceedings of the 
2023 ACM Designing Interactive Systems Conference, 1277–1292. https://doi .org /10 .1145 /3563657 .3596079

Q1
Nguyen, Q., Rienties, B., & Whitelock, D. (2020). A mixed-method study of how instructors design for learning in online and distance education. J. Learn. 
Anal., 7(3), 64–78. https://doi .org /10 .18608 /JLA .2020 .73 .6

Q3
Ochoa, X., & Dominguez, F. (2020). Controlled evaluation of a multimodal system to improve oral presentation skills in a real learning setting. Br J Educ 
Technol, 51(5), 1615–1630. https://doi .org /10 .1111 /bjet .12987

Q3
Ocumpaugh, J., Baker, R., Pedro, M., Hawn, M., Heﬀernan, C., Heﬀernan, N., & Slater, S. (2017). Guidance Counselor Reports of the ASSISTments College 
Prediction Model (ACPM) (WOS:000570180700063). 479–488. https://doi .org /10 .1145 /3027385 .3027435

Q2
Oliver-Quelennec, K., Bouchet, F., Carron, T., Fronton Casalino, K., & Pinçon, C. (2022). Adapting Learning Analytics Dashboards by and for University 
Students. In Lecture Notes in Computer Science (including subseries Lecture Notes in Artiﬁcial Intelligence and Lecture Notes in Bioinformatics): Vol. 13450 
LNCS (p. 309). https://doi .org /10 .1007 /978 -3 -031 -16290 -9 _22

Q4
Olsen, J. K., Rummel, N., & Aleven, V. (2021). Designing for the Co-Orchestration of Social Transitions between Individual, Small-Group and Whole-Class 
Learning in the Classroom. International Journal of Artiﬁcial Intelligence in Education, 31(1), 24–56.

Q4
Ooge, J., Dereu, L., & Verbert, K. (2023). Steering recommendations and visualising its impact: Eﬀects on adolescents’ trust in E-learning platforms. 
Proceedings of the 28th International Conference on Intelligent User Interfaces, 156–170. https://doi .org /10 .1145 /3581641 .3584046

Q2
Pishtari, G., Rodríguez-Triana, M. J., & Väljataga, T. (2021). A multi-stakeholder perspective of analytics for learning design in location-based learning. 
International Journal of Mobile and Blended Learning, 13(1), 1–17. https://doi .org /10 .4018 /IJMBL .2021010101

Q4
Pozdniakov, S., Martinez-Maldonado, R., Tsai, Y.-S., Cukurova, M., Bartindale, T., Chen, P., Marshall, H., Richardson, D., & Gasevic, D. (2022). The 
Question-driven Dashboard: How Can We Design Analytics Interfaces Aligned to Teachers’ Inquiry? 175–185. https://doi .org /10 .1145 /3506860 .3506885

Q2
Rapp, C., & Kauf, P. (2018). Scaling Academic Writing Instruction: Evaluation of a Scaﬀolding Tool (Thesis Writer). Int. J. Artif. Intell. Educ., 28(4), 590–615. 
https://doi .org /10 .1007 /s40593 -017 -0162 -z

Q2
Read, S., Dela Merced, A., & Zachry, M. (2012). Participatory Design in the Development of a Web-based Technology for Visualizing Writing Activity as 
Knowledge Work (WOS:000324841800045). 333–340.

Q2
Rodrigues, L., Palomino, P. T., Toda, A. M., Klock, A. C. T., Pessoa, M., Pereira, F. D., Oliveira, E. H. T., Oliveira, D. F., Cristea, A. I., Gasparini, I., & Isotani, S. 
(2023). How Personalization Aﬀects Motivation in Gamiﬁed Review Assessments. Int. J. Artif. Intell. Educ. https://doi .org /10 .1007 /s40593 -022 -00326 -x

Q4
Rodríguez-Triana, M. J., Prieto, L. P., Dimitriadis, Y., de Jong, T., & Gillet, D. (2021). Ada for ibl: Lessons learned in aligning learning design and analytics for 
inquiry-based learning orchestration. J. Learn. Anal., 8(2), 22–50. https://doi .org /10 .18608 /JLA .2021 .7357

Q4
Ruiz-Calleja, A., Dennerlein, S., Kowald, D., Theiler, D., Lex, E., & Ley, T. (2019). An infrastructure for workplace learning analytics: Tracing knowledge 
creation with the social semantic server. J. Learn. Anal., 6(2), 120–139. https://doi .org /10 .18608 /jla .2019 .62 .9

Q3
Santos, J. L., Govaerts, S., Verbert, K., & Duval, E. (2012). Goal-Oriented Visualizations of Activity Tracking: A Case Study with Engineering Students. 
143–152. https://doi .org /10 .1145 /2330601 .2330639

Q4
Sato, A. J., Sramek, Z., & Yatani, K. (2023). Groupnamics: Designing an interface for overviewing and managing parallel group discussions in an online 
classroom. Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems. https://doi .org /10 .1145 /3544548 .3581322

Q4
Schulz, S., Mc Laren, B. M., & Pinkwart, N. (2022). Towards a Tutoring System to Support Robotics Activities in Classrooms – Two Wizard-of-Oz Studies. Int. J. 
Artif. Intell. Educ. https://doi .org /10 .1007 /s40593 -022 -00305 -2

Q3
Shardlow, M., Sellar, S., & Rousell, D. (2022). Collaborative Augmentation and Simpliﬁcation of Text (Co AST): Pedagogical Applications of Natural Language 
Processing in Digital Learning Environments. Learning Environments Research, 25(2), 399–421.

Q4
Shibani, A., Knight, S., & Buckingham Shum, S. (2022). Questioning learning analytics? Cultivating critical engagement as student automated feedback 
literacy. 326–335. https://doi .org /10 .1145 /3506860 .3506912

Q2
Shreiner, T. L., & Guzdial, M. (2022). The information won’t just sink in: Helping teachers provide technology-assisted data literacy instruction in social 
studies. British Journal of Educational Technology, 53(5), 1134–1158. https://doi .org /10 .1111 /bjet .13255

Q2
Shute, V. J., Smith, G., Kuba, R., Dai, C.-P., Rahimi, S., Liu, Z., & Almond, R. (2021). The Design, Development, and Testing of Learning Supports for the 
Physics Playground Game. Int. J. Artif. Intell. Educ., 31(3), 357–379. https://doi .org /10 .1007 /s40593 -020 -00196 -1

Q1
Soreny, C., Takhar, P., Vickers, E., Bartlett, R., Coates, E., Stavroulakis, T., Fox, E., Davidson, H., Harrison, A., & Mc Dermott, C. (2022). Co-design of digital 
learning resources for care workers: Reﬂections on the neurocare knowhow project. Journal of Medical Engineering and Technology, 46(6), 518–526. https://
doi .org /10 .1080 /03091902 .2022 .2089253

Q4
Suleman, R. M., Mizoguchi, R., & Ikeda, M. (2016). A New Perspective of Negotiation-Based Dialog to Enhance Metacognitive Skills in the Context of Open 
Learner Models. Int. J. Artif. Intell. Educ., 26(4), 1069–1115. https://doi .org /10 .1007 /s40593 -016 -0118 -8

Q4
Tegos, S., Demetriadis, S., & Tsiatsos, T. (2014). A conﬁgurable conversational agent to trigger students’ productive dialogue: A pilot study in the CALL 
domain. Int. J. Artif. Intell. Educ., 24(1), 62–91. https://doi .org /10 .1007 /s40593 -013 -0007 -3

Q2
Tenório, K., Dermeval, D., Monteiro, M., Peixoto, A., & Silva, A. P. (2022). Exploring Design Concepts to Enable Teachers to Monitor and Adapt Gamiﬁcation 
in Adaptive Learning Systems: A Qualitative Research Approach. Int. J. Artif. Intell. Educ., 32(4), 867–891. https://doi .org /10 .1007 /s40593 -021 -00274 -y

Q2
Ternblad, E.-M., Haake, M., Anderberg, E., & Gulz, A. (2018). Do Preschoolers ‘Game the System’? A Case Study of Children’s Intelligent (Mis)Use of a 
Teachable Agent Based Play-&-Learn Game in Mathematics. In Artiﬁcial Intelligence in Education (Vol. 10947, pp. 557–569). Springer International 
Publishing. http://link .springer .com /10 .1007 /978 -3 -319 -93843 -1 _41

Q4
Tissenbaum, M., & Slotta, J. (2019). Supporting classroom orchestration with real-time feedback: A role for teacher dashboards and real-time agents. 
INTERNATIONAL JOURNAL OF COMPUTER-SUPPORTED COLLABORATIVE LEARNING, 14(3), 325–351. https://doi .org /10 .1007 /s11412 -019 -09306 -1

Q2
Topali, P., Ortega-Arranz, A., Chounta, I., Asensio-Perez, J., Martinez-Mones, A., & Villagra-Sobrino, S. (2022). Supporting instructors in the design of 
actionable feedback for MOOCs (WOS:000836390500274). 1881–1887. https://doi .org /10 .1109 /EDUCON52537 .2022 .9766546

Q2
Treasure-Jones, T., Dent-Spargo, R., & Dharmaratne, S. (2018). How do students want their workplace-based feedback visualized in order to support 
self-regulated learning? Initial results & reﬂections from a co-design study in medical education. 2193. https://
www .scopus .com /inward /record .uri ?eid =2 -s2 .0 -85053678222 &partner ID =40 &md5 =0e13f7113188599442308fba21e0cc57

Q2
Tsai, Y.-S., Singh, S., Rakovic, M., Lim, L.-A., Roychoudhury, A., & Gasevic, D. (2022). Charting Design Needs and Strategic Approaches for Academic 
Analytics Systems through Co-Design. 381–391. https://doi .org /10 .1145 /3506860 .3506939

Q4
Vannaprathip, N., Haddawy, P., Schultheis, H., & Suebnukarn, S. (2022). Intelligent Tutoring for Surgical Decision Making: A Planning-Based Approach. Int. J. 
Artif. Intell. Educ., 32(2), 350–381. https://doi .org /10 .1007 /s40593 -021 -00261 -3

Q1
Vezzoli, Y., Mavrikis, M., & Vasalou, A. (2020). Inspiration Cards Workshops with Primary Teachers in the Early Co-Design Stages of Learning Analytics 
(WOS:000558753800010). 73–82. https://doi .org /10 .1145 /3375462 .3375537

Q2
Vinella, F. L., Koppelaar, S., & Masthoﬀ, J. (2022). Forming Teams of Learners Online in a User as Wizard Study with Openness, Conscientiousness, and 
cognitive Ability. 283–292. https://doi .org /10 .1145 /3511047 .3537660

Q2
Wang, Q., Jing, S., & Goel, A. K. (2022). Co-Designing AI Agents to Support Social Connectedness Among Online Learners: Functionalities, Social 
Characteristics, and Ethical Challenges. 541–556. https://doi .org /10 .1145 /3532106 .3533534

Q4
Wang, Y., Nguyen, H., Harpstead, E., Stamper, J., & Mc Laren, B. M. (2019). How Does Order of Gameplay Impact Learning and Enjoyment in a Digital 
Learning Game? In Artiﬁcial Intelligence in Education (Vol. 11625, pp. 518–531). Springer International Publishing. http://
link .springer .com /10 .1007 /978 -3 -030 -23204 -7 _43

--- Page 19 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
Table 2 (continued)
No.
Quadrant
Reference

Q3
Weigand, A. C., & Kindsmüller, M. C. (2021). HCD3A: An HCD Model to Design Data-Driven Apps. In Lecture Notes in Computer Science (including subseries 
Lecture Notes in Artiﬁcial Intelligence and Lecture Notes in Bioinformatics): Vol. 12797 LNAI (p. 297). https://doi .org /10 .1007 /978 -3 -030 -77772 -2 _19

Q4
Wiley, K., Dimitriadis, Y., & Linn, M. (2023). A human-centred learning analytics approach for developing contextually scalable K-12 teacher dashboards. 
BRITISH JOURNAL OF EDUCATIONAL TECHNOLOGY. https://doi .org /10 .1111 /bjet .13383

Q3
Wilson, J., Huang, Y., Palermo, C., Beard, G., & Mac Arthur, C. A. (2021). Automated Feedback and Automated Scoring in the Elementary Grades: Usage, 
Attitudes, and Associations with Writing Outcomes in a Districtwide Implementation of MI Write. Int. J. Artif. Intell. Educ., 31(2), 234–276. https://
doi .org /10 .1007 /s40593 -020 -00236 -w

Q4
Zhang, Z., Xu, Y., Wang, Y., Yao, B., Ritchie, D., Wu, T., Yu, M., Wang, D., & Li, T. J.-J. (2022). Story Buddy: A Human-AI Collaborative Chatbot for 
Parent-Child Interactive Storytelling with Flexible Parental Involvement. Conference on Human Factors in Computing Systems - Proceedings. https://
doi .org /10 .1145 /3491102 .3517479

Q3
Zhou, Q., Suraworachet, W., Pozdniakov, S., Martinez-Maldonado, R., Bartindale, T., Chen, P., Richardson, D., & Cukurova, M. (2021). Investigating Students’ 
Experiences with Collaboration Analytics for Remote Group Meetings. In Lecture Notes in Computer Science (including subseries Lecture Notes in Artiﬁcial 
Intelligence and Lecture Notes in Bioinformatics): Vol. 12748 LNAI (p. 485). https://doi .org /10 .1007 /978 -3 -030 -78292 -4 _38

Q1
Zwolinski, G., Kaminska, D., Laska-Lesniewicz, A., Haamer, R. E., Vairinhos, M., Raposo, R., Urem, F., & Reisinho, P. (2022). Extended Reality in Education 
and Training: Case Studies in Management Education. ELECTRONICS, 11(3). https://doi .org /10 .3390 /electronics11030336
References
Ahn, J., Campos, F., Hays, M., & Digiacomo, D. (2019). Designing in context: Reaching 
beyond usability in learning analytics dashboard design. Journal of Learning Analytics, 
6, 70–85. https://doi .org /10 .18608 /jla .2019 .62 .5.
Ahn, J., Campos, F., Nguyen, H., Hays, M., & Morrison, J. (2021). Co-designing for pri-
vacy, transparency, and trust in K-12 learning analytics. In LAK21: 11th international 
learning analytics and knowledge conference (pp. 55–65). ACM.
Al-Doulat, A., Nur, N., Karduni, A., Benedict, A., Al-Hossami, E., Maher, M. L., Dou, W., 
Dorodchi, M., & Niu, X. (2020). Making sense of student success and risk through unsu-
pervised machine learning and interactive storytelling In Artiﬁcial intelligence in education: 
Vol. 12163 (pp. 3–15). Cham: Springer International Publishing.
Albó, L., Barria-Pineda, J., Brusilovsky, P., & Hernández-Leo, D. (2022). Knowledge-based 
design analytics for authoring courses with smart learning content. Journal of Artiﬁcial 
Intelligence in Education, 32, 4–27. https://doi .org /10 .1007 /s40593 -021 -00253 -3.
Aleven, V., Blankestijn, J., Lawrence, L., Nagashima, T., & Taatgen, N. (2022). A dash-
board to support teachers during students’ self-paced AI-supported problem-solving practice. 
Springer International Publishing (pp. 16–30).
Alfredo, R. D., Nie, L., Kennedy, P., Power, T., Hayes, C., Chen, H., Mc Gregor, C., Swiecki, 
Z., Gaševi´c, D., & Martinez-Maldonado, R. (2023). “That Student Should Be a Lion 
Tamer!” Stress Viz: Designing a stress analytics dashboard for teachers. In LAK23: 
13th international learning analytics and knowledge conference (pp. 57–67).
Alzahrani, A. S., Tsai, Y. S., Aljohani, N., Whitelock-Wainwright, E., & Gasevic, D. (2023). 
Do teaching staﬀ trust stakeholders and tools in learning analytics? A mixed methods 
study. Educational Technology Research and Development, 71, 1471–1501.
Assim, M., Al-Bahri, H., Zafar, Q., Shahada, M., & Al-Ammary, J. (2021). Remote teach-
ing during COVID-19 pandemic in higher education institutions in the Kingdom of 
Bahrain: Challenges and innovative solutions. In 2021 sustainable leadership and aca-
demic excellence international conference, SLAE 2021.
Baker, R. S. (2016). Stupid tutoring systems, intelligent humans. International Journal of 
Artiﬁcial Intelligence in Education, 26, 600–614. https://doi .org /10 .1007 /s40593 -016 -
0105 -0.
Barreiros, C., Leitner, P., Ebner, M., Veas, E., & Lindstaedt, S. (2023). Students in focus 
– moving towards human-centred learning analytics. In O. Viberg, & Å. Grönlund 
(Eds.), Advances in analytics for learning and teaching. Practicable learning analytics
(pp. 77–94). Cham: Springer International Publishing.
van Berkel, N., Tag, B., Goncalves, J., & Hosio, S. (2022). Human-centred artiﬁcial intel-
ligence: A contextual morality perspective. Behaviour & Information Technology, 41, 
502–518.
Biesta, G., Priestley, M., & Robinson, S. (2015). The role of beliefs in teacher 
agency. Teachers and Teaching, 21, 624–640. https://doi .org /10 .1080 /13540602 .
2015 .1044325.
Bishop, E., Allington, D., Ringrose, T., Martin, C., Aldea, A., Garcia-Jaramillo, M., Leon-
Vargas, F., Leal, Y., Henao, D., & Gomez, A. M. (2022). Design and usability of an 
avatar-based learning program to support diabetes education: Quality improvement 
study in Colombia. Journal of Diabetes Science and Technology, 17(5). https://doi .org /
10 .1177 /19322968221136141.
Boateng, S., Alex, J., Adelabu, F., Sihele, T., & Momoti, V. (2022). Pre-service teachers’ 
perspectives towards the use of Gamma Tutor in teaching physical sciences in South 
African secondary schools. International Journal of Learning, Teaching and Educational 
Research, 21, 304–323. https://doi .org /10 .26803 /ijlter .21 .6 .18.
Bodily, R., & Verbert, K. (2017). Trends and issues in student-facing learning analytics re-
porting systems research. In Proceedings of the seventh international learning analytics & 
knowledge conference (pp. 309–318). New York, NY, USA: Association for Computing 
Machinery.
Bødker, S., Dindler, C., Iversen, O. S., & Smith, R. C. (2022). What is participatory de-
sign? In S. Bødker, C. Dindler, O. S. Iversen, & R. C. Smith (Eds.), Synthesis lectures 
on human-centered informatics. Participatory design (pp. 5–13). Cham: Springer Inter-
national Publishing.
Bond, M., Viberg, O., & Bergdahl, N. (2023). The current state of using learning analytics 
to measure and support K-12 student engagement: A scoping review. In LAK2023: 
LAK23: 13th international learning analytics and knowledge conference (pp. 240–249). 
New York, NY, USA: Association for Computing Machinery.
Bonnat, C., & Sanchez, E. (2022). Toward a digital companion to monitor a mixed reality 
game. International Journal of Serious Games, 9, 5–21. https://doi .org /10 .17083 /ijsg .
v9i3 .504.
Borjigin, A., Miao, C., Lim, S. F., Li, S., & Shen, Z. (2015). Teachable agents with intrinsic 
motivation. Artiﬁcial intelligence in education: Vol. 9112. Cham: Springer International 
Publishing (pp. 34–43).
Braun, V., & Clarke, V. (2012). Thematic analysis. In APA handbooks in psychology®.. APA 
handbook of research methods in psychology, Vol 2: Research designs: Quantitative, qual-
itative, neuropsychological, and biological (pp. 57–71). Washington, DC, US: American 
Psychological Association.
Brossi, L., Castillo, A. M., & Cortesi, S. (2022). Student-centred requirements for the ethics 
of ai in education. In W. Holmes, & K. Porayska-Pomsta (Eds.), The ethics of artiﬁcial 
intelligence in education. Routledge (pp. 91–112).
Buckingham Shum, S., Ferguson, R., & Martinez-Maldonado, R. (2019). Human-centred 
learning analytics. Journal of Learning Analytics, 6, 1–9.
Buckingham Shum, S., & Luckin, R. (2019). Learning analytics and AI: Politics, pedagogy 
and practices. British Journal of Educational Technology, 50, 2785–2793. https://doi .
org /10 .1111 /bjet .12880.
Camara Olim, S. M., Nisi, V., & Rubegni, E. (2023). “Periodic fable discovery” using tan-
gible interactions and augmented reality to promote STEM subjects. In Proceedings of 
the seventeenth international conference on tangible, embedded, and embodied interaction.
Carter, M., & Egliston, B. (2023). What are the risks of virtual reality data? Learning 
analytics, algorithmic bias and a fantasy of perfect data. New Media & Society, 23, 
485–504.
Cavalcante Siebert, L., Lupetti, M. L., Aizenberg, E., Beckers, N., Zgonnikov, A., 
Veluwenkamp, H., Abbink, D., Giaccardi, E., Houben, G. J., Jonker, C. M., van den 
Hoven, J., Forster, D., & Lagendijk, R. L. (2023). Meaningful human control: Ac-
tionable properties for AI system development. AI and Ethics, 3, 241–255. https://
doi .org /10 .1007 /s43681 -022 -00167 -3.
Cavalcanti, A. P., Barbosa, A., Carvalho, R., Freitas, F., Tsai, Y. S., Gaševi´c, D., & Mello, 
R. F. (2021). Automatic feedback in online learning environments: A systematic lit-
erature review. Computers and Education: Artiﬁcial Intelligence, 2, Article 100027.
Chakraborty, U., Banerjee, A., Saha, J. K., Sarkar, N., & Chakraborty, C. (2022). Artiﬁcial 
intelligence and the fourth industrial revolution. CRC Press.
Challco, G. C., Bittencourt, I. I., & Isotani, S. (2020). Can ontologies support the gamiﬁcation 
of scripted collaborative learning sessions? Artiﬁcial intelligence in education: Vol. 12163. 
Cham: Springer International Publishing (pp. 79–91).
Chang, H. T., Lin, C. Y., Jheng, W. B., Chen, S. H., Wu, H. H., Tseng, F. C., & Wang, 
L. C. (2023). AI, please help me choose a course: Building a personalized hybrid 
course recommendation system to assist students in choosing courses adaptively. Ed-
ucational Technology & Society, 26, 203–217. https://doi .org /10 .30191 /ETS .202301 _
26(1 ).0015.
Chatti, M., Muslim, A., Guesmi, M., Richtscheid, F., Nasimi, D., Shahin, A., & Damera, 
R. (2020). How to design eﬀective learning analytics indicators? In A human-centered 
design approach. LNCS: Vol. 12315.
Chavan, P., & Mitra, R. (2022). Tcherly: A teacher-facing dashboard for online video lec-
tures. Journal of Learning Analytics, 9, 125–151. https://doi .org /10 .18608 /jla .2022 .
7555.
Chen, B. D., & Zhu, H. Y. (2019). Towards value-sensitive learning analytics design. In Pro-
ceedings of the 9th international conference on learning analytics & knowledge (LAK’19)
(pp. 343–352).
Chignell, M., Wang, L., Zare, A., & Li, J. (2022). The evolution of hci and human factors: 
Integrating human and artiﬁcial intelligence. ACM Transactions on Computer-Human 
Interaction, 30(2), Article 17. https://doi .org /10 .1145 /3557891.
Conijn, R., Martinez-Maldonado, R., Knight, S., Shum, S. B., Van Waes, L., & van Zaanen, 
M. (2020). How to provide automated feedback on the writing process? A participa-

--- Page 20 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
tory approach to design writing analytics tools. Computer Assisted Language Learning, 
35(8), 1838–1868. https://doi .org /10 .1080 /09588221 .2020 .1839503.
Conijn, R., Van Waes, L., & van Zaanen, M. (2020). Human-centered design of a dashboard 
on students’ revisions during writing. LNCS: Vol. 12315.
Crain, P., Lee, J., Yen, Y. C. G., Kim, J., Aiello, A., & Bailey, B. (2022). Visualizing topics 
and opinions helps students interpret large collections of peer feedback for creative 
projects. ACM Transactions on Computer-Human Interaction, 30(3), Article 49. https://
doi .org /10 .1145 /3571817.
Cukurova, M., Mavrikis, M., Luckin, R., Clark, J., & Crawford, C. (2017). Interaction anal-
ysis in online maths human tutoring: The case of third space learning. Artiﬁcial intelligence 
in education: Vol. 10331. Cham: Springer International Publishing (pp. 636–643).
Darvishi, A., Khosravi, H., Sadiq, S., Gaševi´c, D., & Siemens, G. (2024). Impact of ai 
assistance on student agency. Computers and Education, 210, Article 104967.
Davenport, T. H. (2018). From analytics to artiﬁcial intelligence. Journal of Business Ana-
lytics, 1, 73–80.
de Quincey, E., Briggs, C., Kyriacou, T., & Waller, R. (2019). Student centred design of 
a learning analytics system. Association for Computing Machinery, 353–362. https://
doi .org /10 .1145 /3303772 .3303793.
De Silva, L., Chounta, I. A., Rodríguez-Triana, M., Roa, E., Gramberg, A., & Valk, A. 
(2022). Toward an institutional analytics agenda for addressing student dropout in 
higher education: An academic stakeholders’ perspective. Journal of Learning Analyt-
ics, 9, 179–201. https://doi .org /10 .18608 /jla .2022 .7507.
Di Mitri, D., Schneider, J., & Drachsler, H. (2022). Keep Me in the loop: Real-time 
feedback with multimodal data. Journal of Artiﬁcial Intelligence in Education, 32, 
1093–1118. https://doi .org /10 .1007 /s40593 -021 -00281 -z.
Dogan, M. E., Goru Dogan, T., & Bozkurt, A. (2023). The use of artiﬁcial intelligence (AI) in 
online learning and distance education processes: A systematic review of empirical studies. 
Applied sciences: Vol. 13 (p. 3056).
Dollinger, M., Liu, D., Arthars, N., & Lodge, J. (2019). Working together in learning ana-
lytics towards the co-creation of value. Journal of Learning Analytics, 6, 10–26. https://
doi .org /10 .18608 /jla .2019 .62 .2.
Drachsler, H., & Greller, W. (2016). Privacy and analytics: It’s a DELICATE issue a check-
list for trusted learning analytics. In LAK ’16: Proc. of the 6th intl. conf. on learning 
analytics & knowledge (pp. 89–98). New York, NY, USA: ACM.
Duan, X., Pei, B., Ambrose, G. A., Hershkovitz, A., Cheng, Y., & Wang, C. (2023). To-
wards transparent and trustworthy prediction of student learning achievement by including 
instructors as co-designers: A case study.
Easterday, M., Rees Lewis, D., & Gerber, E. (2017). Designing crowdcritique systems for 
formative feedback. Journal of Artiﬁcial Intelligence in Education, 27, 623–663. https://
doi .org /10 .1007 /s40593 -016 -0125 -9.
Echeverria, V., Martinez-Maldonado, R., & Buckingham Shum, S. (2019). Towards collab-
oration translucence: Giving meaning to multimodal group data. In Proceedings of the 
2019 CHI conference on human factors in computing systems (pp. 1–16).
Echeverria, V., Martinez-Maldonado, R., Shum, S. B., Chiluiza, K., Granda, R., & Conati, 
C. (2018). Exploratory versus explanatory visual learning analytics: Driving teach-
ers’ attention through educational data storytelling. Journal of Learning Analytics, 5, 
73–97. https://doi .org /10 .18608 /jla .2018 .53 .6.
Echeverria, V., Yan, L., Zhao, L., Abel, S., Alfredo, R., Dix, S., Jaggard, H., Wother-
spoon, R., Osborne, A., Buckingham Shum, S., Gaševi´c, D., & Martinez-Maldonado, R. 
(2024). Teamslides: A multimodal teamwork analytics dashboard for teacher-guided 
reﬂection in a physical learning space. In LAK24: 14th international learning analytics 
and knowledge conference. ACM.
Echeverria, V., Yang, K., Lawrence, L., Rummel, N., & Aleven, V. (2023). Designing hybrid 
human–ai orchestration tools for individual and collaborative activities: A technology 
probe study. IEEE Transactions on Learning Technologies, 16, 191–205. https://doi .org /
10 .1109 /TLT .2023 .3248155.
Edelenbos, J., & Klijn, E. H. (2006). Managing stakeholder involvement in decision mak-
ing: A comparative analysis of six interactive processes in the Netherlands. Journal 
of Public Administration Research and Theory, 16, 417–446. https://doi .org /10 .1093 /
jopart /mui049.
Ekstrom, S., & Pareto, L. (2022). The dual role of humanoid robots in education: As didac-
tic tools and social actors. Education and Information Technologies, 27, 12609–12644. 
https://doi .org /10 .1007 /s10639 -022 -11132 -2.
Engelbart, D. C. (1962). Augmenting human intellect: A conceptual framework. Summary 
Report, Contract AF 49–1024 21.
Eradze, M., Rodríguez-Triana, M., Milikic, N., Laanpere, M., & Tammets, K. (2020). Con-
textualising learning analytics with classroom observations: A case study. Interaction 
Design and Architecture(s), 44, 71–95.
Fernandez-Nieto, G., An, P., Zhao, J., Buckingham Shum, S., & Martinez-Maldonado, R. 
(2022). Classroom dandelions: Visualising participant position, trajectory and body 
orientation augments teachers’ sensemaking. In CHI ’22: CHI conference on human 
factors in computing systems (pp. 1–17). ACM.
Fernandez Nieto, G. M., Kitto, K., Buckingham Shum, S., & Martinez-Maldonado, R. 
(2022). Beyond the learning analytics dashboard: Alternative ways to communicate 
student data insights combining visualisation, narrative and storytelling. In LAK22: 
12th international learning analytics and knowledge conference (pp. 219–229).
Fernandez-Nieto, G. M., Martinez-Maldonado, R., Kitto, K., & Buckingham Shum, S. 
(2021). Modelling spatial behaviours in clinical team simulations using epistemic 
network analysis: Methodology and teacher evaluation. In LAK21: 11th international 
learning analytics and knowledge conference (pp. 386–396). ACM.
Garcia-Ruiz, M., Santana-Mancilla, P., Gaytan-Lugo, L., & Iniguez-Carrillo, A. (2022). Par-
ticipatory design of soniﬁcation development for learning about molecular structures 
in virtual reality. Multimodal Technologies and Interaction, 6. https://doi .org /10 .3390 /
mti6100089.
Gerdes, A., Heeren, B., Jeuring, J., & van Binsbergen, L. (2017). Ask-elle: An adaptable 
programming tutor for Haskell giving automated feedback. Journal of Artiﬁcial Intel-
ligence in Education, 27, 65–100. https://doi .org /10 .1007 /s40593 -015 -0080 -x.
Giacomin, J. (2014). What is human centred design? Design Journal, 17, 606–623.
Gibson, A., Aitken, A., Sándor, Á., Buckingham Shum, S., Tsingos-Lucas, C., & Knight, S. 
(2017). Reﬂective writing analytics for actionable feedback. Association for Computing 
Machinery, 153–162. https://doi .org /10 .1145 /3027385 .3027436.
Gorkovenko, K., Burnett, D. J., Thorp, J. K., Richards, D., & Murray-Rust, D. (2020). 
Exploring the future of data-driven product design. In Proc. of the 2020 CHI conference 
on human factors in computing systems (pp. 1–14). New York, NY, USA: ACM.
Grani´c, A. (2022). Educational technology adoption: A systematic review. Education 
and Information Technologies, 27, 9725–9744. https://doi .org /10 .1007 /s10639 -022 -
10951 -7.
Grudin, J. (2009). Ai and hci: Two ﬁelds divided by a common focus. AI Magazine, 30, 
48.
Han, S., Liu, M., Pan, Z., Cai, Y., & Shao, P. (2022). Making FAQ chatbots more inclusive: 
An examination of non-native English users’ interactions with new technology in 
massive open online courses. Journal of Artiﬁcial Intelligence in Education, 33, 752–780. 
https://doi .org /10 .1007 /s40593 -022 -00311 -4.
Hanington, B., & Martin, B. (2012). Universal methods of design: 100 ways to research 
complex problems, develop innovative ideas, and design eﬀective solutions. Rockport Pub-
lishers.
Head, A., Xu, Y., & Wang, J. (2014). Tone Wars: Connecting language learners and na-
tive speakers through collaborative mobile games. Intelligent tutoring systems: Vol. 8474. 
Cham: Springer International Publishing (pp. 368–377).
Holmes, W., Porayska-Pomsta, K., Holstein, K., Sutherland, E., Baker, T., Shum, S. B., 
Santos, O. C., Rodrigo, M. T., Cukurova, M., Bittencourt, I. I., et al. (2022). Ethics 
of AI in education: Towards a community-wide framework. International Journal of 
Artiﬁcial Intelligence in Education, 32, 504–526.
Holstein, K., Aleven, V., & Rummel, N. (2020). A conceptual framework for human–
AI hybrid adaptivity in education. In I. I. Bittencourt, M. Cukurova, K. Muldner, R. 
Luckin, & E. Millán (Eds.), Artiﬁcial intelligence in education: Vol. 12163 (pp. 240–254). 
Cham: Springer International Publishing.
Holstein, K., Mc Laren, B. M., & Aleven, V. (2019). Co-designing a real-time classroom or-
chestration tool to support teacher–AI complementarity. Learning Analytics, 6, 27–52. 
https://doi .org /10 .18608 /jla .2019 .62 .3.
Hooshyar, D., Tammets, K., Ley, T., Aus, K., & Kollom, K. (2023). Learning analytics 
in supporting student agency: A systematic review. Sustainability, 15, Article 13662. 
https://doi .org /10 .3390 /su151813662.
Hosseini, R., Akhuseyinoglu, K., Brusilovsky, P., Malmi, L., Pollari-Malmi, K., Schunn, 
C., & Sirkiä, T. (2020). Improving engagement in program construction examples 
for learning python programming. Journal of Artiﬁcial Intelligence in Education, 30, 
299–336. https://doi .org /10 .1007 /s40593 -020 -00197 -0.
Hu, L., Wu, J., & Chen, G. (2022). i Talk–i See: A participatory visual learning analytical 
tool for productive peer talk. International Journal of Computer-Supported Collaborative 
Learning, 17, 397–425. https://doi .org /10 .1007 /s11412 -022 -09374 -w.
Hutchins, N., & Biswas, G. (2023). Using teacher dashboards to customize lesson plans 
for a problem-based, middle school STEM curriculum. In ACM international conference 
proceeding series (pp. 324–332).
Hutt, S., Krasich, K., Brockmole, J. R., & D’Mello, S. K. (2021). Breaking out of the lab: Mit-
igating mind wandering with gaze-based attention-aware technology in classrooms.
In CHI ’21: Proceedings of the 2021 CHI conference on human factors in computing sys-
tems.
Jääskelä, P., Heilala, V., Kärkkäinen, T., & Häkkinen, P. (2021). Student agency analytics: 
Learning analytics as a tool for analysing student agency in higher education. Be-
haviour & Information Technology, 40, 790–808. https://doi .org /10 .1080 /0144929X .
2020 .1725130.
Jamalova, G., Aymatova, F., & Ikromov, S. (2022). The state-of-the-art applications of arti-
ﬁcial intelligence in distance education: A systematic mapping study. In Proceedings of 
the 6th international conference on future networks & distributed systems (pp. 600–606). 
Tashkent TAS Uzbekistan: ACM.
Jelinek, T., Wallach, W., & Kerimi, D. (2021). Policy brief: The creation of a g20 co-
ordinating committee for the governance of artiﬁcial intelligence. AI and Ethics, 1, 
141–150.
Jeong, Y., Cho, H., Kim, T., & Nam, T. J. (2023). Automata Stage: An AR-mediated cre-
ativity support tool for hands-on multidisciplinary learning. In Proceedings of the 2023 
CHI conference on human factors in computing systems.
Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of ai ethics guidelines. 
Nature Machine Intelligence, 1, 389–399.
Kaliisa, R., Jivet, I., & Prinsloo, P. (2023). A checklist to guide the planning, designing, 
implementation, and evaluation of learning analytics dashboards. International Jour-
nal of Educational Technology in Higher Education, 20, 28. https://doi .org /10 .1186 /
s41239 -023 -00394 -6.
Kaliisa, R., Kluge, A., & Mørch, A. (2020). Combining checkpoint and process learning an-
alytics to support learning design decisions in blended learning environments. Journal 
of Learning Analytics, 7, 33–47. https://doi .org /10 .18608 /JLA .2020 .73 .4.

--- Page 21 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
Kang, S., Shokeen, E., Byrne, V. L., Norooz, L., Bonsignore, E., Williams-Pierce, C., & 
Froehlich, J. E. (2020). ARMath: Augmenting everyday life with math learning. In
Proceedings of the 2020 CHI conference on human factors in computing systems (CHI’20).
Khachatryan, G., Romashov, A., Khachatryan, A., Gaudino, S., Khachatryan, J., Guarian, 
K., & Yufa, N. (2014). Reasoning mind genie 2: An intelligent tutoring system as a 
vehicle for international transfer of instructional methods in mathematics. Journal of 
Artiﬁcial Intelligence in Education, 24, 333–382. https://doi .org /10 .1007 /s40593 -014 -
0019 -7.
Khosravi, H., Kitto, K., & Williams, J. (2019). Ri PPLE: A crowdsourced adaptive platform 
for recommendation of learning activities. Journal of Learning Analytics, 6, 91–105. 
https://doi .org /10 .18608 /jla .2019 .63 .12.
Khosravi, H., Shum, S. B., Chen, G., Conati, C., Tsai, Y. S., Kay, J., Knight, S., Martinez-
Maldonado, R., Sadiq, S., & Gaševi´c, D. (2022). Explainable artiﬁcial intelligence in 
education. Computers and Education: Artiﬁcial Intelligence, 3, Article 100074.
Kim, G., Kim, J., & Kim, Y. S. (2023). “Explain what a treemap is”: Exploratory investi-
gation of strategies for explaining unfamiliar chart to blind and low vision users. In
Proceedings of the 2023 CHI conference on human factors in computing systems.
Kitto, K., Buckingham Shum, S., & Gibson, A. (2018). Embracing imperfection in learning 
analytics. In LAK ‘18: Proc. of the 8th int. conf. on learning analytics and knowledge
(pp. 451–460). ACM.
Kivimäki, V., Pesonen, J., Romanoﬀ, J., Remes, H., & Ihantola, P. (2019). Curricular con-
cept maps as structured learning diaries: Collecting data on self-regulated learning 
and conceptual thinking for learning analytics applications. Journal of Learning Ana-
lytics, 6, 106–121. https://doi .org /10 .18608 /jla .2019 .63 .13.
Kloos, C. D., Dimitriadis, Y., Hernández-Leo, D., Alario-Hoyos, C., Martínez-Monés, A., 
Santos, P., Muñoz-Merino, P. J., Asensio-Pérez, J. I., & Safont, L. V. (2022). H2O learn 
- hybrid and human-oriented learning: Trustworthy and human-centered learning 
analytics (Ta HCLA) for hybrid education. In 2022 IEEE global engineering education 
conference (EDUCON) (pp. 94–101).
Labonte-Le Moyne, E., Leger, P. M., Robert, J., Babin, G., Charland, P., & Michon, J. F. 
(2017). Business intelligence serious game participatory development: Lessons from 
ERPsim for big data. Business Process Management Journal, 23, 493–505. https://doi .
org /10 .1108 /BPMJ -12 -2015 -0177.
Lallé, S., Taub, M., Mudrick, N. V., Conati, C., & Azevedo, R. (2017). The impact of stu-
dent individual diﬀerences and visual attention to pedagogical agents during learning with 
Meta Tutor. Artiﬁcial intelligence in education: Vol. 10331. Cham: Springer International 
Publishing (pp. 149–161).
Lang, C., & Davis, L. (2023). Learning analytics and stakeholder inclusion: What do we 
mean when we say “human-centered”? In LAK23: 13th international learning analytics 
and knowledge conference, ACM, Arlington TX USA (pp. 411–417).
Lawrence, L., Echeverria, V., Yang, K., Aleven, V., & Rummel, N. (2023). How teachers 
conceptualise shared control with an AI co-orchestration tool: A multiyear teacher-
centred design process. British Journal of Educational Technology, 00. https://doi .org /
10 .1111 /bjet .13372.
Lee, A., Luco, A., & Tan, S. (2023). A human-centric automated essay scoring and feedback 
system for the development of ethical reasoning. Educational Technology & Society, 26, 
147–159. https://doi .org /10 .30191 /ETS .202301 _26(1 ).0011.
Lee, E., Kamat, M., Temor, L., Schiafone, C., Fan, L., Liu, J., Coppin, P., Uribe-Quevedo, 
A., Ingino, R., Syed, A., Rojas, D., Lee, T., Perera, S., Dubrowski, A., & Sukhai, M. 
(2022). Prototyping a spatial skills AR authoring tool for partially sighted, blind, and 
sighted individuals. In 2022 IEEE games, entertainment, media conference.
Leitner, P., Khalil, M., & Ebner, M. (2017). Learning analytics in higher education—a 
literature review. In A. Peña-Ayala (Ed.), Learning analytics: Fundaments, applications, 
and trends: A view of the current state of the art to enhance e-learning. Studies in systems, 
decision and control (pp. 1–23). Springer International Publishing.
Li, S., & Gu, X. (2023). A risk framework for human-centered artiﬁcial intelligence in edu-
cation. Educational Technology & Society, 26, 187–202. https://www .jstor .org /stable /
48707976.
Liaqat, A., Munteanu, C., & Demmans Epp, C. (2021). Collaborating with mature En-
glish language learners to combine peer and automated feedback: A user-centered 
approach to designing writing support. International Journal of Artiﬁcial Intelligence in 
Education, 31, 638–679.
Lim, L. A., Gasevic, D., Matcha, W., Ahmad Uzir, N., & Dawson, S. (2021). Impact of 
learning analytics feedback on self-regulated learning: Triangulating behavioural logs 
with students’ recall. Association for Computing Machinery, 364–374. https://doi .org /
10 .1145 /3448139 .3448174.
Lin, C. C., Huang, A. Y. Q., & Lu, O. H. T. (2023). Artiﬁcial intelligence in intelligent 
tutoring systems toward sustainable education: A systematic review. Smart Learning 
Environments, 10, 41. https://doi .org /10 .1186 /s40561 -023 -00260 -y.
Long, Y., Aman, Z., & Aleven, V. (2015). Motivational design in an intelligent tutoring system 
that helps students make good task selection decisions. Artiﬁcial intelligence in education: 
Vol. 9112. Cham: Springer International Publishing (pp. 226–236).
Luckin, R., Underwood, J., du Boulay, B., Holmberg, J., Kerawalla, L., O’Connor, J., Smith, 
H., & Tunley, H. (2006). Designing educational systems ﬁt for use: A case study in 
the application of human centred design for aied. International Journal of Artiﬁcial 
Intelligence in Education, 16, 353–380.
Luo, J., & Zhang, S. (2022). Research on the design of project-based teaching & learning 
mode assisted by educational robot. In Proceedings of the 4th world symposium on 
software engineering (pp. 148–154).
Ma, S., Zhou, T., Nie, F., & Ma, X. (2022). Glancee: An adaptable system for instructors to 
grasp student learning status in synchronous online classes. In Proceedings of the 2022 
CHI conference on human factors in computing systems (pp. 1–25).
Macfadyen, L. P. (2022). Institutional implementation of learning analytics: Current state, 
challenges, and guiding frameworks. In C. Lang, G. Siemens, A. F. Wise, D. Gaševi´c, & 
A. Merceron (Eds.), The handbook of learning analytics (2 ed.) (pp. 173–186). So LAR. 
Section: 17.
Maguire, M. (2001). Methods to support human-centred design. International Journal of 
Human-Computer Studies, 55, 587–634. https://doi .org /10 .1006 /ijhc .2001 .0503.
Maier, U., & Klotz, C. (2022). Personalized feedback in digital learning environments: 
Classiﬁcation framework and literature review. Computers and Education: Artiﬁcial 
Intelligence, 3, Article 100080. https://doi .org /10 .1016 /j .caeai .2022 .100080.
Mangaroska, K., Sharma, K., Giannakos, M., Trætteberg, H., & Dillenbourg, P. (2018). 
Gaze insights into debugging behavior using learner-centred analysis. Association for 
Computing Machinery, 350–359. https://doi .org /10 .1145 /3170358 .3170386.
Markauskaite, L., Marrone, R., Poquet, O., Knight, S., Martinez-Maldonado, R., Howard, 
S., Tondeur, J., De Laat, M., Shum, S. B., Gaševi´c, D., et al. (2022). Rethinking the 
entwinement between artiﬁcial intelligence and human learning: What capabilities 
do learners need for a world with ai? Computers and Education: Artiﬁcial Intelligence, 
3, Article 100056.
Martinez, J. P. C., Catasus, M. G., & Fontanillas, T. R. (2020). Impact of using learning 
analytics in asynchronous online discussions in higher education. International Journal 
of Educational Technology in Higher Education, 17. https://doi .org /10 .1186 /s41239 -
020 -00217 -y.
Martinez-Maldonado, R. (2023). Human-centred learning analytics: Four challenges in 
realising the potential. Learning Letters, 1, 6. https://doi .org /10 .59453 /FIZJ7007. 
https://learningletters .org /index .php /learn /article /view /6.
Martinez-Maldonado, R., Pardo, A., Mirriahi, N., Yacef, K., Kay, J., & Clayphan, A. (2015). 
The LATUX workﬂow: Designing and deploying awareness tools in technology-
enabled learning settings. Association for Computing Machinery, 1–10. https://doi .org /
10 .1145 /2723576 .2723583.
Mavrikis, M., & Cukurova, M. (2021). Same, same but diﬀerent: The fading boundaries be-
tween LA and AIED.
Mcneill, G., Sondag, M., Powell, S., Asplin, P., Turkay, C., Moller, F., & Archambault, 
D. (2023). From asymptomatics to zombies: Visualization-based education of disease 
modeling for children. In Proceedings of the 2023 CHI conference on human factors in 
computing systems.
Michos, K., Lang, C., Hernandez-Leo, D., & Price-Dennis, D. (2020). Involving teachers in 
learning analytics design: Lessons learned from two case studies. In Proceedings of the 
10th international conference on learning analytics & knowledge (pp. 94–99).
Moore, J. W. (2016). What is the sense of agency and why does it matter? Frontiers in 
Psychology, 7, 1272. https://doi .org /10 .3389 /fpsyg .2016 .01272.
Moya, B., Eaton, S. E., Pethrick, H., Hayden, K. A., Brennan, R., Wiens, J., Mc Dermott, B., 
& Lesage, J. (2023). Academic integrity and artiﬁcial intelligence in higher education 
contexts: A rapid scoping review protocol. Canadian Perspectives on Academic Integrity, 
5, 59–75.
Muldner, K., Lozano, C., Girotto, V., Burleson, W., & Walker, E. (2013). Designing a tangible 
learning environment with a teachable agent. Artiﬁcial intelligence in education: Vol. 7926. 
Berlin, Heidelberg: Springer Berlin Heidelberg (pp. 299–308).
Muslim, A., Chatti, M. A., Mahapatra, T., & Schroeder, U. (2016). A rule-based indicator 
deﬁnition tool for personalized learning analytics. Association for Computing Machin-
ery, 264–273. https://doi .org /10 .1145 /2883851 .2883921.
Nazaretsky, T., Ariely, M., Cukurova, M., & Alexandron, G. (2022). Teachers’ trust in AI-
powered educational technology and a professional development program to improve 
it. British Journal of Educational Technology, 53, 914–931. https://doi .org /10 .1111 /
bjet .13232.
Nazaretsky, T., Bar, C., Walter, M., & Alexandron, G. (2022). Empowering teachers with 
AI: Co-designing a learning analytics tool for personalized instruction in the science 
classroom. In ACM international conference proceeding series (pp. 1–12).
Nazaretsky, T., Cukurova, M., & Alexandron, G. (2022). An instrument for measuring 
teachers’ trust in AI-based educational technology. In LAK22: 12th international learn-
ing analytics and knowledge conference (pp. 56–66). ACM. Online USA.
Ngoon, T. J., Kovalev, D., Patidar, P., Harrison, C., Agarwal, Y., Zimmerman, J., & Ogan, 
A. (2023). “An instructor is [already] able to keep track of 30 students”: Students’ per-
ceptions of smart classrooms for improving teaching & their emergent understandings 
of teaching and learning. In Proceedings of the 2023 ACM designing interactive systems 
conference (pp. 1277–1292). Pittsburgh PA USA: ACM.
Nguyen, Q., Rienties, B., & Whitelock, D. (2020). A mixed-method study of how instruc-
tors design for learning in online and distance education. Journal of Learning Analytics, 
7, 64–78. https://doi .org /10 .18608 /JLA .2020 .73 .6.
Ochoa, X., & Dominguez, F. (2020). Controlled evaluation of a multimodal system to 
improve oral presentation skills in a real learning setting. British Journal of Educational 
Technology, 51, 1615–1630. https://doi .org /10 .1111 /bjet .12987.
Ochoa, X., Domínguez, F., Guamán, B., Maya, R., Falcones, G., & Castells, J. (2018). 
The RAP system: Automatic feedback of oral presentation skills using multimodal 
analysis and low-cost sensors. In LAK ’18: International conference on learning analytics 
and knowledge (pp. 360–364). ACM.
Ocumpaugh, J., Baker, R. S., Pedro, M. O. C. Z. S., Hawn, M. A., Heﬀernan, C., Heﬀernan, 
N., & Slater, S. A. (2017). Guidance counselor reports of the ASSISTments college 
prediction model (ACPM). In Proceedings of the 7th international conference on learning 
analytics & knowledge (pp. 479–488).

--- Page 22 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
Oliver-Quelennec, K., Bouchet, F., Carron, T., Fronton Casalino, K., & Pinçon, C. 
(2022). Adapting learning analytics dashboards by and for university students. LNCS: 
Vol. 13450.
Olsen, J. K., Rummel, N., & Aleven, V. (2021). Designing for the co-orchestration of social 
transitions between individual, small-group and whole-class learning in the class-
room. International Journal of Artiﬁcial Intelligence in Education, 31, 24–56. https://
doi .org /10 .1007 /s40593 -020 -00228 -w.
Onnasch, L., Wickens, C. D., Li, H., & Manzey, D. (2014). Human performance con-
sequences of stages and levels of automation: An integrated meta-analysis. Human 
Factors, 56, 476–488. https://doi .org /10 .1177 /0018720813501549.
Ooge, J., Dereu, L., & Verbert, K. (2023). Steering recommendations and visualising its 
impact: Eﬀects on adolescents’ trust in E-learning platforms. In Proceedings of the 28th 
international conference on intelligent user interfaces (pp. 156–170).
Ozmen Garibay, O., Winslow, B., Andolina, S., Antona, M., Bodenschatz, A., Coursaris, 
C., Falco, G., Fiore, S. M., Garibay, I., Grieman, K., et al. (2023). Six human-centered 
artiﬁcial intelligence grand challenges. International Journal of Human-Computer Inter-
action, 1–47.
Page, M. J., Mc Kenzie, J. E., Bossuyt, P. M., Boutron, I., Hoﬀmann, T. C., Mulrow, C. 
D., Shamseer, L., Tetzlaﬀ, J. M., Akl, E. A., Brennan, S. E., Chou, R., Glanville, J., 
Grimshaw, J. M., Hróbjartsson, A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson, 
E., Mc Donald, S., . . . Moher, D. (2021). The PRISMA 2020 statement: An updated 
guideline for reporting systematic reviews. BMJ, 372(71). https://doi .org /10 .1136 /
bmj .n71.
Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of 
human interaction with automation. IEEE Transactions on Systems, Man and Cybernet-
ics. Part A. Systems and Humans, 30, 286–297. https://doi .org /10 .1109 /3468 .844354.
Pardo, A., & Siemens, G. (2014). Ethical and privacy principles for learning analytics. 
British Journal of Educational Technology, 45, 438–450. https://doi .org /10 .1111 /bjet .
12152.
Pinski, M., Adam, M., & Benlian, A. (2023). AI knowledge: Improving AI delegation 
through human enablement. In Proceedings of the 2023 CHI conference on human fac-
tors in computing systems (pp. 1–17). Hamburg Germany: ACM.
Pishtari, G., Rodríguez-Triana, M., & Väljataga, T. (2021). A multi-stakeholder perspective 
of analytics for learning design in location-based learning. International Journal of 
Mobile and Blended Learning, 13, 1–17. https://doi .org /10 .4018 /IJMBL .2021010101.
Pozdniakov, S., Martinez-Maldonado, R., Tsai, Y. S., Cukurova, M., Bartindale, T., Chen, 
P., Marshall, H., Richardson, D., & Gasevic, D. (2022). The question-driven dash-
board: How can we design analytics interfaces aligned to teachers’ inquiry? In ACM 
international conference proceeding series (pp. 175–185).
Prestigiacomo, R., Hadgraft, R., Hunter, J., Locker, L., Knight, S., Van Den Hoven, E., 
& Martinez-Maldonado, R. (2020). Learning-centred translucence: An approach to 
understand how teachers talk about classroom data. In Proceedings of the tenth inter-
national conference on learning analytics & knowledge (pp. 100–105).
Prieto, L. P., Rodríguez-Triana, M. J., Martínez-Maldonado, R., Dimitriadis, Y., & Gaševi´c, 
D. (2019). Orchestrating learning analytics (orla): Supporting inter-stakeholder com-
munication about adoption of learning analytics at the classroom level. Australasian 
Journal of Educational Technology, 35.
Prieto-Alvarez, C. G., Martinez-Maldonado, R., & Anderson, T. D. (2018). Co-designing 
learning analytics tools with learners. In J. Lodge, K. Thompson, J. Horvath, P. De 
Barba, & M. Blumenstein (Eds.), Learning analytics in the classroom (pp. 93–110). Rout-
ledge.
Rapp, C., & Kauf, P. (2018). Scaling academic writing instruction: Evaluation of a scaf-
folding tool (thesis writer). Journal of Artiﬁcial Intelligence in Education, 28, 590–615. 
https://doi .org /10 .1007 /s40593 -017 -0162 -z.
Read, S., Dela Merced, A., & Zachry, M. (2012). Participatory design in the develop-
ment of a web-based technology for visualizing writing activity as knowledge work.
In Proceedings of the 30th ACM international conference on design of communication
(pp. 333–340).
Reimann, P. (2016). Connecting learning analytics with learning research: The role of 
design-based research. Routledge, 2, 130–142. https://doi .org /10 .1080 /23735082 .
2016 .1210198.
Renz, A., & Vladova, G. (2021). Reinvigorating the discourse on human-centered artiﬁcial 
intelligence in educational technologies. Technology Innovation Management Review, 
11, 5–16. https://doi .org /10 .22215 /timreview /1438.
Rienties, B., Køhler Simonsen, H., & Herodotou, C. (2020). Deﬁning the boundaries be-
tween artiﬁcial intelligence in education, computer-supported collaborative learning, 
educational data mining, and learning analytics: A need for coherence. Frontiers in 
Education, 5.
Rodrigues, L., Palomino, P., Toda, A., Klock, A., Pessoa, M., Pereira, F., Oliveira, E., 
Oliveira, D., Cristea, A., Gasparini, I., & Isotani, S. (2023). How personalization af-
fects motivation in gamiﬁed review assessments. Journal of Artiﬁcial Intelligence in 
Education. https://doi .org /10 .1007 /s40593 -022 -00326 -x.
Rodríguez-Triana, M., Prieto, L., Dimitriadis, Y., de Jong, T., & Gillet, D. (2021). Ada 
for ibl: Lessons learned in aligning learning design and analytics for inquiry-based 
learning orchestration. Journal of Learning Analytics, 8, 22–50. https://doi .org /10 .
18608 /JLA .2021 .7357.
Ruiz-Calleja, A., Dennerlein, S., Kowald, D., Theiler, D., Lex, E., & Ley, T. (2019). An 
infrastructure for workplace learning analytics: Tracing knowledge creation with the 
social semantic server. Journal of Learning Analytics, 6, 120–139. https://doi .org /10 .
18608 /jla .2019 .62 .9.
Santos, J. L., Govaerts, S., Verbert, K., & Duval, E. (2012). Goal-oriented visualizations of 
activity tracking: A case study with engineering students. Association for Computing 
Machinery, 143–152. https://doi .org /10 .1145 /2330601 .2330639.
Sarmiento, J. P., Campos, F., & Wise, A. (2020). Engaging students as co-designers of 
learning analytics. In Companion proceedings of the 10th international learning analytics 
and knowledge conference (pp. 29–32). Frankfurt: So LAR.
Sarmiento, J. P., & Wise, A. F. (2022). Participatory and co-design of learning analytics: 
An initial review of the literature. In LAK22: 12th international learning analytics and 
knowledge conference (pp. 535–541).
Sato, A. J., Sramek, Z., & Yatani, K. (2023). Groupnamics: Designing an interface for 
overviewing and managing parallel group discussions in an online classroom. In Pro-
ceedings of the 2023 CHI conference on human factors in computing systems.
Schmitz, M., Scheﬀel, M., Bemelmans, R., & Drachsler, H. (2022). Fola 2–a method for co-
creating learning analytics-supported learning design. Journal of Learning Analytics, 9, 
265–281.
Schulz, S., Mc Laren, B., & Pinkwart, N. (2022). Towards a tutoring system to support 
robotics activities in classrooms – two wizard-of-oz studies. Journal of Artiﬁcial Intel-
ligence in Education, 33, 688–719. https://doi .org /10 .1007 /s40593 -022 -00305 -2.
Shardlow, M., Sellar, S., & Rousell, D. (2022). Collaborative augmentation and simpli-
ﬁcation of text (Co AST): Pedagogical applications of natural language processing in 
digital learning environments. Learning Environments Research, 25, 399–421.
Shetty, S. V., Guruvyas, K. R., Patil, P. P., & Acharya, J. J. (2022). Essay scoring systems 
using AI and feature extraction: A review, in: Proceedings of third international conference 
on communication, computing and electronics systems. Singapore: Springer (pp. 45–57).
Shibani, A., Knight, S., & Buckingham Shum, S. (2022). Questioning learning analytics? 
Cultivating critical engagement as student automated feedback literacy. In LAK22: 
12th international learning analytics and knowledge conference (pp. 326–335).
Shneiderman, B. (2020a). Bridging the gap between ethics and practice: Guidelines for 
reliable, safe, and trustworthy human-centered ai systems. ACM Transactions on Inter-
active Intelligent Systems (Tii S), 10, 1–31.
Shneiderman, B. (2020b). Human-centered artiﬁcial intelligence: Three fresh ideas. AIS 
Transactions on Human-Computer Interaction, 109–124. https://doi .org /10 .17705 /
1thci .00131.
Shneiderman, B. (2021). Human-centered AI. Issues Science Technology, 37, 56–61.
Shneiderman, B. (2022). Human-centered AI. Oxford, New York: Oxford University Press.
Shreiner, T., & Guzdial, M. (2022). The information won’t just sink in: Helping teachers 
provide technology-assisted data literacy instruction in social studies. British Journal 
of Educational Technology, 53, 1134–1158. https://doi .org /10 .1111 /bjet .13255.
Shute, V., Smith, G., Kuba, R., Dai, C. P., Rahimi, S., Liu, Z., & Almond, R. (2021). The 
design, development, and testing of learning supports for the physics playground 
game. Journal of Artiﬁcial Intelligence in Education, 31, 357–379. https://doi .org /10 .
1007 /s40593 -020 -00196 -1.
da Silva, F. L., Slodkowski, B. K., da Silva, K. K. A., & Cazella, S. C. (2023). A systematic 
literature review on educational recommender systems for teaching and learning: 
Research trends, limitations and opportunities. Education Information Technology, 28, 
3289–3328. https://doi .org /10 .1007 /s10639 -022 -11341 -9.
Slade, S., & Prinsloo, P. (2013). Learning analytics: Ethical issues and. Dilemmas, 57, 
1510–1529. https://doi .org /10 .1177 /0002764213479366.
Soreny, C., Takhar, P., Vickers, E., Bartlett, R., Coates, E., Stavroulakis, T., Fox, E., David-
son, H., Harrison, A., & Mc Dermott, C. (2022). Co-design of digital learning resources 
for care workers: Reﬂections on the neurocare knowhow project. Journal of Medi-
cal Engineering & Technology, 46, 518–526. https://doi .org /10 .1080 /03091902 .2022 .
2089253.
Suleman, R., Mizoguchi, R., & Ikeda, M. (2016). A new perspective of negotiation-based 
dialog to enhance metacognitive skills in the context of open learner models. Journal 
of Artiﬁcial Intelligence in Education, 26, 1069–1115. https://doi .org /10 .1007 /s40593 -
016 -0118 -8.
Swiecki, Z., Khosravi, H., Chen, G., Martinez-Maldonado, R., Lodge, J. M., Milligan, S., 
Selwyn, N., & Gaševi´c, D. (2022). Assessment in the age of artiﬁcial intelligence. 
Computers and Education: Artiﬁcial Intelligence, 3, Article 100075.
Tegos, S., Demetriadis, S., & Tsiatsos, T. (2014). A conﬁgurable conversational agent to 
trigger students’ productive dialogue: A pilot study in the CALL domain. Journal of 
Artiﬁcial Intelligence in Education, 24, 62–91. https://doi .org /10 .1007 /s40593 -013 -
0007 -3.
Tenório, K., Dermeval, D., Monteiro, M., Peixoto, A., & Silva, A. (2022). Exploring design 
concepts to enable teachers to monitor and adapt gamiﬁcation in adaptive learning 
systems: A qualitative research approach. Journal of Artiﬁcial Intelligence in Education, 
32, 867–891. https://doi .org /10 .1007 /s40593 -021 -00274 -y.
Ternblad, E. M., Haake, M., Anderberg, E., & Gulz, A. (2018). Do preschoolers ‘game the sys-
tem’? A case study of children’s intelligent (mis)use of a teachable agent based play-&-learn 
game in mathematics. Artiﬁcial intelligence in education: Vol. 10947. Cham: Springer In-
ternational Publishing (pp. 557–569).
Tissenbaum, M., & Slotta, J. (2019). Supporting classroom orchestration with real-time 
feedback: A role for teacher dashboards and real-time agents. International Journal 
of Computer-Supported Collaborative Learning, 14, 325–351. https://doi .org /10 .1007 /
s11412 -019 -09306 -1.
Topali, P., Ortega-Arranz, A., Chounta, I. A., Asensio-Perez, J. I., Martinez-Mones, A., & 
Villagra-Sobrino, S. L. (2022). Supporting instructors in the design of actionable feed-
back for MOOCs. In Proceedings of the 2022 IEEE global engineering education conference
(pp. 1881–1887).

--- Page 23 ---

Computers and Education: Artificial Intelligence 6 (2024) 100215

R. Alfredo, V. Echeverria, Y. Jin et al.
Treasure-Jones, T., Dent-Spargo, R., & Dharmaratne, S. (2018). How do students want 
their workplace-based feedback visualized in order to support self-regulated learning? 
Initial results & reﬂections from a co-design study in medical education. In CEUR 
workshop proceedings.
Tsai, Y. S., Perrotta, C., & Gaševi´c, D. (2020). Empowering learners with personalised 
learning approaches? Agency, equity and transparency in the context of learning an-
alytics. Assessment & Evaluation in Higher Education, 45, 554–567.
Tsai, Y. S., Singh, S., Rakovic, M., Lim, L. A., Roychoudhury, A., & Gasevic, D. (2022). 
Charting design needs and strategic approaches for academic analytics systems through 
co-design. ACM international conference proceeding series (pp. 381–391).
Usmani, U. A., Happonen, A., & Watada, J. (2023). Human-centered artiﬁcial intelligence: 
Designing for user empowerment and ethical considerations. In 2023 5th international 
congress on human-computer interaction, optimization and robotic applications (HORA)
(pp. 01–05). Istanbul, Turkiye: IEEE.
Uttamchandani, S., & Quick, J. (2022). An introduction to fairness, absence of bias, and 
equity in learning analytics. In C. Lang, G. Siemens, A. F. Wise, D. Gaševi´c, & A. 
Merceron (Eds.), The handbook of learning analytics (2 ed.) (pp. 205–212). So LAR. 
https://www .solaresearch .org /publications /hla -22 /hal22 -chapter20/. section: 20.
Vannaprathip, N., Haddawy, P., Schultheis, H., & Suebnukarn, S. (2022). Intelligent tu-
toring for surgical decision making: A planning-based approach. Journal of Artiﬁcial 
Intelligence in Education, 32, 350–381. https://doi .org /10 .1007 /s40593 -021 -00261 -3.
Vezzoli, Y., Mavrikis, M., & Vasalou, A. (2020). Inspiration cards workshops with primary 
teachers in the early co-design stages of learning analytics. In Proceedings of the 10th 
international conference on learning analytics & knowledge (pp. 73–82).
Viberg, O., Jivet, I., & Scheﬀel, M. (2023). Designing culturally aware learning analytics: A 
value sensitive perspective. Cham: Springer International Publishing (pp. 177–192).
Viberg, O., Mutimukwe, C., & Grönlund, Å. (2022). Privacy in la research: Understanding 
the ﬁeld to improve the practice. Journal of Learning Analytics, 9, 169–182.
Vinella, F., Koppelaar, S., & Masthoﬀ, J. (2022). Forming teams of learners online in 
a user as wizard study with openness, conscientiousness, and cognitive ability. In
UMAP2022 - adjunct proceedings of the 30th ACM conference on user modeling, adapta-
tion and personalization (pp. 283–292).
Wang, Q., Jing, S., & Goel, A. (2022). Co-designing AI agents to support social connectedness 
among online learners: Functionalities, social characteristics, and ethical challenges In DIS 
2022 - proceedings of the 2022 ACM designing interactive systems conference: Digital 
Wellbeing (pp. 541–556).
Wang, Y., Nguyen, H., Harpstead, E., Stamper, J., & Mc Laren, B. M. (2019). How does 
order of gameplay impact learning and enjoyment in a digital learning game? Artiﬁ-
cial intelligence in education: Vol. 11625. Cham: Springer International Publishing 
(pp. 518–531).
Weigand, A., & Kindsmüller, M. (2021). HCD3A: An HCD model to design data-driven 
Apps. LNAI: Vol. 12797.
Wiley, K., Dimitriadis, Y., & Linn, M. (2023). A human-centred learning analytics approach 
for developing contextually scalable K-12 teacher dashboards.
Williamson, K., & Kizilcec, R. (2022). A review of learning analytics dashboard research in 
higher education: Implications for justice, equity, diversity, and inclusion. In LAK22: 
12th international learning analytics and knowledge conference (pp. 260–270).
Williamson, K., & Kizilcec, R. F. (2021). Learning analytics dashboard research has ne-
glected diversity, equity and inclusion. In Proceedings of the eighth ACM conference on 
learning@ scale (pp. 287–290).
Wilson, J., Huang, Y., Palermo, C., Beard, G., & Mac Arthur, C. (2021). Automated feed-
back and automated scoring in the elementary grades: Usage, attitudes, and associa-
tions with writing outcomes in a districtwide implementation of MI write. Journal of 
Artiﬁcial Intelligence in Education, 31, 234–276. https://doi .org /10 .1007 /s40593 -020 -
00236 -w.
Wise, A. F., Sarmiento, J. P., & Boothe Jr, M. (2021). Subversive learning analytics. In
LAK21: 11th international learning analytics and knowledge conference (pp. 639–645).
Xu, W., Dainoﬀ, M. J., Ge, L., & Gao, Z. (2023). Transitioning to human interaction with 
AI systems: New challenges and opportunities for HCI professionals to enable human-
centered AI. International Journal of Human-Computer Interaction, 39, 494–518.
Yan, L., Zhao, L., Gasevic, D., & Martinez-Maldonado, R. (2022). Scalability, sustainabil-
ity, and ethicality of multimodal learning analytics. In LAK22: LAK22: 12th interna-
tional learning analytics and knowledge conference (pp. 13–23). New York, NY, USA: 
Association for Computing Machinery.
Yang, S. J. H., Ogata, H., Matsui, T., & Chen, N. S. (2021). Human-centered artiﬁcial 
intelligence in education: Seeing the invisible through the visible. Computers and Ed-
ucation: Artiﬁcial Intelligence, 2. https://doi .org /10 .1016 /j .caeai .2021 .100008.
Zhang, K., & Aslan, A. B. (2021). AI technologies for education: Recent research & future 
directions. Computer Education Artiﬁcial Intelligence, 2, Article 100025. https://doi .
org /10 .1016 /j .caeai .2021 .100025. https://www .sciencedirect .com /science /article /
pii /S2666920X21000199.
Zhang, Z., Xu, Y., Wang, Y., Yao, B., Ritchie, D., Wu, T., Yu, M., Wang, D., & Li, T. 
J. (2022). Story Buddy: A human-AI collaborative chatbot for parent-child interac-
tive storytelling with ﬂexible parental involvement. In Conference on human factors in 
computing systems - proceedings.
Zhao, F., Liu, G. Z., Zhou, J., & Yin, C. (2023). A learning analytics framework based on 
human-centered artiﬁcial intelligence for identifying the optimal learning strategy 
to intervene in learning behavior. Journal of Artiﬁcial Intelligence in Education, 26, 
132–146. https://www .jstor .org /stable /48707972. http://arxiv .org /abs /48707972.
Zhou, Q., Suraworachet, W., Pozdniakov, S., Martinez-Maldonado, R., Bartindale, T., 
Chen, P., Richardson, D., & Cukurova, M. (2021). Investigating students’ experiences 
with collaboration analytics for remote group meetings. LNAI: Vol. 12748.
Zwolinski, G., Kaminska, D., Laska-Lesniewicz, A., Haamer, R. E., Vairinhos, M., Ra-
poso, R., Urem, F., & Reisinho, P. (2022). Extended reality in education and train-
ing: Case studies in management education. Electronics, 11. https://doi .org /10 .3390 /
electronics11030336.
