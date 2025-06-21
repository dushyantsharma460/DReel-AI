# This file looks for new folder inside user uploads and converts them into reel if they are not already converted

# Firstly to make the speech converted mp3 file from the description text file 

import os
from text_to_audio import text_to_speech_file
import time 
# Use FFmpeg to complete the project
# FFmpeg is a powerful open-source tool used to process audio, video, and other multimedia files and streams. It's widely used by developers, content creators, and media engineers.
import subprocess

def text_to_audio(folder):
    print("TTA",folder)
    # To give the text you need to read the folder
    with open(f"user_upload/{folder}/desc.txt") as f:
        text = f.read()
    print(text,folder)
    text_to_speech_file(text,folder)

def create_reel(folder):
    command = ""
    subprocess.run(command, shell=True, check=True)  # shell = True makes sure that this is running as a shell command as a string 
    # check = True makes sures that it doesn't through non zero error
    

    print("CR", folder)

if __name__ == "__main__":

# Create a done.txt to remember which folder reel is complete we can use database mainly for this type of task 
    

    # Now to run it in every 4 second i use loop for that

    # Now it check in every 4 second which new folder came and and process it and append it into the done list

    while True:
        print("Processing queue ......")
        with open("done.txt", "r") as f:
            done_folders = f.readlines()

        # Use list comprehension that creates a new list by removing leading and trailing whitespace from each element in done_folders

        # Simple list comprehension -> [i for i in done_folders]

        done_folders = [i.strip() for i in done_folders]    # Remove extra white spaces and special character
        
        print("Done folder :",done_folders)
        folders = os.listdir("user_upload")
        for folder in folders:
            if(folder not in done_folders):
                text_to_audio(folder)      # Generate the audio.mp3 from desc.txt
                create_reel(folder)        # Convert the images and audio.mp3 inside the folder to a reel 
                with open("done.txt","a") as f:    # If done append in done.txt
                    f.write(folder + "\n")
        time.sleep(4)