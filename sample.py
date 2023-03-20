import spacy

def analyze_strengths(text):
    strengths = ['strong', 'talented', 'skilled', 'knowledgeable', 'experienced', 'proficient', 'capable', 'competent', 'gifted', 'resourceful', 'creative', 'innovative', 'dedicated', 'reliable', 'responsible', 'organized', 'efficient', 'productive', 'motivated', 'confident', 'positive', 'adaptable', 'flexible', 'open-minded', 'collaborative', 'communicative', 'empathetic']
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    strengths = {}
    for chunk in doc.noun_chunks:
        for word in chunk:
            if word.pos_ == 'ADJ' and word.dep_ == 'amod' and word.text.lower() in strengths:
                strength_name = word.text.lower()
                example_start = chunk.start
                if example_start >= 1 and doc[example_start - 1].text.lower() in ['example', 'such', 'like']:
                    example_text = chunk.doc[chunk.start:].text
                    strengths[strength_name] = example_text
                    break
    if len(strengths) < 1:
        return "No strengths were identified in the given text."
    else:
        feedback_intro = [
            "It sounds like you possess several strengths that could make you a great fit for the position.",
            "From what you've shared, it seems like you could be a great candidate for the position.",
            "It's clear that you have several strengths that would be valuable in this role.",
            "Based on your response, it seems like you could bring several key strengths to the position.",
            "You've mentioned several strengths that could make you an excellent fit for the role."
        ]
        feedback_idx = nlp(text).count_by(spacy.attrs.POS)[spacy.lang.en.English.vocab.strings['.']] % len(feedback_intro)
        feedback = feedback_intro[feedback_idx]
        strengths_list = []
        for strength_name, example_text in strengths.items():
            strengths_list.append(f"{strength_name} (e.g. {example_text})")
        feedback += ' For instance, you mentioned strengths such as ' + ', '.join(strengths_list[:-1]) + ', and ' + strengths_list[-1] + '.'
        return feedback

text = "I am a very skilled and creative problem-solver. For example, I once developed a new software program that streamlined our company's accounting processes and saved us a significant amount of time and money."
print(analyze_strengths(text))