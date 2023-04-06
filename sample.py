# from spacy import displacy
# import os
# from path import Path
#
#
# def strength(input_text):
#     strengths = ["Excellent communication skills", "Strong problem solving abilities", "Leadership skills",
#                  "Teamwork and collaboration", "Adaptability", "flexibility", "Attention to detail",
#                  "Ability to learn quickly", "Innovation and creativity",
#                  "Strong work ethic", "time management", "Positive attitude and enthusiasm",
#                  "Effective decision-making", "Customer service orientation", "Organizational skills",
#                  "Ability to work under pressure", "Strategic thinking", "Interpersonal skills",
#                  "Conflict resolution", "Negotiation skills", "Critical thinking", "Analytical skills",
#                  "Project management", "Data analysis", "interpretation", "Self-motivation", "Networking",
#                  "Mentoring", "coaching", "Public speaking", "Financial acumen", "Sales and marketing",
#                  "Risk management", "Multitasking", "Initiative", "proactivity", "Cultural sensitivity",
#                  "Empathy", "Resilience", "Problem identification", "Research and development", "Creativity",
#                  "Technical proficiency", "Emotional intelligence", "Collaborative decision-making",
#                  "Active listening"]
#
#     strengths_found = []
#
#     for strength in strengths:
#         if strength.lower() in input_text.lower():
#             start_pos = input_text.lower().find(strength.lower())
#             end_pos = start_pos + len(strength)
#             strengths_found.append((strength, start_pos, end_pos))
#
#     ents1 = []
#     ex = {}
#     # dic_str = {"start":0,"end":0,"label":"Strength"};
#     for strength, start_pos, end_pos in strengths_found:
#         dic_str = {"start": start_pos, "end": end_pos, "label": "Strength"};
#         ents1.append(dic_str)
#     print("ENTS", ents1)
#
#     ex['text']= input_text
#     ex['ents']=ents1
#     print("ex",ex)
#     svg = displacy.render(ex, style="ent", manual=True)
#     directory = os.getcwd()
#     output_path = Path(directory + "/images/sentence.svg")
#     output_path.open("w", encoding="utf-8").write(svg)
#
#
# strength("I am a creative problem solver with excellent communication skills and a strong work ethic.")
#
# # ex = [{"text": "I am a creative problem solver with excellent communication skills and a strong work ethic.",
# #        "ents": [{"start": 36, "end": 66, "label": "Strength"},{"start": 73, "end": 90, "label": "Strength"}],
# #        }]
# #
# # # colors = {'Strength': "#85C1E9"}
# # # options = {"ents": ['Strength'], "colors": colors}
# # svg = displacy.render(ex, style="ent",manual=True)
# # directory = os.getcwd()
# # output_path = Path(directory + "/images/sentence.svg")
# # output_path.open("w", encoding="utf-8").write(svg)
import matplotlib.pyplot as plt
import plotly.graph_objects as go
fig = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=168,
        mode="gauge+number+delta",
        title={'text': "WPM"},
        delta={'reference': 130},
        gauge={'axis': {'range': [None, 250]},
                'bar': {'color': "#F5F1F0"},
               'steps': [
                   {'range': [0, 130], 'color': "#B27575"},
                   {'range': [130, 190], 'color': "#9A5454"},
                    {'range': [190, 250], 'color': "#7E3F3F"}],
               'threshold': {'line': {'color': "#DF0B0B", 'width': 4}, 'thickness': 0.75, 'value': 190}}))

fig.write_image("images/pace.png")