import sounddevice as sd
import soundfile as sf
import speech_recognition as sr1
# import mutagen
# from mutagen.wave import WAVE
import nlp

r = sr1.Recognizer()

samplerate = 44100  # Hertz
duration = 5 # seconds
filename = 'output.wav'

print("\n")
print("\n")
print("Start talking:")
mydata = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, blocking=True)
# mydata.start()
sf.write(filename, mydata, samplerate)
hellow = sr1.AudioFile('output.wav')
with hellow as source:
    audio = r.record(source)
s = r.recognize_google(audio)

print(s)

# punc_text=nlp.punctuation(s)
# print(punc_text)
sent = nlp.lemmatization(s)
# print(sent)
print(nlp.sentiment_analysis(sent))
print(nlp.entity_analysis(sent))

print(nlp.confidence_analysis(filename))