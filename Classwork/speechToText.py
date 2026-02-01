import queue
import sounddevice as sd
from vosk import Model,  KaldiRecognizer
import pyttsx3
import json
import datetime

model = Model("model")
recogniser = KaldiRecognizer(model, 16000)

audio_queue = queue.Queue()

tts_engine  = pyttsx3.init()

def callback(indata,frames, time , status):
    if status:
        print(status)
    audio_queue.put(bytes(indata))

def process_query():
    query = query.lower()
    
    if "time" in query:
        now = datetime.datetime.now().strftime("%m : %S")
        return f"Todays date is {now}"
    
    elif "date" in query:
        today = datetime.datetime.today().strftime("%B : %d : %Y")
        return f"Todays date is {today}"
    
    elif "exit" or "stop" in query:
        return "Gooodbye !!"
    
    else:
        return "Sorry I didnt understand"
    
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def main():
    print("🎤 Voice Assistant Started")
    print(" Say 'Time' , 'Date' or 'Exit ")

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype="int16",
        channels=1,
        callback=callback
    ):
        while True:
            data = audio_queue.get()    
            if recogniser.AcceptWaveform(data):
                result = json.loads(recogniser.Result())
                text = result.get("text", " ")

