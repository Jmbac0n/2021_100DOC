import pyaudio, os, pyttsx3
import speech_recognition as sr
import pocketsphinx

r = sr.Recognizer()
m = sr.Microphone(device_index=0)
engine = pyttsx3.init()

# Listen to audio and save as audio file
with m as source:
    print('Speak')
    audio = r.listen(source)

with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())

# Uses audio file saved in same file as script                                                                       
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "microphone-results.wav")

# Uses PocketSphinx to transcribe
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
    
try:
    print(r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("No understand")
except sr.RequestError as e:
    print("Error; {0}".format(e))

# Save transcribed audio to string and use if to determine response
text_string = r.recognize_sphinx(audio)
if text_string == "shut down":
    engine.say("Okay shutting down")
    engine.runAndWait()

#for index, name in enumerate(sr.Microphone.list_microphone_names()):
    #print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))