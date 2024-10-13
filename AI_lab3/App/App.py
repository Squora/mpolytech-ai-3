#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Модуль для голосового взаимодействия.
Использует библиотеки pyttsx3 для синтеза речи и speech_recognition для распознавания голоса.
"""
import datetime
import sys
import webbrowser

import pyttsx3
import speech_recognition as sr


def talk(words):
    """
    Произносит переданную строку с помощью синтезатора речи.
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # скорость речи
    engine.setProperty('volume', 0.9)  # громкость (0-1)
    engine.say(words)
    engine.runAndWait()


def command():
    """
    Запрашивает голосовую команду у пользователя, используя микрофон.
    Возвращает строку с распознанной командой.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите!")
        talk("Говорите!")
        recognizer.pause_threshold = 1  # пауза 1 сек
        recognizer.adjust_for_ambient_noise(source, duration=1)  # игнорирование фоновых шумов
        audio = recognizer.listen(source)
    try:
        zadanie = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + zadanie)
        talk("Вы сказали: " + zadanie)
    except sr.UnknownValueError:
        talk("Не понимаю Вас!")
        return command()  # повторяем запрос команды
    except sr.RequestError:
        talk("Ошибка сервиса распознавания.")
        return None
    return zadanie


def time_to_text():
    """
    Возвращает текущее время в текстовом формате.
    """
    dict_hours = {
        1: 'час', 2: 'часа', 3: 'часа', 4: 'часа', 5: 'часов', 6: 'часов',
        7: 'часов', 8: 'часов', 9: 'часов', 10: 'часов', 11: 'часов', 12: 'часов',
        13: 'часов', 14: 'часов', 15: 'часов', 16: 'часов', 17: 'часов', 18: 'часов',
        19: 'часов', 20: 'часов', 21: 'час', 22: 'часа', 23: 'часа', 0: 'часов'
    }
    dict_minutes = {
        'минута': [1, 21, 31, 41, 51],
        'минуты': [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54],
        'минут': list(range(5, 21)) + list(range(25, 31)) + list(range(35, 41)) +
                 list(range(45, 51)) + list(range(55, 60))
    }

    now = datetime.datetime.now()
    h = now.hour
    m = now.minute

    str_time = f"{h} {dict_hours[h]} "

    for minute_form in dict_minutes:
        if m in dict_minutes[minute_form]:
            str_time += f"{m} {minute_form}"
            break

    return str_time


def parse_zadanie(zadanie):
    """
    Разбирает и выполняет голосовые команды.
    """
    if 'открой почту' in zadanie:
        talk('Хорошо, открываю почту!')
        url = 'https://mail.ru'
        webbrowser.open(url)
    elif 'сколько времени' in zadanie or 'который час' in zadanie:
        talk(time_to_text())
    elif 'как тебя зовут' in zadanie or 'как твоё имя' in zadanie or 'кто ты' in zadanie:
        talk('Меня зовут Татьяна! А как зовут тебя?')
    elif 'стоп' in zadanie:
        talk('Хорошо, заканчиваем разговор... До встречи!')
        sys.exit()


def main():
    """
    Основная функция программы. Цикл взаимодействия с пользователем.
    """
    # узнаем какие голоса есть в системе
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    for voice in voices:  # голоса и параметры каждого
        print('------')
        print(f'Имя: {voice.name}')
        print(f'ID: {voice.id}')
        print(f'Язык(и): {voice.languages}')
        print(f'Пол: {voice.gender}')
        print(f'Возраст: {voice.age}')

    # Устанавливаем предпочтительный голос "Татьяна", если доступен
    selected_voice = None
    for voice in voices:
        if 'Tatiana' in voice.name:
            selected_voice = voice.id
            engine.setProperty('voice', selected_voice)

    if not selected_voice:
        talk("Предпочтительный голос не найден. Использую голос по умолчанию.")

    talk('Привет, меня зовут Татьяна! Давай поговорим!')

    while True:
        zadanie = command()
        if zadanie:
            parse_zadanie(zadanie)
        talk("Поговорим еще?")


if __name__ == "__main__":
    main()
