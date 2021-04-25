import pyttsx3
import datetime as dt
import speech_recognition as sr
import wikipedia as wp
import webbrowser
import os
import random
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def logic():
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wp.summary(query, sentences=2)
            speak("According to wikipedia ")
            print(results)
            speak(results)
        elif 'thanks' in query:
            speak("Your welcome sir")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            video_dir = 'E:\\videos\\BOLLYWOOD'
            videos = os.listdir(video_dir)
            n = random.randint(0,len(videos)-1)
            print(videos[n])
            os.startfile(os.path.join(video_dir,videos[n]))
        elif 'time' in query:
            strTime = dt.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}\n")
        elif 'joke' in query:
            speak(pyjokes.get_joke())


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer();
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')
        return query
    except Exception as e:
        print("Say that again Please...")
        return 'None'


def wishMe():
    hour = int(dt.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning Sir')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon Sir')
    else:
        speak('Good Evening Sir')

    speak('I am Jarvis. Please tell me how may I help you')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    wishMe()
    logic()
