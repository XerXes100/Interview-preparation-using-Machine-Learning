def sentiment_find(t):
    pos, neu, neg = 0, 0, 0
    for i in t:
        if i['sentiment'] == 'POSITIVE':
            pos += 1
        elif i['sentiment'] == 'NEUTRAL':
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
    ideal_ent = ["Name", "Position", "Organization", "Degree", "Interest", "Interest", "Quality", "Goals", "Hobbies"]
    y = set(ideal_ent) ^ set(entity)
    print(y)

def pauses():
    pass

def pace():
    pass




