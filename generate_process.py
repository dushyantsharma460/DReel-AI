
# Use when you want made audio only with AI

# # This file looks for new folder inside user uploads and converts them into reel if they are not already converted

# # Firstly to make the speech converted mp3 file from the description text file 

# import os
# from text_to_audio import text_to_speech_file
# import time 
# # Use FFmpeg to complete the project
# # FFmpeg is a powerful open-source tool used to process audio, video, and other multimedia files and streams. It's widely used by developers, content creators, and media engineers.
# import subprocess

# def text_to_audio(folder):
#     print("TTA",folder)
#     # To give the text you need to read the folder
#     with open(f"user_upload/{folder}/desc.txt") as f:
#         text = f.read()
#     print(text,folder)
#     text_to_speech_file(text,folder)

# def create_reel(folder):
#     command = f'''ffmpeg -f concat -safe 0 -i user_upload/{folder}/input.txt -i user_upload/{folder}/audio.mp3 -vf "scale=1080:1920: force_original_aspect_ratio=decrease, pad=1080:1920: (ow-iw)/2: (oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4
# '''
#     subprocess.run(command, shell=True, check=True)  # shell = True makes sure that this is running as a shell command as a string 
#     # check = True makes sures that it doesn't through non zero error
    

#     print("CR", folder)

# if __name__ == "__main__":

# # Create a done.txt to remember which folder reel is complete we can use database mainly for this type of task 
    

#     # Now to run it in every 4 second i use loop for that

#     # Now it check in every 4 second which new folder came and and process it and append it into the done list

#     while True:
#         print("Processing queue ......")
#         with open("done.txt", "r") as f:
#             done_folders = f.readlines()

#         # Use list comprehension that creates a new list by removing leading and trailing whitespace from each element in done_folders

#         # Simple list comprehension -> [i for i in done_folders]

#         done_folders = [i.strip() for i in done_folders]    # Remove extra white spaces and special character
        
#         print("Done folder :",done_folders)
#         folders = os.listdir("user_upload")
#         for folder in folders:
#             if(folder not in done_folders):
#                 text_to_audio(folder)      # Generate the audio.mp3 from desc.txt
#                 create_reel(folder)        # Convert the images and audio.mp3 inside the folder to a reel 
#                 with open("done.txt","a") as f:    # If done append in done.txt
#                     f.write(folder + "\n")
#         time.sleep(4)


# Use this when audio with upload + AI Generate

import os
from text_to_audio import text_to_speech_file
import time
import subprocess

def text_to_audio(folder):
    """Generate audio from text if desc.txt exists"""
    desc_path = f"user_upload/{folder}/desc.txt"
    if os.path.exists(desc_path):
        print(f"Generating audio for {folder}")
        with open(desc_path) as f:
            text = f.read()
        text_to_speech_file(text, folder)
    else:
        print(f"No desc.txt found in {folder}, using uploaded audio if available")

def create_reel(folder):
    """Create video reel from images and audio"""
    input_txt = f"user_upload/{folder}/input.txt"
    audio_file = f"user_upload/{folder}/audio.mp3"
    output_file = f"static/reels/{folder}.mp4"
    
    # Check if audio file exists (either uploaded or generated)
    if not os.path.exists(audio_file):
        print(f"No audio file found for {folder}")
        return
    
    # FFmpeg command with error handling
    try:
        command = [
            'ffmpeg',
            '-f', 'concat',
            '-safe', '0',
            '-i', input_txt,
            '-i', audio_file,
            '-vf', 'scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black',
            '-c:v', 'libx264',
            '-c:a', 'aac',
            '-shortest',
            '-r', '30',
            '-pix_fmt', 'yuv420p',
            output_file
        ]
        
        subprocess.run(command, check=True)
        print(f"Successfully created reel: {output_file}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error creating reel for {folder}: {e}")
    except Exception as e:
        print(f"Unexpected error processing {folder}: {e}")

def process_new_folders():
    """Check for and process new folders"""
    with open("done.txt", "r") as f:
        done_folders = [i.strip() for i in f.readlines()]
    
    folders = [f for f in os.listdir("user_upload") 
               if os.path.isdir(f"user_upload/{f}") and f not in done_folders]
    
    for folder in folders:
        print(f"Processing new folder: {folder}")
        try:
            text_to_audio(folder)
            create_reel(folder)
            
            # Only mark as done if successful
            with open("done.txt", "a") as f:
                f.write(folder + "\n")
                
        except Exception as e:
            print(f"Failed to process {folder}: {e}")

if __name__ == "__main__":
    # Create required directories if they don't exist
    os.makedirs("user_upload", exist_ok=True)
    os.makedirs("static/reels", exist_ok=True)
    
    if not os.path.exists("done.txt"):
        open("done.txt", "w").close()
    
    print("DReel AI processing started...")
    while True:
        process_new_folders()
        time.sleep(4)