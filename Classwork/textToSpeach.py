import speech_recognition as sr
import pyttsx3

from googletrans import Translator

def speak(text,language = "en"):

    engine  = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voice')

    if language == "en":
        engine.setProperty('voice', voices[0].id)

    else:
        engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recogniser = sr.Recognizer

    with sr.Microphone as source:
        print("?????? Please speak now in english")
        audio  = recogniser.listen(source)

    try:
        print("??????Recognising speak")
        text = recogniser.recognize_google(audio, language = "en-US")
        print(f"✅ You said{text}")
        return text
    
    except sr.UnknownValueError:
        print("❌ Couldn't understand the audio")


