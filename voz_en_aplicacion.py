import pyttsx3
engine = pyttsx3.init()

#CONFIGURACION DE VOZ
engine.setProperty("rate",150)
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[20].id)
#FIN DE CONFIGURACION 
engine.say("Hola a todos como estan")
engine.runAndWait()
