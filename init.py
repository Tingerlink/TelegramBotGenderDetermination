# -*- coding: utf-8 -*-
import telebot
import config
import re

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.send_message(message.chat.id, 
    "Привет! Если хочешь узнать пол человека, введи его ФИО, в формате Фамилия Имя Отчество, через пробел.\nНапример вот так: \n\nИванов Иван Иванович\nили\nСидорова Ольга Владимировна\n\nИ я скажу какого пола владелец ФИО.")

@bot.message_handler(commands=['next'])
def handle_start_help(message):
    bot.send_message(message.chat.id, 
    "Я готов определить пол. Введите ФИО человека.")

@bot.message_handler(commands=['help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, 
    "Если хочешь узнать пол человека, введи его ФИО, в формате Фамилия Имя Отчество, через пробел.\nНапример вот так: \n\nИванов Иван Иванович\nили\nСидорова Ольга Владимировна\n\nИ я скажу какого пола владелец ФИО.")

@bot.message_handler(content_types=['text'])
def handle_start_help(message):
    text = message.text
    arr = text.split()

    if (len(arr) < 3):
         bot.send_message(message.chat.id, "Что-то не так, я не знаю как это обработать.\nПопробуйте повторить ввод или обратитесь за помощью /help")
         return
      
    c = re.compile(u'[а-яА-Я\-]{1,}')

    name = re.search(c, arr[0])
    surname = re.search(c, arr[1])
    patronimic = re.search(c, arr[2])

    if (not name or not surname or not patronimic):
        bot.send_message(message.chat.id, "Что-то не так, посмотрите, верно ли написаны ФИО")
        return
    
    if (arr[2][-3:].lower() == u"вич"):
        bot.send_message(message.chat.id, "Пол определён как: Мужчина\n\nОпределить ещё одно /next")
    elif (arr[2][-3:].lower() == u"вна"):
        bot.send_message(message.chat.id, "Пол определён как: Женщина\n\nОпределить ещё одно /next")
    else:
        bot.send_message(message.chat.id, "Что-то не так, посмотрите, верно ли написаны ФИО")
        return

bot.polling(none_stop=True, interval=0)
