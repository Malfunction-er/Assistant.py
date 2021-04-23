import speech_recognition as sr
from time import sleep
from datetime import datetime
import webbrowser
import pyttsx3, os

r = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
  engine.say(text)
  engine.runAndWait()

speak("Hey!!! how can I help you today?") 
def recognize_voice():
  text = ''
  with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    voice = r.listen(source)
    try:
      text = r.recognize_google(voice)
    except sr.RequestError:
      speak("Sorry, the I can't access the Google API...")
    except sr.UnknownValueError:
      speak("Sorry, Unable to recognize your speech...")
  return text.lower()
  
def reply(text_version):
    if "google" in text_version:                                #say google to search for something
        speak("What do you want me to search for?")
        keyword = recognize_voice()
        if keyword != '':
            url = ("https://google.com/search?q=" + keyword)
            speak("Here are the search results for " + keyword)
            webbrowser.open(url)
            sleep(3)
    elif "bye" in text_version:
        speak("okay bye")
        exit()
    elif "time" in text_version:
        time = datetime.now().time().strftime("%H %M")
        speak("The time is " + time)
    elif "hi assistant" in text_version:                    #You can give it a name and put that instead of 'assistant'
        speak("hey. that's me")
    elif "date" in text_version:
        date = datetime.now().strftime("%d/%m/%Y")
        speak(date)
    elif "thanks" in text_version:
        speak("my pleasure!")
    elif "open" in text_version:
        speak("What do you want me to open?")
        key = recognize_voice()
        os.system(key)
    else:
        speak("say that again please?")
        
while True:
  speak("What would you like me to do?")
  text_version = recognize_voice()
  reply(text_version)
