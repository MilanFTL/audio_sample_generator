import os
import shutil

def delete_directory_contents(directory):
    try:
        # Remove all files in the directory
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

        # Remove all subdirectories in the directory
        for subdirectory in os.listdir(directory):
            subdirectory_path = os.path.join(directory, subdirectory)
            if os.path.isdir(subdirectory_path):
                shutil.rmtree(subdirectory_path)

        print(f"Contents of {directory} have been deleted.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    original_tracks_path = 'tracks'
    trimmed_tracks_path = 'trimmed_tracks'

    delete_directory_contents(original_tracks_path)

    delete_directory_contents(trimmed_tracks_path)
