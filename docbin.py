import pandas as pd
import os
from tqdm import tqdm
from spacy.tokens import DocBin
import spacy

db = DocBin() # create a DocBin object
nlp = spacy.load("en_core_web_sm")


train = [ ("My name is John Smith, and I am a recent graduate of Stanford University, where I earned my degree in Computer Science. My interests include Artificial Intelligence, Cloud Computing, and software development. Through my coursework and internships, I have gained experience in software development, database management, and agile methodologies. I am self-motivated, always seeking opportunities to improve my skills and contribute to a team. I enjoy playing sports and reading about the latest technology trends in my free time.",{"entities":[(11,21,"Name"),(53,72,"Organization"),(101,118,"Degree"),(141,164,"Interest"),(166,181,"Interest"),(187,207,"Interest"),(276,296,"Experience"),(298,317,"Experience"),(323,342,"Experience"),(351,366,"Quality"),(388,453,"Goals"),(462,477,"Hobbies"),(482,489,"Hobbies")]}),
        ("My name is Darsh Parekh, I am a final year student of NMIMS University, Mumbai currently pursuing a degree in Computer Engineering. My interests lie in the fields of Data Analytics, Machine Learning, Design Thinking, and my previous experiences have been in the fields of Graphic and Web Designing. I am a goal oriented individual who strives for perfection and showcasing a good work ethic. My hobbies are playing badminton and video games. Actively looking for opportunities to grow and learn in a company while help achieve the goals and the vision of the company.",{"entities":[(33,51,"Position"),(12,24,"Name"),(55,71,"Organization"),(111,131,"Degree"),(273,298,"Experience"),(416,441,"Hobbies"),(307,331,"Quality"),(348,358,"Quality"),(376,391,"Quality"),(167,181,"Interest"),(183,199,"Interest"),(200,216,"Interest"),(443,485,"Goals"),(490,495,"Goals")]}),
("My name is Jane Doe, and I am a highly motivated and dedicated professional with a background in Computer Science. I have a strong passion for programming and software development and have worked in the field for the last five years. My expertise lies in developing web applications using technologies like JavaScript, Python, and React. I am a quick learner and enjoy taking on new challenges. I am also a team player who thrives in a collaborative environment. In my free time, I enjoy hiking and experimenting with new recipes in the kitchen.",{"entities":[(11,19,"Name"),(32,48,"Quality"),(53,75,"Quality"),(97,113,"Degree"),(143,155,"Interest"),(159,179,"Interest"),(266,282,"Experience"),(307,317,"Experience"),(319,325,"Experience"),(331,336,"Experience"),(345,358,"Quality"),(407,418,"Quality"),(488,494,"Hobbies"),(518,544,"Hobbies"),(363,393,"Goals")]}),
("My name is John Doe. I am a final year Mechanical Engineering student at Purdue University. During my time in the program, I developed an interest in various mechanical systems, machine design, and thermodynamics. I have completed an internship at Tata Consultancy Services, where I was exposed to industrial design processes and got hands-on experience in CAD software such as Solidworks and Autocad. I am passionate about problem-solving and enjoy applying my knowledge to real-world scenarios. After graduation, I aspire to work in the research and development field of advanced manufacturing and automation; and use my knowledge and skills to make an impact in the industry and help companies improve their production processes. I also love Robotics, and I have participated in several competitions and have won a few of them.",{"entities":[(11,19,"Name"),(28,38,"Position"),(39,61,"Degree"),(73,90,"Organization"),(158,176,"Interest"),(178,192,"Interest"),(198,212,"Interest"),(234,272,"Experience"),(424,439,"Quality"),(450,496,"Quality"),(515,548,"Goals"),(552,595,"Goals"),(647,677,"Goals"),(682,731,"Goals"),(759,802,"Experience"),(740,753,"Interest")]}),
("My name is Jane Smith, and I am a final year engineering student at Duke University, majoring in Electrical Engineering. I have a strong passion for developing innovative solutions to real-world problems through my studies in engineering. I have completed various projects and internships in the field of power systems, renewable energy, and control systems. I have a strong interest in the field of machine learning and have taken relevant courses to further my knowledge in this area. I am a highly motivated individual who is always eager to take on new challenges and expand my skill set. I aim to work in a research and development role where I can continue to learn and innovate in the field of engineering. Outside of my studies, I am an active member of the robotics club, where I have been a team lead for the past two years",{"entities":[(11,21,"Name"),(34,64,"Position"),(68,83,"Organization"),(130,203,"Interest"),(277,358,"Experience"),(368,417,"Interest"),(486,522,"Quality"),(536,568,"Quality"),(595,637,"Goals"),(737,779,"Experience"),(801,833,"Experience")]}),
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

