import nltk
import spacy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from punctuator import Punctuator
# from deepmultilingualpunctuation import PunctuationModel
from spacy.lang.en import English

# nltk.download('stopwords')
# nltk.download("punkt")
# nltk.download("vader_lexicon")
# nltk.download('wordnet')
# nltk.download('omw-1.4')

# Load spaCy language model
nlp = spacy.load("en_core_web_sm")


# nlp = en_core_web_sm.load()

def sentiment_analysis(transcript):
    sid = SentimentIntensityAnalyzer()
    print("Sentimental scores", sid.polarity_scores(transcript))
    doc = nlp(transcript)
    # print(doc)
    # Find named entities in doc
    
def entity_analysis(transcript):
    doc = nlp(transcript)
    for entity in doc.ents:
        print(entity.text, entity.label_)

def lemmatization(transcript):
    sentences = nltk.sent_tokenize(transcript)
    lemmatizer = WordNetLemmatizer()
    for i in range(len(sentences)):
        words = nltk.word_tokenize(sentences[i])
        # words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
        sentences[i] = ' '.join(words)
    listToStr = ' '.join([str(elem) for elem in sentences])
    return listToStr

def punctuation(transcript):
    # model = PunctuationModel()
    # result = model.restore_punctuation(transcript)
    # return result
    p = Punctuator('INTERSPEECH-T-BRNN.pcl')
    text_audio_punc = p.punctuate(transcript)
    return text_audio_punc

