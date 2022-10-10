import nltk
import spacy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from spacy.lang.en import English
nltk.download("punkt")
nltk.download("vader_lexicon")

# Load spaCy language model
nlp = spacy.load("en_core_web_sm")


# nlp = en_core_web_sm.load()


def nlp_analysis(transcript):
    sid = SentimentIntensityAnalyzer()

    print("Sentimental scores", sid.polarity_scores(transcript))
    doc = nlp(transcript)

    # Find named entities in doc
    for entity in doc.ents:
        print(entity.text, entity.label_)
