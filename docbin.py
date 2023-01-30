import pandas as pd
import os
from tqdm import tqdm
from spacy.tokens import DocBin
import spacy

db = DocBin() # create a DocBin object
nlp = spacy.load("en_core_web_sm")


train = [("My name is John Smith, and I am a recent graduate of Stanford University where I earned my degree in Computer Science. My interests include Artificial Intelligence, Cloud Computing, and software development. Through my coursework and internships, I have gained experience in software development, database management, and agile methodologies. I am a self-motivated individual who is always looking for opportunities to improve my skills and contribute to a team. In my free time, I enjoy playing sports and reading about the latest technology trends.",{"entities":[(0,21,"Name"),(34,49,"Position"),(53,72,"Organization"),(91,117,"Degree"),(119,206,"Interest"),(247,341,"Interest"),(350,375,"Quality"),(390,461,"Goals"),(463,549,"Hobbies")]}),
("My name is Michael Brown, and I am a recent graduate from the University of California, Berkeley with a degree in Computer Science. Throughout my education, I have gained experience in a variety of programming languages and technologies including Java, Python and C++. I am passionate about Machine Learning and Artificial Intelligence, and have experience working on several projects in this field. I am an analytical thinker and a problem-solver. I am also a team player and always looking for opportunities to collaborate and learn from others. In my free time, I enjoy reading and playing video games.",{"entities":[(0,24,"Name"),(37,52,"Position"),(62,96,"Organization"),(104,130,"Degree"),(157,219,"Experience"),(224,267,"Experience"),(269,335,"Interest"),(341,398,"Experience"),(408,426,"Quality"),(433,447,"Quality"),(461,472,"Quality"),(484,546,"Goals"),(548,580,"Hobbies"),(585,605,"Hobbies")]}),
("My name is Jane Doe, and I am a highly motivated and dedicated professional with a background in Computer Science. I have a strong passion for programming and software development and have worked in the field for the last five years. My expertise lies in developing web applications using technologies like JavaScript, Python, and React. I am a quick learner and enjoy taking on new challenges. I am also a team player who thrives in a collaborative environment. In my free time, I enjoy hiking and experimenting with new recipes in the kitchen.",{"entities":[(0,19,"Name"),(32,48,"Quality"),(53,75,"Quality"),(97,113,"Degree"),(124,179,"Interest"),(234,282,"Experience"),(283,336,"Experience"),(345,358,"Quality"),(363,393,"Goals"),(407,461,"Quality"),(480,494,"Hobbies"),(498,544,"Hobbies")]}),
("My name is John Doe. I am a Mechanical Engineering final-year student at Purdue University. During my time in the program, I developed an interest in various mechanical systems, machine design, and thermodynamics. I have completed an internship at Tata Consultancy Services, where I was exposed to industrial design processes and got hands-on experience in CAD software such as Solidworks and Autocad. I am passionate about problem-solving and enjoy applying my knowledge to real-world scenarios. After graduation, I aspire to work in the research and development field of advanced manufacturing and automation; and use my knowledge and skills to make an impact in the industry and help companies improve their production processes. I also love Robotics, and I have participated in several competitions and have won a few of them.",{"entities":[(0,19,"Name"),(28,50,"Degree"),(51,69,"Position"),(73,90,"Organization"),(123,212,"Interest"),(234,273,"Experience"),(287,325,"Experience"),(334,400,"Experience"),(407,439,"Quality"),(450,495,"Quality"),(515,610,"Goals"),(616,677,"Goals"),(682,731,"Goals"),(733,753,"Hobbies")]}),
("My name is Jane Smith, and I am a final year engineering student at Duke University, majoring in Electrical Engineering. I have a strong passion for developing innovative solutions to real-world problems through my studies in engineering. I have completed various projects and internships in the field of power systems, renewable energy, and control systems. I have a strong interest in the field of machine learning and have taken relevant courses to further my knowledge in this area. I am a highly motivated individual who is always eager to take on new challenges and expand my skill set. I aim to work in a research and development role where I can continue to learn and innovate in the field of engineering. Outside of my studies, I am an active member of the robotics club, where I have been a team lead for the past two years.",{"entities":[(0,21,"Name"),(34,64,"Position"),(68,83,"Organization"),(97,119,"Degree"),(375,416,"Interest"),(264,357,"Experience"),(426,485,"Interest"),(494,521,"Quality"),(536,567,"Quality"),(572,591,"Quality"),(130,203,"Interest"),(595,641,"Goals"),(654,712,"Goals"),(745,779,"Hobbies")]}),
]

for text, annot in tqdm(train): # data in previous format
    doc = nlp.make_doc(text) # create doc object from text
    ents = []
    for start, end, label in annot["entities"]: # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents # label the text with the ents
    db.add(doc)

db.to_disk("./train.spacy") # save the docbin object

