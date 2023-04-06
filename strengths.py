# import spacy
#
#
# def extract_strengths(text):
#     # Load the small English language model of spaCy
#     nlp = spacy.load('en_core_web_sm')
#
#     # Process the text with spaCy
#     doc = nlp(text)
#
#     # Define a list of strength keywords
#     # strengths = ['strong', 'talented', 'skilled', 'knowledgeable', 'experienced', 'proficient', 'capable', 'competent',
#     #              'gifted', 'resourceful', 'creative', 'innovative', 'dedicated', 'reliable', 'responsible', 'organized',
#     #              'efficient', 'productive', 'motivated', 'confident', 'positive', 'adaptable', 'flexible',
#     #              'open-minded', 'collaborative', 'communicative', 'empathetic']
#     strengths = ["Excellent communication skills", "Strong problem-solving abilities", "Leadership skills",
#                            "Teamwork and collaboration", "Adaptability and flexibility", "Attention to detail",
#                            "Ability to learn quickly", "Innovation and creativity",
#                            "Strong work ethic and time management", "Positive attitude and enthusiasm",
#                            "Effective decision-making", "Customer service orientation", "Organizational skills",
#                            "Ability to work under pressure", "Strategic thinking", "Interpersonal skills",
#                            "Conflict resolution", "Negotiation skills", "Critical thinking", "Analytical skills",
#                            "Project management", "Data analysis and interpretation", "Self-motivation", "Networking",
#                            "Mentoring and coaching", "Public speaking", "Financial acumen", "Sales and marketing",
#                            "Risk management", "Multitasking", "Initiative and proactivity", "Cultural sensitivity",
#                            "Empathy", "Resilience", "Problem identification", "Research and development", "Creativity",
#                            "Technical proficiency", "Emotional intelligence", "Collaborative decision-making",
#                            "Active listening"]
#
#     # Initialize empty lists for strengths and their examples
#     strength_examples = {}
#     extracted_strengths = []
#
#     # Iterate over each sentence in the document
#     for sentence in doc.sents:
#         # Iterate over each word in the sentence
#         for word in sentence:
#             # Check if the word is a strength keyword
#             if word.text.lower() in strengths:
#                 # Add the strength to the list of extracted strengths
#                 extracted_strengths.append(word.text.capitalize())
#
#                 # Iterate over the sentence again to find examples related to the strength
#                 examples = []
#                 for token in sentence:
#                     # Check if the token is related to the strength keyword
#                     if token.text.lower() == word.text.lower() or token.text.lower() in ['very', 'extremely']:
#                         examples.append(token.text_with_ws)
#                     elif token.head.text.lower() == word.text.lower():
#                         examples.append(token.text_with_ws)
#
#                 # Join the examples into a string and add it to the dictionary of strength examples
#                 example_str = ''.join(examples).strip()
#                 strength_examples[word.text.capitalize()] = {
#                     'example': example_str,
#                     'usage': sentence.text.strip(),
#                 }
#
#     # If less than 3 strengths are extracted, return None
#     # if len(extracted_strengths) < 3:
#     #     return None
#
#     # Return the extracted strengths and their examples as a tuple
#     return tuple([extracted_strengths[:3], strength_examples])
#
#
# text = "I'm a detail-oriented person, and have strong problem-solving skills. For example, I was able to resolve a complex issue by breaking it down into smaller parts and tackling each one systematically. I'm also a great communicator and have excellent interpersonal skills. Like, I was able to effectively lead a cross-functional team to complete a project on time and within budget."
#
# result = extract_strengths(text)
#
# # if result is not None:
# extracted_strengths, strength_examples = result
# print("Extracted strengths:")
# print(extracted_strengths)
# print()
#
# print("Strength examples:")
# for strength in extracted_strengths:
#     print(f"{strength}:")
#     print(f"  Example: {strength_examples[strength]['example']}")
#     print(f"  Usage: {strength_examples[strength]['usage']}")
#     print()
# # else:
# #     print("Less than 3 strengths were extracted.")
input_text = "I am a creative problem solver with excellent communication skills and a strong work ethic."

strengths = ["Excellent communication skills", "Strong problem solving abilities", "Leadership skills",
             "Teamwork and collaboration", "Adaptability","flexibility", "Attention to detail",
             "Ability to learn quickly", "Innovation and creativity",
             "Strong work ethic","time management", "Positive attitude and enthusiasm",
             "Effective decision-making", "Customer service orientation", "Organizational skills",
             "Ability to work under pressure", "Strategic thinking", "Interpersonal skills",
             "Conflict resolution", "Negotiation skills", "Critical thinking", "Analytical skills",
             "Project management", "Data analysis","interpretation", "Self-motivation", "Networking",
             "Mentoring","coaching", "Public speaking", "Financial acumen", "Sales and marketing",
             "Risk management", "Multitasking", "Initiative","proactivity", "Cultural sensitivity",
             "Empathy", "Resilience", "Problem identification", "Research and development", "Creativity",
             "Technical proficiency", "Emotional intelligence", "Collaborative decision-making",
             "Active listening"]

strengths_found = []

for strength in strengths:
    if strength.lower() in input_text.lower():
        start_pos = input_text.lower().find(strength.lower())
        end_pos = start_pos + len(strength)
        strengths_found.append((strength, start_pos, end_pos))

print("Strengths identified in input text: ")
for strength, start_pos, end_pos in strengths_found:
    print(f"{strength} - Starting position: {start_pos}, Ending position: {end_pos}")

ents1=[]
ex=[]
# dic_str = {"start":0,"end":0,"label":"Strength"};
for strength, start_pos, end_pos in strengths_found:
    dic_str = {"start":start_pos , "end": end_pos, "label": "Strength"};
    ents1.append(dic_str)
print("ENTS",ents1)

ex.append({'text':input_text})
ex.append(ents1)
print("EXX",ex)

