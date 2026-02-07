import speech_recognition as sr
import pyttsx3
from datetime import datetime


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak now...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print(f"✅ You said: {command}")
            return command.lower()
        
        except sr.UnknownValueError:
            print("❌ Couldn't understand.")

        except sr.RequestError as e:
            print(f"❌ API error: {e}")

    return ""

def respond_to_command(command):
     
    if "hello" in command:
        speak("Hi there! How can I help!")

    elif "your name" in command:
         
        speak("Hello I am a Ai assistant, What do you want!!!!!!!!!!!")

    elif "time" in command:
        now = datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}")
    
    elif "exit" in command:
        speak("Why did you have to leave me. AAAAAAAAAAAAAhhhhhhhhhhhh!!!!!!")
        return False
    
    else:
        speak("I am not sure about that, Next time talk english properly")
    return True

def main():
    speak("Voice assistant activated, start yapping!!!")

    while True:
        command = get_audio()
        if command and not respond_to_command(command):
            break

if __name__ == "__main__":
    main()
        
     
