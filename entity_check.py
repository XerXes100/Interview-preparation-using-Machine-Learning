import spacy
from spacy import displacy

nlp1 = spacy.load(r"output2/model-best") #load the best model

doc = nlp1("I have a deep passion for the field of sustainability and the ways in which we can create a more environmentally friendly world. I hope to continue to develop the expertise I have gained in environmental policy, sustainable development, and renewable energy. In the future, I see myself working in a leadership role in a company that is committed to sustainability and making a positive impact on the planet. My ultimate goal is to develop and implement innovative solutions that can help us to reduce our carbon footprint, protect natural resources, and create a more sustainable future for generations to come.")

ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
print(ents)