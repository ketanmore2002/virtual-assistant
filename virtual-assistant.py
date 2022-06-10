import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
from pytube import YouTube

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Ketan!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Ketan!")   

    else:
        speak("Good Evening Ketan!")  

    speak("I am Kay. Sir Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 300000
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            try:
                speak("Which song you want to hear")
                content = takeCommand()
                pywhatkit.playonyt(content)
            except Exception as e:
                print(e)
                speak("Sorry cannot play this song")  
            
         
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
            
            
        elif 'play songs' in query:
            try:
                speak("Which song you want to hear")
                content = takeCommand()
                pywhatkit.playonyt(content)
            except Exception as e:
                print(e)
                speak("Sorry cannot play this song")    
                
                
                
        elif 'who are you' in query:
            try:
                speak("I am kay. Made by ketaan. in India")
                
            except Exception as e:
                print(e)
                speak("Sorry cannot play this song")
                
                
        elif 'play song' in query:
            try:
                speak("Which song you want to hear")
                content = takeCommand()
                pywhatkit.playonyt(content)
            except Exception as e:
                print(e)
                speak("Sorry cannot play this song")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open Chorme' in query:
            codePath = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"
            os.startfile(codePath)
            
            
        elif 'find these' in query:   #under progress
            try:
                speak("what should i search!")
                content = takeCommand()
                pywhatkit.search(content)
            except Exception as e:
                print(e)
                speak("Sorry cannot search at a moment!")
                
                
                
        elif 'download youtube video' in query:
             try:
                speak("which video should i download!")
                content = takeCommand()
                link = YouTube(pywhatkit.playonyt(content))
                speak('downloading video!')
                video = url.stream.first()
             except Exception as e:
                  print(e)
                  speak("Sorry cannot search at a moment!")
            
            
        elif 'download youtube videos' in query:
            try:
                speak("which video should i download!")
                content = takeCommand()
                link = YouTube(pywhatkit.playonyt(content))
                speak('downloading video!')
                video = url.stream.first()
            except Exception as e:
                print(e)
                speak("Sorry cannot search at a moment!")
              
        

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")    
