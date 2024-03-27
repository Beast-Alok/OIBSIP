import pyttsx3
import speech_recognition as sr
import os
import webbrowser

#audio engine from windows

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

#triggering for audio

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommands(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    speak("Hello sir, this is your jarvis")
    query = ""
    while query != "quit":
        query = takeCommands().lower()
        speak(query)
