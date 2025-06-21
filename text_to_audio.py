# By using the elevenlabs
# Use this link to go on elevenlabs ->   https://elevenlabs.io/

# To import in python search ->  elevenlabs text to speech python

# Use this link to copy the command -> https://elevenlabs.io/docs/cookbooks/text-to-speech/streaming

# pip install elevenlabs
# Now after that copy the text to speech (file) and paste it ...


# import os
# import uuid
# from elevenlabs import VoiceSettings
# from elevenlabs.client import ElevenLabs
# from config import ELEVENLABS_API_KEY

# elevenlabs = ElevenLabs(
#     api_key=ELEVENLABS_API_KEY,
# )


# def text_to_speech_file(text: str, folder: str) -> str:
#     # Calling the text_to_speech conversion API with detailed parameters
#     response = elevenlabs.text_to_speech.convert(
#         voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
#         output_format="mp3_22050_32",
#         text=text,
#         model_id="eleven_turbo_v2_5", # use the turbo model for low latency
#         # Optional voice settings that allow you to customize the output
#         voice_settings=VoiceSettings(
#             stability=0.0,
#             similarity_boost=1.0,
#             style=0.0,
#             use_speaker_boost=True,
#             speed=1.0,
#         ),
#     )

#     # uncomment the line below to play the audio back
#     # play(response)

#     # Generating a unique file name for the output MP3 file
#     save_file_path = os.path.join(f"user_upload/{folder}", "audio.mp3")

#     # Writing the audio to a file
#     with open(save_file_path, "wb") as f:
#         for chunk in response:
#             if chunk:
#                 f.write(chunk)

#     print(f"{save_file_path}: A new audio file was saved successfully!")

#     # Return the path of the saved audio file
#     return save_file_path






# If elevenlabs not working with free use this TTS
# Gtts Link  ->  https://pypi.org/project/gTTS/

# Use Gtts without an api and not preinstall library
# As in elevenlabs you can change your voice, edit your voice and do lot of stuff

import os
import uuid
from gtts import gTTS

def text_to_speech_file(text: str, folder: str) -> str:
    # Convert text to speech using gTTS
    tts = gTTS(text=text, lang='en')

    # Generate the path where the audio will be saved
    save_file_path = os.path.join(f"user_upload/{folder}", "audio.mp3")

    # Make sure the folder exists
    os.makedirs(os.path.dirname(save_file_path), exist_ok=True)

    # Save the audio file
    tts.save(save_file_path)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    return save_file_path

# Example usage
# text_to_speech_file("Hey I am the Dushyant Sharma from Haryana", "3710c810-4e68-11f0-940a-e4a8dff0f5bf")
