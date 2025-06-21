# from gtts import gTTS

# text = "Hello, this is a test using Google Text to Speech."
# tts = gTTS(text)
# tts.save("output.mp3")


from gtts import gTTS

text = "नमस्ते, मेरा नाम दुश्यंत शर्मा है।"
tts = gTTS(text=text, lang='hi')
tts.save("output.mp3")
