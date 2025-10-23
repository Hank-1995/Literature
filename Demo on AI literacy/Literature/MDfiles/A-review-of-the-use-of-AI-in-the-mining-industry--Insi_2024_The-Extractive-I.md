# A review of the use of AI in the mining industry: Insights and ethical considerations for multi-objective optimization

## Metadata
- **Author**: Caitlin C. Corrigan
- **Subject**: The Extractive Industries and Society, 17 (2024) 101440. doi:10.1016/j.exis.2024.101440
- **Creator**: Elsevier
- **Producer**: Acrobat Distiller 8.1.0 (Windows)
- **Creation Date**: D:20240401071149Z
- **Modification Date**: D:20240401084304Z
- **Source File**: A-review-of-the-use-of-AI-in-the-mining-industry--Insi_2024_The-Extractive-I.pdf
- **Converted**: 2025-10-23 22:46:11

---

## Content

--- Page 1 ---

The Extractive Industries and Society 17 (2024) 101440
Available online 14 March 2024
2214-790X/© 2024 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).
Review article 
A review of the use of AI in the mining industry: Insights and ethical 
considerations for multi-objective optimization 
Caitlin C. Corrigan a,*, Svetlana A. Ikonnikova b,c 
a Technical University of Munich, School of Social Science and Technology, Institute for Ethics in Artificial Intelligence, Arcisstraße 21, 80333 München, Germany 
b Technical University of Munich, School of Management, Center for Energy Markets, Arcisstraße 21, 80333 München, Germany 
c Bureau of Economic Geology, Jackson School of Geosciences, the University of Texas at Austin, 10611 Exploration Way, Austin, TX 78758, USA   
A R T I C L E  I N F O   
Keywords: 
Artificial intelligence 
Mining industry 
Multi-objective optimization 
AI Ethics 
Sustainability 
Global South 
A B S T R A C T   
In the effort to rapidly transform the way we use energy, valuable minerals are coming increasingly into high 
demand. Various metals, such as copper and cobalt, are required to advance new technologies and accelerate the 
lowering of carbon emissions. However, their extraction often comes with high societal and environmental costs. 
Therefore, developing ways to extract valuable minerals in a way that benefits global as well as an individual 
country’s sustainability goals and mitigates direct and indirect negative impacts of extraction, is a worthwhile 
endeavor. Artificial intelligence (AI) enabled applications provide one avenue by which to potentially speed up 
this process. The question remains, how do we ensure AI is used in an ethical way that benefits communities, 
societal development, and environmental sustainability in the mining industry? In this article we give an 
overview of current and potential uses of AI in the mining sector and present some ethical considerations for the 
use of AI in the industry. We then outline a way forward to a more ethical and sustainable approach to using AI in 
the mining sector through multi-objective optimization.   
1. Introduction 
The transition to clean energy and a more sustainable future requires 
the transformation of existing energy systems and industrial processes, 
which translates into a multifold increase in metals and minerals con-
sumption (IEA, 2021;Mackenzie, 2020). To realize the plans for elec-
trification of transport, power, and heat sectors, and for deployment of 
fossil-fuel-based alternatives, the expansion of mining operations is 
needed to meet the growing demand for copper, cobalt, nickel, lithium, 
and other earth resources. To help finance and accelerate the supply 
capacity growth, the EU has even proposed to add copper and nickel to 
the list of critical raw materials (Burton, 2023). However, whereas metal 
and mineral resources should help address the climate change and 
environmental problems brought by the utilization of fossil fuels, their 
extraction is often associated with water, land, and air pollution, health 
problems, and other issues (Adler et al., 2007; Ayuk et al., 2020; Bolger 
et al., 2021). Although the total land footprint estimates vary depending 
on the methodology applied, the most recent global mining assessments 
suggest that close to 100,000 km2, or an area larger than Portugal or 
South Korea, has been used for mining or mining associated activities, 
such as waste dumps, across 135 countries (Tang and Werner, 2023). 
Moreover, over 50 % of current mining sites1 and deposits are 
located in politically unstable and economically poor countries of South 
America, Africa, and Asia, or the ‘Global South’ group.2 In many loca-
tions, counterintuitively, the growth in production correlates with acute 
social and economic challenges, threatening the ability of poor and 
underdeveloped countries to follow the sustainable development path 
(L`ebre et al., 2020; Sengupta, 2021; UNEP, 2019). The often termed 
‘resource curse’ phenomenon, wherein valuable-resource-rich countries 
experience exploitation, environmental degradation, detrimental health 
effects, and in some cases a worsening of a country’s economic situation 
(Collier, 2007; Humphreys et al., 2007; Oduyemi et al., 2021; Sachs and 
Warner, 2001; Sala-i-Martin and Subramanian, 2003) is a major concern 
because the mining industry will only continue to grow as the energy 
* Corresponding author at: Arcisstr. 21 80333 Munich, Germany. 
E-mail address: c.corrigan@tum.de (C.C. Corrigan).   
1 Based on the global mining site (geo-polygon) data presented in the open database by www.fineprint.global.  
2 In this paper, we adopt the United Nations Finance Center for South-South Cooperation’s nomenclature on the division of countries to Global South and Global 
North, underlying the UN Sustainability and Mineral Resource Governance reporting (UNEP, 2022). Notably, the list of Global South countries coincides with the 
members of Group 77, formed to promote their collective economic prosperity. 
Contents lists available at Science Direct 
The Extractive Industries and Society 
journal homepage: www.elsevier.com/locate/exis 
https://doi.org/10.1016/j.exis.2024.101440    

--- Page 2 ---

The Extractive Industries and Society 17 (2024) 101440

transition progresses. 
Besides the climate-related considerations, there is an important 
economic development and value argument that urges mining growth. 
Resource extraction is a strong contributor to the economic sustain-
ability of 81 countries (United Nations, 2021), of which 63 % are low- 
and middle-income countries whose their national budgets increasingly 
depend on resource production revenues (Roe, 2016). For example, 
mining provides almost 50 % of the government’s revenues and gener-
ates over 99 % of the exports revenues in the Democratic Republic of 
Congo3 (DRC), the country expected to control as much as 80 % of the 
global supply of cobalt by mid-decade (Mackenzie, 2020). 
Yet, despite observed negative impacts of mineral extraction, the 
energy transition must advance quickly and efficiently in light of rising 
Earth temperatures and associated dangers (IPCC, 2023). The pressing 
question is: are there ways to (i) extract valuable resources to achieve global 
sustainability goals (United Nations, 2021) and (ii) mitigate the negative 
(direct and indirect) impacts of extraction that fall on the mining dependent 
countries? 
Such a large-scope and multifaceted question calls for an approach 
powerful enough to perform a complex system analysis and to run 
simulations of future developments, capturing nonlinear time-varying 
behavior of the involved parties. Recent advances in methods for opti-
mization and simulations highlight artificial intelligence (AI) capabil-
ities and AI-enabled applications as a promising tool for identifying a 
development venue leading to the desired outcome (Barmer et al., 2021; 
Mirjalili and Dong, 2020; Xu et al., 2021). Improvements in computa-
tional abilities and data availability empower AI algorithms and lead to 
a new era of AI-based research. The fast-growing body of research shows 
that machine-learning (ML) and AI-driven approaches may enhance 
mining economics. Superior in data mining and analytics, AI algorithms 
used for projections and simulations help people choose the best pat-
terns of behavior and management practices, boosting productivity, 
optimizing operations, and increasing profitability (Jung and Choi, 
2021; Kumar and Dimitrakopoulos, 2021; Noriega and Pourrahimian, 
2022; Sircar et al., 2021).4 
The benefits of using the same models and approaches for achieving 
environmental sustainability and/or social justice, however, are obscure 
and questionable (Dauvergne, 2021, 2022; Francisco, 2023; Halpern, 
2021). Along with the worries regarding the narrow focus and, thereby, 
impact of AI solutions, scientists and the general public have raised 
concerns about the ethics of AI solutions (Boddington, 2017; Hickok, 
2021; Jobin et al., 2019; Srikumar et al., 2022). Debates on the subject, 
namely on the guidelines and principles for conducting research and 
using AI applications, signal that consensus has not yet been reached and 
that the developed recommendations have not spread far (Chatila and 
Havens 2019; Hagendorff, 2020). It is important to also note that while 
much of the increase in mining activities, and therefore related AI use, 
occurs in “developing” countries of the Global South, a prevailing body 
of the frameworks mentioned above have been established by the 
“developed” members of the Global North region, appealing to its ethics, 
community values, and political and institutional capabilities (Amu-
gongo et al., 2023; Corrigan et al., 2023; Eke et al., 2023). The differ-
ences in cultural perspectives, immediate needs, technical capabilities, 
and institutional capacities of the two regions have given rise to the 
debate over the use and design of AI-enabled tools and associated data. 
Along with the necessity to recognize those distinctions comes the need 
for review of where, with which tools, and how AI can be employed. 
In this context, driven by the question of how AI approaches can help 
communities in societal development, environmental sustainability, and 
economic growth when it comes to the mining industry, we discuss the 
use and applicability of AI in the mining sector, what ethical consider-
ations need to be discussed alongside the use, and how multi-objective 
optimization, as an approach, has the potential to use AI to provide a 
more sustainable, in terms of the UN’s definition, pathway forward in 
this important industry. 
2. Overview of AI in mining 
Formulated at the United Nations summit in Rio de Janeiro in 2012, 
the seventeen UN Sustainable Development Goals (SDGs) set the ob-
jectives for the balanced economic, societal, and environmental devel-
opment needed for achieving equity and prosperity on a global or 
planetary level. The comprehensive system of SDG indicators helps track 
an individual country’s, but not industry’s, progress. The industry sus-
tainability taxonomy substituted by the environmental, social, and 
governance (ESG) reporting lacks clarity, transparency, and interna-
tional consistency. Therefore, in this section, we outline the need for 
innovative solutions for making mining sustainable in the ‘global’ UN 
SDGs sense. We review the current state of the mining industry, 
particularly in the countries of the Global South that are falling far 
behind on their SDGs, and we point out the scope of changes needed and 
the associated complexity that calls for the use of powerful AI algo-
rithms. Next, we take a general view on mining processes and discuss 
how AI-based approaches may help with particular operations and de-
cisions. We purposely focus on the opportunities for AI applications, 
leaving the discussion of the associated ethical challenges for Section 3. 
2.1. Background 
To mitigate climate change, which is threatening human populations 
around the world, countries should cooperate in reducing greenhouse 
gas (GHG) emissions and switching to clean energy technologies (IPCC, 
2023). The solutions, such as adopting battery-based electric vehicles or 
increasing large-scale offshore and onshore wind power generation, 
however, requires a manifold increase in metals and minerals supply.5 
According to the International Energy Agency (IEA, 2022), by 2040 the 
world demand for nickel and cobalt may grow 20 times, for lithium close 
to 40 times, and for copper 2.6 times (IEA, 2021). The resource-use 
projections draw attention to locations of sizable geologic deposits 
and mining, prevalent in the countries of the Global South6 with a 
combination of economic, environmental, and political problems 
(Hoggard et al., 2020; Nakajima et al., 2018). According to estimates by 
the United Nations Environment group (UNEP, 2016, 2019), African 
countries alone are home to at least 30 % of the world’s mineral re-
serves. This raises a critical question of whether such developments will 
bring low-income and resource-rents-dependent economies more pros-
perity and improvements along multiple axes of sustainability or instead 
will deepen the often-cited “resource curse”. 
To understand why AI algorithms, applications, and their design are 
of great value and importance in the mining industry, consider the SDGs’ 
multidimensionality and complex interdependencies. Embracing eco-
nomic, social, and environmental aspects of an individual country’s 
development, the system of SDG indicators and SDG-Tracker allows for 
3 According to the Extractive Industries Transparency Initiative (EITI) open 
database https://eiti.org/open-data.  
4 Note that machine learning is a branch of AI, primarily concerned with the 
analysis of large sets of data. The explicit mentioning of ML is used to 
emphasize the role of data and research in data analytics. 
5 Based on https://www.iea.org/data-and-statistics/charts/minerals-used-in- 
electric-cars-compared-to-conventional-cars,licence: CC BY 4.0  
6 Despite the controversy around the origin and use of the term ‘Global 
South’, as marked by Pagel et al. (2014), it is extensively used to refer to the 
developing countries of Africa, the Middle East, Asia, Oceania, and Latin 
America. We use the term following the United Nations’ nomenclature, 
denoting the countries having severe economic and political concerns but rich 
in natural resources (UNEP, 2022). 
C.C. Corrigan and S.A. Ikonnikova                                                                                                                                                                                                         

--- Page 3 ---

The Extractive Industries and Society 17 (2024) 101440

quantitative analyses of progress and cross-country comparisons 
(Horan, 2020; Schmidt-Traub et al., 2017). For instance, the World Bank 
statistics7 on mining and the UN SDG data reveal that while the DRC’s 
natural resource rents and GDP increase, largely thanks to growing 
copper extraction, the country continues to be one of the poorest, with 
hunger, access to clean water, and other problems (Fig. 1). Environ-
mental and social problems may not be directly related to mining ac-
tivities, but in resource-dependent and -export oriented developing 
countries, 
the 
concerns 
of 
profit-expropriation 
by 
foreign 
multi-nationals, 
economy 
destabilization 
due 
to 
intensified 
extraction-specialization, and allocation of resource rents to dominant 
elites often associated with the “resource curse”, raise the question: can 
mining create and support the much needed improvements along a di-
versity of sustainability axis? (Soros, 2007). 
The DRC example, with its population growth, corruption, environ-
mental degradation, and social issues associated with mining, is repre-
sentative of not all, but many, mining locations in the Global South. The 
UN SDG indicators reveal the need to address poverty, hunger, growing 
health issues, poor quality of education, and other problems, which are 
less common in developed nations, from where a sizable share of the 
demand for the mined resource is coming (Table 1). 
The above evidence calls for further collection, analysis, and 
dissemination of information crucial for the understanding of implica-
tions of mining, given the complexity of evolving economic, social, and 
political relationships (Addison and Roe, 2018). Global organizations, 
such as World Bank and IMF, international industrial initiatives, and 
alliances of scientists from around the world, have compiled data un-
derpinning the SDGs statistics (Jasansky et al., 2023; Maus et al., 2020; 
Tang and Werner, 2023). With that, however, comes (1) the need for 
powerful tools to handle the large arrays of numerical, textual, and other 
digital information and (2) ethical questions and challenges of data 
collection, storage, use, and reporting. 
Data biases, such as over- or underrepresentation of genders or 
people of a certain race or language group, may translate into the so-
lutions biasing the algorithms and, ultimately, lead to discrimination or 
sub-optimal or unfair decisions and results (Buolamwini, 2023). 
Therefore, turning now to review AI applications and solutions 
emerging from the compiled data, we pay particular attention to the 
factors determining AI usability in mining. We highlight neglected 
impact factors and the fragmentation of past studies that will later justify 
our focus on the multi-objective optimization solutions for more sus-
tainable mining practices. We then discuss the related ethical issues in 
Section 3. 
2.2. Current and upcoming uses of AI applications in mining 
We have identified several areas where AI applications have already 
proven to be useful in the mining industry. Loosely speaking, resource 
extraction may be divided into the exploration, exploitation, and 
reclamation phases. Mining activities and upstream operations may 
differ dramatically depending on resource, production method, location, 
equipment used, and more. Taking a general look at the data types and 
decisions made, we distinguish a few more stages and position the re-
view of AI use around them (Fig. 2). We start the discussion with the 
models focused on exploration. Next, we review AI methods supporting 
mining and production approach and design decisions. We discuss the 
use of AI in mine operation and management practices separately, 
highlighting the aspects overlapping with SDGs. Additionally, with the 
goal of analyzing the effect of mining on sustainability, we consider 
activities associated with mining, namely extracted ore processing. 
Finally, we highlight the critical but often neglected stage of mine- 
closure and abandonment. 
Note, our objective is to provide an overview of AI’s capabilities 
assisting decision-making related to resource extraction and enhancing 
mining industry operations. Therefore, technical details on AI models 
and algorithms are beyond the scope of this paper. The provided list of 
references and discussions, however, should inspire interested readers to 
critically review and revisit the setups and frameworks of AI applica-
tions, following the suggestions provided in the next two sections. 
2.2.1. Exploration 
The first stream of AI applications focuses on prospecting and 
exploration, representing the initial stage of resource development. It 
includes the potential mining site or deposit location and an analysis of 
its grade or characteristics critical for productivity and profitability (e. 
g.,Ali and Frimpong 2020; Saljoughi and Hezarkhani 2018; Sharma 
et al., 2021; Williams et al., 2021; Zuo et al., 2019). Existing AI-enabled 
approaches use data obtained from geologic and geophysical resource 
properties mapping, remote and other sensing surveys, and chemical 
and mineralogical analyses, among others. Such data are compiled 
during exploration sampling and borehole logging, during laboratory 
work, and upon further investigation of prospects’ operations (B¨ohmer 
and Kucera, 2013). ML methods such as support vector machines (SVMs) 
and deep learning models are commonly used to clean and process data, 
perform imputations, and conducting data mining, addressing missing 
and erroneous data issues. Those functions are especially useful when it 
comes to information collected from drilling, sensors, or measurements 
made in real time (Jung and Choi, 2021). 
Results generated with the help of AI aid in understanding and 
predicting future resource production characteristics and supply po-
tential, examples of use having come already from Goldspot Discoveries 
Incorporated and IBM Watson (Murphy, 2019). Thereby, AI-based an-
alyses underpin and facilitate economic evaluations, enable measuring 
the financial potential of mining operations under various market con-
ditions, and support investment and fiscal decisions (Lane, 1988). 
2.2.2. Mining setup 
After the location of the deposits is known, producers have to make a 
decision about mining method. The two commonly distinguished min-
ing approaches are open-case or surface mining and underground min-
ing. The primary characteristics influencing the decision on mining 
approach are geologic and mineralogy properties of the deposit, i.e. its 
depth and size, which affect productivity and extracted resource quality. 
The next most influential factors are economic. Open pit and under-
ground production methods are compared on the basis of expected 
profitability, accounting for the equipment needed, its costs and oper-
ational expenses, costs to comply with corresponding regulations, min-
ing site abandonment costs, and more. 
Advances in experimental geomechanics, combined with the 
growing collections of geologic rock data and insights from rock engi-
neering, led to applications of AI in mining site design, e.g. tunneling 
and underground excavations, for improved productivity and profit-
ability (Morgenroth et al., 2019). Along with that, the understanding of 
rock physical properties allows providing recommendations on safer and 
resilient mining. 
Thanks to continuous operational data collection, AI models can also 
now be applied to the analysis of surface vibrations (and micro- 
earthquakes) and slides predicting blasts and various failures (Montiel 
et al., 2016; Ali and Frimpong 2020; Bui et al., 2020; Ali, 2022). Thus, AI 
not only helps improve mining efficiency and economics, but also can 
reduce life-risks, suggesting the optimal mining approach. 
2.2.3. Operations 
Mining setup and operations management studies intertwine with 
AI-enabled tools by incorporating workplace safety considerations along 
with productivity and environmental impact analyses. Mining activities 
may be associated with a variety of risks, for instance, when resource 
extraction environment is represented by small workspace with 
7 We retrieved the corresponding indicators from https://data.worldbank. 
org/ and https://unstats.un.org/sdgs/ . 
C.C. Corrigan and S.A. Ikonnikova                                                                                                                                                                                                         

--- Page 4 ---

The Extractive Industries and Society 17 (2024) 101440

inadequate lighting and contact with toxic materials, waste, and gasses. 
Inhalation of harmful particles not only damages the health of involved 
workers, but also leads to respiratory infections, which have become the 
top cause of death in Africa (Madhi and Klugman, 2006; Reiner et al., 
2019). Drilling and blasting, heavy machinery, and specialized equip-
ment operations may result in critical injuries, thus raising questions of 
mine safety and calling for monitoring and mine hazard assessments. For 
this reason, AI tools have been created to limit workers’ exposure to 
these conditions through machines that ‘autonomously monitor the at-
mosphere, send signals and warnings, locate problematic areas, and 
work continuously even in dangerous situations’ (Hyder et al., 2019). 
Furthermore, AI-enabled tools have a potential role for government 
use in monitoring mining site and worker safety violations. For instance, 
some of the same technologies being already used to monitor 
biodiversity (Arteta et al., 2016; Kesari, 2019; Microsoft, n.d.) or detect 
air or water pollution violations (Carbon Tracker Initiative, n.d; Han 
et al., 2022), could help governments in mining communities also 
monitor violations. Earth observation techniques that employ machine 
learning can also potentially aid in identifying illegal mining, speeding 
up verifications or administration for land management, or identifying 
and planning for effective reclamation of land.8 On the company side, 
facial recognition and image detection systems are already being used in 
public spaces (Tucker, 2020) and could aid in monitoring and 
Fig. 1. The growth in copper and cobalt mining in DRC in comparison to selected SDG indicators.  
Table 1 
Average region rankings showing the variability in the distance to SDGs, from major challenges (in red) to targets achieved (in green), based on the UN’s SDG Index 
data.  
Fig. 2. A stylized representation of a variety of data associated with resource exploration, extraction, and production.  
8 While a number of Earth observatory projects have been initiated around 
the world, our review is informed by the work at the Technical University of 
Munich, namely “Artificial Intelligence for Earth Observation: Reasoning, 
Uncertainties, Ethics and Beyond (AI4EO, 2023)”. 
C.C. Corrigan and S.A. Ikonnikova                                                                                                                                                                                                         

--- Page 5 ---

The Extractive Industries and Society 17 (2024) 101440

responding to trespassers or other perimeter/entry aspects of mining site 
operations. 
Moreover, data investigation and visualization methods can poten-
tially predict and consequently prevent potentially dangerous situations 
or eliminate the need for human work within hazardous environments, 
such as transporting, loading and triggering explosives, installing roof 
supports or removing toxic gasses and dust (Narkhede et al., 2021). 
AI-enabled tools can also help improve operational efficiency 
throughout the supply chain, predicting maintenance, reducing waste or 
lower transportation costs, among others (Kaack et al., 2020). 
AI is also being used directly in operational processes. Autonomous 
mining haulage trucks, such as from the company Caterpillar, have 
created a 15 % reduction in operating costs since these trucks can 
function continuously without breaks or changes in shifts (Dyson, 2019). 
This would also likely add to worker/driver safety. Within production, 
autonomous machines may soon be able to calculate things such as rock 
strength and hardness or monitor gas and methane, all while surveilling 
roof conditions (He et al., 2019; Isleyen et al., 2021; Wang et al., 2008). 
The data from these operations are collected and then used to analyze 
working conditions so that informed decisions can be made, and 
corrective actions can be taken in the case of error or malfunction (Ge 
et al., 2022). 
Other AI-enabled tools are in development. To further improve 
worker conditions, robots or sensors that investigate the areas of 
concern and collect data on the levels of dangerous gasses, toxic dust, 
and radiation in the mine can be used before human interaction with the 
area (Zhao et al., 2017). These systems would additionally trigger 
alarms or signals and/or redirect ventilation networks whenever unsafe 
conditions occur. This would not only improve working conditions, but 
could also aid in reducing breaks, increasing productivity, and lower 
risks of accidents and related costs (Hyder et al., 2019). 
2.2.4. Processing & abandonment 
Another focus area with applications for AI-enabled tools is mineral 
processing and leaching (Saldana et al., 2022; Flores et al., 2020; Zhang 
et al., 2022). Relatedly, one could consider AI systems for use in 
color-sorting and in identifying various physical, mineralogical, and 
chemical properties. 
Given AI’s capability to handle large arrays of data, it emerges as a 
valuable tool for near-infrared sensor data analysis and waste manage-
ment (Bashir et al., 2019). By integrating geologic, hydrologic, and other 
information on surface environment and characteristics, AI could help in 
the analysis of impacts and thereby, management of water and land 
(Ochieng et al., 2010; Worlanyo and Jiangfeng 2021). Tools to improve 
water management could also ‘greatly increase the efficiency of the 
comminution process and reduce energy cost, as crushing and grinding 
are the most energy consuming and least energy efficient parts of the 
mineral processing cycle’ (Hyder et al., 2019). The use of tools for water 
and waste management, may thus improve both efficiency and 
sustainability. 
2.3. Challenges not yet considered 
Turning to non-AI related studies on mining, we find further ques-
tions and decisions receiving increasing attention with, as yet, little if 
any consideration by AI modelers. Among those studies, we mark: 
timing of the transition from open-pit to underground mining (Chung 
et al., 2022); optimization of long-term production (Epstein et al., 2012); 
disposal of wastes from mines (Lu and Cai, 2012); and finally, envi-
ronmental impact assessment as a part of the dynamic mining process 
planning (Castilla-Gomez and Herrera-Herbert 2014). But what is more 
importantly is a fast growing number of works on mining practices 
related to health issues (Loewenson, 2001; Toteu et al., 2020), negative 
social developments (Kilian, 2008; Wegenast et al., 2019), and other 
consequences, inspired by data reported by Afrobarometer surveys, 
IPUMS, HDX, the UN SDGs, and other databases. These considerations 
motivate the next step in our discussion, namely the ethical aspects of 
the use of AI. 
3. Challenges and ethical considerations of AI implementation 
in mining 
Recognizing the importance of natural resources to the global 
economy, notably in the mining industry, we acknowledge that a 
comprehensive list of stakeholders includes: national and local govern-
ments, mining companies and their mid-stream and downstream part-
nering entities, small scale and artisan miners, NGOs, and local 
communities. And yet, a modern perspective on mining is over-
whelmingly biased toward the maximization of the monetary value 
derived from resource extraction (Davis and Newman, 2008). Given the 
power imbalances in terms of monetary resources and access to infor-
mation among companies and the other stakeholders identified above, it 
is not surprising that operational efficiency and profit maximization are 
the major focuses of innovative application in the industry. 
In this context, in our broader search for all types of AI-enabled tools 
currently used in the mining industry, described above, it is also un-
surprising that the tools are focused heavily on operational and invest-
ment cost efficiency. Given the resources involved in developing and 
training AI-enabled tools, those with the most monetary and organiza-
tional resources will tend to lead the development. While the incentives 
for this focus may be corrected as policy environments change and new 
(operational and other) data are more readily able to be collected, in our 
research to date, changes in the focus areas and analysis framework are 
rarely reconsidered. Therefore, many issues that emerge in association 
with the extraction process are neglected. 
Research on mining will likely continue to be concentrated on the 
economic and financial aspects until a structural shift occurs in corpo-
rate and social responsibility considerations, environmental, social, and 
governance principles, and data collection. The UN SDGs have already 
urged further changes in studies and discussions on approaches and 
mining settings, pushing attention to data and considerations beyond 
technical, financial, and even environmental. Thus, with the introduc-
tion of AI-enabled tools within the mining industry to optimize practices 
and improve efficiency, there is an immense opportunity to explore a 
diversity of economic, environmental, and societal impacts of mining in 
a large-scale way. However, AI-usage brings tradeoffs and potentially 
significant ethical challenges. 
Ethical considerations in the development and use of AI are coming 
increasingly to the forefront of corporate and political discussions. It is 
important to note that AI does not necessarily create the ethical di-
lemmas often outlined in discussions of the impacts of AI, but it has the 
potential to exacerbate or accelerate the dynamics already at play. For 
example, from the focus of this paper, mining, AI did not create the 
power imbalances between corporations and workers or communities. 
AI is not responsible for inequalities between high-income mining na-
tions and low-income ones, but because the technology allows the player 
that controls it to speed up analysis, knowledge, and decision making, AI 
can amplify these trends. Thus, exploring the exacerbation of these 
challenges is an important endeavor. 
In terms of analyzing these challenges, many ethical frameworks co- 
exist, including those from the OECD, UNESCO, and AI4People (Floridi 
et al., 2018; OECD, 2023; UNESCO, 2021).9 Using these well-known 
9 As in one example, Floridi et al. (2018) define 5 principles: beneficence puts 
forth the promotion of well-being, perseveration, and dignity. Non-maleficence 
ensures privacy, security, and “capability caution” (upper limit of future AI 
capabilities). Autonomy involves finding a balance between the decision- 
making power that lies in the hands of humans and the one that is attributed 
to AI. Justice entails creating benefits that are (or could be) shared in order to 
preserve solidarity. Explicability, a concept particularly applicable to AI ethics, 
involves enabling the principles through intelligibility and accountability. 
C.C. Corrigan and S.A. Ikonnikova                                                                                                                                                                                                         

--- Page 6 ---

The Extractive Industries and Society 17 (2024) 101440

overlapping, but not identical, principles as a starting point, we focus on 
the four main ethical considerations and concerns raised by various 
stakeholders on the use of AI in the mining industry:  
(1) autonomy and observation,  
(2) balance of rewards,  
(3) bias and prioritization, and  
(4) explainability and acceptance. 
In discussing the above-listed aspects, we focus especially of the 
trade-offs and objectives of the decision-makers. 
3.1. Autonomy and observation 
As with the introduction of AI in other fields, persistent pushback 
remains from multiple stakeholder groups, including workers, supervi-
sors, surrounding communities, and researchers. This distress is driven 
by concern of how AI tools could negatively impact job availability, 
access to social services, stakeholder relations, and communication 
(Cazes, 2021). These concerns often stem from anxieties about auto-
mation tasks taking over the role of humans within the workforce, as 
well as increased surveillance or observation leading to a loss of data 
privacy or ability to independently make decisions. For instance, auto-
mated vehicles or worksite monitoring systems have the potential to 
replace human drivers or operators. Tools that monitor driver alertness 
also may induce feelings of over surveillance. Nevertheless, the 
increased safety and efficiency benefits of these same tools have to be 
considered alongside the potential for job costs. Systems that enhance 
rather than replace human workers, as in human-in-the-loop interactive 
AI methods, have potential to address the concerns and could alleviate 
the negative impacts of these innovations or even prevent them (Mos-
queira-Rey et al., 2023). 
A further ethical consideration involves misuse. For instance, sur-
veillance and facial monitoring tools designed for environmental impact 
monitoring, worker safety, or the security of mining site perimeters 
could be misused and employed beyond their originally defined pur-
pose. This may include unauthorised monitoring of workers and local 
communities, deceiving community expectations. Therefore, surveil-
lance, data collecting, and human-activity monitoring systems must be 
set up and implemented with privacy and human rights-preserving pa-
rameters in mind (Mazurek and Małagocka, 2019; Fontes et al., 2022). 
The above-discussed concerns represent just a few of numerous 
recorded by researchers in developing countries with weak legal and 
data control systems (Stahl & Stahl, 2021). Overall, the trade-off be-
tween (1) improved (economic, environmental) efficiency and safety 
and (2) loss of worker’s and community self-determination and privacy 
calls for AI implementation frameworks, AI-enabled tools, and 
data-related infrastructures that balance economic and non-economic 
gains versus risks and establish clear and necessary boundaries. 
3.2. Balance of rewards 
Adoption of new technologies brings benefits, in absolute or relative 
economic and non-economic terms, to some and often harms the others, 
creating ‘winners’ and ‘losers’, as marked in the classic Schumpeter’s 
1942 paper on ‘Creative Destruction’. The uneven distribution of re-
wards raises issues related to the principle of justice. Potential discrep-
ancies in the balance of gains become an especially sensitive topic 
considering the inequality between companies, governments, the public, 
and private-sector capabilities (Evans, 2017). For instance, a lack of 
excess capital and or local relevant skills to keep up with the pace of 
progress in terms of AI-enabled mining puts smaller or more local firms 
into a disadvantageous position in comparison to the international 
large-scale firms’ ability to employ AI in their processes. This inequality 
reinforce dynamics that allow large-scale firms to grow and expand 
operations, while smaller or more locally based firms struggle to keep 
up. 
Moreover, governments in smaller or less developed countries, like 
many of those in the “Global South”, may not have financial and human 
capital to develop, deploy, and maintain AI tools on the same level as the 
governments and companies from the “Global North”. Considering the 
necessity for monitoring environmental and other violations, advanced 
technologies and AI-based innovations may exacerbate, rather than 
correct, detrimental relative effects associated with the resource curse. 
Requiring high-skilled labor, and high-tech hardware and software 
sparsely available in less-developed nations, AI may deepen the eco-
nomic and technical development gap among nations, hindering prog-
ress on poverty and inequality reduction (Korinek and Stiglitz, 2021; 
Zhao et al., 2022). 
Furthermore, one should consider the balance of rewards in the 
relation to beneficence. AI has the potential to lower certain environ-
mental and social costs of mining, e.g., utilizing advanced mineral 
processing and waste management through AI-based or controlled 
equipment. However, the improved functionality and efficiency of ma-
chinery often comes with its own environmental footprint, as well as the 
emissions and materials costs related to building and training AI systems 
(Coeckelbergh, 2021; van Wynsberghe, 2021). For instance, in a 
much-cited study, the authors found the lifecycle for one natural lan-
guague processing system was equivalent to five times the average 
lifetime emissions from an American car (Strubell et al., 2019). And the 
computing energy has only expanded since then. An Open AI analysis 
argues that the amount of computing power needed for the largest AI 
training runs has expanded by 300,000 times since 2012 (Open AI, 
2018). Moving beyond energy needed just for training, the OECD out-
lines the direct environmental impacts of AI along the entire system, 
including costs related to production, transport, operations, and 
end-of-life processes in AI use. They also explicitly argue, however, that 
we need better measures of “AI compute and applications” to under-
stand the emissions impacts of the entire AI lifecycle (OECD, 2022). As 
measurement mechanisms improve, the energy savings created by 
AI-enabled tools needs to considered alongside the energy costs of 
developing and deploying those tools themselves. 
Moreover, making mining more efficient and profitable could lead to 
a Jevons paradox or to the over-extraction of minerals and unnecessary 
growth of waste or by-product resources, such as coal. The over-
production or increased availability of minerals could help speed up the 
transition away from fossil fuels, e.g., supporting electrification, an 
apparent positive development. Yet, if the spread of the same tools and 
approaches facilitates the extraction and processing of fossil fuels, 
making them cheaper, a counterintuitive outcome may occur when the 
transition is delayed for economic reasons (Victor, 2019). At the scale of 
one mine, an improvement in the energy efficiency of equipment, with 
the corresponding reduction in energy costs, may result in a refusal to 
invest and switch to cleaner energy alternatives. 
Hence, one may need to think about how and where innovations and 
AI tools are being employed in order to make sure they contribute to 
broader sustainability goals rather than slowing them down. In 
designing and employing AI in the mining sector, the tradeoffs between 
the effectiveness of the tool for a particular function and the implications 
or consequences on a broader scale must be considered. In more general 
terms, the ethics and the value of the action should be viewed in com-
bination with the expectations on the overall outcome or the conse-
quences (Staveren, 2007). 
3.3. Bias and justice 
The increased deployment of data collection tools and a growing 
number of access channels have made data more available for scientists 
working on AI algorithms and applications. That explains why AI- 
enabled tools within the mining sector have come into play only in 
recent years, once sufficient arrays of data have become available. Yet, 
the inequality in data availability and access among mining regions in 
C.C. Corrigan and S.A. Ikonnikova                                                                                                                                                                                                         

--- Page 7 ---

The Extractive Industries and Society 17 (2024) 101440

the Global South versus in the Global North once again leads to ques-
tions of bias and justice. 
Presenting their statistical indicators on the sustainability develop-
ment goals, the OECD and UN organizations often emphasize the lack of 
data, erroneous data, and missing data issues especially in the poor and 
less-developed nations of Africa.10 AI-enabled applications that are 
informed, trained, and tested on inappropriate data, truncated datasets 
that exclude some critical variables, or data with (gender, location, 
historical, or other) sample bias could misinform decision-making that 
may have negative impacts on national or individual development. 
For instance, if an AI-enabled application uses environmental data 
based on historic occurrences in another part of the country, another 
country or even another region, to make decisions about land use in a 
mining region, the predictions could be highly inaccurate because 
relevant data were not used to train the system. Moreover, not including 
data covering certain aspects and impacts of mining, such as environ-
mental and health damage, could lead to a bias in a feature selection, 
with erroneous or biased results. Using biased data or the wrong data, 
therefore, could result in decision-making that misuses land or under 
prepares for certain externalities for local populations. 
Another well-known bias in AI systems, also already discussed in 
Section 2, is along the lines of race and gender. If face recognition sys-
tems, used for employee access or mining area monitoring, are not 
trained or designed with the local population in mind (i.e. in Sub- 
Saharan Africa, where a large number of workers and community 
members are people of color), they might be less accurate and result in a 
lack of access for certain groups (Raji et al., 2020). Similarly, machine 
learning algorithms relying on the historical employment data, often 
skewed in terms of male-to-female ratio, may promote qualifications 
more associated with male candidates while discounting qualifications 
more associated with female candidates. This can lead to a bias in 
candidate selection and promotion, undermining equal treatment in line 
with the targets of the SDGs (UNESCO, OECD, IDB, 2022). 
Although some of these examples sound isolated to one company or 
instance, bias in data used in AI-based applications for decision-making 
in a variety of areas related to mining could have repercussions in a 
country heavily dependent on the resource extraction, such as DRC or 
Zambia. Such concerns include where to mine, how much, what to 
invest in land or population development, who to hire and other con-
siderations (Australian Resources and Investment, 2021). 
Hand in hand with bias goes fairness and justice issues. The biases 
mentioned above may not only distort the immediate outcome, e.g., the 
level of female employment at mine, but could also translate into 
deepening inequality and lack of justice for women: the lack of their 
rights in public domain, reduced access to education, and even decision- 
making on the household level. For instance, the lack of data on female 
employment in African countries would lead machine learning algo-
rithms to suggest changes in employment practices or services related 
only to male works, neglecting female labor completely or being igno-
rant of, for instance, maternity needs. Hence, biases may drive the in-
justices and inequality affecting the lives and society as a whole 
(´Oh´Eigeartaigh et al., 2020; Roche et al., 2022). The misuse of data 
could also yield issues of fairness between regions. If the data used to 
train an AI-enabled tool is more appropriate for mining regions in say 
Canada verses Zambia, the tool will also be more accurate for Canada, 
leading to more effective or informed decision making. This means that 
we might see a widening of the gap between the positive impacts of the 
mining industry in certain regions verse others. 
AI development and design is often driven by (non-AI) modeling 
traditions and may suffer from a lack of expert knowledge to identify 
bias and limitations in data or to correct for biases (Tubella et al., 2019). 
The involvement of local or regional stakeholders may help address the 
standing or preventing of bias issues altogether. Mining company 
management, workers, along with policymakers and surrounding com-
munities, might be able to provide improved data or ways to collect new 
information, vital to revealing potential bias and justice issues. If we 
want to factor environmental, cultural (i.e., language), governance, or 
community-level decisions and objectives into machine learning and 
other AI applications used in the mining industry, extra surveys and data 
collection may be in order. In addition, thorough data analysis for biases 
should be included to prevent any unjust outcomes. 
3.4. Explainability and acceptance 
A final category of ethical considerations is explicitly related to the 
principle of explainability and the concept of transparency in AI systems 
(Angelovet al., 2021; Larsson and Heintz, 2020). Trust in AI methods 
and the produced results or recommendations based on AI-simulations 
depends on algorithmic transparency and understandability; this im-
plies that decision-makers agree on (and/or contributed to) the AI tool 
setup and functionality and can interpret and thereby utilize the results 
(Tubella et al., 2019). With that, the worries of stakeholders, such as job 
loss, surveillance, or misuse of AI-enabled tools around mines, can be 
addressed and managed with insights and knowledge-sharing on AI 
applications. 
With mining-related activities inherently tied to the use of land and, 
therefore, the communities surrounding the production site, it is para-
mount to build local community understanding and acceptance through 
transparency and education on the creation of these technologies, their 
methods, and the extent to which they are or will be employed. AI offers 
tremendous potential in enhancing day-to-day mining operations, em-
ployees’ working conditions, and production efficiency, thereby 
improving financial performance, health conditions, productivity, and 
more. However, without engaged decision-makers’ and beneficiaries’ 
trust and acceptance, AI technologies are at risk of failing or providing 
only incremental impact, based on the evidence from multiple industries 
(Bedu´e and Fritzsche, 2022; Esmaeilzadeh, 2020; Rus et al., 2002). 
Building knowledge within a community about new innovations is 
by no means an easy task. But this is also not a new task. Making sure 
public consultation is real and informed is not confined to the case of AI, 
the mining industry, or only populations in rural or under resourced 
areas (Bryson et al., 2013). The perception of AI as a black box and a lack 
of education and “AI literacy” do, however, pose a challenge related to 
ignorance. This may lead to an increased chance of misuse of AI tools. 
Involvement of the public in decision-making and, therewith, AI algo-
rithm design would help educate, inform, and empower the users, as 
marked by studies on AI education (Long and Magerko, 2020). 
For instance, “Smart Cities” emerging around the world, with a focus 
on people-centered applications informed by public participation, 
represent a notable positive example of the possibility of such education 
and user involvement. Designing a particular tool to be more user- 
friendly and intuitive, with transparent and open access to data collec-
tion, may come at extra costs. But the benefits are likely to outweigh 
them, offering a smoother process of obtaining the social license to 
operate and even improve tool performance, by informing AI designers 
and operators of likely biases or pitfalls. If communities and workers are 
informed about trade-offs, as in the case of the human-in-the-loop de-
signs, they are more likely to be willing to engage with the systems, help 
boost its performance by sharing the data, and participating in the 
needed experiments on adjustments. While the challenges associated 
with informed public participation may never fully be solved, by 
working together, companies, communities, and governments may 
create inclusive and secure spaces, empowering all stakeholders with the 
information on wins, dangers, and trade-offs (UN Habitat, 2020). 
Stakeholder engagement at the stage of the AI design could help 
formulate ethically acceptable boundaries. Moving beyond corporate 
interest, building real awareness of how AI tools are being used should 
10 For further discussion on the big data and data availability by the United 
Nations see https://www.un.org/en/global-issues/big-data-for-sustainable-de 
velopment. 
C.C. Corrigan and S.A. Ikonnikova                                                                                                                                                                                                         

--- Page 8 ---

The Extractive Industries and Society 17 (2024) 101440

increasingly be seen as a core responsibility of a company that plans to 
employ invasive tools within a workplace or a community. 
3.5. Path forward 
Different areas for AI applications pose different goals, face various 
constraints, and may present a diversity of ethical dilemmas. However, 
applying the generally formulated principles of (1) autonomy and 
observation, (2) balance of rewards, (3) bias and prioritization, and (4) 
explainability and acceptance is the key to enable further adoption and 
improvements in AI technologies that can support the transition towards 
sustainable development in mining engaged communities and enable 
the global decarbonization, critical to mitigating climate change and 
preventing its harmful consequences. 
In sum, responsible AI applications should consider the following 
algorithm design and data collection related tasks:  
(1) Perform the analysis on AI feature and data selection to support 
non-biased comprehensive social and environmental, in addition 
to economic, outcome analysis;  
(2) Develop algorithms with human-in-the-loop options to allow 
reviewing the trade-offs between the optimal solutions support-
ing the informed (and adjusted to the evolving surrounding 
conditions) decision-making; 
(3) Establish ethics-based boundaries for AI applicability and us-
ability in communication with the involved stakeholders, 
including workers, communities, and others. 
The above-stated requirements may appear restrictive and raise 
questions on applicability and feasibility. Therefore, in the following 
final sections, we present a possible class of solutions and investigate 
their potential and avenues for further research. 
4. Shaping the future of mining with ethical AI 
The above overview of AI applications in mining is far from com-
plete, but it highlights the need for ethical, in addition to sustainable, 
criteria. Focusing on that critical addition, we return to the overarching 
goal of our review paper and suggest directions for research that em-
phasizes ethical requirements for AI applications to shape the relation-
ship between extractive industries and society. 
Existing and continuously amended sustainability standards for 
mining vary in their targets, objectives, scope, decision groups 
addressed, and more, but all feature multi-objective or multi-criteria 
frameworks (Erdmann and Franken, 2022). However rich, the existing 
systems of standards often overlook the diversity of societal needs, 
institutional capabilities for monitoring, successful implementation of 
the formulated principles, and necessity for information dissemination 
and decision transparency. Addressing the critique, we point out a 
strand of multi-objective optimization (MOO) research that promotes 
informative interactions within a group of decision-makers. To that end, 
we purposely leave technical details on the algorithms that enable 
interactive MOO-based AI tools, such as evolutionary algorithms or 
neural networks, outside the scope of this review. With the mere goal of 
depicting the potential for capturing and integrating ethics and sus-
tainability principles into data handling and AI algorithm design, we 
point to solutions for a wide spectrum of mining activities that can pave 
a path for an ethical and sustainable future. 
4.1. An interactive multi-objective optimization solution 
Studies of resource extraction highlight three major axes along which 
mining related operations may be judged and evaluated: financial or 
economic, environmental, and social impacts, (Bofo et al., 2020; IEA, 
2022; Korinek, 2020; Korinek and Stiglitz, 2021; UNSDSN, 2016; Wu 
et al., 2023). Hence, a class of the multi-objective optimization models 
emerges as a natural way to assess and optimize mining activity while 
accounting for the multiplicity of objectives or evaluation criteria. 
Yet, internally set or externally imposed constraints, e.g., financial, 
time, environmental, or other, may lead to conflicts among the objec-
tives. In this case, decision-makers (DMs) would require a comprehen-
sive assessment of the possible outcomes or alternative solutions and the 
associated trade-offs in order to make an informed decision. It is due to 
the need to ensure the agreement between involved DMs, or to find a 
compromise solution given the differences (in changing) preferences, 
that calls for the interactive group multi-objective optimization (i MOO) in 
mining. 
To comprehend the challenges and the capabilities of i MOO, we 
provide a graphical illustration for a two-objectives case. Imagine a 
mining company negotiating with local community over investments in 
two options: (1) boosting production process efficiency and (2) reducing 
environmental footprint. Denote the financial and environmental ob-
jectives considered by the two negotiating DM groups as fx and fy, 
respectively. Mathematically, one may think of MOO as: co- 
minimization of economic costs and environmental damage problem; 
co-maximization of the financial performance and environmental 
improvement, or a mixed min-max optimization problem.11 Optimiza-
tion of one objective may leave insufficient funds for the second objec-
tive to reach its optimum, so the DMs would have to compromise. Using 
AI algorithms, as discussed in Section 2, one could capture the linkage 
between the investment decision and the outcome(s) and calculate the 
combinations of (fx, fy) for the feasible capital allocations defining the 
dominant or Pareto solutions (Fig. 3). Those solutions form a so-called 
Pareto frontier showing the trade-off between the two objectives or 
how much an improvement in fx costs in terms of a change in fy (Addison 
& Roe, 2018; Miettinen et al., 2008). The transparency of those results is 
critical for information equality, supporting argumentation of the de-
bates and the solid foundation for negotiations and conflict resolution 
(Maybee et al., 2023; Mitchell, 2021). It serves to expose the benefi-
ciaries, review rewards, find biases, and assess acceptance. 
Considering multiple (in times, conflicting) objectives, DMs have to 
prioritize, ration, or neglect the success in some areas in order to ensure 
the progress or compliance with the requirements in others (Acheam-
pong and Boateng, 2019; Vaninsky, 2021). In this context, MOO has 
become a tool for finding optimal control or development paths (Cui 
et al., 2017; del Castillo-Romo et al., 2016; Falke et al., 2016). The 
developed algorithms compete in their performance and ability to 
answer the questions relying on the available data.12 A shifting focus on 
the SDGs and ethics, however, would enhance algorithmic outputs that 
are based on inclusivity and responsibility, raising dominance of the 
human-in-a-loop or interactive multi-objective optimization (Deb et al., 
2016, 2020; Ma et al., 2023; Tanabe, and Ishibuchi, 2019). 
By design, i MOO informs DMs of alternatives and helps them choose 
paths and strategies given the preferences, reference points, or envi-
sioned goals (Meignan et al., 2015; Xin et al., 2018). To understand the 
application, we turn to a 3D expansion of our 2D problem, considering 
the economic, environmental, and social objectives, f(k) = (fec(k),
fen(k), fso(k)), in relation to the decision space points k = (kec, ken, kso)
reflecting the allocation of financial capital, environmental resources, 
such as land and water, and social or human capital, respectively 
(Fig. 4). In this case, the i MOO algorithm translates possible decisions k 
into the outcomes f(k) informing DMs of the resulting Pareto front. DMs, 
in their turn, could communicate their preferences to guide the choice 
between the presented feasible solutions. 
11 Mathematically, all four cases can be converted to co-maximization. 
Therefore, without loss of generality, in what follows, we use “optimization” 
and “maximization” terms implying a variety of optimization problems.  
12 However,Wolpert & Macready (1997) showed that no unique optimization 
procedure can solve all MOO with the same (superior) performance efficiency, 
calling researchers to review their needs and purposes. 
C.C. Corrigan and S.A. Ikonnikova                                                                                                                                                                                                         

--- Page 9 ---

The Extractive Industries and Society 17 (2024) 101440

The decision-outcome correspondence reveals how and why some 
solutions may not be feasible owing to (1) constraints on decisions, such 
as the total budget constraint or minimum spending requirement on the 
environmental maintenance or social needs of the local communities, or 
(2) constraints on outcomes, e.g., the maximum level of pollution, car-
bon footprint, or financial profitability. So, formally, a MOO in the 
context of mining and the SDGs, can be defined as13: 
max
k f(k) =
(
.., f SDGec(k), f SDGen(k), f SDGso(k), ..
)
with k = (.., kec, ken, kso..)
(1)  
subject to ki ≤ ki ≤ k
i,
(2)  
f i ≤ f i(k) ≤ f
i
(3) 
The exhaustive body of research on the resource curse, climate jus-
tice, and intergenerational sustainability agrees that the distribution of 
resource rents and human and natural resource capital is critical for 
equitable and sustainable growth (Acemoglu et al., 2002; Addison & 
Roe, 2018; Adhikari et al., 2023; Howarth, 1991; John and Pecchenino, 
2017; Marini, G., and Scaramozzino, 1995; Newell et al., 2021). 
In this context, whether imposed voluntarily or established through 
regulation, the constraints, such as given by inequality (2), represent, for 
instance, the minimum and maximum allowed spending (e.g., on land 
restoration and environmental stewardship). Through inequality (3) 
they also suggest at least a certain level of improvement and/or non- 
degradation along each goal. These constraints should be transparent 
and continuously reviewed. Through those constraints, the DMs as well 
as by the governments and policy authorities of the affected parties, who 
do not take an active role in decision-making, may navigate positive 
development and ensure sustainability and justice. Computing the Par-
eto front, thus quantifying the trade-offs and establishing the constraints 
or feasibility corridors, helps communication among the DMs and other 
parties in a consistent manner, creating an important feedback link that 
addresses “autonomy and observation” and “explainability and under-
standing” concerns, checks the “balance of rewards”, and controls for “bias 
and justice”. 
5. Conclusions 
The use of AI-enabled tools in the mining industry is already un-
derway. Given the key role of this sector in the energy transition and the 
speed with which that transition needs to occur, AI has the potential, if 
used correctly, to increase the efficiency of this process. If AI is employed 
while factoring in sustainability and community development needs, the 
potentially negative ethical implication of AI use could be significantly 
reduced. However, if considerations for the ethical use of these tools, 
and the tradeoffs that accompany their use, are not taken into account, 
we risk losing the opportunity to transition away from fossil fuels in a 
sustainable and planet/human-centric way. Thus, it is a pressing and 
worthwhile endeavor for both industry players and policy-makers to 
take an ethical and holistic perspective on the use of AI in the mining 
sector. 
Moving beyond economic and efficiency gains, AI-enabled tools have 
the potential to help improve the comprehensiveness or sustainability of 
decision-making in mining operations. By incorporating not only large 
amounts of economic data, but also significant amounts of data on 
Fig. 3. 2D MOO inner (blue points) and dominant (red points) solutions, forming Pareto frontiers (red curves).  
Fig. 4. The decision - objective correspondence and the trade-offs of moving along the Pareto front. Red, green, and blue arrows show the effect of an incremental 
decision-value change on the outcome or individual objective values. 
13 With the presented setup, one may proceed with i MOO, for example, 
leaning on the R and Python codes available, as those provided for the public by 
Hakanen et al. (2021). 
C.C. Corrigan and S.A. Ikonnikova                                                                                                                                                                                                         

--- Page 10 ---

The Extractive Industries and Society 17 (2024) 101440

environmental, land use, communities, and governance factors, multi- 
objective optimization of operations through machine learning pro-
cesses is potentially useful. By being able to better explore the inter-
connectedness of different types of ecosystems and to quickly identify 
things such as the type of ground cover through AI-enabled image 
detection for earth observation, AI could contribute to more sustainable 
mining (Vinuesa et al., 2020). 
With the presented i MOO underpinning the fast growing AI algo-
rithms, extractive activities could be reviewed for cost and benefit 
compromises and costs of risks to ensure that DMs’ preferences lead to 
the compromise acceptable to all stakeholders. Iterative approaches and 
reference-points-based evolutionary algorithms are just a few lines of 
further investigations to review in the exhaustive list of solutions 
available to support i MOO. 
Generally, AI applications aimed at decision-making for economic 
outcomes are prone to accept utilitarianism, originated from conse-
quentialism moral theory, focusing on the maximization of the overall 
consequences. Although this concept allows for redistribution of bene-
fits to compensate for suboptimal individual outcomes, the inclusion of 
transparency and moral principles often remains neglected. Without 
scrutiny and transparency in the trade-offs, the use of such tools may 
accelerate already unjust or suboptimal results: for example, the accel-
erated metals and minerals production in the Global South to achieve 
the decarbonization in the Global North could justify (partial) defores-
tation or loss of some species. 
Hence, supported by the quantification of the consequences, an 
interactive approach emerges as a mechanism to help prevent wrong- 
doing, offering guidance on the AI algorithm’s setup and parameters. 
Acknowledging that this is just a starting point, we conclude our review 
of the path forward, noting that whereas data and AI algorithms may 
empower the scientists and decision-makers, without transparency and 
continuous verification of ethical principles, the society may not be able 
to use its powerful tools for a greater good, stepping out of the way 
toward SDGs. We emphasize that at every step, the DMs must consider 
the trade-offs and reevaluate their gains versus losses in order to enable 
mining activities that improve and check against specific environmental, 
social and economic impacts, helping industry representatives and 
policy-makers arrive at the decisions promoting SDGs and serving the 
well-being of planetary society. 
Funding sources 
This work was supported by the TUM Institute for Ethics in Artificial 
Intelligence under the project “The Potential for AI in the Extractive 
Industries to Promote Multi-objective Optimization.” 
CRedi T authorship contribution statement 
Caitlin C. Corrigan: Conceptualization, Funding acquisition, 
Investigation, Writing – original draft, Writing – review & editing. 
Svetlana A. Ikonnikova: Conceptualization, Investigation, Methodol-
ogy, Visualization, Writing – original draft, Writing – review & editing. 
Acknowledgements 
We are very thankful to our researchers who participated in the 
project that informed this paper “The Potential for AI in the Extractive 
Industries to Promote Multi-objective Optimization”, provided their 
feedback, or helped with data and literature search, including Dr. 
Pamela Duran Diaz, Gen Li, Franziska Lagos L´opez, Paloma Laye. We are 
also thankful to our partners at Kwame Nkrumah University of Science 
and Technology’s Department of Land Economy for facilitating stake-
holder discussions and local workshops on this topic with us, including: 
Dr Eric Tudzi and Bridget Adjei. 
References 
Acemoglu, D., Johnson, S., Robinson, J.A., 2002. An African success story: botswana. 
Avail. SSRN, 304100. https://ssrn.com/abstract=304100. 
Acheampong, A.O., Boateng, E.B., 2019. Modelling carbon emission intensity: 
application of artificial neural network. J. Clean. Prod. 225, 833–856. https://doi. 
org/10.1016/j.jclepro.2019.03.352. 
Addison, T., Roe, A., 2018. Extractive industries: The management of resources as a 
driver of sustainable development: WIDER studies in development economics. 
Oxford University Press, p. 2018. https://doi.org/10.1093/oso/ 
9780198817369.001.0001. 
Adhikari, B., King, J., Vadlamannati, K.C., Chachu, D.O., 2023. Why do some natural 
resource-rich countries adopt prudent fiscal rules? An empirical analysis. Extr. Ind. 
Soc. 14 (10123), 4. https://doi.org/10.1016/j.exis.2023.101234. 
Adler, R.A., Claassen, M., Godfrey, L., Turton, A.R., 2007. Water, mining, and waste: an 
historical and economic perspective on conflict management in South Africa. Econ. 
Peace Sec. J. 2, 2. https://doi.org/10.15355/epsj.2.2.33. 
Ali, D., 2022. Advanced analytics for surface mining. in advanced analytics in mining 
engineering: leverage advanced analytics in mining industry to make better business 
decisions. In Advanced Analytics for Surface Mining. Springer, Cham. https://doi. 
org/10.1007/978-3-030-91589-6.  
Ali, D., Frimpong, S., 2020. Artificial intelligence, machine learning and process 
automation: existing knowledge frontier and way forward for mining sector. Artif. 
Intell. Rev. 53, 6025–6042. https://doi.org/10.1007/s10462-020-09841-6. 
Amugongo, L.M., Bidwell, N.J., Corrigan, C.C., 2023. Invigorating ubuntu ethics in AI for 
healthcare: enabling equitable care. 23). Associat. Comp. Machinery, New York, NY, 
USA 583–592. https://doi.org/10.1145/3593013.3594024. 
Angelov, P.P., Soares, E.A., Jiang, R., Arnold, N.I., Atkinson, P.M., 2021. Explainable 
artificial intelligence: an analytical review. Interdisciplin. Rev. 11 (5), e1424. 
https://doi.org/10.1002/widm.1424. 
Australian Resources and Investment. Ethical considerations of artificial intelligence in 
mining. https://www.australianresourcesandinvestment.com.au/2021/06/07/ethi 
cal-considerations-of-artificial-intelligence-in-mining/, 2021.  
Ayuk, E., Pedro, A., Ekins, P., Gatune, J., Milligan, B., Oberle, B., Christmann, P., Ali, S., 
Kumar, S.V., Bringezu, S., Acquatella, J., Bernaudat, L., Bodouroglou, C., Brooks, S., 
Bonanomi, B., E, C., J, C., N, D., K, D, 2020. Mineral Resource Governance in the 21st 
Century: gearing extractive industries towards sustainable development. Internat. 
Res. Panel, United Nations Environ. Programme. https://doi.org/10.1007/s13563- 
021-00265-4. 
Barmer, H., Dzombak, R., Gaston, M., Palat, V., Redner, F., Smith, T., Wohlbier, J., 2021. 
Scalable AI, White paper prepared by the national AI engineering initiative. the 
National AI Engineering Initiative. https://insights.sei.cmu.edu/library/scalable-ai/. 
Bashir, R.N., Bajwa, I.S., Shahid, M.M.A., 2019. Internet of Things and machine-learning- 
based leaching requirements estimation for saline soils. IEEe Internet. Things. J. 7 
(5), 4464–4472. https://doi.org/10.1109/JIOT.2019.2954738. 
Bedue, P., Fritzsche, A., 2022. Can we trust AI? An empirical investigation of trust 
requirements and guide to successful AI adoption. J. Enterprise Info. Manage. (JEIM) 
35 (2), 530–549. https://doi.org/10.1108/JEIM-06-2020-0233. 
Boddington, P., 2017. Towards a Code of Ethics For Artificial Intelligence. Springer. 
https://link.springer.com/book/10.1007/978-3-319-60648-4. 
Boehmer, M., Kucera, M., 2013. Prospecting and exploration of mineral deposits (ISSN), 
2nd ed. Elsevier Science https://shop.elsevier.com/books/prospecting-and-explora 
tion-of-mineral-deposits/bohmer/978-0-444-99515-5. 
Boffo, R., Marshall, C., Patalano, R., 2020. ESG Investing: Environmental pillar scoring 
and reporting. OECD, Paris. https://www.oecd.org/finance/esg-investing-environ 
mental-pillar-scoring-and-reporting.pdf.  
Bolger, M., Marin, D., Tofighi-Niaki, A., Seelmann, L., 2021. ’Green mining’ is a myth: 
the case for cutting EU resource consumption. Brussels. https://eeb.org/library/gree 
n-mining-is-a-myth/. 
Bryson, J., Quick, K., Slotterback, C., Crosby, B., 2013. Designing public participation 
processes. Public Adm. Rev. 73 (1), 23–34. https://doi.org/10.1111/j.1540- 
6210.2012.02678.x. 
Bui, X.N., Nguyen, H., Choi, Y., Nguyen-Thoi, T., Zhou, J., Dou, J., 2020. Prediction of 
slope failure in open-pit mines using a novel hybrid artificial intelligence model 
based on decision tree and evolution algorithm. Sci. Rep. 10 (1), 1–17. https://doi. 
org/10.1038/s41598-020-66904-y. 
Buolamwini, J., 2023. Unmasking AI: My mission to protect what is human in a world of 
machines. Penguin Random House. https://www.penguinrandomhouse.com/books 
/670356/unmasking-ai-by-joy-buolamwini/. 
Burton, M., 2023. EU proposes designating copper and nickel as critical metals. 
Bloomberg News. March 2023. https://www.bloomberg.com/news/articles/2023-0 
3-16/eu-proposes-designating-copper-and-nickel-as-critical-metals. 
Castilla-Gomez, J., Herrera-Herbert, J., 2014. Comparative criteria for a dynamic 
approach to environmental impact assessment and its influence in mine planning. In: 
Planning, M., Selection, E. (Eds.), Proceedings of the 22nd MPES Conference, 
Dresden, Germany, 14th–19th October 2013. Springer, pp. 685–696. https://doi. 
org/10.1007/978-3-319-02678-7_66. 
Chatila, R., Havens, J.C., 2019. The IEEE global initiative on ethics of autonomous and 
intelligent systems. Robotics Well-Being 11–16. https://doi.org/10.1007/978-3-030- 
12524-0_2. 
Chung, J., Asad, M.W.A., Topal, E., 2022. Timing of transition from open-pit to 
underground mining: a simultaneous optimisation model for open-pit and 
underground mine production schedules. Resour. Policy. 77, 10263. https://doi.org/ 
10.1016/j.resourpol.2022.102632. 
Coeckelbergh, M., 2021. AI for climate: freedom, justice, and other ethical and political 
challenges. AI. Ethics 1, 67–72. https://doi.org/10.1007/s43681-020-00007-2. 
C.C. Corrigan and S.A. Ikonnikova                                                                                                                                                                                                         

--- Page 11 ---

The Extractive Industries and Society 17 (2024) 101440

Collier, P., 2007. The bottom billion: why the poorest countries are failing and what can 
be done about it. Oxford University Press 85 (11), 898–899. https://doi.org/ 
10.2471/BLT.07.045229. 
Corrigan, C.C., Asakipaam, S.A., Kponyo, J.J., Luetge, C., 2023. AI Ethics in Higher 
Education: Insights from Africa and Beyond. Springer Nature. https://doi.org/ 
10.1007/978-3-031-23035-6. 
Cui, Y., Geng, Z., Zhu, Q., Han, Y., 2017. Multi-objective optimization methods and 
application in energy saving. Energy 125, 681–704. https://doi.org/10.1016/j. 
energy.2017.02.174. 
Dauvergne, P., 2021. The globalization of artificial intelligence: consequences for the 
politics of environmentalism. Globalizations. 18 (2), 285–299. https://doi.org/ 
10.1080/14747731.2020.1785670. 
Dauvergne, P., 2022. Is artificial intelligence greening global supply chains? Exposing 
the political economy of environmental costs. Rev. Int. Polit. Econ. 29 (3), 696–718. 
https://doi.org/10.1080/09692290.2020.1814381. 
Davis, G.A., Newman, A.M., 2008. Modern strategic mine planning. In: Proceedings of 
the Australian Mining Technology Conference, Ausl MM, pp. 129–139. 
Deb, K., Roy, P.C., Hussein, R., 2020. Surrogate modeling approaches for multiobjective 
optimization: methods, taxonomy, and results. Math. Comput. Appl. 26 (1), 5. 
https://doi.org/10.3390/mca26010005. 
Deb, K., Sindhya, K., Hakanen, J., 2016. Multi-objective optimization. Decision Sciences. 
CRC Press. https://doi.org/10.1201/9781315183176. 
del Castillo-Romo, A.´A.del, Morales-Rodriguez, R., Rom´an-Martínez, A., 2016. Multi- 
objective optimization for the biotechnological conversion of lingocellulosic biomass 
to value-added products. In: Kravanja, Z., Bogataj, M. (Eds.), 26th European 
Symposium on Computer Aided Process Engineering. Elsevier, pp. 1515–1520. 
https://doi.org/10.1016/B978-0-444-63428-3.50257-5. 
Dyson, N., 2019. BHP to double autonomous trucks at jimblebar. Mining Magazine. htt 
ps://www.miningmagazine.com/innovation/news/1331400/bhp-to-double-auto 
nomous-trucks-at-jimblebar. 
Eke, D.O., Wakunuma, K., Akintoye, S., 2023. Introducing Responsible AI in Africa. In: 
Eke, D.O., Wakunuma, K., Akintoye, S. (Eds.), Responsible AI in Africa. Social and 
Cultural Studies of Robots and AI. Palgrave Macmillan, Cham. https://doi.org/ 
10.1007/978-3-031-08215-3_1.  
Epstein, R., Goic, M., Weintraub, A., Catal´an, J., Santib´a˜nez, P., Urrutia, R., Caro, F., 
2012. Optimizing long-term production plans in underground and open-pit copper 
mines. Oper. Res. 60 (1), 4–17. https://doi.org/10.1287/opre.1110.1003. 
Erdmann, M., Franken, G., 2022. Sustainability standard systems for mineral resources: a 
comparative overview. Bundesanstalt für Geowissenschaften und Rohstoffe. https 
://www.bgr.bund.de/DE/Themen/Min_rohstoffe/Downloads/studie_sustainabi 
lity_standard_systems_2022.pdf?__blob=publication File&v=14. 
Esmaeilzadeh, P., 2020. Use of AI-based tools for healthcare purposes: a survey study 
from consumers’ perspectives. BMC. Med. Inform. Decis. Mak. 20 (1), 1–19. https:// 
doi.org/10.1186/s12911-020-01191-1. 
Evans, L.G., 2017. Disruptive technology and the board: the tip of the iceberg. Econ. Bus. 
Rev. 3, 1. https://doi.org/10.18559/ebr.2017.1.11. 
Falke, T., Krengel, S., Meinerzhagen, A.K., Schnettler, A., 2016. Multi-objective 
optimization and simulation model for the design of distributed energy systems. 
Appl. Energy 184, 1508–1516. https://doi.org/10.1016/j.apenergy.2016.03.044. 
Flores, V., Keith, B., Leiva, C., 2020. Using artificial intelligence techniques to improve 
the prediction of copper recovery by leaching. J. Sens. 2020, 1–12. https://doi.org/ 
10.1155/2020/2454875. 
Floridi, L., Cowls, J., Beltrametti, M., Chatila, R., Chazerand, P., Dignum, V., Lütge, C., 
Madelin, R., Pagallo, U., Rossi, F., Schafer, B., Valcke, P., Vayena, E., 2018. 
AI4People – An ethical framework for a good society: opportunities, risks, principles, 
and recommendations. Minds and Machines 28 (4), 689–707. 
Fontes, C., Hohma, E., Corrigan, C.C., Lütge, C., 2022. AI-powered public surveillance 
systems: why we (might) need them and how we want them. Techn. Soc. 71 https:// 
doi.org/10.1016/j.techsoc.2022.102137. 
Francisco, M., 2023. Artificial intelligence for environmental security: national, 
international, human and ecological perspectives. Curr. Opin. Environ. Sustain. 61, 
10125. https://doi.org/10.1016/j.cosust.2022.101250. 
Ge, S., Wang, F.-Y., Yang, J., Ding, Z., Wang, X., Li, Y., Teng, S., Liu, Z., Ai, Y., Chen, L., 
2022. Making standards for smart mining operations: intelligent Vehicles for 
autonomous mining transportation. IEEE Transact. Intelligent Vehicles 3 (7), 
413–416. https://doi.org/10.1109/TIV.2022.3197820. 
Hagendorff, T., 2020. The ethics of AI ethics: an evaluation of guidelines. Minds. Mach. 
(Dordr) 30 (1), 99–120. https://doi.org/10.1007/s11023-020-09517-8. 
Hakanen, J., Miettinen, K., Matkovi´c, K., 2021. Task-based visual analytics for interactive 
multiobjective optimization. J. Operat. Res. Soc. 72 (9), 2073–2090. https://doi.org/ 
10.1080/01605682.2020.1768809. 
Halpern, O., 2021. The cultural life of machine learning: an incursion into critical AI 
studies. Planetary Intell. 227–256. https://doi.org/10.1007/978-3-030-56286-1_8. 
He, M., Zhang, Z., Ren, J., Huan, J., Li, G., Chen, Y., Li, N., 2019. Deep convolutional 
neural network for fast determination of the rock strength parameters using drilling 
data. Internat. J. Rock Mech. Mining Sci. 123, 104084 https://doi.org/10.1016/j. 
ijrmms.2019.104084. 
Hickok, M., 2021. Lessons learned from AI ethics principles for future actions. AI. Ethics 
1 (1), 41–47. https://doi.org/10.1007/s43681-020-00008-1. 
Hoggard, M.J., Czarnota, K., Richards, F.D., Huston, D.L., Jaques, A.L., Ghelichkhan, S., 
2020. Global distribution of sediment-hosted metals controlled by craton edge 
stability. Nat. Geosci. 13 (7), 504–510. https://doi.org/10.1038/s41561-020-0593- 
2. 
Horan, D., 2020. National baselines for integrated implementation of an environmental 
sustainable development goal assessed in a new integrated SDG index. 
Sustainability. 12 (17), 6955. https://doi.org/10.3390/su12176955. 
Howarth, R.B., 1991. Intertemporal equilibria and exhaustible resources: an overlapping 
generations approach. Ecolog. Econ. 4 (3), 237–252. https://doi.org/10.1016/0921- 
8009(91)90053-H. 
Humphreys, M., Sachs, J.D., Stiglitz, J.E., 2007. Escaping the resource curse. Columbia 
University Press. https://www.jstor.org/stable/10.7312/hump14196. 
Hyder, Z., Siau, K., Nah, F., 2019. Artificial Intelligence, machine learning, and 
autonomous technologies in the mining industry. J. Database Manage. 30, 2. https:// 
doi.org/10.4018/JDM.2019040104. 
Cazes, S. (2021). The impact of artificial intelligence on the labour market: what do we know 
so far? OECD. https://www.oecd.org/publications/the-impact-of-artificial-intelligen 
ce-on-the-labour-market-7c895724-en.htm. 
IEA, 2021. The role of critical minerals in clean energy transitions. International Energy 
Agency. https://www.iea.org/reports/the-role-of-critical-minerals-in-clean-ener 
gy-transitions. 
IPCC. (2023). Synthesis report of the IPCC Sixth assessment: intergovernmental panel on 
climate change 2023. https://www.ipcc.ch/report/ar6/syr/. 
IEA. Why is ESG so important to critical mineral supplies, and what can we do about it? 
International Energy Agency. https://www.iea.org/commentaries/why-is-esg-so- 
important-to-critical-mineral-supplies-and-what-can-we-do-about-it, 2022.  
Isleyen, E., Duzgun, S., Mc Kell Carter, R., 2021. Interpretable deep learning for roof fall 
hazard detection in underground mines. J. Rock Mechan. Geotechnical Eng. 13 (6), 
1246–1255. https://doi.org/10.1016/j.jrmge.2021.09.005. 
Jasansky, S., Lieber, M., Giljum, S., Maus, V., 2023. An open database on global coal and 
metal mine production. Sci. Data 10 (1), 52. https://doi.org/10.1038/s41597-023- 
01965-y. 
Jobin, A., Ienca, M., Vayena, E., 2019. The global landscape of AI ethics guidelines. Nat. 
Mach. Intell. 1 (9), 389–399. https://doi.org/10.1038/s42256-019-0088-2. 
John, A., Pecchenino, R., 2017. An overlapping generations model of growth and the 
environment * 143–160. https://doi.org/10.4324/9781315257570-7. 
Jung, D., Choi, Y., 2021. Systematic review of machine learning applications in mining: 
exploration, exploitation, and reclamation. Minerals 11 (2), 148. https://doi.org/ 
10.3390/min11020148. 
Kaack, L., Donti, P.L., Strubell, E., Rolnick, D., 2020. Artificial Intelligence and Climate 
Change: opportunities, considerations, and policy levers to align AI with climate 
change goals. E-Paper. Heinrich-B¨oll Stiftung. https://eu.boell.org/en/2020/12/0 
3/artificial-intelligence-and-climate-change. 
Kilian, J.M., 2008. Addressing the social impact of mining activities on communities for 
sustainability: environmental. Civil Engineering= Siviele Ingenieurswese 2008 (8), 
22–24. https://hdl.handle.net/10520/EJC25978. 
Korinek, A., Stiglitz, J.E., 2021. Artificial intelligence, globalization, and Strategies For 
Economic development. No. w28453. https://doi.org/10.3386/w28453. 
Korinek, J., 2020. The mining global value chain. OECD Trade Policy Papers, 235. https:// 
doi.org/10.1787/2827283e-en. 
Kumar, A., Dimitrakopoulos, R., 2021. Production scheduling in industrial mining 
complexes with incoming new information using tree search and deep reinforcement 
learning. Appl. Soft. Comput. https://doi.org/10.1016/j.asoc.2021.107644. 
Lane, K.F., 1988. The economic definition of ore–cut-off grades in theory and practice. 
(Retroactive Coverage). Mining Journal Books. COMET Strategy Pty Ltd. https://dl. 
acm.org/doi/abs/10.5555/3133413. 
Larsson, S., Heintz, F., 2020. Transparency in artificial intelligence. Internet. Policy. Rev. 
9, 2. https://doi.org/10.14763/2020.2.1469. 
L`ebre, ´E., Stringer, M., Svobodova, K., Owen, J.R., Kemp, D., Cˆote, C., Arratia-Solar, A., 
Valenta, R.K., 2020. The social and environmental complexities of extracting energy 
transition metals. Nat. Commun. 11 (1), 1 https://doi.org/10.1038/s41467-020- 
18661-9. 
Loewenson, R., 2001. Globalization and occupational health: a perspective from 
southern Africa. Bull. World Health Organ. 79, 863–868. https://www.scielosp. 
org/pdf/bwho/2001.v79n9/863-868/en. 
Long, D., Magerko, B., 2020. What is AI literacy? in i. proc (ed.), competencies and design 
considerations. In: ACM CHI Conference on Human Factors in Computing Systems. 
Lu, Z., Cai, M., 2012. Disposal methods on solid wastes from mines in transition from 
open-pit to underground mining. Procedia Environ. Sci. 16, 715–721. https://doi. 
org/10.1016/j.proenv.2012.10.098. 
Ma, H., Zhang, Y., Sun, S., Liu, T., Shan, Y., 2023. A comprehensive survey on NSGA-II 
for multi-objective optimization and applications. Artif. Intell. Rev. 1–54. https:// 
doi.org/10.1007/s10462-023-10526-z. 
Mackenzie, W., 2020. The Energy Transition Will Be Built With Metals. Forbes. htt 
ps://www.forbes.com/sites/woodmackenzie/2020/10/29/the-energy-transition-wi 
ll-be-built-with-metals. 
Madhi, S.A., KP, K., others, 2006. Acute Respiratory Infections. In: Jamison, R.G., 
Feachem, DT, Makgoba, M.W. (Eds.), Disease and Mortality in Sub-Saharan Africa, 
2nd edition. The International Bank for Reconstruction and Development /The 
World Bank, p. Chapter 11. https://www.ncbi.nlm.nih.gov/books/NBK2283/. 
Marini, G., Scaramozzino, P., 1995. Overlapping generations and environmental control. 
J. Environ. Econ. Manage 29 (1), 64–77. https://doi.org/10.1006/jeem.1995.1031. 
Maus, V., Giljum, S., Gutschlhofer, J., da Silva, D.M., Probst, M., Gass, S.L., Mc Callum, I., 
2020. A global-scale data set of mining areas. Sci. Data 7 (1), 289. https://doi.org/ 
10.1038/s41597-020-00624-w. 
Maybee, B., Lilford, E., Hitch, M., 2023. Environmental, Social and Governance (ESG) 
risk, uncertainty, and the mining life cycle. Extr. Ind. Soc. 14, 101244 https://doi. 
org/10.1016/j.exis.2023.101244. 
Mazurek, G., Małagocka, K., 2019. Perception of privacy and data protection in the 
context of the development of artificial intelligence. J. Manage. Anal. 6 (4), 
344–364. https://doi.org/10.1080/23270012.2019.1671243. 
C.C. Corrigan and S.A. Ikonnikova                                                                                                                                                                                                         

--- Page 12 ---

The Extractive Industries and Society 17 (2024) 101440

Meignan, D., Knust, S., Frayret, J.M., Pesant, G., Gaud, N., 2015. A review and taxonomy 
of interactive optimization methods in operations research. ACM Transact. Interact. 
Intell.t Sys. (Tii S) 5 (3), 1–43. https://doi.org/10.1145/2808234. 
Miettinen, K., Ruiz, F., Wierzbicki, A.P., 2008. Introduction to multiobjective 
optimization: interactive approaches. In Multiobjective optimization: Interactive and 
Evolutionary Approaches. Springer, pp. 27–57. https://doi.org/10.1007/978-3-540- 
88908-3_2. 
Mirjalili, S., Dong, J.S., 2020. Multi-objective optimization using artificial intelligence 
techniques. Springer. http://www.springer.com/series/10618. 
Mitchell, P., 2021. Top 10 Business risks and opportunities for mining and metals in 
2022. EY. https://www.ey.com/en_gl/mining-metals/top-10-business-risks-and-o 
pportunities-for-mining-and-metals-in-2022. 
Montiel, L., Dimitrakopoulos, R., Kawahata, K., 2016. Globally optimising open-pit and 
underground mining operations under geological uncertainty. Mining Techn. 125 
(1), 2–14. https://doi.org/10.1179/1743286315Y.0000000027. 
Morgenroth, J., Khan, U.T., Perras, M.A., 2019. An overview of opportunities for 
machine learning methods in underground rock engineering design. Geosciences. 
(Basel) 9 (12), 504. https://doi.org/10.3390/geosciences9120504. 
Mosqueira-Rey, E., Hern´andez-Pereira, E., Alonso-Ríos, D., Bobes-Bascar´an, J., 
Fern´andez-Leal, ´A., 2023. Human-in-the-loop machine learning: a state of the art. 
Artif. Intell. Rev. 56 (4), 3005–3054. https://doi.org/10.1007/s10462-022-10246- 
w. 
Murphy, P., 2019. How AI technology can make mining more productive. IBM. htt 
ps://www.ibm.com/blogs/client-voices/ai-technology-mining-productive/. 
Nakajima, K., Noda, S., Nansai, K., Matsubae, K., Takayanagi, W., Tomita, M., 2018. 
Global distribution of used and unused extracted materials induced by consumption 
of iron, copper, and nickel. Environ. Sci. Technol. 53 (3), 1555–1563. https://doi. 
org/10.1021/acs.est.8b04575. 
Narkhede, P., Walambe, R., Mandaokar, S., Chandel, P., Kotecha, K., Ghinea, G., 2021. 
Gas detection and identification using multimodal artificial intelligence based sensor 
fusion. Appl. Syst. Innov. 4 (1), 3. https://doi.org/10.3390/asi4010003. 
Newell, P., Srivastava, S., Naess, L.O., Contreras, T., A, G., Price, R, 2021. Toward 
transformative climate justice: an emerging research agenda. Climate Change 12, 
e733. https://doi.org/10.1002/wcc.733. 
Noriega, R., Pourrahimian, Y., 2022. A systematic review of artificial intelligence and 
data-driven approaches in strategic open-pit mine planning. Resour. Policy. 77, 
102727 https://doi.org/10.1016/j.resourpol.2022.102727. 
Ochieng, G.M., Seanego, E.S., Nkwonta, O.I., 2010. Impacts of mining on water resources 
in South Africa: a review. Scientific Res. Ess. 5 (22), 3351–3357. https://doi.org/ 
10.5897/SRE.9000572. 
Oduyemi, G.O., Owoeye, T., Adekoya, O.B., 2021. Health outcomes and the resource 
curse paradox: the experience of African oil-rich countries. Resour. Policy. 73, 
102201 https://doi.org/10.1016/j.resourpol.2021.102201. 
OECD, 2022a. Measuring the environmental impact of artificial intelligence compute and 
applications: the AI footprint. OECD Digital Economy Papers, No. 341. https://doi. 
org/10.1787/7babf571-en. 
OECD, 2023. Recommendation of the council on artificial intelligence. OECD/LEGAL/ 
0449. https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449. 
´Oh´Eigeartaigh, S.S., Whittlestone, J., Liu, Y., Zeng, Y., Liu, Z., 2020. Overcoming barriers 
to cross-cultural cooperation in AI ethics and governance. Philos. Technol. 33 (4), 
571–593. https://doi.org/10.1007/s13347-020-00402-x. 
Open AI. (2018). AI and compute. https://openai.com/blog/ai-and-compute/. 
Pagel, H., Ranke, K., Hempel, F., K¨ohler, J., 2014. The use of the concept „global south “ 
in social science & humanities, 125. University of California, Berkeley. https://www. 
academia.edu/7917466/The_Use_of_the_Concept_Global_South_in_Social_Science_ 
and_Humanities. 
Raji, I.D., Gebru, T., Mitchell, M., Buolamwini, J., Lee, J., Denton, E., 2020. Saving face: 
investigating the ethical concerns of facial recognition auditing. In: Proceedings of 
the 3rd AAAI/ACM Conference on Artificial Intelligence, Eithics, and Society (AIES). 
https://doi.org/10.1145/3375627.3375820. 
Reiner, R.C., Welgan, C.A., Casey, D.C., others, 2019. Identifying residual hotspots and 
mapping lower respiratory infection morbidity and mortality in African children 
from 2000 to 2017. Nat. Microbiol. 4, 2310–2318. https://doi.org/10.1038/s41564- 
019-0562-y. 
Roche, C., Wall, P.J., Lewis, D., 2022. Ethics and diversity in artificial intelligence 
policies, strategies and initiatives. AI. Ethics 3, 1095–1115. https://doi.org/ 
10.1007/s43681-022-00218-9. 
Roe, A.R. (2016). Like it or not, poor countries are increasingly dependent on mining and oil & 
gas. https://www.wider.unu.edu/publication/it-or-not-poor-countries-are-increasin 
gly-dependent-mining-and-oil-gas. 
Rus, I., Lindvall, M., Sinha, S., 2002. Knowledge management in software engineering. 
IEEe Softw. 19 (3), 26–38. https://doi.org/10.1109/MS.2002.1003450. 
Sachs, J.D., Warner, A.M., 2001. The curse of natural resources. Eur Econ. Rev. 45, 
827–838. https://doi.org/10.1016/S0014-2921(01)00125-8. 
Sala-i-Martin, X., Subramanian, A., 2003. Addressing the natural resource curse: an 
illustration from Nigeria. NBER Working Paper, 9804. https://doi.org/10.3386/ 
w9804. 
Saldana, M., Neira, P., Gallegos, S., Salinas-Rodriguez, E., Perez-Rey, I., Toro, N., 2022. 
Mineral leaching modeling through machine learning algorithms− a review. Front. 
Earth. Sci. (Lausanne) 10, 560. https://doi.org/10.3389/feart.2022.816751. 
Saljoughi, B.S., Hezarkhani, A., 2018. A comparative analysis of artificial neural network 
(ANN), wavelet neural network (WNN), and support vector machine (SVM) data- 
driven models to mineral potential mapping for copper mineralizations in the Shahr- 
e-Babak region, Kerman, Iran. Applied Geomatics 10, 229–256. https://doi.org/ 
10.1007/s12518-018-0229-z. 
Schmidt-Traub, G., Kroll, C., Teksoz, K., Durand-Delacre, D., Sachs, J.D., 2017. National 
baselines for the sustainable development goals assessed in the SDG index and 
dashboards. Nat. Geosci. 10 (8), 547–555. https://doi.org/10.1038/ngeo2985. 
Sengupta, M., 2021. Environmental impacts of mining: monitoring, restoration and 
control. CRC Press. https://doi.org/10.1201/9781003164012. 
Sharma, L.K., Gupta, R., Pandey, P.C., 2021. Future aspects and potential of the remote 
sensing technology to meet the natural resource needs. Adv. Remote Sens. Nat.l Res. 
Monitor. 445–464. https://doi.org/10.1002/9781119616016.ch22. 
Sircar, A., Yadav, K., Rayavarapu, K., Bist, N., Oza, H., 2021. Application of machine 
learning and artificial intelligence in oil and gas industry. Petroleum Research 6 (4), 
379–391. https://doi.org/10.1016/j.ptlrs.2021.05.009. 
Soros, G. (2007). Escaping the Resource Curse (M. Humphreys, J. D. Sachs, & J. E. 
Stiglitz, Eds.). Columbia University Press. http://www.jstor.org/stable/10.7312/h 
ump14196. 
Srikumar, M., Finlay, R., Abuhamad, G., Ashurst, C., Campbell, R., Campbell-Ratcliffe, E., 
Pineau, J., 2022. Advancing ethics review practices in AI research. Nat. Mach. Intell. 
4 (12), 1061–1064. https://doi.org/10.1038/s42256-022-00585-2. 
Stahl, B.C., 2021. Artificial intelligence for a better future: an ecosystem perspective on 
the ethics of AI and emerging digital technologies. Springer Nature. https://doi.org/ 
10.1007/978-3-030-69978-9. 
Strubell, E., Ganesh, A., Mc Callum, A.. Energy and policy considerations for deep leanring in 
NLP. https://arxiv.org/pdf/1906.02243.pdf, 2019.  
Tanabe, R., Ishibuchi, H., 2019. A review of evolutionary multimodal multiobjective 
optimization. IEEE Transact. Evolut. Comput. 24 (1), 193–200. https://doi.org/ 
10.1109/TEVC.2019.2909744. 
Tang, L., Werner, T.T., 2023. Global mining footprint mapped from high-resolution 
satellite imagery. Commun. Earth. Environ. 4 (1), 1 https://doi.org/10.1038/ 
s43247-023-00805-6. 
Toteu, S.F., Mahe, G., Moritz, R., Sracek, O., Davies, T.C., Ramasamy, J., 2020. Special 
issue: environmental, Health and Social legacies of mining activities in Sub-Saharan 
Africa. J. Geochem. Explor. 209, 106441 https://doi.org/10.1016/j. 
gexplo.2019.106441. 
Tubella, A.A., Theodorou, A., Dignum, V., Dignum, F., 2019. Governance by glass-box: 
implementing transparent moral bounds for AI behaviour (ar Xiv:1905.04994). Ar Xiv. 
https://doi.org/10.48550/ar Xiv.1905.04994. 
Tucker, A., 2020. The citizen question: making identities visible Via facial recognition 
software at the border. IEEE Techn. Soci. Mag. 39 (4), 52–59. https://doi.org/ 
10.1109/MTS.2020.3031847. 
UN, 2021. Transforming extractive industries for sustainable development. United 
Nations. https://www.un.org/sites/un2.un.org/files/sg_policy_brief_extractives.pdf. 
UNEP, 2016. GEO-6 regional assessment For Africa [United nations environment 
programme, nairobi, kenya]. United Nations. https://www.unep.org/resources 
/assessment/geo-6-regional-assessment-africa. 
UNEP, 2019. Mineral resource governance in the 21st century: gearing extractive 
industries towards sustainable development—summary for policymakers and 
business leaders. United Nations Environment Programme. https://www.unep.or 
g/resources/report/mineral-resource-governance-21st-century. 
UNEP, 2022. Mineral resource governance and the global goals: an agenda for 
international collaboration. Report of Activities to Implement United Nations 
Environment Assembly Resolution on Mineral Resource Governance (UNEP/EA.4/ 
Res.19) By United Nations Environment Programme and the University of 
Queensland. https://wedocs.unep.org/handle/20.500.11822/40782. 
UNESCO, 2021. Recommendation on the ethics of artificial intelligence. https://unesdoc. 
unesco.org/ark:/48223/pf0000380455. 
UNESCO, OECD, IDB, 2022. The effects of ai on the working lives of women, p. 82. 
https://doi.org/10.1787/14e9b92c-en. 
UN-Habitat, 2020. Centering people in smart cities: a playbook for local and regional 
governments. https://unhabitat.org/programme/legacy/people-centered-smart-citie 
s/centering-people-in-smart-cities. 
UNSDSN, 2016. Mapping mining to the sustainable development goals: an atlas. 
columbia center on sustainable investment. United Nations Sustainable Development 
Solutions Network. https://www.undp.org/publications/mapping-mining-sdgs-atlas 
. 
Van Staveren, I., 2007. Beyond utilitarianism and deontology: ethics in economics. Rev. 
Political Econ. 19 (1), 21–35. https://doi.org/10.1080/09538250601080776. 
van Wynsberghe, A., 2021. Sustainable AI: AI for sustainability and the sustainability of 
AI. AI. Ethics 1, 213–218. https://doi.org/10.1007/s43681-021-00043-6. 
Vaninsky, A., 2021. Multiobjective restructuring aimed at green economic growth. 
Environ. Sys. Decis. 41 (1), 110–130. https://doi.org/10.1007/s10669-021-09798-z. 
Victor, D.G., 2019. How artificial intelligence will affect the future of energy and climate. 
Brookings Institute. https://policycommons.net/artifacts/4141208/how-artificial- 
intelligence-will-affect-the-future-of-energy-and-climate/4949960/on, 03 Feb 2024. 
CID: 20.500.12592/1qdn3v.  
Vinuesa, R., Azizpour, H., Leite, I., Balaam, M., Dignum, V., Domisch, S., Fell¨ander, A., 
Langhans, S.D., Tegmark, M., Nerini, F.F., 2020. The role of artificial intelligence in 
achieving the sustainable development goals. Nat. Commun. 11 (1), 1–10. https:// 
doi.org/10.1038/s41467-019-14108-y. 
Wang, X.R., Lizier, J.T., Obst, O., Prokopenko, M., Wang, P., 2008. Spatiotemporal 
anomaly detection in gas monitoring sensor networks. Lecture Note. Comp. Sci. 
90–105. https://link.springer.com/chapter/10.1007/978-3-540-77690-1_6. 
Wegenast, T., Krauser, M., Strüver, G., Giesen, J., 2019. At Africa’s expense? 
Disaggregating the employment effects of Chinese mining operations in sub-Saharan 
Africa. World Dev. 118, 39–51. https://doi.org/10.1016/j.worlddev.2019.02.007. 
Williams, J., Singh, J., Kumral, M., Ramirez Ruiseco, J., 2021. Exploring deep learning 
for dig-limit optimization in open-pit mines. Nat. Re. Res. 30, 2085–2101. https:// 
doi.org/10.1007/s11053-021-09864-y. 
C.C. Corrigan and S.A. Ikonnikova                                                                                                                                                                                                         

--- Page 13 ---

The Extractive Industries and Society 17 (2024) 101440

Wolpert, D.H., Macready, W.G., 1997. No free lunch theorems for optimization. IEEE 
Trans. Evol. Comput. 1 (1), 67–82. https://doi.org/10.1109/4235.585893. 
Worlanyo, A.S., Jiangfeng, L., 2021. Evaluating the environmental and economic impact 
of mining for post-mined land restoration and land-use: a review. J. Environ. 
Manage. 279 (11162), 3. https://doi.org/10.1016/j.jenvman.2020.111623. 
Wu, D., Jia, W., Xie, Y., 2023. The impact of environmental information disclosure on 
green innovation in extractive enterprises: promote or crowd out? Extr. Ind. Soc. 14, 
101247 https://doi.org/10.1016/j.exis.2023.101247. 
Xin, B., Chen, L., Chen, J., Ishibuchi, H., Hirota, K., Liu, B., 2018. Interactive 
multiobjective optimization: a review of the state-of-the-art. IEEe Access. 6, 
41256–41279. https://doi.org/10.1109/ACCESS.2018.2856832. 
Xu, Y., Liu, X., Cao, X., Huang, C., Liu, E., Qian, S., Liu, X., Wu, Y., Dong, F., Qiu, C.-W., 
Qiu, J., Hua, K., Su, W., Wu, J., Xu, H., Han, Y., Fu, C., Yin, Z., Liu, M., Zhang, J., 
2021. Artificial intelligence: a powerful paradigm for scientific research. Innovation 
2 (4). https://doi.org/10.1016/j.xinn.2021.100179. 
Zhang, Z., Zhang, X., Zhang, D., Zhang, X., Qiu, F., Li, W., Tang, C., 2022. Application of 
machine learning in a mineral leaching process- taking pyrolusite leaching as an 
example. ACS. Omega 7 (51), 48130–48138. https://doi.org/10.1021/ 
acsomega.2c06129. 
Zhao, J., Gao, J., Zhao, F., Liu, Y., 2017. A SEARCH-and-rescue robot system for remotely 
sensing the underground coal mine environment. Sensors 17 (10), 2426. https://doi. 
org/10.3390/s17102426. 
Zhao, P., Gao, Y., Sun, X., 2022. How does artificial intelligence affect green economic 
growth?—Evidence from China. Sci. Total Environ. (155306), 834. https://doi.org/ 
10.1016/j.scitotenv.2022.155306. 
Zuo, R., Xiong, Y., Wang, J., Carranza, E.J.M., 2019. Deep learning and its application in 
geochemical mapping. Earth. Sci. Rev. 192, 1–14. https://doi.org/10.1016/j. 
earscirev.2019.02.023. 
Arteta, V., Lempitsky, V., Zisserman, A. (2016). Counting in the Wild. European 
Conference on Computer Vision. Retrieved 12 August 2020 from: https://www.robot 
s.ox.ac.uk/~vgg/publications/2016/Arteta16/a rteta16.pdf. 
Kesari, G. (2019). How AI can save earths biodiversity. 21 February 2019. Retrieved 2 
August 2020 from: https://medium.com/@kesari/how-ai-can-save-earthsbiodivers 
ity-94555d57dd28. 
Microsoft. n.d. A Planetary Computer for a Sustainable Future. Retrived 4 March 2024 
from: https://planetarycomputer.microsoft.com/. 
Carbon Tracker Initiative. n.d. About Us. Retrieved 4 march 2024 from: https://carbont 
racker.org/about/. 
Han, S., Sotani, I., Ma, P., Wojcik, N., Shenk, J. (2022). Jetson Clean Water AI. hackster. 
io. (accessed 07.03.2024) https://www.hackster.io/clean-water-ai/jetson-clean-wat 
er-ai-79a797. 
C.C. Corrigan and S.A. Ikonnikova
