import nltk
import spacy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
# from punctuator import Punctuator
# from deepmultilingualpunctuation import PunctuationModel
from spacy.lang.en import English
from scipy.io import wavfile
import crepe
import librosa
import numpy as np
from pydub import AudioSegment
import wave
import speech_recognition as sr
import speech_text

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


def entity_analysis_q1(transcript):
    nlp1 = spacy.load(r"output/model-best")  # load the best model
    doc = nlp1(transcript)
    # for entity in doc.ents:
    #     print(entity.text, entity.label_)
    ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
    return ents


def entity_analysis_q2(transcript):
    nlp1 = spacy.load(r"output2/model-best")  # load the best model
    doc = nlp1(transcript)
    # for entity in doc.ents:
    #     print(entity.text, entity.label_)
    ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
    print(ents)


def pauses(audio_file1):
    # ge
    audio_file = AudioSegment.from_wav(audio_file1)

    # Set the minimum length of a pause in milliseconds
    pause_threshold = 500

    # Set the minimum length of a long pause in milliseconds
    long_pause_threshold = 5000

    # Find the silent chunks
    silence_chunks = []
    for i, chunk in enumerate(audio_file[::500]):  # Check every 500ms
        if chunk.dBFS < -50:  # You may want to adjust the threshold
            silence_chunks.append(i)

    # Convert the chunks to time ranges in milliseconds
    pause_ranges = []
    for i in range(len(silence_chunks)):
        if i == 0:
            start = 0
        else:
            start = silence_chunks[i - 1] * 500
        end = silence_chunks[i] * 500
        if end - start >= pause_threshold:
            if end - start >= long_pause_threshold:  # Add this condition
                pause_ranges.append((start, end))

    # Print the pause ranges
    return len(pause_ranges)


# def confidence_analysis(audio_path):
#     sr, audio = wavfile.read(audio_path)
#     time, frequency, confidence, activation = crepe.predict(audio, sr, viterbi=True)
#     print(confidence)
#     # print(sum(confidence)*100,len(confidence))
#     print('average',sum(confidence)*100/len(confidence))


def detect_stutter(audio_file, limit=2):
    # Load the audio file
    y, sr = librosa.load(audio_file, sr=None)

    # Extract the MFCCs
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

    # Calculate the delta and delta-delta MFCCs
    delta_mfcc = librosa.feature.delta(mfcc)
    delta2_mfcc = librosa.feature.delta(mfcc, order=2)

    # Concatenate the MFCCs, delta MFCCs, and delta-delta MFCCs
    feature_matrix = np.concatenate((mfcc, delta_mfcc, delta2_mfcc), axis=0)

    # Calculate the mean and standard deviation of the feature matrix
    mean_matrix = np.mean(feature_matrix, axis=1)
    std_matrix = np.std(feature_matrix, axis=1)

    # Calculate the Z-score of each feature
    zscore_matrix = (feature_matrix - mean_matrix[:, None]) / std_matrix[:, None]

    # Calculate the Euclidean distance between consecutive frames
    distances = np.sqrt(np.sum(np.diff(zscore_matrix, axis=1) ** 2, axis=0))

    # Detect stutter
    threshold = 3 * np.mean(distances)
    stutter = np.where(distances > threshold)[0]

    # Limit the number of stutters if specified
    if limit is not None and stutter.size > limit:
        stutter = stutter[:limit]

    # Return the number of stutters found
    num_stutters = stutter.size
    return num_stutters


def get_audio_pace(audio_file_path, s):
    r = sr.Recognizer()

    # with sr.AudioFile(audio_file_path) as source:
    #     audio = r.record(source)  # read the entire audio file
    #
    # try:

    # audio_url = speech_text.upload(audio_file_path)
    # s, t = speech_text.save_transcript(audio_url, 'file_title', sentiment_analysis=True)
    # print(s)

    with wave.open(audio_file_path, 'rb') as wave_file:
        frame_rate = wave_file.getframerate()
        num_frames = wave_file.getnframes()

    duration = num_frames / float(frame_rate)  # calculate the duration of the audio file in seconds
    num_words = len(s.split())  # get the number of words spoken in the audio file
    pace = num_words / (duration / 60)  # calculate the pace in WPM
    # print(pace)
    if pace > 190:
        return "While your response contains valuable content, the pace of your delivery seems to be too fast. It's " \
               "important to ensure that your speech is clear and easy to follow for the listener. Try to slow down a " \
               "bit and allow the information to sink in, while still maintaining a confident and articulate tone. " \
               "Remember, pacing is crucial in effective communication, so be mindful of your speed to ensure your " \
               "message is effectively conveyed", pace
    elif pace < 130:
        return "While your response contains valuable information, the pace of your delivery seems to be too slow. It " \
               "may be beneficial to pick up the pace a bit in order to maintain the listener's engagement. Remember " \
               "to strike a balance between providing thorough information and maintaining an appropriate speed to " \
               "keep your audience attentive and interested",pace
    else:
        return "Your response is delivered at a good speed, allowing the information to flow naturally and keeping " \
               "the listener engaged. It's evident that you have taken the time to organize your thoughts and convey " \
               "your ideas clearly and efficiently. Keep up the good work in maintaining a balanced and effective " \
               "pace in your future responses!", pace
