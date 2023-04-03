import spacy


def extract_strengths(text):
    # Load the small English language model of spaCy
    nlp = spacy.load('en_core_web_sm')

    # Process the text with spaCy
    doc = nlp(text)

    # Define a list of strength keywords
    strengths = ['ambitious', 'analytical', 'assertive', 'attentive', 'authentic', 'charismatic', 'communicative',
                 'compassionate', 'confident', 'conscientious', 'creative', 'decisive', 'determined', 'disciplined',
                 'dynamic', 'empathetic', 'energetic', 'enthusiastic', 'flexible', 'focused', 'friendly', 'generous',
                 'helpful', 'honest', 'independent', 'innovative', 'insightful', 'intelligent', 'kind', 'knowledgeable',
                 'loyal', 'motivated', 'optimistic', 'organized', 'patient', 'persuasive', 'positive', 'proactive',
                 'productive', 'reliable', 'resilient', 'resourceful', 'self-assured', 'self-disciplined',
                 'self-motivated', 'sincere', 'strategic', 'strong', 'team-oriented', 'tenacious','strength', 'skill', 'ability', 'strong', 'talented', 'knowledgeable', 'experienced', 'proficient',
                  'capable', 'competent', 'gifted', 'resourceful', 'creative', 'innovative', 'dedicated', 'reliable', 'responsible',
                  'organized', 'efficient', 'productive', 'motivated', 'confident', 'positive', 'adaptable', 'flexible', 'hard work',
                 'open minded', 'collaborative', 'communicative', 'empathetic', 'trustworthy', 'discipline', 'patient', 'honest', 'determined',
                  'detail oriented', 'versatile', 'problem solver', 'go getter', 'opportunistic', 'teamwork', 'collaboration', 'active listener']

    strengths = [x.lower() for x in strengths]
    # print(strengths)

    # Initialize empty lists for strengths and their examples
    strength_examples = {}
    extracted_strengths = []

    # Iterate over each sentence in the document
    for sentence in doc.sents:
        # Iterate over each word in the sentence
        # print("1")
        for word in sentence:
            # Check if the word is a strength keyword
            # print("2")
            if word.text.lower() in strengths:
                # Add the strength to the list of extracted strengths

                extracted_strengths.append(word.text.capitalize())

                # Iterate over the sentence again to find examples related to the strength
                examples = []
                for token in sentence:
                    # Check if the token is related to the strength keyword
                    if token.text.lower() == word.text.lower() or token.text.lower() in ['very', 'extremely']:
                        examples.append(token.text_with_ws)
                    elif token.head.text.lower() == word.text.lower():
                        examples.append(token.text_with_ws)

                # Join the examples into a string and add it to the dictionary of strength examples
                example_str = ''.join(examples).strip()
                strength_examples[word.text.capitalize()] = {
                    'example': example_str,
                    'usage': sentence.text.strip(),
                }

    # If less than 3 strengths are extracted, return None
    # if len(extracted_strengths) < 3:
    #     return None

    # Return the extracted strengths and their examples as a tuple
    return tuple([extracted_strengths[:3], strength_examples])


text = "I'm a detail-oriented person, and have strong problem-solving skills. For example, I was able to resolve a " \
       "complex issue by breaking it down into smaller parts and tackling each one systematically. I'm also a great " \
       "communicator and have excellent interpersonal skills. Like, I was able to effectively lead a cross-functional " \
       "team to complete a project on time and within budget. "

result = extract_strengths(text)

# if result is not None:
extracted_strengths, strength_examples = result
print("Extracted strengths:")
print(extracted_strengths)
print()

print("Strength examples:")
for strength in extracted_strengths:
    print(f"{strength}:")
    print(f"  Example: {strength_examples[strength]['example']}")
    print(f"  Usage: {strength_examples[strength]['usage']}")
    print()
# else:
#     print("Less than 3 strengths were extracted.")`


