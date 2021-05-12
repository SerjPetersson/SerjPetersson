import subprocess
import pyttsx3
import smtplib
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
from gtts import gTTS
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from clint.textui import progress
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 6 and hour<12:
        speak("Доброе утро !")
  
    elif hour>= 12 and hour<18:
        speak("Добрый день !")   
  
    else:
        speak("Добрый вечер !")  
  
    assname =("Меня зовут Сири")
    speak("Я твоя помощница")
    speak(assname)
     
 
def usrname():
    speak("Как зовут тебя?")
    uname = takeCommand()
    speak("Рада знакомству")
    speak(uname)
    
     
    
     
    speak("Что делать будем?")
 
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Слушаю...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Обрабатываю...")    
        query = r.recognize_google(audio, language ='ru-RU')
        print(f"Ты сказал: {query}\n")
  
    except Exception as e:
        print(e)    
        print("Не могу понять тебя")  
        return "None"
     
    return query
if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    
    clear()
    wishMe()
    usrname()
     
    while True:
         
        query = takeCommand().lower()
         
        
        if 'википедия' in query:
            speak('Ищу в Википедии...')
            query = query.replace("википедия", "")
            wikipedia.set_lang("ru")
            results = wikipedia.summary(f'{query}', sentences = 5)
            speak("Согласно википедии")
            print(results)
            speak(results)

            
        
 
        elif 'открой бомбардир' in query:
            url='https://bombardir.ru/'   
            speak("Открываю сайт бомбардир\n")
            webbrowser.open_new(url)
 
        elif 'открой гугл' in query:
            url='https://www.google.com'    
            speak("Открываю гугл\n")
            webbrowser.open(url)
 
        elif 'открой' in query:
            reg_ex = re.search('открой (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                print(domain)
                url = 'https://www.' + domain
                webbrowser.open(url)
                speak('Открываю сайт')
        
 
        elif 'включи музыку' in query or "включи песню" in query:
            speak("Послушай музыку")
            
            music_dir = "D:\Triangle Sun"
            songs = os.listdir(music_dir)
                
            random = os.startfile(os.path.join(music_dir, songs[1]))
 
        elif 'подскажи время' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
    
            speak(f"Сейчас {strTime}")

        elif 'включи проигрыватель' in query:
            speak("Включаю проигрыватель")
            import gui
            
            
            
                    
            
            
            

            
            
            
            
                 
        elif 'как поживаешь' in query or "как дела" in query:
            speak("Я замечательно, спасибо")
            speak("А как у тебя дела?")
 
        elif 'отлично' in query or "хорошо" in query:
            speak("Я рада, что так")

        elif 'не очень' in query or "плохо" in query:
            speak("Бедняжка")
 
        
 
        elif "измени имя" in query or "поменяй имя" in query:
            speak("Хорошо. Как хочешь меня называть? ")
            assname = takeCommand()
            speak("Спасибо за имя")
 
        elif "как тебя зовут" in query or "как твоё имя" in query:
            speak("Меня зовут")
            assname =("Сири")
            speak(assname)
            
 
        elif 'пока' in query or "до свидания" in query:
            speak("Жаль, что уходишь. Но знаю, что ненадолго")
            exit()
 
        elif "кому ты помогаешь" in query or "кто ещё знает о тебе" in query: 
            speak("Я только твоя")
            speak(uname)
             
                 
        elif "для чего ты создана" in query:
            
            speak("Я создана, чтобы помогать")
 
       
        elif "кто ты" in query:
            speak("Я та, что поможет тебе. Хоть немного")
 
         
        elif "где находится" in query or "найди на карте" in query:
            
            query = query.replace("найди на карте", "")
            
            location = query
            speak("Ты искал на карте")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")
 
 
        

        elif 'найди в гугл' in query:
            
            query = query.replace("найди в гугл", "")

            webbrowser.open("https://google.com/search?q=" + query + "")
            speak("Ты искал в интернете" + query)
            speak("Вот, я нашла" + query)





            


  

    
