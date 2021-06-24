from os import close
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Monkey and How may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query: r.recognize_google(audio, language='en-in')
            print(f"User Said: (query)\n")
            
        except Exception as e:
            print("Please Say that again...")
            return "None"
        return query

    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.email('youremail@gmail.com', 'password')
    server.sendEmail('email@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    speak("Hey there")
    wishMe()
    while True:
        query =  takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
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

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is (strTime)")

        elif 'email to vivek' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "email@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Sorry for the inconvinence, I'm unable to send this email.")



