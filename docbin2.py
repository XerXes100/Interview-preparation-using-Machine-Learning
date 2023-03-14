import pandas as pd
import os
from tqdm import tqdm
from spacy.tokens import DocBin
import spacy

db = DocBin() # create a DocBin object
nlp = spacy.load("en_core_web_sm")


train = [
("I am passionate about using my skills in technology to make a positive impact on society, and I see myself continuing to work in this field in the future. As the industry evolves, I plan to keep up with the latest developments and continue learning new technologies. Ultimately, I hope to become a respected leader in the field, mentoring and guiding others to develop innovative solutions to important problems.",{"entities":[(5,88,"Passion"),(94,178,"Vision"),(182,265,"Growth"),(279,327,"Leadership"),(329,357,"Leadership")]}),
("I am passionate about marketing and would like to continue developing my marketing expertise over the next several years. One of the reasons Im interested in working for a fast-growing start-up company is that Ill have the ability to wear many hats and collaborate with many different departments. I believe this experience will serve me well in achieving my ultimate goal of leading a marketing department someday.",{"entities":[(0,31,"Passion"),(59,92,"Growth"),(141,298,"Vision"),(378,416,"Leadership")]}),
("I am passionate about pursuing a career in the field of finance, and I am excited about the opportunities for growth and development in the financial industry. In the future, I see myself working in a higher role that allows me to apply my analytical skills and experience to provide value to my clients and the organization. I believe that by continuing to develop my expertise and staying up-to-date on the latest trends and best practices, I can make a meaningful contribution to the industry and achieve my long-term career goals.",{"entities":[(0,63,"Passion"),(69,158,"Vision"),(174,212,"Leadership"),(344,441,"Growth"),(443,533,"Vision")]}),
("I have developed a keen interest in software development, and I see myself continuing to grow in this field. As new technologies emerge, I am eager to stay up to date and learn as much as I can about the latest trends and advancements. In the future, I hope to take on a leadership role in a dynamic and innovative company that values creativity, collaboration, and continuous learning. My ultimate goal is to create software solutions that can make a positive impact on people's lives and help to solve some of the world's most pressing challenges.",{"entities":[(0,56,"Passion"),(62,107,"Growth"),(137,234,"Growth"),(251,385,"Leadership"),(387,485,"Vision"),(490,548,"Vision")]}),
("As an aspiring graphic designer, I am excited about the possibilities of the field and the ways in which it can be used to communicate important messages and ideas. In the future, I see myself leading a team of talented designers to create innovative visual content that can engage and inspire people. I am passionate about branding, marketing, and advertising, and I believe that my experience and skills can help me to make a significant impact in these areas. Ultimately, I hope to be part of a company that is dedicated to creating meaningful and memorable experiences for its customers through exceptional design.",{"entities":[(33,163,"Growth"),(180,300,"Leadership"),(302,360,"Passion"),(366,461,"Vision"),(475,617,"Vision"),(6,31,"Passion")]}),
("I am passionate about the field of education and the ways in which it can be used to empower individuals and transform communities. Over the years, I have gained valuable experience in teaching and mentoring students, and I hope to continue to develop my skills and knowledge in this area. In the future, I see myself working in a leadership role in a school or educational institution where I can make a positive impact on the lives of students and teachers. My ultimate goal is to create a learning environment that is inclusive, dynamic, and responsive and to help prepare students for success in the 21st century.",{"entities":[(0,44,"Passion"),(132,288,"Growth"),(305,385,"Leadership"),(392,458,"Vision"),(460,555,"Vision"),(560,616,"Vision")]}),
("I have a deep passion for the field of sustainability and the ways in which we can create a more environmentally friendly world. I hope to continue to develop the expertise I have gained in environmental policy, sustainable development, and renewable energy. In the future, I see myself working in a leadership role in a company that is committed to sustainability and making a positive impact on the planet. My ultimate goal is to develop and implement innovative solutions that can help us to reduce our carbon footprint, protect natural resources, and create a more sustainable future for generations to come.",{"entities":[(0,127,"Passion"),(129,257,"Growth"),(274,364,"Leadership"),(409,611,"Vision")]}),
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

db.to_disk("./train2.spacy") # save the docbin object

