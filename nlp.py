import nltk
import ssl
import spacy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from spacy.lang.en import English

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# nltk.download("punkt")
# nltk.download("vader_lexicon")


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
