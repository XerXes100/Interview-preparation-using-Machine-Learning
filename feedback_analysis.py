import nlp
import speech_text

filename = "output.wav"


def sentiment_find(t):
    pos, neu, neg = 0, 0, 0
    for i in t:
        if i["sentiment"] == "POSITIVE":
            pos += 1
        elif i["sentiment"] == "NEUTRAL":
            neu += 1
        else:
            neg += 1
    return pos, neu, neg


def entity_highlight(ent):
    entity = []
    for i in ent:
        entity.append(i[-1])
    return entity


def miss_entity_q2(entity):
    ideal_ent = ["Passion", "Growth", "Vision", "Leadership"]
    y = set(ideal_ent) ^ set(entity)
    print(y)


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
    print(y)


pauses_count = nlp.pauses(filename)


def pace():
    audio_url = speech_text.upload(filename)
    s, t = speech_text.save_transcript(audio_url, "file_title", sentiment_analysis=True)
    # print(s)
    pace_result = nlp.get_audio_pace(filename, s)
    return pace_result


stutter_find = nlp.detect_stutter(filename)
