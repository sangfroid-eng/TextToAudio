from gtts import gTTS
text=""
with open ("AudioText.txt","r") as file:
    for line in file:
        text=text+line
speech=gTTS(text,"en")
speech.save("audio.mp3")
