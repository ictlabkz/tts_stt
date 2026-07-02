import numpy as np #библиотека для работы с камерой
import os #библиотека для озвучки
from googletrans import Translator #библиотека для перевода
import pyaudio #библиотека для определения голоса
import speech_recognition as sr #библиотека для распознавания голоса
import serial #библиотека для работы с портами и передачей информации по ним
import time #библиотека для временных задержек
import wolframalpha #библиотека для работы с поисковой системой
import wikipedia #библиотека для вывода информации из Википедии
import requests
import random as rand #библиотека для рандомного выбора сказок
from bs4 import BeautifulSoup #библиотека для вывода сигналов
import vosk 
from vosk import Model, KaldiRecognizer #библиотека для распознавания речи
import beepy
from rhvoice_wrapper import TTS #библиотека 
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
    data = tts.get('Спрашивайте', voice="anna", format_='wav')
    subprocess.check_output(['aplay', '-q'], input=data)
    rec = asdf()
    try:
        text = wikipedia.summary(rec, sentences = 1)
        data = tts.get(text, voice="anna", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)
    except:
        data = tts.get('Возникли трудности, попробуйте ещё раз', voice="anna", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)
        



def sensor(): #функция для получения данных с датчиков и их озвучивания
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    ser.reset_input_buffer()
    g = 0
    t = 0
    while 1:
        line = ser.readline().decode('utf-8').rstrip()
        if "Heavy gases" in line:
            s1 = "Показатель углекислого газа " + line[14:17] + " милиграмм на метр кубический"
            data = tts.get(s1, voice="anna", format_='wav')
            subprocess.check_output(['aplay', '-q'], input=data)
    
            if int(line[14:17]) < 600:
                data = tts.get('Уровень в норме', voice="anna", format_='wav')
                subprocess.check_output(['aplay', '-q'], input=data)
                
            else:
                data = tts.get('Превышение допустимого значения', voice="anna", format_='wav')
                subprocess.check_output(['aplay', '-q'], input=data)
                
            print(s1)
            g += 1
        if "Temp" in line:
            print()
            s2 = "Температура " + line[7:9] + " градусов Цельсия"
            data = tts.get(s2, voice="anna", format_='wav')
            subprocess.check_output(['aplay', '-q'], input=data)
            
            t += 1
            print(s2)
        if t == 1 and g == 1:
            print (2)
            break
        time.sleep(1)



def wolf(): #функция для работы с поисковиком
        data = tts.get('Задайте вопрос:', voice="anna", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)
        
        rec = asdf()
        

        translationw1 = translator.translate(rec, dest = "en")
        print (translationw1.text)

        try:
            app_id = 'PU5VGQ-YAWPRVQL42'
            client = wolframalpha.Client(app_id)
            res = client.query(translationw1.text)
            answer = next(res.results).text
            translationw2 = translator.translate(answer, dest = "ru")
            print(f"{translationw2.text}")
            a = "Ответ:" + translationw2.text
            data = tts.get(a, voice="anna", format_='wav')
            subprocess.check_output(['aplay', '-q'], input=data)
            
        except:
            data = tts.get('Возникли трудности, попробуйте ещё раз', voice="anna", format_='wav')
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

'''def word_tr(): #функция перевода фраз на выбранный язык
    data = tts.get('Выберите язык для перевода', voice="anna", format_='wav')
    subprocess.check_output(['aplay', '-q'], input=data)
    
    rec = asdf()
    print(rec)
    user_language = translator.translate(rec, dest = "En")
    if "russian" in user_language.text.lower():
        tr_language = "ru"
    elif "english" in user_language.text.lower():
        tr_language = "en"
    elif "kazakh" in user_language.text.lower():
        tr_language = "kk"
    print(tr_language)
    data = tts.get('Хорошо! Говорите для перевода', voice="anna", format_='wav')
    subprocess.check_output(['aplay', '-q'], input=data)
    
    rec = asdf()
    try:
        translaation1 = translator.translate(rec, dest = tr_language)
        data = tts.get(translaation1.text, voice="anna", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)
        
    except:
        data = tts.get('Возникли трудности, попробуйте ещё раз', voice="anna", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)'''
        

def tail():
    data = tts.get('Ищу сказку, подождите минутку, пожалуйста', voice="anna", format_='wav')
    subprocess.check_output(['aplay', '-q'], input=data)
    
    x = rand.randint(0,10)
    url = 'https://tales.ictlab.kz/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('p',class_=x)
    for quote in quotes:
        data = tts.get(quote.text, voice="anna", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)

def chat():
    openai.api_key = "sk-..."
    # задаем модель и промпт
    model_engine = "text-davinci-003"
    prompt = asdf()

    data = tts.get("Минутку, я думаю", voice="anna", format_='wav')
    subprocess.check_output(['aplay', '-q'], input=data)
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
    
    data = tts.get("Минутку, я думаю", voice="anna", format_='wav')
    subprocess.check_output(['aplay', '-q'], input=data)

    # выводим ответ
    translationw2 = translator.translate(completion.choices[0].text, dest = "ru")
    data = tts.get(translationw2.text, voice="anna", format_='wav')
    subprocess.check_output(['aplay', '-q'], input=data)


model = Model(model_name="vosk-model-small-ru-0.22")
recognizer = KaldiRecognizer(model,16000)
language = 'ru'
wikipedia.set_lang("ru")
translator = Translator()
r = sr.Recognizer()
tts = TTS(threads=1)

while True:
    data = tts.get('Привет! Меня зовут Ева. Чтобы продолжить работу, скажите привет!', voice="anna", format_='wav')
    subprocess.check_output(['aplay', '-q'], input=data)
    if "привет" in asdf():
        data = tts.get('Чем могу быть полезна?', voice="anna", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)
        while True:
            query = asdf()
            print(query)
            if "вопрос" in query:
                print("w")
                wiki()
            elif "задач" in query:
                print("Ok!")
                wolf()
            elif "включ" in query:
                print("m")
                lon()
            elif "выкл" in query:
                print("m")
                loff()
            elif "сенсор" in query:
                print("sss")
                sensor()
            elif "сказк" in query:
                print("sk")
                tail()
            elif "объясни" in query:
                print("ch")
                chat()
            elif "пока" in query:
                print("...")
                break
            else:
                continue 
