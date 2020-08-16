import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate",150)
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[20].id)
engine.say("Hola a todos como estan")
engine.runAndWait()
