import pyttsx3

from gtts import gTTS
import os


engine  = pyttsx3.init()
engine.say('Say a Command')
engine.runAndWait()

tts = gTTS(text= 'Say a Command I\'m bilal ahmed', lang='en',slow ="True")
tts.save('hello.mp3')
os.system('hello.mp3')
