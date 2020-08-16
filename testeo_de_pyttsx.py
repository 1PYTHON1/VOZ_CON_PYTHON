import pyttsx3


engine = pyttsx3.init()

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[20].id)   #changing index, changes voices. 1 for female

""" RATE_VELOCIDAD"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
velocidad = 170          #valor de velocidad de voz
engine.setProperty('rate',velocidad)     # setting up new voice rate

engine.say("HOLA MUNDO")
engine.say('Mi tasa de velocidad actual es ' + str(velocidad))
engine.runAndWait()
engine.stop()

engine.save_to_file('HOLA A TODOS BUENOS DIAS ', 'test.mp3')
engine.runAndWait()
# engine.say("BUENAS NOCHES JOSE")
# engine.runAndWait()
