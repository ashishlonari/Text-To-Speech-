from gtts import gTTS
#gTTS (Google Text-to-Speech), a Python library

import os

#The OS module in python provides functions for interacting with the operating system

f=open('1.txt');
x=f.read()

language='en'

audio=gTTS(text=x,lang=language,slow = False)
audio.save("1.mp3")
os.system("1.mp3")
