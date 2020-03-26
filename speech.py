# Программа для распознавания речи

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)
    try:
        output = r.recognize_google(audio)
        print("You said: {}".format(ottput))
    except:
        print("I don't understand :c")
