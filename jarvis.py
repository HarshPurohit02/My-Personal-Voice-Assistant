import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak ("Hello Harsh, I am here to help you!")

def takeCommand():
    # It takes microphone inpur from the user and returns string output from the user.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language = "en-in")
        print(f"User said:{query}\n")
              
    except Exception as e:
        #print(e)
        print("Say it again Please")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gnail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mailhrp007@gmail.com', 'tiqsraopspjdvpxr')
    server.sendmail('forpics833@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    speak ("Jay Shree Ram")
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
         
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searcing Wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("Accouding to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
                webbrowser.open("youtube.com")

        elif 'open google' in query:
                webbrowser.open("google.com")

        elif 'open facebook' in query:
                webbrowser.open("facebook.com")

        elif 'play music' in query:
                music_dir = 'D:\Projects\Software Projects\JarvisAI\Songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir The time is {strTime}")

        elif 'open code' in query:
                codePath = "C:\\Users\\HARSH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

        elif 'email to harsh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "forpics833@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                    print(e)
                    speak("Sorry my firend, I am not able to send this Email")