import wave
import numpy as np
import os
from pydub import AudioSegment
import platform

ffmpeg_executable = 'C:\\ffmpeg\\bin\\ffmpeg.exe'


# Determine the operating system
system = platform.system()
if system == "Windows":
    # Replace this path with the correct path to ffmpeg.exe on Windows
    ffmpeg_path = r'C:\path\to\ffmpeg.exe'
elif system == "Darwin":  # macOS
    ffmpeg_path = '/opt/homebrew/bin/ffmpeg'
else:  # Linux
    ffmpeg_path = '/usr/bin/ffmpeg'

# Set the ffmpeg path
AudioSegment.converter = ffmpeg_path

def crop_and_fade_out(input_file, output_file, start_time=0, end_time=30, fade_duration=2):
    audio = AudioSegment.from_file(input_file)
    cropped_audio = audio[start_time * 1000:end_time * 1000]  # Convert times to milliseconds
    faded_audio = cropped_audio.fade_out(fade_duration * 1000)  # Convert fade duration to milliseconds
    faded_audio.export(output_file, format="mp3")


if __name__ == "__main__":
    original_tracks_path = 'tracks'
    trimmed_tracks_path = 'trimmed_tracks'
    file_list = os.listdir(original_tracks_path)

    for filename in file_list:
        raw_name, raw_extension = os.path.splitext(filename)

        input_file_path = os.path.join(original_tracks_path, filename)
        output_file_path = os.path.join(trimmed_tracks_path, f"{raw_name}_preview.mp3")

        # Specify start_time, end_time, and fade_duration as needed
        crop_and_fade_out(input_file_path, output_file_path, start_time=0, end_time=30, fade_duration=2)

print("previews succesfully produced")
