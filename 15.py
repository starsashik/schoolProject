import asyncio
import hashlib
import sqlite3

import telebot
from telebot import types

TOKEN = '1633681368:AAEHBoqBKhg26ai_tPsw16qZJrgn-2tqFyU'
db_name = "tmp/TeleDB.db"

start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
start_markup.row("/logIn")
start_markup.row('/registration')
start_markup.row("/help")

login_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
login_markup.add("/1_5", "/6_10", "/11_15")
login_markup.add("/16_20", "/21_25", "/26_27")
login_markup.row('/profile', '/logOut')

task1_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
task1_markup.add("/task1", "/task2", '/task3').add('/task4', '/task5').add('/back')

task6_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
task6_markup.add("/task6", "/task7", '/task8').add('/task9', '/task10').add('/back')

task11_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
task11_markup.add("/task11", "/task12", '/task13').add('/task14', '/task15').add('/back')

task16_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
task16_markup.add("/task16", "/task17", '/task18').add('/task19', '/task20').add('/back')

task21_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
task21_markup.add("/task21", "/task22", '/task23').add('/task24', '/task25').add('/back')

task26_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
task26_markup.add("/task26", "/task27").add('/back')


async def main():
    bot = telebot.TeleBot(TOKEN)
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    command = f"""SELECT id FROM User"""
    result = cur.execute(command).fetchall()
    cur.close()
    dd = {i[0]: False for i in result}

    @bot.message_handler(commands=["start"])
    def start(message):
        mess = f"Привет, <b><u>{message.from_user.username}</u></b>, Я бот помощник для ЕГЭ по информатике.\n" \
               f"Для удобной работы со мной, лучше всего зарегистрироваться\n" \
               f"Если у вас уже есть аккаунт, то можете войти в него.\n" \
               f"Для лучшего понимания работы бота используйте функцию /help"
        bot.send_message(message.chat.id, mess, reply_markup=start_markup, parse_mode='html')

    @bot.message_handler(commands=['help'])
    def help(message):
        doc = open("tmp/help.txt", mode="rb")
        bot.send_document(message.chat.id, doc)
        doc.close()

    @bot.message_handler(commands=['close'])
    def close(message):
        bot.send_message(message.chat.id, "Клавиатура скрыта", reply_markup=telebot.types.ReplyKeyboardRemove())

    @bot.message_handler(commands=["registration"])
    def reg1(message):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""SELECT id FROM User"""
        result = cur.execute(command).fetchall()
        result = [i[0] for i in result]
        cur.close()
        if int(message.from_user.id) in result:
            bot.send_message(message.chat.id, "Пользователь с вашем id уже зарегистрирован")
        else:
            tb = bot.send_message(message.chat.id, "Придумайте и отправьте пароль.\n"
                                                   "Хорошо запомните его, так как его нельзя будет восстановить.")
            bot.register_next_step_handler(tb, reg2)

    def reg2(message):
        passwords = "b" + message.text
        password = hashlib.md5(passwords.encode("utf8"))
        bot.delete_message(message.chat.id, message.message_id)
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""INSERT INTO User  VALUES(?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), message.from_user.username, password.hexdigest()))
        command = f"""INSERT INTO Task1  VALUES(?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0))
        command = f"""INSERT INTO Task2  VALUES(?, ?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0, 0))
        command = f"""INSERT INTO Task3  VALUES(?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0))
        command = f"""INSERT INTO Task4  VALUES(?, ?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0, 0))
        command = f"""INSERT INTO Task5 VALUES(?, ?, ?, ?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0, 0, 0, 0))
        command = f"""INSERT INTO Task6 VALUES(?, ?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0, 0))
        command = f"""INSERT INTO Task7 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0, 0, 0, 0, 0, 0))
        command = f"""INSERT INTO Task8 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0, 0, 0, 0, 0))
        command = f"""INSERT INTO Task9 VALUES(?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0))
        command = f"""INSERT INTO Task10 VALUES(?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0))
        command = f"""INSERT INTO Task11 VALUES(?, ?, ?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0, 0, 0))
        command = f"""INSERT INTO Task12 VALUES(?, ?, ?, ?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0, 0, 0, 0))
        command = f"""INSERT INTO Task13 VALUES(?, ?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0, 0))
        command = f"""INSERT INTO Task14 VALUES(?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0))
        command = f"""INSERT INTO Task15 VALUES(?, ?, ?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0, 0, 0))
        command = f"""INSERT INTO Task16 VALUES(?, ?, ?, ?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0, 0, 0, 0))
        command = f"""INSERT INTO Task17 VALUES(?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0))
        command = f"""INSERT INTO Task18 VALUES(?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0))
        command = f"""INSERT INTO Task19 VALUES(?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0))
        command = f"""INSERT INTO Task20 VALUES(?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0))
        command = f"""INSERT INTO Task21 VALUES(?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0))
        command = f"""INSERT INTO Task22 VALUES(?, ?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0, 0))
        command = f"""INSERT INTO Task23 VALUES(?, ?, ?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0, 0, 0))
        command = f"""INSERT INTO Task24 VALUES(?, ?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0, 0))
        command = f"""INSERT INTO Task25 VALUES(?, ?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0, 0))
        command = f"""INSERT INTO Task26 VALUES(?, ?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0, 0))
        command = f"""INSERT INTO Task27 VALUES(?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0))
        con.commit()
        bot.send_message(message.chat.id, f"Добро пожаловать, <b><u>{message.from_user.username}</u></b>!",
                         parse_mode='html',
                         reply_markup=login_markup)
        dd[int(message.from_user.id)] = True

    @bot.message_handler(commands=["logIn"])
    def login(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, вы уже вошли в аккаунт, "
                                 f"можете приступать к выполнению заданий\n(снизу)",
                                 reply_markup=login_markup, parse_mode='html')
            else:
                tb = bot.send_message(message.chat.id, "Пароль:")
                bot.register_next_step_handler(tb, log2)

        except KeyError:
            bot.send_message(message.chat.id, f"Аккаунта с вашем логином не существуют.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    def log2(message):
        passwords = "b" + message.text
        password = hashlib.md5(passwords.encode("utf8"))
        bot.delete_message(message.chat.id, message.message_id)
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""SELECT password FROM User WHERE id = {int(message.from_user.id)}"""
        result = cur.execute(command).fetchall()
        cur.close()
        if password.hexdigest() == result[0][0]:
            dd[int(message.from_user.id)] = True
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы успешно вошли в аккаунт, "
                             f"можете приступать к выполнению заданий\n(снизу)",
                             reply_markup=login_markup, parse_mode='html')
        else:
            bot.send_message(message.chat.id, f"Пароль неверный.\n"
                                              f"Попробуйте еще раз /login \n"
                                              f"Если вы забыли пароль, то к сожалению вам придется удалить аккаунт.\n"
                                              f"Для этого напишите '/' + 'del_acc'",
                             reply_markup=start_markup)

    @bot.message_handler(commands=["logOut"])
    def logout(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                dd[int(message.from_user.id)] = False
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, вы успешно вышли из аккаунта",
                                 reply_markup=start_markup, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, вы и так были не в сети",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Аккаунта с вашем логином не существуют.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['del_acc'])
    def del_acc(message):
        idd = message.message_id
        img = open("tmp/dpf.jpg", mode="rb")
        bot.send_photo(message.chat.id, img)
        img.close()
        tb = bot.send_message(message.chat.id, "Для подтверждения удаления аккаунта введите то, что увидите на фото")
        bot.register_next_step_handler(tb, del_acc2)

    def del_acc2(message):
        if message.text == ">Delete.":
            if int(message.from_user.id) in dd:
                con = sqlite3.connect(db_name)
                cur = con.cursor()
                command = f"""DELETE FROM User WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task1 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task2 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task3 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task4 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task5 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task6 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task7 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task8 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task9 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task10 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task11 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task12 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task13 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task14 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task15 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task16 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task17 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task18 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task19 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task20 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task21 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task22 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task23 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task24 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task25 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task26 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task27 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                con.commit()
                cur.close()
                dd.pop(int(message.from_user.id))
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, ваш аккаунт был удален:)",
                                 reply_markup=start_markup, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"У вас нет аккаунта для удаления:/",
                                 reply_markup=start_markup, parse_mode='html')
        else:
            bot.send_message(message.chat.id,
                             f"Вы ввели неправильное контрольное слово",
                             reply_markup=start_markup, parse_mode='html')
        bot.delete_message(message.chat.id, message.message_id - 2)
        bot.delete_message(message.chat.id, message.message_id)

    @bot.message_handler(commands=['profile'])
    def prof(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                con = sqlite3.connect(db_name)
                cur = con.cursor()
                command = f"""Select User.id, Task1.Total, Task2.Total, Task3.Total, Task4.Total, Task5.Total, 
Task6.Total, Task7.Total, Task8.Total, Task9.Total, Task10.Total, Task11.Total, Task12.Total, Task13.Total, 
Task14.Total, Task15.Total, Task16.Total, Task17.Total, Task18.Total, Task19.Total, Task20.Total,Task21.Total, 
Task22.Total, Task23.Total, Task24.Total, Task25.Total, Task26.Total, Task27.Total FROM User,Task1,Task2,Task3,Task4,
Task5,Task6,Task7,Task8,Task9,Task10,Task11,Task12,Task13,Task14,Task15,Task16,Task17,Task18,Task19,Task20,Task21,Task22,
Task23,Task24,Task25,Task26,Task27 WHERE User.id = {int(message.from_user.id)}"""
                result = cur.execute(command).fetchall()
                cur.close()
                bot.send_message(message.chat.id,
                                 f"<b>{message.from_user.username}: {message.from_user.first_name} "
                                 f"{message.from_user.last_name if message.from_user.last_name is not None else ''}"
                                 f"</b>\n Анализ информационных моделей - {result[0][1]}%\n"
                                 f"Построение таблиц истинности логических выражений - {result[0][2]}%\n"
                                 f"Поиск информации в реляционных базах данных - {result[0][3]}%\n"
                                 f"Кодирование и декодирование информации - {result[0][4]}%\n"
                                 f"Анализ и построение алгоритмов для исполнителей - {result[0][5]}%\n"
                                 f"Анализ программ - {result[0][6]}%\n"
                                 f"Кодирование и декодирование информации. Передача информации - {result[0][7]}%\n"
                                 f"Перебор слов и системы счисления - {result[0][8]}%\n"
                                 f"Работа с таблицами - {result[0][9]}%\n"
                                 f"Поиск символов в текстовом редакторе - {result[0][10]}%\n"
                                 f"Вычисление количества информации - {result[0][11]}%\n"
                                 f"Выполнение алгоритмов для исполнителей - {result[0][12]}%\n"
                                 f"Поиск путей в графе - {result[0][13]}%\n"
                                 f"Кодирование чисел. Системы счисления - {result[0][14]}%\n"
                                 f"Преобразование логических выражений - {result[0][15]}%\n"
                                 f"Рекурсивные алгоритмы - {result[0][16]}%\n"
                                 f"Обработки числовой последовательности - {result[0][17]}%\n"
                                 f"Робот-сборщик монет - {result[0][18]}%\n"
                                 f"Выигрышная стратегия. Задание 1 - {result[0][19]}%\n"
                                 f"Выигрышная стратегия. Задание 2 - {result[0][20]}%\n"
                                 f"Выигрышная стратегия. Задание 3 - {result[0][21]}%\n"
                                 f"Анализ программы с циклами и условными операторами - {result[0][22]}%\n"
                                 f"Оператор присваивания и ветвления. Перебор вариантов, построение дерева - "
                                 f"{result[0][23]}%\nОбработка символьных строк - {result[0][24]}%\n"
                                 f"Обработка целочисленной информации - {result[0][25]}%\n"
                                 f"Обработка целочисленной информации - {result[0][26]}%\n"
                                 f"Программирование - {result[0][27]}%\n"
                                 f"Всего выполнено: {str(round(sum(result[0][1:]) / 27 * 100))}%",
                                 reply_markup=login_markup, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b> чтобы посмотреть свой профиль "
                                 f"залогинтесь\n "
                                 f"/logIn",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"У вас еще нет профиля, сначала зарегистрируйтесь.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=["1_5"])
    def task1_5(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, пожалуйста выберете номер задания: 1-5",
                                 reply_markup=task1_markup, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=["6_10"])
    def task6_10(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, пожалуйста выберете номер задания: 6-10",
                                 reply_markup=task6_markup, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=["11_15"])
    def task11_15(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, пожалуйста выберете номер задания: 11-15",
                                 reply_markup=task11_markup, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=["16_20"])
    def task16_20(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, пожалуйста выберете номер задания: 16-20",
                                 reply_markup=task16_markup, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=["21_25"])
    def task21_25(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, пожалуйста выберете номер задания: 21-25",
                                 reply_markup=task21_markup, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=["26_27"])
    def task26_27(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, пожалуйста выберете номер задания: 26-27",
                                 reply_markup=task26_markup, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task1'])
    def task1(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Неоднозначное соотнесение таблицы и графа', callback_data="t1_1")
                i2 = types.InlineKeyboardButton(text='Однозначное соотнесение таблицы и графа', callback_data="t1_2")
                i3 = types.InlineKeyboardButton(text='Поиск оптимального маршрута по таблице', callback_data="t1_3")
                mi1.add(i1).add(i2).add(i3)
                bot.send_message(message.chat.id,
                                 f"Задание 1:\n<u>Анализ информационных моделей</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task2'])
    def task2(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Монотонные функции', callback_data="t2_1")
                i2 = types.InlineKeyboardButton(text='Немонотонные функции', callback_data="t2_2")
                i3 = types.InlineKeyboardButton(text='Строки с пропущенными значениями', callback_data="t2_3")
                i4 = types.InlineKeyboardButton(text='Разные задачи', callback_data="t2_4")
                mi1.add(i1).add(i2).add(i3).add(i4)
                bot.send_message(message.chat.id,
                                 f"Задание 2:\n<u>Построение таблиц истинности логических выражений</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task3'])
    def task3(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Задания для подготовки 1', callback_data="t3_1")
                i2 = types.InlineKeyboardButton(text='Задания для подготовки 2', callback_data="t3_2")
                mi1.add(i1).add(i2)
                bot.send_message(message.chat.id,
                                 f"Задание 3:\n<u>Поиск информации в реляционных базах данных</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task4'])
    def task4(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Выбор кода при неиспользуемых сигналах', callback_data="t4_1")
                i2 = types.InlineKeyboardButton(text='Шифрование по известному коду и перевод в различные СС',
                                                callback_data="t4_2")
                i3 = types.InlineKeyboardButton(text='Расшифровка сообщений', callback_data="t4_3")
                i4 = types.InlineKeyboardButton(text='Передача информации. Выбор кода', callback_data="t4_4")
                mi1.add(i1).add(i2).add(i3).add(i4)
                bot.send_message(message.chat.id,
                                 f"Задание 4:\n<u>Кодирование и декодирование информации</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task5'])
    def task5(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Исполнители на плоскости', callback_data="t5_1")
                i2 = types.InlineKeyboardButton(text='Посимвольное двоичное преобразование', callback_data="t5_2")
                i3 = types.InlineKeyboardButton(text='Разные задачи', callback_data="t5_3")
                i4 = types.InlineKeyboardButton(text='Арифмометры', callback_data="t5_4")
                i5 = types.InlineKeyboardButton(text='Арифмометры с движением в обе стороны', callback_data="t5_5")
                i6 = types.InlineKeyboardButton(text='Посимвольное десятичное преобразование', callback_data="t5_6")
                mi1.add(i1).add(i2).add(i3).add(i4).add(i5).add(i6)
                bot.send_message(message.chat.id,
                                 f"Задание 5:\n<u>Анализ и построение алгоритмов для исполнителей</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task6'])
    def task6(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Две линейные функции', callback_data="t6_1")
                i2 = types.InlineKeyboardButton(text='Сумма двух линейных функций', callback_data="t6_2")
                i3 = types.InlineKeyboardButton(text='Арифметическая прогрессия', callback_data="t6_3")
                i4 = types.InlineKeyboardButton(text='Условие выполнения цикла while', callback_data="t6_4")
                mi1.add(i1).add(i2).add(i3).add(i4)
                bot.send_message(message.chat.id,
                                 f"Задание 6:\n<u>Анализ программ</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task7'])
    def task7(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Передача звуковых файлов', callback_data="t7_1")
                i2 = types.InlineKeyboardButton(text='Передача изображений', callback_data="t7_2")
                i3 = types.InlineKeyboardButton(text='Передача текстовых файлов', callback_data="t7_3")
                i4 = types.InlineKeyboardButton(text='Хранение звуковых файлов', callback_data="t7_4")
                i5 = types.InlineKeyboardButton(text='Сравнение двух способов передачи данных', callback_data="t7_5")
                i6 = types.InlineKeyboardButton(text='Определение времени передачи файла', callback_data="t7_6")
                i7 = types.InlineKeyboardButton(text='Хранение изображений', callback_data="t7_7")
                i8 = types.InlineKeyboardButton(text='Определение размера записанного файла', callback_data="t7_8")
                mi1.add(i1).add(i2).add(i3).add(i4).add(i5).add(i6).add(i7).add(i8)
                bot.send_message(message.chat.id,
                                 f"Задание 7:\n<u>Кодирование и декодирование информации. Передача информации</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task8'])
    def task8(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Подсчет количества слов', callback_data="t7_1")
                i2 = types.InlineKeyboardButton(text='Подсчет количества слов с ограничениями', callback_data="t7_2")
                i3 = types.InlineKeyboardButton(text='Последовательность лампочек', callback_data="t7_3")
                i4 = types.InlineKeyboardButton(text='Последовательность сигнальных ракет', callback_data="t7_4")
                i5 = types.InlineKeyboardButton(text='Разное', callback_data="t7_5")
                i6 = types.InlineKeyboardButton(text='Подсчет количества разных последовательностей',
                                                callback_data="t7_6")
                i7 = types.InlineKeyboardButton(text='Слова по порядку', callback_data="t7_7")
                mi1.add(i1).add(i2).add(i3).add(i4).add(i5).add(i6).add(i7)
                bot.send_message(message.chat.id,
                                 f"Задание 8:\n<u>Перебор слов и системы счисления</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task9'])
    def task9(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Задания для подготовки 1', callback_data="t9_1")
                i2 = types.InlineKeyboardButton(text='Задания для подготовки 2', callback_data="t9_2")
                i3 = types.InlineKeyboardButton(text='Задания для подготовки 3', callback_data="t9_3")
                mi1.add(i1).add(i2).add(i3)
                bot.send_message(message.chat.id,
                                 f"Задание 9:\n<u>Работа с таблицами</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task10'])
    def task10(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Задания для подготовки 1', callback_data="t10_1")
                i2 = types.InlineKeyboardButton(text='Задания для подготовки 2', callback_data="t10_2")
                i3 = types.InlineKeyboardButton(text='Задания для подготовки 3', callback_data="t10_3")
                mi1.add(i1).add(i2).add(i3)
                bot.send_message(message.chat.id,
                                 f"Задание 10:\n<u>Поиск символов в текстовом редакторе</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task11'])
    def task11(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Пароли с дополнительными сведениями', callback_data="t11_1")
                i2 = types.InlineKeyboardButton(text='Разное', callback_data="t11_2")
                i3 = types.InlineKeyboardButton(text='Номера спортсменов', callback_data="t11_3")
                i4 = types.InlineKeyboardButton(text='Автомобильные номера', callback_data="t11_4")
                i5 = types.InlineKeyboardButton(text='Пароли', callback_data="t11_5")
                mi1.add(i1).add(i2).add(i3).add(i4).add(i5)
                bot.send_message(message.chat.id,
                                 f"Задание 11:\n<u>Вычисление количества информации</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task12'])
    def task12(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Исполнитель Редактор', callback_data="t12_1")
                i2 = types.InlineKeyboardButton(text='Исполнитель Чертёжник', callback_data="t12_2")
                i3 = types.InlineKeyboardButton(text='Остановка в заданной клетке, циклы с оператором ПОКА',
                                                callback_data="t12_3")
                i4 = types.InlineKeyboardButton(text='Нестандартные задачи', callback_data="t12_4")
                i5 = types.InlineKeyboardButton(text='Остановка в заданной клетке, циклы с операторами ПОКА и ЕСЛИ',
                                                callback_data="t12_5")
                i6 = types.InlineKeyboardButton(text='Остановка в клетке, из которой начато движение',
                                                callback_data="t12_6")
                mi1.add(i1).add(i2).add(i3).add(i4).add(i5).add(i6)
                bot.send_message(message.chat.id,
                                 f"Задание 12:\n<u>Выполнение алгоритмов для исполнителей</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task13'])
    def task13(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Подсчёт путей с избегаемой вершиной', callback_data="t13_1")
                i2 = types.InlineKeyboardButton(text='Подсчёт путей с обязательной и избегаемой вершинами',
                                                callback_data="t13_2")
                i3 = types.InlineKeyboardButton(text='Подсчёт путей', callback_data="t13_3")
                i4 = types.InlineKeyboardButton(text='Подсчёт путей с обязательной вершиной', callback_data="t13_4")
                mi1.add(i1).add(i2).add(i3).add(i4)
                bot.send_message(message.chat.id,
                                 f"Задание 13:\n<u>Поиск путей в графе</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task14'])
    def task14(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Разное', callback_data="t14_1")
                i2 = types.InlineKeyboardButton(text='Прямое сложение в СС',
                                                callback_data="t14_2")
                i3 = types.InlineKeyboardButton(text='Определение основания', callback_data="t14_3")
                mi1.add(i1).add(i2).add(i3)
                bot.send_message(message.chat.id,
                                 f"Задание 14:\n<u>Кодирование чисел. Системы счисления</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task15'])
    def task15(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Побитовая конъюнкция', callback_data="t15_1")
                i2 = types.InlineKeyboardButton(text='Числовые отрезки', callback_data="t15_2")
                i3 = types.InlineKeyboardButton(text='Дискретные множества', callback_data="t15_3")
                i4 = types.InlineKeyboardButton(text='Координатная плоскость', callback_data="t15_4")
                i5 = types.InlineKeyboardButton(text='Разное', callback_data="t15_5")
                mi1.add(i1).add(i2).add(i3).add(i4).add(i5)
                bot.send_message(message.chat.id,
                                 f"Задание 15:\n<u>Преобразование логических выражений</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task16'])
    def task16(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(
                    text='Программы с двумя рекурсивными функциями с возвращаемыми значениями', callback_data="t16_1")
                i2 = types.InlineKeyboardButton(text='Программы с двумя рекурсивными функциями с текстовым выводом',
                                                callback_data="t16_2")
                i3 = types.InlineKeyboardButton(text='Рекурсивные функции с возвращаемыми значениями',
                                                callback_data="t16_3")
                i4 = types.InlineKeyboardButton(text='Алгоритмы, опирающиеся на несколько предыдущих значений',
                                                callback_data="t16_4")
                i5 = types.InlineKeyboardButton(text='Рекурсивные функции с текстовым выводом', callback_data="t16_5")
                i6 = types.InlineKeyboardButton(text='Алгоритмы, опирающиеся на одно предыдущее значение',
                                                callback_data="t16_6")
                mi1.add(i1).add(i2).add(i3).add(i4).add(i5).add(i6)
                bot.send_message(message.chat.id,
                                 f"Задание 16:\n<u>Рекурсивные алгоритмы</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task17'])
    def task17(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Задания для подготовки 1', callback_data="t17_1")
                i2 = types.InlineKeyboardButton(text='Задания для подготовки 2', callback_data="t17_2")
                mi1.add(i1).add(i2)
                bot.send_message(message.chat.id,
                                 f"Задание 17:\n<u>Обработки числовой последовательности</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task18'])
    def task18(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Задания для подготовки 1', callback_data="t18_1")
                i2 = types.InlineKeyboardButton(text='Задания для подготовки 2', callback_data="t18_2")
                mi1.add(i1).add(i2)
                bot.send_message(message.chat.id,
                                 f"Задание 18:\n<u>Робот-сборщик монет</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task19'])
    def task19(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Одна куча', callback_data="t19_1")
                i2 = types.InlineKeyboardButton(text='Две кучи', callback_data="t19_2")
                mi1.add(i1).add(i2)
                bot.send_message(message.chat.id,
                                 f"Задание 19:\n<u>Выигрышная стратегия. Задание 1</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task20'])
    def task20(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Одна куча', callback_data="t20_1")
                i2 = types.InlineKeyboardButton(text='Две кучи', callback_data="t20_2")
                mi1.add(i1).add(i2)
                bot.send_message(message.chat.id,
                                 f"Задание 20:\n<u>Выигрышная стратегия. Задание 2</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task21'])
    def task21(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Одна куча', callback_data="t21_1")
                i2 = types.InlineKeyboardButton(text='Две кучи', callback_data="t21_2")
                mi1.add(i1).add(i2)
                bot.send_message(message.chat.id,
                                 f"Задание 21:\n<u>Выигрышная стратегия. Задание 3</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task22'])
    def task22(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Посимвольная обработка восьмеричных чисел', callback_data="t22_1")
                i2 = types.InlineKeyboardButton(text='Посимвольная обработка чисел в разных СС', callback_data="t22_2")
                i3 = types.InlineKeyboardButton(text='Разное', callback_data="t22_3")
                i4 = types.InlineKeyboardButton(text='Посимвольная обработка десятичных чисел', callback_data="t22_4")
                mi1.add(i1).add(i2).add(i3).add(i4)
                bot.send_message(message.chat.id,
                                 f"Задание 22:\n<u>Анализ программы с циклами и условными операторами</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task23'])
    def task23(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Количество программ с обязательным этапом', callback_data="t23_1")
                i2 = types.InlineKeyboardButton(text='Количество программ с избегаемым этапом', callback_data="t23_2")
                i3 = types.InlineKeyboardButton(text='Количество программ с обязательным и избегаемым этапами',
                                                callback_data="t23_3")
                i4 = types.InlineKeyboardButton(text='Поиск количества программ по заданному числу',
                                                callback_data="t23_4")
                i5 = types.InlineKeyboardButton(text='Поиск количества чисел по заданному числу команд',
                                                callback_data="t23_5")
                mi1.add(i1).add(i2).add(i3).add(i4).add(i5)
                bot.send_message(message.chat.id,
                                 f"Задание 23:\n<u>Оператор присваивания и ветвления. Перебор вариантов, "
                                 f"построение дерева</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task24'])
    def task24(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Задания для подготовки 1', callback_data="t24_1")
                i2 = types.InlineKeyboardButton(text='Задания для подготовки 2', callback_data="t24_2")
                i3 = types.InlineKeyboardButton(text='Задания для подготовки 3', callback_data="t24_3")
                i4 = types.InlineKeyboardButton(text='Задания для подготовки 4', callback_data="t24_4")
                mi1.add(i1).add(i2).add(i3).add(i4)
                bot.send_message(message.chat.id,
                                 f"Задание 24:\n<u>Обработка символьных строк</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task25'])
    def task25(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Задания для подготовки 1', callback_data="t25_1")
                i2 = types.InlineKeyboardButton(text='Задания для подготовки 2', callback_data="t25_2")
                i3 = types.InlineKeyboardButton(text='Задания для подготовки 3', callback_data="t25_3")
                i4 = types.InlineKeyboardButton(text='Задания для подготовки 4', callback_data="t25_4")
                mi1.add(i1).add(i2).add(i3).add(i4)
                bot.send_message(message.chat.id,
                                 f"Задание 25:\n<u>Обработка целочисленной информации. Задание 1</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task26'])
    def task26(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Задания для подготовки 1', callback_data="t26_1")
                i2 = types.InlineKeyboardButton(text='Задания для подготовки 2', callback_data="t26_2")
                i3 = types.InlineKeyboardButton(text='Задания для подготовки 3', callback_data="t26_3")
                i4 = types.InlineKeyboardButton(text='Задания для подготовки 4', callback_data="t26_4")
                mi1.add(i1).add(i2).add(i3).add(i4)
                bot.send_message(message.chat.id,
                                 f"Задание 26:\n<u>Обработка целочисленной информации. Задание 2</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(commands=['task27'])
    def task27(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Задания для подготовки 1', callback_data="t27_1")
                i2 = types.InlineKeyboardButton(text='Задания для подготовки 2', callback_data="t27_2")
                mi1.add(i1).add(i2)
                bot.send_message(message.chat.id,
                                 f"Задание 27:\n<u>Программирование</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий.",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    @bot.message_handler(content_types=['text'])
    def teat(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                bot.send_message(message.chat.id,
                                 f"Чтобы приступить к выполнению заданий введите их "
                                 f"диапозон как показано снизу. \n"
                                 f"Если вам что-то непонятно /help",
                                 reply_markup=login_markup)
            else:
                bot.send_message(message.chat.id, f"/logIn",
                                 reply_markup=start_markup)
        except KeyError:
            bot.send_message(message.chat.id, f"/start",
                             reply_markup=start_markup)

    @bot.callback_query_handler(func=lambda call: True)
    def task(call):
        if call.data == "t1_1":
            pass
        elif call.data == "t1_2":
            pass
        elif call.data == "t1_3":
            pass

        elif call.data == "t2_1":
            pass
        elif call.data == "t2_2":
            pass
        elif call.data == "t2_3":
            pass
        elif call.data == "t2_4":
            pass

        elif call.data == "t3_1":
            pass
        elif call.data == "t3_2":
            pass

        elif call.data == "t4_1":
            pass
        elif call.data == "t4_2":
            pass
        elif call.data == "t4_3":
            pass
        elif call.data == "t4_4":
            pass

        elif call.data == "t5_1":
            pass
        elif call.data == "t5_2":
            pass
        elif call.data == "t5_3":
            pass
        elif call.data == "t5_4":
            pass
        elif call.data == "t5_5":
            pass
        elif call.data == "t5_6":
            pass

        elif call.data == "t6_1":
            pass
        elif call.data == "t6_2":
            pass
        elif call.data == "t6_3":
            pass
        elif call.data == "t6_4":
            pass

        elif call.data == "t7_1":
            pass
        elif call.data == "t7_2":
            pass
        elif call.data == "t7_3":
            pass
        elif call.data == "t7_4":
            pass
        elif call.data == "t7_5":
            pass
        elif call.data == "t7_6":
            pass
        elif call.data == "t7_7":
            pass
        elif call.data == "t7_8":
            pass

        elif call.data == "t8_1":
            pass
        elif call.data == "t8_2":
            pass
        elif call.data == "t8_3":
            pass
        elif call.data == "t8_4":
            pass
        elif call.data == "t8_5":
            pass
        elif call.data == "t8_6":
            pass
        elif call.data == "t8_7":
            pass

        elif call.data == "t9_1":
            pass
        elif call.data == "t9_2":
            pass
        elif call.data == "t9_3":
            pass

        elif call.data == "t10_1":
            pass
        elif call.data == "t10_2":
            pass
        elif call.data == "t10_3":
            pass

        elif call.data == "t11_1":
            pass
        elif call.data == "t11_2":
            pass
        elif call.data == "t11_3":
            pass
        elif call.data == "t11_4":
            pass
        elif call.data == "t11_5":
            pass

        elif call.data == "t12_1":
            pass
        elif call.data == "t12_2":
            pass
        elif call.data == "t12_3":
            pass
        elif call.data == "t12_4":
            pass
        elif call.data == "t12_5":
            pass
        elif call.data == "t12_6":
            pass

        elif call.data == "t13_1":
            pass
        elif call.data == "t13_2":
            pass
        elif call.data == "t13_3":
            pass
        elif call.data == "t13_4":
            pass

        elif call.data == "t14_1":
            pass
        elif call.data == "t14_2":
            pass
        elif call.data == "t14_3":
            pass

        elif call.data == "t15_1":
            pass
        elif call.data == "t15_2":
            pass
        elif call.data == "t15_3":
            pass
        elif call.data == "t15_4":
            pass
        elif call.data == "t15_5":
            pass

        elif call.data == "t16_1":
            pass
        elif call.data == "t16_2":
            pass
        elif call.data == "t16_3":
            pass
        elif call.data == "t16_4":
            pass
        elif call.data == "t16_5":
            pass
        elif call.data == "t16_6":
            pass

        elif call.data == "t17_1":
            pass
        elif call.data == "t17_2":
            pass

        elif call.data == "t18_1":
            pass
        elif call.data == "t18_2":
            pass

        elif call.data == "t19_1":
            pass
        elif call.data == "t19_2":
            pass

        elif call.data == "t20_1":
            pass
        elif call.data == "t20_2":
            pass

        elif call.data == "t21_1":
            pass
        elif call.data == "t21_2":
            pass

        elif call.data == "t22_1":
            pass
        elif call.data == "t22_2":
            pass
        elif call.data == "t22_3":
            pass
        elif call.data == "t22_4":
            pass

        elif call.data == "t23_1":
            pass
        elif call.data == "t23_2":
            pass
        elif call.data == "t23_3":
            pass
        elif call.data == "t23_4":
            pass
        elif call.data == "t23_5":
            pass

        elif call.data == "t24_1":
            pass
        elif call.data == "t24_2":
            pass
        elif call.data == "t24_3":
            pass
        elif call.data == "t24_4":
            pass

        elif call.data == "t25_1":
            pass
        elif call.data == "t25_2":
            pass
        elif call.data == "t25_3":
            pass
        elif call.data == "t25_4":
            pass

        elif call.data == "t26_1":
            pass
        elif call.data == "t26_2":
            pass
        elif call.data == "t26_3":
            pass
        elif call.data == "t26_4":
            pass

        elif call.data == "t27_1":
            pass
        elif call.data == "t27_2":
            pass

    @bot.message_handler(content_types='sticker')
    def fff(message):
        bot.send_sticker(message.chat.id, message.sticker.file_id)
        bot.send_message(message.chat.id, message.sticker.emoji)

    @bot.message_handler(content_types='photo')
    def ff(message):
        print(message)

    bot.polling(none_stop=True)


if __name__ == '__main__':
    asyncio.run(main())
