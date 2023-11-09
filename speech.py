import os 
import speech_recognition as sr

commandmp3 = "ffmpg -i Bolna.mp4 Bolna.mp3"
command2wav = "ffmpg -i Bolna.mp3 bolna,wav"

os.system(commandmp3)
os.system(command2wav)

r = sr.Recognizer()

audio = sr.AudioFile('Bolna.wav')
audio = r.record(commandmp3,duration=100)
print(r.recognize_google(audio))