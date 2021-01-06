import pyaudio, os
import speech_recognition as sr
import pocketsphinx

r = sr.Recognizer()
m = sr.Microphone(device_index=0)

#with m as source:
    #print('Speak')
    #print(m.list_microphone_names())
    #audio = r.listen(source)
                                                                       

#for index, name in enumerate(sr.Microphone.list_microphone_names()):
    #print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "hello.wav")

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
    print(str(audio))