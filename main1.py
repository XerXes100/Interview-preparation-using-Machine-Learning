import sounddevice as sd
import soundfile as sf
import speech_recognition as sr1
# import mutagen
# from mutagen.wave import WAVE
import nlp
# import speech_text

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

r = sr1.Recognizer()

samplerate = 44100  # Hertz
duration = 10 # seconds
filename = 'output.wav'


print("\n")
print("\n")
print("Start talking:")
mydata = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, blocking=True)
sf.write(filename, mydata, samplerate)
hellow = sr1.AudioFile('output.wav')
with hellow as source:
    audio = r.record(source)
# s = r.recognize_google(audio)
# audio_url = speech_text.upload(filename)
if __name__ == '__main__':
    import speech_text
    audio_url = speech_text.upload(filename)
    s,t=speech_text.save_transcript(audio_url, 'file_title', sentiment_analysis=True)
    print(s)
    print(nlp.entity_analysis_q1(s))
    print("confidence analysis:",t)