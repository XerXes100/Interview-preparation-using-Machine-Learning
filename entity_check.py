import spacy
nlp1 = spacy.load(r"output/model-best") #load the best model

doc = nlp1("My name is Michael Brown, and I am a recent graduate from the University of California, Berkeley with a degree in Computer Science.") # input sample text

ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
print(ents)
