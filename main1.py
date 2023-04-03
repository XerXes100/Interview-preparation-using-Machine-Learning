import sounddevice as sd
import soundfile as sf
import speech_recognition as sr1
# import mutagen
# from mutagen.wave import WAVE

import nlp

# import speech_text

r = sr1.Recognizer()

samplerate = 44100  # Hertz
duration = 20  # seconds
filename = 'output.wav'

print("\n")
print("\n")
print("Start talking:")
# mydata = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=2, blocking=True)
# sf.write(filename, mydata, samplerate)
hellow = sr1.AudioFile('output.wav')
with hellow as source:
    audio = r.record(source)
# s = r.recognize_google(audio)
# audio_url = speech_text.upload(filename)
if __name__ == '__main__':
    import speech_text

    audio_url = speech_text.upload(filename)
    s, t = speech_text.save_transcript(audio_url, 'file_title', sentiment_analysis=True)
    print(s)
    y=nlp.entity_analysis_q1(s)
    print(y)
    nlp.get_audio_pace(filename,s)
    # print(nlp.get_audio_pace(filename))
    # print("confidence analysis:", t[1]['sentiment'])
