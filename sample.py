import wave
import speech_recognition as sr
import speech_text

def get_audio_pace(audio_file_path):
    r = sr.Recognizer()
    audio_url = speech_text.upload(audio_file_path)
    s, t = speech_text.save_transcript(audio_url, 'file_title', sentiment_analysis=True)
    print(s)

    with wave.open(audio_file_path, 'rb') as wave_file:
        frame_rate = wave_file.getframerate()
        num_frames = wave_file.getnframes()

    duration = num_frames / float(frame_rate)  # calculate the duration of the audio file in seconds
    num_words = len(s.split())  # get the number of words spoken in the audio file
    pace = num_words / (duration / 60)  # calculate the pace in WPM
    print(pace)
    if pace > 120:
        return "The audio is too fast. You may want to slow down the pace."
    elif pace < 80:
        return "The audio is too slow. You may want to increase the pace."
    else:
        return "The pace of the audio is just right."