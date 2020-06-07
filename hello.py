import pyttsx3 #pip install pyttx3
import datetime
import speech_recognition as sr #install 
import wikipedia #pip install wikipedia
import smtplib
import webbrowser
import os

engine = pyttsx3.init()
#engine.say("HELLO NIKHIL SHARMA HOPE YOU ARE AT HOME STAY HOME STAY SAFE ")
#engine.runAndWait()



#speak function 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak("this is jarvis")

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

#time()

def date():
    year = datetime.datetime.now().year  #give year nd convert integer
    month = datetime.datetime.now().month
    speak("the current date is")
    date = datetime.datetime.now().date
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("welcome back sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good morning sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir!")
    elif hour >=18 and hour<24:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")
    speak("jarvis at your service please tell me how i can help you")

#wishme()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1) #wait for 1 sec and after that listen to audio
        audio=r.listen(source)
    try:
        print("Recongnizing ...")
        query=r.recognize_google(audio,language='en-in')
        print(query)
    
    except Exception as e:
        print(e)
        #speak("say again")
        
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query=takeCommand().lower() #in lower case
        
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("SEARCHING... ")
            query = query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif  'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'logout' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
             os.system("shutdown /s /t l")
        
        elif 'play songs' in query:
            songs_dir='D:\\music'
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
           
        elif 'offline' in query:
            quit()
        
        



