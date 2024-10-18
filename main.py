import pyttsx3
import speech_recognition as sr
import webbrowser
import time 
import datetime
import os
from pydub import AudioSegment
from pydub.playback import play
import pyautogui 

# Initialize pyttsx3 engine
wel = pyttsx3.init()
voices = wel.getProperty('voices')
wel.setProperty('voice', voices[1].id)  # Correct the property name

def Speak(audio):
    wel.say(audio)
    wel.runAndWait()

def TakeComments():
    recognizer = sr.Recognizer()  # Renamed for clarity
    with sr.Microphone() as mic:
        print('Say something...')
        recognizer.phrase_threshold = 0.4
        audio = recognizer.listen(mic)
        try:
            print('Recording...')
            query = recognizer.recognize_google(audio, language='ar')  # Changed to recognize_google
            print(f'You said: {query}')
        except Exception as Error:
            print("Error recognizing speech:", Error)
            return None
        return query.lower()

# Play welcome music
music = AudioSegment.from_mp3('sounds/welcome.mp3')
play(music)
time.sleep(1)
music = AudioSegment.from_mp3('sounds/wecome2.mp3')
play(music)

# Main loop
while True:
    try:
        query = TakeComments()
        if query is None:
            continue

        if 'صباح الخير' in query:
            b = AudioSegment.from_mp3('sounds/goodmorning.mp3')
            play(b)
        
        elif 'مساء الخير' in query:
            b = AudioSegment.from_mp3('sounds/goodevening.mp3')
            play(b)

        elif 'افتح جوجل' in query:
            b = AudioSegment.from_mp3('sounds/google.mp3')
            play(b)
            time.sleep(2)
            webbrowser.open_new_tab('https://www.google.com')

        elif 'ماذا لدى اليوم' in query:
            b = AudioSegment.from_mp3('sounds/mot3ab.mp3')
            play(b)

        elif 'اغلق الحاسوب' in query:
            b = AudioSegment.from_mp3('sounds/closePC.mp3')
            play(b)
            os.system("shutdown /s /t 1")
            break  # Exit after shutdown command

        elif 'اريد ان ابرمج قليلا' in query:
            b = AudioSegment.from_mp3('sounds/program.mp3')
            play(b)
            cpath = "C:\\Users\\ToT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(cpath)

        elif 'اريد ان انشر منشور على فيسبوك' in query:
            b = AudioSegment.from_mp3('sounds/post.mp3')
            play(b)
            post = input('Enter your post: ')
            webbrowser.register('chrome', None, 
                                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open_new('https://www.facebook.com')
            time.sleep(10)
            pyautogui.typewrite(post)
            pyautogui.click(670, 585)  # Coordinates may need adjustment

        elif 'ذكرنى بموعد دوائى' in query:
            reminder_time = input('Enter Time (HH:MM:SS): ')
            b = AudioSegment.from_mp3('sounds/alarm.mp3')
            play(b)
            while True:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                if current_time == reminder_time:
                    b = AudioSegment.from_mp3('sounds/doaa.mp3')
                    play(b)
                    break
                time.sleep(1)  # Avoid busy looping

    except Exception as e:
        print(f"An error occurred: {e}")
