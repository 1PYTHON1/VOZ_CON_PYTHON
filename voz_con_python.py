# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 18:57:31 2020

@author: Admin
"""
# investigar pygsr reconocimiento de voz

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("HOLA MUNDO")
# engine.runAndWait()
#
import pyttsx3 as pyttsx
#para definir una voz en particular
engine = pyttsx.init()
voices = engine.getProperty('voices')
#indice para voz [0] - Español-HELENA ; [1] Ingles-ZIRA;[2] Ingles-SABINA
engine.setProperty('voice', voices[2].id)
engine.say('Hola Jose, bienvenido ')
engine.runAndWait()


import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voice.id)
    engine.say('hola mundo')
engine.runAndWait()
# import pyttsx3
# engine = pyttsx3.init() # object creation

# """ RATE"""
# rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
# engine.setProperty('rate', 125)     # setting up new voice rate


# """VOLUME"""
# volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)                          #printing current volume level
# engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

# """VOICE"""
# voices = engine.getProperty('voices')       #getting details of current voice
# #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[2].id)   #changing index, changes voices. 1 for female

# engine.say("Hello World!")
# engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()

# """Saving Voice to a file"""
# # On linux make sure that 'espeak' and 'ffmpeg' are installed
# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()
