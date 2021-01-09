import pyaudio, os, pyttsx3, pocketsphinx
import speech_recognition as sr

from playsound import playsound

def main():

    r = sr.Recognizer()
    m = sr.Microphone(device_index=0)
    engine = pyttsx3.init()

    def listen():

        # Listen to audio and save as audio file
        with m as source:
            print('Speak')
            audio = r.listen(source)

        with open("microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())

        # Uses audio file saved in same file as script                                                                       
        from os import path
        AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "microphone-results.wav")

        transcribe(AUDIO_FILE)

    def transcribe(audio_file):

            # Uses PocketSphinx to transcribe
            r = sr.Recognizer()
            with sr.AudioFile(audio_file) as source:
                audio = r.record(source)
                
            try:
                print(r.recognize_sphinx(audio))
            except sr.UnknownValueError:
                print("No understand")
            except sr.RequestError as e:
                print("Error; {0}".format(e))

            respond(audio)

    def respond(recorded_audio):

            # Save transcribed audio to string and use if to determine response
            text_string = r.recognize_sphinx(recorded_audio)
            if text_string == "play":
                engine.say("Okay playing music")
                engine.runAndWait()
                playsound('examplemusic') # Testing that other functionality works with voice command

    #for index, name in enumerate(sr.Microphone.list_microphone_names()):
        #print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

    listen()

main()

# TODO
# Place recogniser into a def, so it can be called multiple times
# Test shutting down using a confirm
# Set mic to listen in background for wake up command