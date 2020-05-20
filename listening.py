import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<=12:
        speak("Good Morning")

    elif hour>12 and hour<=18:
        speak("Good Afternoon")

    else:
        speak("hii")

    speak("I am Jarvis Sir. Please tell me how can I help you")  

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration=5)
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n") 

    except Exception as e:
        print (e)
        print("Say that again please...")
        return "none"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mayureshsevekar22@gmail.com', 'shwetavidhi')
    server.sendmail('mayureshsevekar22@gmail.com', to ,content)
    server.close()

if __name__ == "__main__":

    wishMe()
    while True:
        query = takeCommand().lower()
     #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results) 
        elif 'open youtube' in query:
            speak("opening please have patience sir...")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening please have patience sir...")
            webbrowser.open("google.com")
        elif 'play music' in query:
            speak("opening please have patience sir...")
            music_dir = 'C:\\Users\\mayur\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))    
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        elif 'open code' in query:
            speak("opening please have patience sir...")
            codePath = 'C:\\Users\\mayur\\Desktop\\Microsoft VS Code'
            os.startfile(codePath)
        elif 'email to receiver name' in query:
            try:
                speak("What should I do..?")
                content = takeCommand()
                to = "receiver email"
                sendEmail(to , content)
                speak("Email has been sent..")
            except Exception as e:
                print(e)
                speak("Sorry email not sent!")
        elif 'open vlc' in query:
            speak("opening please have patience sir...")
            vlc = 'C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe'
            os.startfile(vlc)
        elif 'open course' in query:
            speak("opening please have patience sir...")
            webbrowser.open("coursera.org")
        elif 'play video' in query:
            speak("opening please have patience sir...")
            video_dir = 'C:\\Users\\mayur\\Videos'
            videos = os.listdir(video_dir)
            print(videos)
            os.startfile(os.path.join(video_dir,videos[0]))
        elif 'how are you' in query:
            speak("Feeling awesome sir.....") 
        elif 'open colours' in query:
            speak("opening please have patience sir...")
            webbrowser.open("voot.com")
        elif 'open whatsapp' in query:
            speak("opening please have patience sir....")
            webbrowser.open("https://web.whatsapp.com/")