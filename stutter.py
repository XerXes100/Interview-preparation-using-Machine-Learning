import librosa
import numpy as np


def detect_stutter(audio_file):
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

    return stutter


audio_file = 'output.wav'
stutter_result = detect_stutter(audio_file)
print("Stutter detected:", stutter_result)
