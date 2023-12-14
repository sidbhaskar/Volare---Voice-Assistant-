#importing modiules

import pyttsx3 
import datetime 
import speech_recognition as sr 
import random 
import RockPaperScissor 
import MathGame 

#selecting voice for volore 
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')  
engine.setProperty('voice',voices[0].id) 
 
def speak(audio):                   #function to speak the text
    engine.say(audio) 
    engine.runAndWait() 
 
def wishMe():                       #for greeting according to time
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12: 
        speak("Good Morning") 
    elif hour>=12 and hour<15: 
        speak("Good Afternoon") 
    elif hour>=15 and hour<19: 
        speak("Good Evening") 
    else: 
        speak("Hello") 
wishMe()

#-------------------------------MENU----------------------------------

print('''
o------------------------------------------------------o
|                                                      |
| I am VOLARE, An Advanced Speech Recognition Program  |
|                                                      |
o------------------------------------------------------o
''')
speak("I am VOLARE, an advanced speech recognition program")                                     
print('Oo-----------------| Menu |---------------oO') 
speak('Menu')
print('')
print('1. Speech-to-text') 
print('2. Text-to-speech') 
print('3. Game') 
speak('First, Speech-to-text') 
speak('Second, Text-to-speech') 
speak('Third, Game') 
speak('What do you want to use? Please enter option number: ')
print('')
print('Oo----------------------------------------oO') 
INPUT=int(input('What do you want to use? Please enter option number: '))
print('Oo----------------------------------------oO')
print('')
 
def takeCommand(): 
    #IT TAKES MICROPHONE INPUT FROM THE USER AND RETURNS STRING OUTPUT 
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        print("Listening...") 
        r.pause_threshold = 1 
        audio = r.listen(source) 
 
    try: 
        print("Recognizing...") 
        query = r.recognize_google(audio, language = 'en-in')               #using GOOGLE's voice recognisation engine
        print(f"User said: {query}\n") 
 
    except Exception as e:  
        print("Say that again please...") 
        speak("Say that again please...") 
        return "None" 
     
    return query 
 

#----------------------------- MAIN PROGRAM AREA ----------------------------

if __name__ == "__main__": 
    if INPUT==1:                                                            #Speech-to-text 
        print('To close the Voice Assistant, please say - Terminate') 
        speak('To close the Voice Assistant, please say - Terminate') 
        while True: 
            query = takeCommand().lower() 
            if 'terminate' in query: 
                break 
    if INPUT==2:                                                            #Text-to-speech
        print('To close the Voice Assistant, please type - Terminate') 
        speak('To close the Voice Assistant, please type - Terminate') 
        while True: 
            x=input('Input: ') 
            speak(x) 
            if (x=='terminate' or x=='Terminate' or x=='TERMINATE'): 
                break 
                 
    if INPUT==3:                                                            #Games
        print('We have two games:') 
        speak('We have two games:') 
        print('1. Math Game') 
        speak('First, Math Game') 
        print('2. Rock Paper Scissor') 
        speak('Second, Rock paper scissors game') 
        speak('Which game do you want to play? Please enter option number: ')
        print('')
        print('Oo----------------------------------------oO')
        x=int(input('Which game do you want to play? [Please enter option number]: '))
        print('Oo----------------------------------------oO')
        print('')
         
        if x==1: 
            MathGame.start()                    #MATHS GAME!
        elif x==2: 
            RockPaperScissor.RockPaperScissor() #ROCK PAPER SCISSOR!
