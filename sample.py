from pydub import AudioSegment

# Load the audio file
audio_file = AudioSegment.from_wav("output.wav")

# Set the minimum length of a pause in milliseconds
pause_threshold = 500

# Set the minimum length of a long pause in milliseconds
long_pause_threshold = 5000

# Find the silent chunks
silence_chunks = []
for i, chunk in enumerate(audio_file[::500]): # Check every 500ms
    if chunk.dBFS < -50: # You may want to adjust the threshold
        silence_chunks.append(i)

# Convert the chunks to time ranges in milliseconds
pause_ranges = []
for i in range(len(silence_chunks)):
    if i == 0:
        start = 0
    else:
        start = silence_chunks[i-1]*500
    end = silence_chunks[i]*500
    if end - start >= pause_threshold:
        if end - start >= long_pause_threshold: # Add this condition
            pause_ranges.append((start, end))

# Print the pause ranges
print(len(pause_ranges))
