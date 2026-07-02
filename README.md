Настройка Операционной системы и программного обеспечения.

DEBIAN пользователь - user/user, системная учетная запись - root/root. 
1.	Далее следует порядок настройки дистрибутива.
2.	Перезагрузить. Выбрать дистрибутив. Нажать клавишу e. В строке linux дописать init=/bin/bash
3.	Монтирование в режиме чтения и записи sudo mount -o remount,rw /
4.	Смена пароля для root - passwd
5.	Смена прав пользователя usermod -a -G wheel имя_пользователя /или usermod -a -G sudo имя_пользователя

Загрузка ОС и открытие терминала
1.	Ввод команды su и переход в корневую папку с использованием cd .. 
2.	Редактирование файла конфигурации gedit /etc/apt/sources.list &>/dev/null
3.	Убрать cdrom добавив знак # в соответствующей строке обновления
4.	Добавить репозиторий deb http://deb.debian.org/debian/ bullseye main или 

sudo nano /etc/apt/sources.list

deb http://deb.debian.org/debian/ bullseye main
deb-src http://deb.debian.org/debian bullseye main

deb http://security.debian.org/debian-security bullseye/updates main
deb-src http://security.debian.org/debian-security bullseye/updates main

deb http://deb.debian.org/debian bullseye-updates main
deb-src http://deb.debian.org/debian bullseye-updates main

deb http://security.debian.org/debian-security bullseye-security main
deb-src http://security.debian.org/debian-security bullseye-security main

5.	Обновление пакетов ОС - sudo apt update, sudo apt upgrade
6.	sudo nano /etc/resolv.conf
7.	Вписать nameserver 8.8.8.8

Отключение запроса пароля при входе в систему (администрирование-> Экран входа)

Установка библиотек и зависимостей:

1.	Установка pip'a - sudo apt install python3-pip
2.	Установка git clone - sudo apt install git
3.	Установка библиотеки pip3 install vosk
4.	pip install pkgconfig==1.5.5
5.	pip install SCons==4.4.0
6.	pip install subprocess.run==0.0.8
7.	sudo apt install python3-pyaudio
8.	git clone --recursive https://github.com/RHVoice/RHVoice.git 
9.	sudo apt install gcc pkg-config scons
10.	sudo apt install libpulse-dev
11.	sudo apt install pulseaudio
12.	sudo apt install lame
13.	sudo apt-install opus-tools
14.	sudo apt-install flac
15.	cd RHVoice
16.	scons spd_module_dir=/usr/lib/speech-dispatcher
17.	sudo scons install
18.	sudo ldconfig
19.	pip install rhvoice-wrapper
20.	pip3 install openai

Установка для поддержки библиотек simpleaudio и beepy - sudo apt-get install libasound2-dev
Установка библиотек pip3 install beepy, pip3 install simpleaudio
Установка модели для распознавания русской речи - 

from vosk import Model, KaldiRecognizer #библиотека для распознавания речи
model = Model(model_name="vosk-model-small-ru-0.22")

Установка модели для распознавания казахской речи - 
from vosk import Model, KaldiRecognizer #библиотека для распознавания речи
model = Model(model_name="vosk-model-small-kz-0.15")

Ниже представлены названия голосов и настройка параметров их произношения (тон, скорость, громкость)

•	aleksandr - Russian
•	elena - Russian
•	talgat - Kazakh
•	nazgul - Kazakh
•	alan - English
•	lyubov - English

from rhvoice_wrapper import TTS
import subprocess
tts = TTS(threads=1)
tts.set_params(absolute_rate=0.5, absolute_pitch=1.0, absolute_volume=2.5)
data = tts.get('Привет, как дела? Как ты себя чувствуешь?', voice="talgat", format_='wav')
#print('data size: ', len(data), ' bytes')
subprocess.check_output(['aplay', '-q'], input=data)
