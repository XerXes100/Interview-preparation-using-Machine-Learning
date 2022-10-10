import sounddevice as sd
import soundfile as sf
import speech_recognition as sr1
import mutagen
from mutagen.wave import WAVE
# import nlp
r = sr1.Recognizer()

samplerate = 44100  # Hertz
duration = 5  # seconds
filename = 'output.wav'

print("Start talking")
mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                channels=2, blocking=True)
sf.write(filename, mydata, samplerate)
hellow = sr1.AudioFile('output.wav')
with hellow as source:
    audio = r.record(source)
s = r.recognize_google(audio)

print(s)
# print(nlp_analysis(s))


# from punctuator import Punctuator
# p=Punctuator('INTERSPEECH-T-BRNN.pcl')
# text_audio_punc = p.punctuate(s)
# print(text_audio_punc)

# def audio_duration(length):
#     hours = length // 3600  # calculate in hours
#     length %= 3600
#     mins = length // 60  # calculate in minutes
#     length %= 60
#     seconds = length  # calculate in seconds
#
#     return hours, mins, seconds  # returns the duration
#
#
# # Create a WAVE object
# # Specify the directory address of your wavpack file
# # "alarm.wav" is the name of the audiofile
# audio = WAVE("output.wav")
#
# # contains all the metadata about the wavpack file
# audio_info = audio.info
# length = int(audio_info.length)
# hours, mins, seconds = audio_duration(length)
# print('Total Duration: {}:{}:{}'.format(hours, mins, seconds))
