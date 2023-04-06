import nlp
import speech_text
import spacy
from path import Path
from spacy import displacy
import os
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

filename = 'output.wav'
audio_url = speech_text.upload(filename)
transcript, sentiment_analysis = speech_text.save_transcript(audio_url, 'file_title', sentiment_analysis=True)
entity = []


def sentiment_find(t):
    pos, neu, neg = 0, 0, 0
    for i in t:
        if i['sentiment'] == 'POSITIVE':
            pos += 1
        elif i['sentiment'] == 'NEUTRAL':
            neu += 1
        else:
            neg += 1
    height = [pos, neu, neg]
    bars = ('Positive', "Negative", "Neutral")
    x_pos = np.arange(len(bars))

    # Create bars with different colors
    plt.bar(x_pos, height, color=['#FF6000', '#454545', '#FFE6C7'])

    # Create names on the x-axis
    plt.xticks(x_pos, bars)
    plt.savefig('sentiment.png')

    if pos > neu and neg >= 0:
        str_sent = "Your response carries a positive sentiment that is evident in your choice of words, tone, " \
                   "and overall demeanor. Your enthusiastic and optimistic approach creates a favorable impression and " \
                   "helps to convey your message effectively. The positive sentiment in your answer is engaging and " \
                   "uplifting, making it enjoyable for the listener to receive your insights. Well done in maintaining " \
                   "a positive tone in your response, as it enhances the overall impact of your communication! "
    elif neu > pos and neg >= 0:
        str_sent = "Your response conveys a neutral sentiment, providing information without expressing any specific " \
                   "emotional tone. While a neutral sentiment can be appropriate in certain situations, be mindful to " \
                   "infuse appropriate emotions and tone when needed to better connect with your audience and make " \
                   "your response more engaging. "
    else:
        str_sent = "Your response carries a negative sentiment that is reflected in your choice of words, tone, " \
                   "and overall demeanor. It's important to be aware that a negative sentiment can impact how your " \
                   "message is received by others. While expressing opinions and feedback is valid, it's crucial to " \
                   "do so in a respectful and constructive manner. Consider using more neutral or positive language " \
                   "to convey your thoughts, and be mindful of the impact that a negative sentiment may have on the " \
                   "listener. "

    return pos, neu, neg, str_sent


def entity_highlight_q2(text):
    nlp1 = spacy.load(r"output2/model-best")
    doc = nlp1(text)
    list1 = []
    ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
    for i in ents:
        list1.append(i[-1])
    global entity
    entity = list1

    colors = {'Passion': "#85C1E9", 'Vision': '#74992e', 'Growth': '#FF6000', 'Leadership': '#B3C99C'}
    options = {"ents": ['Passion', 'Vision', 'Growth', 'Leadership'], "colors": colors}
    svg = displacy.render(doc, style="ent", options=options)
    directory = os.getcwd()
    output_path = Path(directory + "/images/sentence.svg")
    output_path.open("w", encoding="utf-8").write(svg)
    str1 = "Given above is your response in which we have highlighted entities that are relevant to the question. By " \
           "mentioning these entities, you have provided valuable context and insight, making your response more " \
           "robust " \
           "and insightful. "
    return str1


def entity_highlight_q1(text):
    nlp1 = spacy.load(r"output/model-best")
    doc = nlp1(text)
    list1 = []
    ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
    for i in ents:
        list1.append(i[-1])
    global entity
    entity = list1

    colors = {'Name': "#85C1E9", 'Position': '#74992e', 'Organization': '#FF6000', 'Degree': '#B3C99C',
              'Interest': '#159895', 'Quality': '#FEFF86', 'Goals': '#27E1C1'}
    options = {"ents": ['Name', 'Position', 'Organization', 'Degree', 'Interest', 'Quality', 'Goals'], "colors": colors}
    # html = displacy.render(doc, style="dep", page=True)
    svg = displacy.render(doc, style="ent", options=options)
    directory = os.getcwd()
    output_path = Path(directory + "/images/sentence.svg")
    output_path.open("w", encoding="utf-8").write(svg)
    str1 = "Given above is your response in which we have highlighted entities that are relevant to the question. By " \
           "mentioning these entities, you have provided valuable context and insight, making your response more " \
           "robust and insightful. "
    return str1


def entity_highlight_q3(text):
    pass


def miss_entity_q2(entity):
    ideal_ent = ["Passion", "Growth", "Vision", "Leadership"]
    y = set(ideal_ent) ^ set(entity)
    y = list(y)
    # print(y)
    if len(y) == 0:
        str2 = "It is evident that you put in the effort to ensure that your answer was informative and comprehensive " \
               "by including the all the necessary entities that are relevant to the question. "
    else:
        str2 = "However, there are some key entities that were missing, which could further enhance your response and " \
               "provide more context. For instance mentioning {} will  enriched your response by " \
               "providing a more crisp and comprehensive viewpoint. Incorporating these additional entities would have " \
               "strengthened your already well-thought-out answer and taken it to the next level. ".format(y)
    return str2


def miss_entity_q1(entity):
    ideal_ent = ["Name", "Position", "Organization", "Degree", "Interest", "Interest", "Quality", "Goals", "Hobbies"]
    y = set(ideal_ent) ^ set(entity)
    y = list(y)
    print(y)
    if len(y) == 0:
        str2 = "It is evident that you put in the effort to ensure that your answer was informative and comprehensive " \
               "by including the all the necessary entities that are relevant to the question. "
    else:
        str2 = "However, there are some key entities that were missing, which could further enhance your response and " \
               "provide more context. For instance mentioning {} will  enriched your response by " \
               "providing a more crisp and comprehensive viewpoint. Incorporating these additional entities would have " \
               "strengthened your already well-thought-out answer and taken it to the next level. ".format(y)
    return str2


def pause():
    pauses_count = nlp.pauses(filename)
    if pauses_count > 2:
        str_pause = "In your response, you incorporated pauses during certain parts of your answer. While pauses can " \
                    "be " \
                    "used strategically for emphasis or to gather your thoughts, it's important to be mindful of their " \
                    "frequency and duration. Pauses can disrupt the flow of your answer and could potentially affect the " \
                    "listener's understanding. It might be helpful to practice and minimize unnecessary pauses to ensure a " \
                    "more fluent and coherent delivery. "
        return str_pause
    else:
        pass


def pace(speech):
    pace_result, pace = nlp.get_audio_pace(filename, speech)

    fig = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=pace,
        mode="gauge+number+delta",
        title={'text': "WPM"},
        delta={'reference': 130},
        gauge={'axis': {'range': [None, 250]},
               'steps': [
                   {'range': [0, 125], 'color': "lightgray"},
                   {'range': [100, 250], 'color': "gray"}],
               'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 190}}))

    fig.write_image("images/pace.png")

    return pace_result


# print("Sentimental analysis", sentiment_find(sentiment_analysis))
# print("Entity highlight", entity_highlight_q1(transcript))
# print("Missing Entity", miss_entity_q1(entity))
# print("Pauses", pause())
# print("Pace", pace(transcript))
