import pyttsx3

# Initialize the text-to-speech engine only once
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
engine.setProperty('rate',180)
engine.say("hello my name is ratik")
engine.runAndWait()