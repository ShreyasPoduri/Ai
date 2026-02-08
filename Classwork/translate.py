import speech_recognition as sr
import pyttsx3
from googletrans import Translator 

def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  
    voices = engine.getProperty('voices')

    if language == "en":
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()


def speech_to_text(): 
    recognizer = sr.Recognizer()
    with sr.Microphone as source:
        print("?????? Please speak english")
        audio = recognizer.listen(source)

    try:
        print("????? Recognising speech...")
        text = recognizer.recognize_google(audio, language = "en-US")

        print(f"✅ You said {text}!!")
        return text
    except sr.UnknownValueError:
        print("❌🗣️ Couldn't understand")

    except sr.RequestErrorm as e:
        print(F"❌🗣️ Api error {e}")
    return " "


def translate_text(text, target_lanuage = 'es'):
    translator = Translator
    translation = translator.translate(text, dest=target_lanuage)
    print(f"?????  Translated text: {translation.text} ")
    return translation.text


def display_language_options():
    print("???? Available translation languages: ")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")
    print("8. Punjabi (pa)")

    choice = input("Please select trangest language number from 1-8")
    language_dict = {
        "1":"hi",
        "2":"ta",
        "3":"te",
        "4":"bn",
        "5":"mr",
        "6":"gu",
        "7":"ml",
        "8":"pa"
    }

    return language_dict.get(choice,"es")

def main():
    target_lanuage = display_language_options()

    original_text = speech_to_text()

    if original_text:
        translated_text = translate_text(original_text, target_lanuage=target_lanuage)
        speak(translated_text, language="en")




