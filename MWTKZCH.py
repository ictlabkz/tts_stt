import cv2 #библиотека для работы с камерой
import numpy as np #библиотека для работы с камерой
import pytesseract #библиотека для считывания текста с изображений
from gtts import gTTS #библиотека для озвучки
import os #библиотека для озвучки
from googletrans import Translator #библиотека для перевода
import pyaudio #библиотека для определения голоса
import speech_recognition as sr #библиотека для распознавания голоса
import serial #библиотека для работы с портами и передачей информации по ним
import time #библиотека для временных задержек
import wolframalpha #библиотека для работы с поисковой системой
import wikipedia #библиотека для вывода информации из Википедии
import requests
import random as rand
from bs4 import BeautifulSoup # библиотека для создания звуковых сигналов
import vosk # библиотека для распознавания речи
from vosk import Model, KaldiRecognizer
import beepy
from rhvoice_wrapper import TTS # библиотека
import subprocess
import openai

def asdf():
    recognizer = KaldiRecognizer(model,16000)
    cap = pyaudio.PyAudio()
    stream = cap.open(format=pyaudio.paInt16,
                      channels = 1,
                      rate=16000,
                      input=True,
                      frames_per_buffer=8192
                        )
    beepy.beep(sound="coin")
    stream.start_stream()
    while True:
        data = stream.read(4096)
        if len(data) == 0:
            break
        
        if recognizer.AcceptWaveform(data):
            s = recognizer.Result()[14:]
            return(s[:-3])
            break

def wiki():
    data = tts.get('Сұраңыз', voice="nazgul", format_='wav')
    subprocess.check_output(['aplay', '-q'], input=data)
    rec = asdf()
    print(rec)
    query = translator.translate(rec, src='kk', dest='ru').text
    try:
        text = wikipedia.summary(query, sentences = 1)
        data = tts.get(translator.translate(text, src='ru', dest='kk').text, voice="nazgul", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)
    except:
        data = tts.get( "Кайталаңыз", voice="nazgul", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)


def sensor(): #функция для получения данных с датчиков и их озвучивания
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    ser.reset_input_buffer()
    g = 0
    t = 0
    while 1:
        line = ser.readline().decode('utf-8').rstrip()
        if "Heavy gases" in line:
            s1 = "Коміркышқыл газынын индикаторы текше метрге " + line[14:17] + " милиграмм"
            data = tts.get(s1, voice="nazgul", format_='wav')
            subprocess.check_output(['aplay', '-q'], input=data)
            if int(line[14:17]) < 600:
                data = tts.get('Кауіпсіз денгей', voice="nazgul", format_='wav')
                subprocess.check_output(['aplay', '-q'], input=data)
            else:
                data = tts.get('Кауіпті денгей', voice="nazgul", format_='wav')
                subprocess.check_output(['aplay', '-q'], input=data)
            print(s1)
            g += 1
        if "Temp" in line:
            print()
            s2 = "Температура " + line[7:9] + " градус"
            data = tts.get(s2, voice="nazgul", format_='wav')
            subprocess.check_output(['aplay', '-q'], input=data)
            t += 1
            print(s2)
        if t == 1 and g == 1:
            print (2)
            break
        time.sleep(1)



def wolf(): #функция для работы с поисковиком
        data = tts.get('Сұраңыз', voice="nazgul", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)
        rec = asdf()
        print(rec)
        que = translator.translate(rec, src='kk', dest='ru').text

        translationw1 = translator.translate(que, dest = "en")
        print (translationw1.text)

        try:
            app_id = 'PU5VGQ-YAWPRVQL42'
            client = wolframalpha.Client(app_id)
            res = client.query(translationw1.text)
            answer = next(res.results).text
            translationw2 = translator.translate(answer, dest = "kk")
            print(f"{translationw2.text}")

            data = tts.get(translationw2.text, voice="nazgul", format_='wav')
            subprocess.check_output(['aplay', '-q'], input=data)
        except:
            data = tts.get( "Кайталаңыз", voice="nazgul", format_='wav')
            subprocess.check_output(['aplay', '-q'], input=data)

def lon(): #функция для передачи команды на плату Arduino uno
    ser = serial.Serial('/dev/rfcomm0', 9600)
    k = 0

    while 1:
        ser.write(b'1\n')
        k += 1
        if k > 1:
            break
        
def loff(): #функция для передачи команды на плату Arduino uno
    ser = serial.Serial('/dev/rfcomm0', 9600)
    k = 0

    while 1:
        ser.write(b'0\n')
        k += 1
        if k > 1:
            break

def word_tr(): #функция перевода фраз на выбранный язык
    data = tts.get( "Тілді таңдау", voice="nazgul", format_='wav')
    subprocess.check_output(['aplay', '-q'], input=data)
    rec = asdf()
    print(rec)
    if "орыс" in rec:
        tr_language = "ru"
    elif "ағыл" in rec:
        tr_language = "en"
    elif "қазақ" in rec:
        tr_language = "kk"
    print(tr_language)
    data = tts.get( "Жаксы. Айтыныз", voice="nazgul", format_='wav')
    subprocess.check_output(['aplay', '-q'], input=data)
    rec = asdf()
    try:
        translaation1 = translator.translate(rec, dest = tr_language)
        data = tts.get(translaation1.text, voice="nazgul", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)
    except:
        data = tts.get( "Кайталаңыз", voice="nazgul", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)

def tail():
    x = rand.randint(0,6)
    lnk = 'mpg321  Projects/ertegiler/' + str(x) + '.mp3'
    os.system(lnk)
    '''url = 'https://tales.ictlab.kz/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('p',class_=x)
    for quote in quotes:
        data = tts.get(quote.text, voice="nazgul", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)'''

def chat():
    openai.api_key = "sk-..."
    # задаем модель и промпт
    model_engine = "text-davinci-003"
    rec = asdf()
    prompt = translator.translate(rec, src='kk', dest='ru').text

    # задаем макс кол-во слов
    max_tokens = 128 

    # генерируем ответ
    completion = openai.Completion.create(    
    engine=model_engine,    
    prompt=prompt,    
    max_tokens=1024,    
    temperature=0.5,    
    top_p=1,    
    frequency_penalty=0,    
    presence_penalty=0) 

    # выводим ответ
    translationw2 = translator.translate(completion.choices[0].text, dest = "kk")
    data = tts.get(translationw2.text, voice="nazgul", format_='wav')
    subprocess.check_output(['aplay', '-q'], input=data)

model = Model(model_name="vosk-model-small-kz-0.15")
recognizer = KaldiRecognizer(model,16000)
language = 'ru'
wikipedia.set_lang("ru")
translator = Translator()
r = sr.Recognizer()
tts = TTS(threads=1)

while True:
    data = tts.get('Салем! Менің атым Ева. Жалғастыру үшін сәлем айтыныз', voice="nazgul", format_='wav')
    subprocess.check_output(['aplay', '-q'], input=data)
    if "сәлем" in asdf() or "салем" in asdf():
        data = tts.get('Немен көмектесе аламын?', voice="nazgul", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)
        while True:
            query = asdf()
            print(query)
            if "сұрақ" in query:
                print("w")
                wiki()
            elif "есеп" in query:
                print("Ok!")
                wolf()
            elif "қос" in query:
                print("m")
                lon()
            elif "өшір" in query:
                print("m")
                loff()
            elif "сенсор" in query:
                print("sss")
                sensor()
            elif "аударма" in query:
                print("ok!")
                word_tr()
            elif "тек" in query:
                print("sk")
                tail()
            elif "көмек" in query or "комек" in query:
                chat()
            elif "орыс" in query:
                import main_with_chat.py
            elif "сау" in query:
                print("...")
                break
            else:
                continue 
