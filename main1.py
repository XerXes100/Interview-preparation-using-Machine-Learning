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
    print(nlp.entity_analysis_q1(s))
    # print("confidence analysis:", t[1]['sentiment'])
    pos, neu, neg = 0, 0, 0
    for i in t:
        if i['sentiment'] == 'POSITIVE':
            pos += 1
        elif i['sentiment'] == 'NEUTRAL':
            neu += 1
        else:
            neg += 1
    print(pos,neu,neg)