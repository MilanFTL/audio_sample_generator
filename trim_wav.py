import wave
import numpy as np
import os

def trim_wav(input_file, output_file, duration=30):
    try:
        with wave.open(input_file, 'rb') as input_wav:
            params = input_wav.getparams()
            sample_width = params.sampwidth
            framerate = params.framerate
            num_frames = int(framerate * duration)
            
            with wave.open(output_file, 'wb') as output_wav:
                output_params = params._replace(nframes=num_frames)
                output_wav.setparams(output_params)
                
                audio_data = np.frombuffer(input_wav.readframes(num_frames), dtype=np.int16)
                output_wav.writeframes(audio_data.tobytes())
                
        print(f"Trimmed {input_file} to {output_file} successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    original_tracks_path = 'tracks'
    trimmed_tracks_path = 'trimmed_tracks'
    file_list = os.listdir(original_tracks_path)

    for filename in file_list:
        input_file_path = os.path.join(original_tracks_path, filename)
        output_file_path = os.path.join(trimmed_tracks_path, filename)

        trim_wav(input_file_path, output_file_path)
