import wave
import numpy as np
import os
from pydub import AudioSegment


def crop_and_fade_out(input_file, output_file, duration=30000, fade_duration=2000):
    audio = AudioSegment.from_file(input_file)
    cropped_audio = audio[:duration]
    faded_audio = cropped_audio.fade_out(fade_duration)
    faded_audio.export(output_file, format="wav")



if __name__ == "__main__":
    original_tracks_path = 'tracks'
    trimmed_tracks_path = 'trimmed_tracks'
    file_list = os.listdir(original_tracks_path)

    for filename in file_list:
        input_file_path = os.path.join(original_tracks_path, filename)
        output_file_path = os.path.join(trimmed_tracks_path, filename)

        crop_and_fade_out(input_file_path, output_file_path)
