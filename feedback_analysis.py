import nlp
import speech_text
import spacy
from path import Path
from spacy import displacy
import os
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from cairosvg import svg2png

filename = "output.wav"
# audio_url = speech_text.upload(filename)
# speech_transcript, sentiment = speech_text.save_transcript(
#     audio_url, "file_title", sentiment_analysis=True
# )


def sentiment_find(t):
    pos, neu, neg = 0, 0, 0
    for i in t:
        if i["sentiment"] == "POSITIVE":
            pos += 1
        elif i["sentiment"] == "NEUTRAL":
            neu += 1
        else:
            neg += 1
    height = [pos, neu, neg]
    bars = ("Positive", "Negative", "Neutral")
    x_pos = np.arange(len(bars))

    plt.switch_backend("Agg")

    # Create bars with different colors
    plt.bar(x_pos, height, color=["#FF6000", "#454545", "#FFE6C7"])

    # Create names on the x-axis
    plt.xticks(x_pos, bars)
    plt.savefig("static/feedbackImages/sentiment.png")
    return pos, neu, neg


def entity_highlight_q1(text):
    nlp1 = spacy.load(r"output/model-best")
    doc = nlp1(text)
    colors = {
        "Name": "#85C1E9",
        "Position": "#74992e",
        "Organization": "#FF6000",
        "Degree": "#B3C99C",
        "Interest": "#159895",
        "Quality": "#FEFF86",
        "Goals": "#27E1C1",
    }
    options = {
        "ents": [
            "Name",
            "Position",
            "Organization",
            "Degree",
            "Interest",
            "Quality",
            "Goals",
        ],
        "colors": colors,
    }
    # html = displacy.render(doc, style="dep", page=True)
    svg = displacy.render(doc, style="ent", options=options)
    directory = os.getcwd()
    output_path = Path(directory + "/static/feedbackImages/sentence.svg")
    output_path.open("w", encoding="utf-8").write(svg)


def entity_highlight_q2(text):
    nlp1 = spacy.load(r"output2/model-best")
    doc = nlp1(text)
    colors = {
        "Passion": "#85C1E9",
        "Vision": "#74992e",
        "Growth": "#FF6000",
        "Leadership": "#B3C99C",
    }
    options = {"ents": ["Passion", "Vision", "Growth", "Leadership"], "colors": colors}
    svg = displacy.render(doc, style="ent", options=options)
    directory = os.getcwd()
    output_path = Path(directory + "/static/feedbackImages/sentence.svg")
    output_path.open("w", encoding="utf-8").write(svg)


def entity_highlight_q3(text):
    return


def miss_entity_q1(entity):
    ideal_ent = [
        "Name",
        "Position",
        "Organization",
        "Degree",
        "Interest",
        "Interest",
        "Quality",
        "Goals",
        "Hobbies",
    ]
    y = set(ideal_ent) ^ set(entity)
    return y


def miss_entity_q2(entity):
    ideal_ent = ["Passion", "Growth", "Vision", "Leadership"]
    y = set(ideal_ent) ^ set(entity)
    return y


# pauses_count = nlp.pauses(filename)


def pace(speech_transcript):
    pace, pace_result = nlp.get_audio_pace(filename, speech_transcript)

    fig = go.Figure(
        go.Indicator(
            domain={"x": [0, 1], "y": [0, 1]},
            value=pace,
            mode="gauge+number+delta",
            title={"text": "WPM"},
            delta={"reference": 120},
            gauge={
                "axis": {"range": [None, 250]},
                "steps": [
                    {"range": [0, 125], "color": "lightgray"},
                    {"range": [100, 250], "color": "gray"},
                ],
                "threshold": {
                    "line": {"color": "red", "width": 4},
                    "thickness": 0.75,
                    "value": 200,
                },
            },
        )
    )

    fig.write_image("static/feedbackImages/pace.png")

    # return pace_result, pace


# stutter_find = nlp.detect_stutter(filename)
# entity_highlight_q1(speech_transcript)
# sentiment_find(t)
