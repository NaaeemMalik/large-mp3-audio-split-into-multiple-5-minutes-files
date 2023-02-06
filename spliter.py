# converts a long mp3 file into multiple 5 minute mp3 files
# put ffmpeg in the path

from pydub import AudioSegment

fileName = "i am rich money affirmations listen before you sleep Pca24nzCdu0.mp3"

f = "E:\\Affirmations\\"
+fileName

print(f)
print("Loading file...")
# Load the .mp3 file into pydub
audio = AudioSegment.from_mp3(f)

# Get the length of the audio in milliseconds
audio_length = len(audio)

# Calculate the number of 5-minute segments
num_segments = audio_length // (5 * 60 * 1000)

# Split the audio into segments of 5 minutes each
for i in range(num_segments):
    print(f"Exporting segment {i } of {num_segments}...")
    start = i * 5 * 60 * 1000
    end = (i + 1) * 5 * 60 * 1000
    segment = audio[start:end]
    segment.export(f"E:/Affirmations/{i} - {fileName}.mp3", format="mp3")
