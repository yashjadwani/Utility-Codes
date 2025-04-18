import os
from moviepy.editor import VideoFileClip

# Folder containing the videos
input_folder = "Input Source File Path"
output_folder = "Input Destination File Path"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all video files in the folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):  # Process only .mp4 files
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.mp4")
        
        print(f"Processing: {filename}")
        
        # Load the video and remove audio
        video = VideoFileClip(input_path)
        video_without_audio = video.without_audio()
        video_without_audio.write_videofile(output_path)

print("All videos processed! Check the 'output' folder.")
