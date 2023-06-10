#!/usr/bin/env python3

"""
Скрипт для чтения pdf-файла и озвучки полученного текста

Написан на основе видео https://youtu.be/Q0lHb-FCATk
Канал: PythonToday
"""

import pdfplumber
from art import tprint
from gtts import gTTS
from pathlib import Path


def pdf_to_mp3(file_path="test.pdf", language="en"):
    if not Path(file_path).is_file():
        return "The file doesn't exist, check the file path!"

    if not Path(file_path).suffix == ".pdf":
        return "Invalid format!"

    print(f"Parsing {Path(file_path).name}")
    with pdfplumber.PDF(open(file=file_path, mode="rb")) as pdf:
        pages = [page.extract_text() for page in pdf.pages]

    text = "".join(pages)
    text = text.replace("\n", "")

    my_audio = gTTS(text=text, lang=language, slow=False)
    file_name = Path(file_path).stem
    my_audio.save(f"{file_name}.mp3")

    return f"[+] {file_name}.mp3 saved successfully!\n---Have a good day!---"


tprint("PDF-TO-MP3", font="bulbhead")
file_path = input("\nEnter file's path to decode: ")

lang = input("Choose the language [en | ru ]: ")
if lang not in ("en", "ru"):
    print(f"Invalig langiage {lang}")

result = pdf_to_mp3(file_path=file_path, lang=lang)
print(result)
