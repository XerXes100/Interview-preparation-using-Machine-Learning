import crepe
from scipy.io import wavfile

sr, audio = wavfile.read('output.wav')
time, frequency, confidence, activation = crepe.predict(audio, sr, viterbi=True)
print(confidence)
# print(sum(confidence)100,len(confidence))
print('average',sum(confidence)100/len(confidence))