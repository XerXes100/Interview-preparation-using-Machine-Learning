import sounddevice as sd
import soundfile as sf
import speech_recognition as sr1
# import mutagen
# from mutagen.wave import WAVE
import nlp

r = sr1.Recognizer()

samplerate = 44100  # Hertz
duration = 20  # seconds
filename = 'output.wav'

print("Start talking")
# mydata = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=2, blocking=True)
# sf.write(filename, mydata, samplerate)
hellow = sr1.AudioFile('output.wav')
with hellow as source:
    audio = r.record(source)
s = r.recognize_google(audio)

print(s)


# punc_text=nlp.punctuation(s)
# print(punc_text)
# sent = nlp.lemmatization(s)
print(nlp.entity_analysis(s))
print(nlp.pitch(filename))

# from punctuator import Punctuator
# p=Punctuator('INTERSPEECH-T-BRNN.pcl')
# text_audio_punc = p.punctuate(s)
# print(text_audio_punc)
