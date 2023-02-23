#!/usr/bin/env python3

"""
Распознавание речи
"""

import speech_recognition as sr


rec = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak:")
    audio = rec.listen(source)
    try:
        output = rec.recognize_google(audio)
        print("You said: {}".format(output))
    except Exception:
        print("I don't understand :c")
