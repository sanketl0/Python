import gtts
import playsound


text = input("enter something : ")
sound = gtts.gTTS(text, lang = "hi")
sound.save("YZ.mp3")
playsound.playsound("YZ.mp3")

