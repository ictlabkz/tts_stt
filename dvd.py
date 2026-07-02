import pyaudio 
import speech_recognition as sr 
import serial 
import time 
import requests
from bs4 import BeautifulSoup 
import vosk 
from vosk import Model, KaldiRecognizer
import beepy
from rhvoice_wrapper import TTS 
import subprocess

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

dict = {1: "В соответствии со статьей 21 Закона Республики Казахстан от двадцатого декабря тысяча девятьсот девяностно первого года «лицо, состоящее в гражданстве Республики Казахстан и принявшее гражданство иностранного государства, в течение тридцати календарных дней со дня приобретения им иного гражданства обязано сообщить о факте приобретения иностранного гражданства в органы внутренних дел Республики Казахстан или загранучреждения Республики Казахстан и сдать паспорт и (или) удостоверение личности Республики Казахстан».",
        2: "Для получения разрешения на постоянное проживание в Республике Казахстан иностранному гражданину необходимо оплатить государственную пошлину в размере 4 МРП (13 тысяч 800 тенге) на расчетный счет 108126.",
        3: "Заграничный паспорт срок действия которого на день подачи документов свыше 180 календарных дней и документ о судимости (отсутствии судимости) в государстве гражданской принадлежности   или постоянного проживания, выданный компетентным органом соответствующего государства срок действия которого не более 180 календарных дней.",
        4: "Зарегистрироваться по месту жительства в Республике Казахстан  граждане Республики Казахстан могут через электронный портал егов точка кей зэт. Для этого гражданину необходимо иметь электронно-цифровую подпись, либо быть зарегистрированным в базе мобильных граждан, где и подается заявка. Собственник жилья одобряет заявку с помощью электронно цифровой подписи. Данная Государственная услуга бесплатная.",
        5: "Паспорт гражданина Республики Казахстан выдается   гражданам РК по их желанию, независимо от возраста, сроком действия на  10 лет.",
        6: "Государственная пошлина за выдачу удостоверения личности Республики Казахстан составляет 0,2 МРП - это 690 тенге, за паспорт Республики Казахстан 8 МРП - это 27 тысяч 600 тенге.",
        7: "Сроком до 90 дней.",
        8: "В течении трёх рабочих дней.",
        9: "разрешение на временное проживание выдается сроком  до 1-го года с правом ежегодного продления до 3-х лет.",
        10: "Граждане указанных стран осуществляют трудовую деятельность сроком до 3-х месяцев и в дальнейшем продлевают до 1 года, только у физического лица в домашнем хозяйстве."}

model = Model(model_name="vosk-model-small-ru-0.22")
recognizer = KaldiRecognizer(model,16000)
language = 'ru'
r = sr.Recognizer()
tts = TTS(threads=1)

data = tts.get('Чем могу быть полезна?', voice="anna", format_='wav')
subprocess.check_output(['aplay', '-q'], input=data)
query = asdf()
print(query)
try:
    if "документ" and "гражданство" in query:
        data = tts.get(dict[1], voice="anna", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)
    elif "пошлин" in query and "жительств" in query:
        data = tts.get(dict[2], voice="anna", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)
    elif "документ" in query  and "жительств" in query:
        data = tts.get(dict[3], voice="anna", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)
    elif "зарегистрироваться" in query and "онлайн" in query:
        data = tts.get(dict[4], voice="anna", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)
    elif "возраст" in query  and "паспорт" in query:
        data = tts.get(dict[5], voice="anna", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)
    elif ("сумма" in query  and "паспорт" in query ) or ("сумма" in query  and "уд" in query ):
        data = tts.get(dict[6], voice="anna", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)
    elif "срок"  in query and "без разрешения на временное проживание" in query:
        data = tts.get(dict[7], voice="anna", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)
    elif "период" in query  and "пребывании у них иностранных" in query:
        data = tts.get(dict[8], voice="anna", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)
    elif "срок" in query  and "граждане российской федерации" in query:
        data = tts.get(dict[9], voice="anna", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)
    elif ("срок" in query  and "узбекистан" in query ) or ("срок" in query  and "таджик" in query ):
        data = tts.get(dict[10], voice="anna", format_='wav')
        subprocess.check_output(['aplay', '-q'], input=data)
except:
    data = tts.get('Возникли трудности, попробуйте ещё раз', voice="anna", format_='wav')
    subprocess.check_output(['aplay', '-q'], input=data)

                


