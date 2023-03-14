import librosa

# Load the audio file
audio_file = 'output.wav'
y, sr = librosa.load(audio_file)

# Calculate the RMS value of the audio signal
rms = librosa.feature.rms(y=y)

# Set a threshold for the RMS value
threshold = 0.1

# Check if the RMS value is below the threshold
if rms.mean() < threshold:
    print('Voice is low.')
else:
    print('Voice is not low.')
