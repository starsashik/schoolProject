# Очень важные импорты
import asyncio
import hashlib
import sqlite3

import telebot
from telebot import types

# константы для использования
TOKEN = '5314353289:AAEvmoJe10pwcMJKmcsKiSYZb1PCCsYQKv8'
db_name = "tmp/TeleDB.db"

# Reply клавиатуры
start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
start_markup.row("/logIn")
start_markup.row('/registration')
start_markup.row("/help")

login_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
login_markup.add("/1_5", "/6_10", "/11_15")
login_markup.add("/16_20", "/21_25", "/26_27")
login_markup.row('/profile', "/top_user", '/logOut')

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


# главная фунция в которой работает бот
async def main():
    bot = telebot.TeleBot(TOKEN)
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    command = f"""SELECT id FROM User"""
    result = cur.execute(command).fetchall()
    cur.close()
    dd = {i[0]: False for i in result}

    # функция для началы работы бота
    @bot.message_handler(commands=["start"])
    def start(message):
        mess = f"Привет, <b><u>{message.from_user.username}</u></b>, Я бот помощник для ЕГЭ по информатике.\n" \
               f"Для удобной работы со мной, лучше всего зарегистрироваться\n" \
               f"Если у вас уже есть аккаунт, то можете войти в него. /logIn\n" \
               f"Для лучшего понимания работы бота используйте функцию /help\n" \
               f"Материалы заданий и решений взяты с сайта 'СДАМ ГИА: РЕШУ ЕГЭ':\nhttps://inf-ege.sdamgia.ru",
        bot.send_message(message.chat.id, mess, reply_markup=start_markup, parse_mode='html')

    # функция для вызова файла с инструкцией по использоавнию
    @bot.message_handler(commands=['help'])
    def help(message):
        doc = open("tmp/help.txt", mode="rb")
        bot.send_document(message.chat.id, doc)
        doc.close()

    # функция для скрытия клавиатуры
    @bot.message_handler(commands=['close'])
    def close(message):
        bot.send_message(message.chat.id, "Клавиатура скрыта", reply_markup=telebot.types.ReplyKeyboardRemove())

    # функция для перехода в меню заданий
    @bot.message_handler(commands=['back'])
    def bacc(message):
        bot.send_message(message.chat.id, "Вы вернулись в меню заданий", reply_markup=login_markup, parse_mode='html')

    # функции для регистрации
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

    # функции для входа в систему
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
                             f"можете приступать к выполнению заданий\n(смотрите клавиатуру)",
                             reply_markup=login_markup, parse_mode='html')
        else:
            bot.send_message(message.chat.id, f"Пароль неверный.\n"
                                              f"Попробуйте еще раз /login \n"
                                              f"Если вы забыли пароль, то к сожалению вам придется удалить аккаунт.\n"
                                              f"Для этого напишите '/' + 'del_acc'",
                             reply_markup=start_markup)

    # функция для выхода из системы
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

    # функции для удаления аккаунта
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

    # функция для отображения топа пользователей
    @bot.message_handler(commands=['top_user'])
    def top_us(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                con = sqlite3.connect(db_name)
                cur = con.cursor()
                command1 = f"""Select id, username FROM User"""
                res = cur.execute(command1).fetchall()
                gg = {}
                for j in res:
                    d = []
                    for i in range(1, 28):
                        command1 = f"""Select Total FROM Task{i} WHERE id = {j[0]}"""
                        res1 = cur.execute(command1).fetchone()
                        d.append(res1[0])
                    gg[j[1]] = round(sum(d) / 27)
                gg = sorted(gg.items(), key=lambda x: (x[0], x[1]))
                cur.close()
                st = ""
                for k in range(len(gg)):
                    st += f"{k + 1} место: {gg[k][0]} - {gg[k][1]}%\n"
                bot.send_message(message.chat.id,
                                 st,
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

    # функция для показа профиля пользователя
    @bot.message_handler(commands=['profile'])
    def prof(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                con = sqlite3.connect(db_name)
                cur = con.cursor()
                d = []
                for i in range(1, 28):
                    command1 = f"""Select Total FROM Task{i} WHERE id = {int(message.from_user.id)}"""
                    res = cur.execute(command1).fetchone()
                    d.append(res[0])
                cur.close()
                bot.send_message(message.chat.id,
                                 f"<b>{message.from_user.username}: {message.from_user.first_name} "
                                 f"{message.from_user.last_name if message.from_user.last_name is not None else ''}"
                                 f"</b>\n Анализ информационных моделей - {d[0]}%\n"
                                 f"Построение таблиц истинности логических выражений - {d[1]}%\n"
                                 f"Поиск информации в реляционных базах данных - {d[2]}%\n"
                                 f"Кодирование и декодирование информации - {d[3]}%\n"
                                 f"Анализ и построение алгоритмов для исполнителей - {d[4]}%\n"
                                 f"Анализ программ - {d[5]}%\n"
                                 f"Кодирование и декодирование информации. Передача информации - {d[6]}%\n"
                                 f"Перебор слов и системы счисления - {d[7]}%\n"
                                 f"Работа с таблицами - {d[8]}%\n"
                                 f"Поиск символов в текстовом редакторе - {d[9]}%\n"
                                 f"Вычисление количества информации - {d[10]}%\n"
                                 f"Выполнение алгоритмов для исполнителей - {d[11]}%\n"
                                 f"Поиск путей в графе - {d[12]}%\n"
                                 f"Кодирование чисел. Системы счисления - {d[13]}%\n"
                                 f"Преобразование логических выражений - {d[14]}%\n"
                                 f"Рекурсивные алгоритмы - {d[15]}%\n"
                                 f"Обработки числовой последовательности - {d[16]}%\n"
                                 f"Робот-сборщик монет - {d[17]}%\n"
                                 f"Выигрышная стратегия. Задание 1 - {d[18]}%\n"
                                 f"Выигрышная стратегия. Задание 2 - {d[19]}%\n"
                                 f"Выигрышная стратегия. Задание 3 - {d[20]}%\n"
                                 f"Анализ программы с циклами и условными операторами - {d[21]}%\n"
                                 f"Оператор присваивания и ветвления. Перебор вариантов, построение дерева - "
                                 f"{d[22]}%\nОбработка символьных строк - {d[23]}%\n"
                                 f"Обработка целочисленной информации - {d[24]}%\n"
                                 f"Обработка целочисленной информации - {d[25]}%\n"
                                 f"Программирование - {d[26]}%\n"
                                 f"Всего выполнено: {str(round(sum(d) / 27))}%",
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

    # функции для перехода между блоками заданий
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    # функции для вывода заданий
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                i1 = types.InlineKeyboardButton(text='Подсчет количества слов', callback_data="t8_1")
                i2 = types.InlineKeyboardButton(text='Подсчет количества слов с ограничениями', callback_data="t8_2")
                i3 = types.InlineKeyboardButton(text='Последовательность лампочек', callback_data="t8_3")
                i4 = types.InlineKeyboardButton(text='Последовательность сигнальных ракет', callback_data="t8_4")
                i5 = types.InlineKeyboardButton(text='Разное', callback_data="t8_5")
                i6 = types.InlineKeyboardButton(text='Подсчет количества разных последовательностей',
                                                callback_data="t8_6")
                i7 = types.InlineKeyboardButton(text='Слова по порядку', callback_data="t8_7")
                mi1.add(i1).add(i2).add(i3).add(i4).add(i5).add(i6).add(i7)
                bot.send_message(message.chat.id,
                                 f"Задание 8:\n<u>Перебор слов и системы счисления</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
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
                                 f"для решения заданий. /logIn",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    # функции для проверки ответов
    def t1_1A(message):
        with open("tmp/Task1/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task1" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t1_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t1_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t1_2A(message):
        with open("tmp/Task1/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task1" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t1_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t1_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t1_3A(message):
        with open("tmp/Task1/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task1" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t1_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t1_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t1_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task1 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:4]) / 3 * 100)
        command = f"""UPDATE "Task1" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t2_1A(message):
        with open("tmp/Task2/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task2" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t2_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t2_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t2_2A(message):
        with open("tmp/Task2/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task2" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t2_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t2_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t2_3A(message):
        with open("tmp/Task2/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task2" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t2_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t2_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t2_4A(message):
        with open("tmp/Task2/4/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task2" SET "4" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t2_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t2_4R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t2_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task2 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:5]) / 4 * 100)
        command = f"""UPDATE "Task2" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t3_1A(message):
        with open("tmp/Task3/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task3" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t3_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t3_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t3_2A(message):
        with open("tmp/Task3/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task3" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t3_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t3_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t3_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task3 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:3]) / 2 * 100)
        command = f"""UPDATE "Task3" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t4_1A(message):
        with open("tmp/Task4/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task4" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t4_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t4_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t4_2A(message):
        with open("tmp/Task4/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task4" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t4_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t4_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t4_3A(message):
        with open("tmp/Task4/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task4" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t4_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t4_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t4_4A(message):
        with open("tmp/Task4/4/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task4" SET "4" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t4_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t4_4R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t4_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task4 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:5]) / 4 * 100)
        command = f"""UPDATE "Task4" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t5_1A(message):
        with open("tmp/Task5/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task5" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t5_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t5_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t5_2A(message):
        with open("tmp/Task5/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task5" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t5_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t5_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t5_3A(message):
        with open("tmp/Task5/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task5" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t5_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t5_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t5_4A(message):
        with open("tmp/Task5/4/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task5" SET "4" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t5_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t5_4R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t5_5A(message):
        with open("tmp/Task5/5/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task5" SET "5" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t5_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t5_5R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t5_6A(message):
        with open("tmp/Task5/6/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task5" SET "6" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t5_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t5_6R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t5_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task5 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:7]) / 6 * 100)
        command = f"""UPDATE "Task5" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t6_1A(message):
        with open("tmp/Task6/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task6" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t6_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t6_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t6_2A(message):
        with open("tmp/Task6/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task6" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t6_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t6_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t6_3A(message):
        with open("tmp/Task6/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task6" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t6_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t6_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t6_4A(message):
        with open("tmp/Task6/4/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task6" SET "4" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t6_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t6_4R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t6_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task6 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:5]) / 4 * 100)
        command = f"""UPDATE "Task6" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t7_1A(message):
        with open("tmp/Task7/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task7" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t7_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t7_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t7_2A(message):
        with open("tmp/Task7/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task7" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t7_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t7_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t7_3A(message):
        with open("tmp/Task7/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task7" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t7_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t7_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t7_4A(message):
        with open("tmp/Task7/4/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task7" SET "4" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t7_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t7_4R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t7_5A(message):
        with open("tmp/Task7/5/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task7" SET "5" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t7_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t7_5R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t7_6A(message):
        with open("tmp/Task7/6/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task7" SET "6" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t7_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t7_6R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t7_7A(message):
        with open("tmp/Task7/7/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task7" SET "7" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t7_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t7_7R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t7_8A(message):
        with open("tmp/Task7/8/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task7" SET "8" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t7_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t7_8R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t7_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task7 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:9]) / 8 * 100)
        command = f"""UPDATE "Task7" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t8_1A(message):
        with open("tmp/Task8/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task8" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t8_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t8_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t8_2A(message):
        with open("tmp/Task8/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task8" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t8_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t8_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t8_3A(message):
        with open("tmp/Task8/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task8" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t8_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t8_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t8_4A(message):
        with open("tmp/Task8/4/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task8" SET "4" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t8_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t8_4R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t8_5A(message):
        with open("tmp/Task8/5/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task8" SET "5" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t8_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t8_5R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t8_6A(message):
        with open("tmp/Task8/6/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task8" SET "6" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t8_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t8_6R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t8_7A(message):
        with open("tmp/Task8/7/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task8" SET "7" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t8_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t8_7R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t8_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task8 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:8]) / 7 * 100)
        command = f"""UPDATE "Task8" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t9_1A(message):
        with open("tmp/Task9/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task9" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t9_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t9_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t9_2A(message):
        with open("tmp/Task9/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task9" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t9_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t9_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t9_3A(message):
        with open("tmp/Task9/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task9" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t9_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t9_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t9_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task9 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:4]) / 3 * 100)
        command = f"""UPDATE "Task9" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t10_1A(message):
        with open("tmp/Task10/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task10" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t10_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t10_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t10_2A(message):
        with open("tmp/Task10/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task10" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t10_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t10_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t10_3A(message):
        with open("tmp/Task10/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task10" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t10_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t10_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t10_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task10 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:4]) / 3 * 100)
        command = f"""UPDATE "Task10" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t11_1A(message):
        with open("tmp/Task11/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task11" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t11_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t11_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t11_2A(message):
        with open("tmp/Task11/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task11" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t11_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t11_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t11_3A(message):
        with open("tmp/Task11/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task11" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t11_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t11_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t11_4A(message):
        with open("tmp/Task11/4/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task11" SET "4" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t11_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t11_4R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t11_5A(message):
        with open("tmp/Task11/5/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task11" SET "5" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t11_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t11_5R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t11_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task11 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:6]) / 5 * 100)
        command = f"""UPDATE "Task11" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t12_1A(message):
        with open("tmp/Task12/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task12" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t12_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t12_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t12_2A(message):
        with open("tmp/Task12/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task12" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t12_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t12_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t12_3A(message):
        with open("tmp/Task12/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task12" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t12_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t12_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t12_4A(message):
        with open("tmp/Task12/4/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task12" SET "4" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t12_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t12_4R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t12_5A(message):
        with open("tmp/Task12/5/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task12" SET "5" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t12_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t12_5R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t12_6A(message):
        with open("tmp/Task12/6/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task12" SET "6" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t12_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t12_6R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t12_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task12 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:7]) / 6 * 100)
        command = f"""UPDATE "Task12" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t13_1A(message):
        with open("tmp/Task13/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task13" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t13_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t13_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t13_2A(message):
        with open("tmp/Task13/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task13" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t13_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t13_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t13_3A(message):
        with open("tmp/Task13/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task13" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t13_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t13_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t13_4A(message):
        with open("tmp/Task13/4/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task13" SET "4" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t13_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t13_4R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t13_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task13 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:5]) / 4 * 100)
        command = f"""UPDATE "Task13" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t14_1A(message):
        with open("tmp/Task14/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task14" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t14_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t14_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t14_2A(message):
        with open("tmp/Task14/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task14" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t14_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t14_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t14_3A(message):
        with open("tmp/Task14/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task14" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t14_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t14_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t14_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task14 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:4]) / 3 * 100)
        command = f"""UPDATE "Task14" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t15_1A(message):
        with open("tmp/Task15/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task15" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t15_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t15_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t15_2A(message):
        with open("tmp/Task15/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task15" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t15_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t15_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t15_3A(message):
        with open("tmp/Task15/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task15" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t15_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t15_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t15_4A(message):
        with open("tmp/Task15/4/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task15" SET "4" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t15_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t15_4R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t15_5A(message):
        with open("tmp/Task15/5/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task15" SET "5" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t15_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t15_5R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t15_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task15 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:6]) / 5 * 100)
        command = f"""UPDATE "Task15" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t16_1A(message):
        with open("tmp/Task16/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task16" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t16_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t16_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t16_2A(message):
        with open("tmp/Task16/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task16" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t16_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t16_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t16_3A(message):
        with open("tmp/Task16/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task16" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t16_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t16_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t16_4A(message):
        with open("tmp/Task16/4/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task16" SET "4" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t16_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t16_4R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t16_5A(message):
        with open("tmp/Task16/5/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task16" SET "5" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t16_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t16_5R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t16_6A(message):
        with open("tmp/Task16/6/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task16" SET "6" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t16_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t16_6R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t16_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task16 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:7]) / 6 * 100)
        command = f"""UPDATE "Task16" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t17_1A(message):
        with open("tmp/Task17/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task17" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t17_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t17_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t17_2A(message):
        with open("tmp/Task17/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task17" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t17_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t17_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t17_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task17 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:3]) / 2 * 100)
        command = f"""UPDATE "Task17" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t18_1A(message):
        with open("tmp/Task18/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task18" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t18_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t18_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t18_2A(message):
        with open("tmp/Task18/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task18" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t18_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t18_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t18_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task18 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:3]) / 2 * 100)
        command = f"""UPDATE "Task18" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t19_1A(message):
        with open("tmp/Task19/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task19" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t19_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t19_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t19_2A(message):
        with open("tmp/Task19/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task19" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t19_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t19_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t19_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task19 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:3]) / 2 * 100)
        command = f"""UPDATE "Task19" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t20_1A(message):
        with open("tmp/Task20/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task20" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t20_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t20_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t20_2A(message):
        with open("tmp/Task20/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task20" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t20_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t20_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t20_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task20 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:3]) / 2 * 100)
        command = f"""UPDATE "Task20" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t21_1A(message):
        with open("tmp/Task21/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task21" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t21_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t21_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t21_2A(message):
        with open("tmp/Task21/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task21" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t21_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t21_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t21_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task21 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:3]) / 2 * 100)
        command = f"""UPDATE "Task21" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t22_1A(message):
        with open("tmp/Task22/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task22" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t2_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t22_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t22_2A(message):
        with open("tmp/Task22/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task22" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t22_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t22_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t22_3A(message):
        with open("tmp/Task22/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task22" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t22_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t22_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t22_4A(message):
        with open("tmp/Task22/4/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task22" SET "4" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t22_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t22_4R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t22_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task22 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:5]) / 4 * 100)
        command = f"""UPDATE "Task22" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t23_1A(message):
        with open("tmp/Task23/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task23" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t23_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t23_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t23_2A(message):
        with open("tmp/Task23/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task23" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t23_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t23_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t23_3A(message):
        with open("tmp/Task23/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task23" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t23_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t23_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t23_4A(message):
        with open("tmp/Task23/4/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task23" SET "4" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t23_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t23_4R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t23_5A(message):
        with open("tmp/Task23/5/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task23" SET "5" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t23_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t23_5R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t23_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task23 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:6]) / 5 * 100)
        command = f"""UPDATE "Task23" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t24_1A(message):
        with open("tmp/Task24/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task24" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t24_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t24_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t24_2A(message):
        with open("tmp/Task24/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task24" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t24_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t24_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t24_3A(message):
        with open("tmp/Task24/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task24" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t24_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t24_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t24_4A(message):
        with open("tmp/Task24/4/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task24" SET "4" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t24_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t24_4R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t24_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task24 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:5]) / 4 * 100)
        command = f"""UPDATE "Task24" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t25_1A(message):
        with open("tmp/Task25/1/answer", encoding='utf8') as f:
            d = f.read().split('\n')
        flag = True
        s = message.text.split(';')
        for i in range(8):
            if not (s[i] == d[i]):
                flag = False
                break
        if flag:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task25" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t25_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t25_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t25_2A(message):
        with open("tmp/Task25/2/answer", encoding='utf8') as f:
            d = f.read().split('\n')
        flag = True
        s = message.text.split(';')
        for i in range(6):
            if not (s[i] == d[i]):
                flag = False
                break
        if flag:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task25" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t25_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t25_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t25_3A(message):
        with open("tmp/Task25/3/answer", encoding='utf8') as f:
            d = f.read().split('\n')
        flag = True
        s = message.text.split(';')
        for i in range(3):
            if not (s[i] == d[i]):
                flag = False
                break
        if flag:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task25" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t25_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t25_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t25_4A(message):
        with open("tmp/Task25/4/answer", encoding='utf8') as f:
            d = f.read().split('\n')
        flag = True
        s = message.text.split(';')
        for i in range(2):
            if not (s[i] == d[i]):
                flag = False
                break
        if flag:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task25" SET "4" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t25_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t25_4R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t25_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task25 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:5]) / 4 * 100)
        command = f"""UPDATE "Task25" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t26_1A(message):
        with open("tmp/Task26/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task26" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t26_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t26_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t26_2A(message):
        with open("tmp/Task26/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task26" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t26_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t26_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t26_3A(message):
        with open("tmp/Task26/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task26" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t26_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t26_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t26_4A(message):
        with open("tmp/Task26/4/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task26" SET "4" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t26_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t26_4R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t26_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task26 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:5]) / 4 * 100)
        command = f"""UPDATE "Task26" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    def t27_1A(message):
        with open("tmp/Task27/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task27" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t27_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t27_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t27_2A(message):
        with open("tmp/Task27/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task27" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t27_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t27_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t27_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task27 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:3]) / 2 * 100)
        command = f"""UPDATE "Task27" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

    # функция для отработки callback"ов (меню заданий)
    @bot.callback_query_handler(func=lambda call: True)
    def task(call):
        idd = call.message.chat.id
        try:
            current = dd[int(call.from_user.id)]
            if current:
                if call.data == "t1_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t1_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t1_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task1/1/task.png", "rb")
                    bot.send_message(idd, f"Задание 1.1:\n<b>Неоднозначное соотнесение таблицы и графа</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t1_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t1_1A)
                if call.data == "t1_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t1_1A")
                    mi1.add(i1)
                    with open("tmp/Task1/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task1/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 1.1\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t1_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t1_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t1_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task1/2/task.png", "rb")
                    bot.send_message(idd, f"Задание 1.2:\n<b>Однозначное соотнесение таблицы и графа</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t1_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t1_2A)
                if call.data == "t1_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t1_2A")
                    mi1.add(i1)
                    with open("tmp/Task1/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task1/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 1.2\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t1_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t1_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t1_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task1/3/task.png", "rb")
                    bot.send_message(idd, f"Задание 1.3:\n<b>Поиск оптимального маршрута по таблице</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t1_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t1_3A)
                if call.data == "t1_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t1_3A")
                    mi1.add(i1)
                    with open("tmp/Task1/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task1/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 1.3\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t2_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t2_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t2_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task2/1/task.png", "rb")
                    bot.send_message(idd, f"Задание 2.1:\n<b>Монотонные функции</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t2_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должен быть набор переменных, "
                                          "запишите его без лишних запятых и знаков. Например: xyz)")
                    bot.register_next_step_handler(tb, t2_1A)
                if call.data == "t2_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t2_1A")
                    mi1.add(i1)
                    with open("tmp/Task2/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task2/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 2.1\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t2_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t2_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t2_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task2/2/task.png", "rb")
                    bot.send_message(idd, f"Задание 2.2:\n<b>Немонотонные функции</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t2_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должен быть набор переменных, "
                                          "запишите его без лишних запятых и знаков. Например: xyz)")
                    bot.register_next_step_handler(tb, t2_2A)
                if call.data == "t2_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t2_2A")
                    mi1.add(i1)
                    with open("tmp/Task2/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task2/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 2.2\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t2_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t2_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t2_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task2/3/task.png", "rb")
                    bot.send_message(idd, f"Задание 2.3:\n<b>Строки с пропущенными значениями</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t2_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должен быть набор переменных, "
                                          "запишите его без лишних запятых и знаков. Например: xyz)")
                    bot.register_next_step_handler(tb, t2_3A)
                if call.data == "t2_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t2_3A")
                    mi1.add(i1)
                    with open("tmp/Task2/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task2/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 2.3\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t2_4":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t2_4A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t2_4R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task2/4/task.png", "rb")
                    bot.send_message(idd, f"Задание 2.4:\n<b>Разные задачи</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t2_4A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t2_4A)
                if call.data == "t2_4R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t2_4A")
                    mi1.add(i1)
                    with open("tmp/Task2/4/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task2/4/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 2.4\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t3_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t3_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t3_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task3/1/task.png", "rb")
                    bot.send_message(idd, f"Задание 3.1:\n<b>Задания для подготовки 1</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t3_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t3_1A)
                if call.data == "t3_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t3_1A")
                    mi1.add(i1)
                    with open("tmp/Task3/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task3/1/solution1.png', "rb")
                    phot2 = open('tmp/Task3/1/solution2.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 3.1\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_photo(idd, phot2, reply_markup=mi1)
                    phot.close()
                    phot2.close()

                if call.data == "t3_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t3_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t3_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task3/2/task.png", "rb")
                    bot.send_message(idd, f"Задание 3.2:\n<b>Задания для подготовки 1</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t3_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t3_2A)
                if call.data == "t3_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t3_2A")
                    mi1.add(i1)
                    with open("tmp/Task3/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task3/2/solution1.png', "rb")
                    phot2 = open('tmp/Task3/2/solution2.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 3.2\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_photo(idd, phot2, reply_markup=mi1)
                    phot.close()
                    phot2.close()

                if call.data == "t4_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t4_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t4_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task4/1/task.png", "rb")
                    bot.send_message(idd, f"Задание 4.1:\n<b>Выбор кода при неиспользуемых сигналах</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t4_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t4_1A)
                if call.data == "t4_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t4_1A")
                    mi1.add(i1)
                    with open("tmp/Task4/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task4/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 4.1\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t4_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t4_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t4_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task4/2/task.png", "rb")
                    bot.send_message(idd,
                                     f"Задание 4.2:\n<b>Шифрование по известному коду и перевод в различные СС</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t4_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число число в шестнадцатеричной системе "
                                          "счисления, запишите его без лишних запятых и знаков. Например: А94)")
                    bot.register_next_step_handler(tb, t4_2A)
                if call.data == "t4_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t4_2A")
                    mi1.add(i1)
                    with open("tmp/Task4/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task4/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 4.2\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t4_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t4_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t4_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task4/3/task.png", "rb")
                    bot.send_message(idd,
                                     f"Задание 4.3:\n<b>Расшифровка сообщений</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t4_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть строка из заглавных латинских букв"
                                          "счисления, запишите его без лишних запятых и знаков. Например: АBVD)")
                    bot.register_next_step_handler(tb, t4_3A)
                if call.data == "t4_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t4_3A")
                    mi1.add(i1)
                    with open("tmp/Task4/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task4/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 4.3\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t4_4":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t4_4A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t4_4R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task4/4/task.png", "rb")
                    bot.send_message(idd,
                                     f"Задание 4.4:\n<b>Передача информации. Выбор кода</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t4_4A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число число в двоичной системе "
                                          "счисления, запишите его без лишних запятых и знаков. Например: 100101)")
                    bot.register_next_step_handler(tb, t4_4A)
                if call.data == "t4_4R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t4_4A")
                    mi1.add(i1)
                    with open("tmp/Task4/4/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task4/4/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 4.4\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t5_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t5_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t5_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task5/1/task.png", "rb")
                    bot.send_message(idd, f"Задание 5.1:\n<b>Исполнители на плоскости</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t5_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t5_1A)
                if call.data == "t5_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t5_1A")
                    mi1.add(i1)
                    with open("tmp/Task5/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task5/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 5.1\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t5_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t5_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t5_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task5/2/task.png", "rb")
                    bot.send_message(idd,
                                     f"Задание 5.2:\n<b>Посимвольное двоичное преобразование</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t5_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t5_2A)
                if call.data == "t5_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t5_2A")
                    mi1.add(i1)
                    with open("tmp/Task5/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task5/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 5.2\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t5_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t5_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t5_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task5/3/task.png", "rb")
                    bot.send_message(idd,
                                     f"Задание 5.3:\n<b>Разные задачи</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t5_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t5_3A)
                if call.data == "t5_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t5_3A")
                    mi1.add(i1)
                    with open("tmp/Task5/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task5/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 5.3\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t5_4":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t5_4A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t5_4R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task5/4/task.png", "rb")
                    bot.send_message(idd,
                                     f"Задание 5.4:\n<b>Арифмометры</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t5_4A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должна быть последовательность из 1 и 2, "
                                          "запишите его без лишних запятых и знаков. Например: 212221)")
                    bot.register_next_step_handler(tb, t5_4A)
                if call.data == "t5_4R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t5_4A")
                    mi1.add(i1)
                    with open("tmp/Task5/4/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task5/4/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 5.4\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t5_5":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t5_5A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t5_5R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task5/5/task.png", "rb")
                    bot.send_message(idd,
                                     f"Задание 5.5:\n<b>Арифмометры с движением в обе стороны</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t5_5A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должна быть последовательность из 1 и 2, "
                                          "запишите его без лишних запятых и знаков. Например: 212221)")
                    bot.register_next_step_handler(tb, t5_5A)
                if call.data == "t5_5R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t5_5A")
                    mi1.add(i1)
                    with open("tmp/Task5/5/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task5/5/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 5.5\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t5_6":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t5_6A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t5_6R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task5/6/task.png", "rb")
                    bot.send_message(idd,
                                     f"Задание 5.6:\n<b>Посимвольное десятичное преобразование</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t5_6A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t5_6A)
                if call.data == "t5_6R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t5_6A")
                    mi1.add(i1)
                    with open("tmp/Task5/6/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task5/6/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 5.6\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t6_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t6_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t6_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task6/1/task.png", "rb")
                    bot.send_message(idd, f"Задание 6.1:\n<b>Две линейные функции</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t6_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t6_1A)
                if call.data == "t6_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t6_1A")
                    mi1.add(i1)
                    with open("tmp/Task6/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task6/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 6.1\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t6_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t6_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t6_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task6/2/task.png", "rb")
                    bot.send_message(idd, f"Задание 6.2:\n<b>Сумма двух линейных функций</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t6_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t6_2A)
                if call.data == "t6_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t6_2A")
                    mi1.add(i1)
                    with open("tmp/Task6/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task6/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 6.2\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t6_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t6_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t6_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task6/3/task.png", "rb")
                    bot.send_message(idd, f"Задание 6.3:\n<b>Арифметическая прогрессия</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t6_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t6_3A)
                if call.data == "t6_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t6_3A")
                    mi1.add(i1)
                    with open("tmp/Task6/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task6/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 6.3\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t6_4":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t6_4A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t6_4R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task6/4/task.png", "rb")
                    bot.send_message(idd, f"Задание 6.4:\n<b>Условие выполнения цикла while</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t6_4A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t6_4A)
                if call.data == "t6_4R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t6_4A")
                    mi1.add(i1)
                    with open("tmp/Task6/4/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task6/4/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 6.4\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t7_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t7_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t7_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task7/1/task.png", "rb")
                    bot.send_message(idd, f"Задание 7.1:\n<b>Передача звуковых файлов</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t7_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t7_1A)
                if call.data == "t7_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t7_1A")
                    mi1.add(i1)
                    with open("tmp/Task7/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task7/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 7.1\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t7_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t7_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t7_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task7/2/task.png", "rb")
                    bot.send_message(idd, f"Задание 7.2:\n<b>Передача изображений</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t7_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t7_2A)
                if call.data == "t7_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t7_2A")
                    mi1.add(i1)
                    with open("tmp/Task7/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task7/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 7.2\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t7_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t7_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t7_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task7/3/task.png", "rb")
                    bot.send_message(idd, f"Задание 7.3:\n<b>Передача текстовых файлов</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t7_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t7_3A)
                if call.data == "t7_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t7_3A")
                    mi1.add(i1)
                    with open("tmp/Task7/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task7/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 7.3\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t7_4":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t7_4A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t7_4R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task7/4/task.png", "rb")
                    bot.send_message(idd, f"Задание 7.4:\n<b>Хранение звуковых файлов</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t7_4A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t7_4A)
                if call.data == "t7_4R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t7_4A")
                    mi1.add(i1)
                    with open("tmp/Task7/4/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task7/4/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 7.4\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t7_5":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t7_5A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t7_5R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task7/5/task.png", "rb")
                    bot.send_message(idd, f"Задание 7.5:\n<b>Сравнение двух способов передачи данных</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t7_5A":
                    tb = bot.send_message(idd, "Ваш ответ:\n(Это должен быть вариант ответа кириллицей А или Б и "
                                               "целое число число, запишите его без лишних запятых и знаков. Например: "
                                               "А223)")
                    bot.register_next_step_handler(tb, t7_5A)
                if call.data == "t7_5R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t7_5A")
                    mi1.add(i1)
                    with open("tmp/Task7/5/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task7/5/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 7.5\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t7_6":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t7_6A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t7_6R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task7/6/task.png", "rb")
                    bot.send_message(idd, f"Задание 7.6:\n<b>Определение времени передачи файла</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t7_6A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t7_6A)
                if call.data == "t7_6R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t7_6A")
                    mi1.add(i1)
                    with open("tmp/Task7/6/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task7/6/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 7.6\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t7_7":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t7_7A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t7_7R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task7/7/task.png", "rb")
                    bot.send_message(idd, f"Задание 7.7:\n<b>Хранение изображений</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t7_7A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t7_7A)
                if call.data == "t7_7R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t7_7A")
                    mi1.add(i1)
                    with open("tmp/Task7/7/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task7/7/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 7.7\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t7_8":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t7_8A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t7_8R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task7/8/task.png", "rb")
                    bot.send_message(idd, f"Задание 7.8:\n<b>Определение размера записанного файла</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t7_8A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t7_8A)
                if call.data == "t7_8R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t7_8A")
                    mi1.add(i1)
                    with open("tmp/Task7/8/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task7/8/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 7.8\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t8_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t8_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t8_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task8/1/task.png", "rb")
                    bot.send_message(idd, f"Задание 8.1:\n<b>Подсчет количества слов</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t8_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t8_1A)
                if call.data == "t8_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t8_1A")
                    mi1.add(i1)
                    with open("tmp/Task8/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task8/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 8.1\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t8_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t8_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t8_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task8/2/task.png", "rb")
                    bot.send_message(idd, f"Задание 8.2:\n<b>Подсчет количества слов с ограничениями</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t8_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t8_2A)
                if call.data == "t8_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t8_2A")
                    mi1.add(i1)
                    with open("tmp/Task8/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task8/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 8.2\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t8_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t8_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t8_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task8/3/task.png", "rb")
                    bot.send_message(idd, f"Задание 8.3:\n<b>Последовательность лампочек</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t8_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t8_3A)
                if call.data == "t8_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t8_3A")
                    mi1.add(i1)
                    with open("tmp/Task8/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task8/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 8.3\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t8_4":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t8_4A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t8_4R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task8/4/task.png", "rb")
                    bot.send_message(idd, f"Задание 8.4:\n<b>Последовательность сигнальных ракет</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t8_4A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t8_4A)
                if call.data == "t8_4R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t8_4A")
                    mi1.add(i1)
                    with open("tmp/Task8/4/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task8/4/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 8.4\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t8_5":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t8_5A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t8_5R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task8/5/task.png", "rb")
                    bot.send_message(idd, f"Задание 8.5:\n<b>Разное</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t8_5A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t8_5A)
                if call.data == "t8_5R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t8_5A")
                    mi1.add(i1)
                    with open("tmp/Task8/5/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task8/5/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 8.5\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t8_6":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t8_6A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t8_6R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task8/6/task.png", "rb")
                    bot.send_message(idd, f"Задание 8.6:\n<b>Подсчет количества разных последовательностей</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t8_6A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t8_6A)
                if call.data == "t8_6R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t8_6A")
                    mi1.add(i1)
                    with open("tmp/Task8/6/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task8/6/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 8.6\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t8_7":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t8_7A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t8_7R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task8/7/task.png", "rb")
                    bot.send_message(idd, f"Задание 8.7:\n<b>Слова по порядку</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t8_7A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должна быть последовательность букв кириллицей, "
                                          "запишите его без лишних запятых и знаков. Например: ОААУУ)")
                    bot.register_next_step_handler(tb, t8_7A)
                if call.data == "t8_7R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t8_7A")
                    mi1.add(i1)
                    with open("tmp/Task8/7/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task8/7/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 8.7\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t9_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t9_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t9_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task9/1/task.png", "rb")
                    docc = open("tmp/Task9/1/9_1.xlsx", "rb")
                    bot.send_message(idd, f"Задание 9.1:\n<b>Задания для подготовки 1</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docc, reply_markup=mi1)
                    docc.close()
                    phot.close()
                if call.data == "t9_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t9_1A)
                if call.data == "t9_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t9_1A")
                    mi1.add(i1)
                    with open("tmp/Task9/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task9/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 9.1\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t9_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t9_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t9_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task9/2/task.png", "rb")
                    docc = open("tmp/Task9/2/9_2.xlsx", "rb")
                    bot.send_message(idd, f"Задание 9.2:\n<b>Задания для подготовки 2</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docc, reply_markup=mi1)
                    docc.close()
                    phot.close()
                if call.data == "t9_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t9_2A)
                if call.data == "t9_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t9_2A")
                    mi1.add(i1)
                    with open("tmp/Task9/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task9/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 9.2\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t9_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t9_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t9_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task9/3/task.png", "rb")
                    docc = open("tmp/Task9/3/9_3.xlsx", "rb")
                    bot.send_message(idd, f"Задание 9.3:\n<b>Задания для подготовки 3</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docc, reply_markup=mi1)
                    docc.close()
                    phot.close()
                if call.data == "t9_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: -25)")
                    bot.register_next_step_handler(tb, t9_3A)
                if call.data == "t9_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t9_3A")
                    mi1.add(i1)
                    with open("tmp/Task9/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task9/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 9.3\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t10_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t10_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t10_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task10/1/task.png", "rb")
                    docc = open("tmp/Task10/1/10_1.docx", "rb")
                    bot.send_message(idd, f"Задание 10.1:\n<b>Задания для подготовки 1</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docc, reply_markup=mi1)
                    docc.close()
                    phot.close()
                if call.data == "t10_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t10_1A)
                if call.data == "t10_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t10_1A")
                    mi1.add(i1)
                    with open("tmp/Task10/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task10/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 10.1\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t10_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t10_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t10_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task10/2/task.png", "rb")
                    docc = open("tmp/Task10/2/10_2.docx", "rb")
                    bot.send_message(idd, f"Задание 10.2:\n<b>Задания для подготовки 2</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docc, reply_markup=mi1)
                    docc.close()
                    phot.close()
                if call.data == "t10_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t10_2A)
                if call.data == "t10_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t10_2A")
                    mi1.add(i1)
                    with open("tmp/Task10/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task10/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 10.2\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t10_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t10_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t10_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task10/3/task.png", "rb")
                    docc = open("tmp/Task10/3/10_3.docx", "rb")
                    bot.send_message(idd, f"Задание 10.3:\n<b>Задания для подготовки </b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docc, reply_markup=mi1)
                    docc.close()
                    phot.close()
                if call.data == "t10_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t10_3A)
                if call.data == "t10_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t10_3A")
                    mi1.add(i1)
                    with open("tmp/Task10/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task10/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 10.3\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t11_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t11_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t11_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task11/1/task.png", "rb")
                    bot.send_message(idd, f"Задание11.1:\n<b>Пароли с дополнительными сведениями</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t11_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t11_1A)
                if call.data == "t11_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t11_1A")
                    mi1.add(i1)
                    with open("tmp/Task11/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task11/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 11.1\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t11_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t11_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t11_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task11/2/task.png", "rb")
                    bot.send_message(idd, f"Задание11.2:\n<b>Разное</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t11_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t11_2A)
                if call.data == "t11_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t11_2A")
                    mi1.add(i1)
                    with open("tmp/Task11/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task11/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 11.2\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t11_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t11_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t11_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task11/3/task.png", "rb")
                    bot.send_message(idd, f"Задание11.3:\n<b>Номера спортсменов</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t11_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t11_3A)
                if call.data == "t11_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t11_3A")
                    mi1.add(i1)
                    with open("tmp/Task11/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task11/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 11.3\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t11_4":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t11_4A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t11_4R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task11/4/task.png", "rb")
                    bot.send_message(idd, f"Задание11.4:\n<b>Автомобильные номера</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t11_4A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t11_4A)
                if call.data == "t11_4R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t11_4A")
                    mi1.add(i1)
                    with open("tmp/Task11/4/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task11/4/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 11.4\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t11_5":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t11_A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t11_5R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task11/5/task.png", "rb")
                    bot.send_message(idd, f"Задание11.5:\n<b>Пароли</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t11_5A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t11_5A)
                if call.data == "t11_5R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t11_5A")
                    mi1.add(i1)
                    with open("tmp/Task11/5/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task11/5/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 11.5\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t12_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t12_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t12_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task12/1/task.png", "rb")
                    bot.send_message(idd, f"Задание12.1:\n<b>Исполнитель Редактор</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t12_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t12_1A)
                if call.data == "t12_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t12_1A")
                    mi1.add(i1)
                    with open("tmp/Task12/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task12/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 12.1\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t12_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t12_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t12_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task12/2/task.png", "rb")
                    bot.send_message(idd, f"Задание12.2:\n<b>Исполнитель Чертёжник</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t12_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t12_2A)
                if call.data == "t12_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t12_2A")
                    mi1.add(i1)
                    with open("tmp/Task12/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task12/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 12.2\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t12_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t12_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t12_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task12/3/task.png", "rb")
                    bot.send_message(idd, f"Задание12.3:\n<b>Остановка в заданной клетке, циклы с оператором ПОКА</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t12_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t12_3A)
                if call.data == "t12_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t12_3A")
                    mi1.add(i1)
                    with open("tmp/Task12/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task12/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 12.3\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t12_4":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t12_4A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t12_4R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task12/4/task.png", "rb")
                    bot.send_message(idd, f"Задание12.4:\n<b>Нестандартные задачи</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t12_4A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t12_4A)
                if call.data == "t12_4R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t12_4A")
                    mi1.add(i1)
                    with open("tmp/Task12/4/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task12/4/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 12.4\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t12_5":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t12_5A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t12_5R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task12/5/task.png", "rb")
                    bot.send_message(idd,
                                     f"Задание12.5:\n<b>Остановка в заданной клетке, циклы с операторами ПОКА и ЕСЛИ</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t12_5A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t12_5A)
                if call.data == "t12_5R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t12_5A")
                    mi1.add(i1)
                    with open("tmp/Task12/5/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task12/5/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 12.5\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t12_6":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t12_6A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t12_6R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task12/6/task.png", "rb")
                    bot.send_message(idd,
                                     f"Задание12.6:\n<b>Остановка в клетке, из которой начато движение</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t12_6A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t12_6A)
                if call.data == "t12_6R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t12_6A")
                    mi1.add(i1)
                    with open("tmp/Task12/6/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task12/6/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 12.6\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t13_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t13_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t13_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task13/1/task.png", "rb")
                    bot.send_message(idd, f"Задание13.1:\n<b>Подсчёт путей с избегаемой вершиной</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t13_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t13_1A)
                if call.data == "t13_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t13_1A")
                    mi1.add(i1)
                    with open("tmp/Task13/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task13/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 13.1\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t13_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t13_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t13_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task13/2/task.png", "rb")
                    bot.send_message(idd, f"Задание13.2:\n<b>Подсчёт путей с обязательной и избегаемой вершинами</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t13_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t13_2A)
                if call.data == "t13_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t13_2A")
                    mi1.add(i1)
                    with open("tmp/Task13/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task13/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 13.2\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t13_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t13_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t13_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task13/3/task.png", "rb")
                    bot.send_message(idd, f"Задание13.3:\n<b>Подсчёт путей</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t13_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t13_3A)
                if call.data == "t13_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t13_3A")
                    mi1.add(i1)
                    with open("tmp/Task13/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task13/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 13.3\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t13_4":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t13_4A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t13_4R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task13/4/task.png", "rb")
                    bot.send_message(idd, f"Задание13.4:\n<b>Подсчёт путей с обязательной вершиной</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t13_4A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t13_4A)
                if call.data == "t13_4R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t13_4A")
                    mi1.add(i1)
                    with open("tmp/Task13/4/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task13/4/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 13.4\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t14_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t14_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t14_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task14/1/task.png", "rb")
                    bot.send_message(idd, f"Задание14.1:\n<b>Разное</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t14_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t14_1A)
                if call.data == "t14_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t14_1A")
                    mi1.add(i1)
                    with open("tmp/Task14/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task14/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 14.1\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t14_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t14_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t14_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task14/2/task.png", "rb")
                    bot.send_message(idd, f"Задание14.2:\n<b>Прямое сложение в СС</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t14_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t14_2A)
                if call.data == "t14_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t14_2A")
                    mi1.add(i1)
                    with open("tmp/Task14/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task14/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 14.2\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t14_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t14_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t14_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task14/3/task.png", "rb")
                    bot.send_message(idd, f"Задание14.3:\n<b>Определение основания</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t14_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t14_3A)
                if call.data == "t14_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t14_3A")
                    mi1.add(i1)
                    with open("tmp/Task14/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task14/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 14.3\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t15_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t15_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t15_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task15/1/task.png", "rb")
                    bot.send_message(idd, f"Задание15.1:\n<b>Побитовая конъюнкция</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t15_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t15_1A)
                if call.data == "t15_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t15_1A")
                    mi1.add(i1)
                    with open("tmp/Task15/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task15/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 15.1\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t15_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t15_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t15_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task15/2/task.png", "rb")
                    bot.send_message(idd, f"Задание15.2:\n<b>Числовые отрезки</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t15_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t15_2A)
                if call.data == "t15_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t15_2A")
                    mi1.add(i1)
                    with open("tmp/Task15/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task15/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 15.2\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t15_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t15_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t15_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task15/3/task.png", "rb")
                    bot.send_message(idd, f"Задание15.3:\n<b>Дискретные множества</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t15_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t15_3A)
                if call.data == "t15_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t15_3A")
                    mi1.add(i1)
                    with open("tmp/Task15/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task15/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 15.3\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t15_4":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t15_4A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t15_4R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task15/4/task.png", "rb")
                    bot.send_message(idd, f"Задание15.4:\n<b>Координатная плоскость</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t15_4A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t15_4A)
                if call.data == "t15_4R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t15_4A")
                    mi1.add(i1)
                    with open("tmp/Task15/4/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task15/4/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 15.4\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t15_5":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t15_5A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t15_5R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task15/5/task.png", "rb")
                    bot.send_message(idd, f"Задание15.5:\n<b>Разное</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t15_5A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t15_5A)
                if call.data == "t15_5R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t15_5A")
                    mi1.add(i1)
                    with open("tmp/Task15/5/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task15/5/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 15.5\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t16_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t16_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t16_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task16/1/task.png", "rb")
                    bot.send_message(idd, f"Задание16.1:\n<b>Программы с двумя рекурсивными функциями с "
                                          f"возвращаемыми значениями</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t16_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t16_1A)
                if call.data == "t16_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t16_1A")
                    mi1.add(i1)
                    with open("tmp/Task16/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task16/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 16.1\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t16_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t16_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t16_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task16/2/task.png", "rb")
                    bot.send_message(idd,
                                     f"Задание16.2:\n<b>Программы с двумя рекурсивными функциями с текстовым выводом</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t16_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t16_2A)
                if call.data == "t16_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t16_2A")
                    mi1.add(i1)
                    with open("tmp/Task16/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task16/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 16.2\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t16_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t16_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t16_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task16/3/task.png", "rb")
                    bot.send_message(idd,
                                     f"Задание16.3:\n<b>Рекурсивные функции с возвращаемыми значениями</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t16_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t16_3A)
                if call.data == "t16_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t16_3A")
                    mi1.add(i1)
                    with open("tmp/Task16/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task16/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 16.3\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t16_4":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t16_4A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t16_4R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task16/4/task.png", "rb")
                    bot.send_message(idd,
                                     f"Задание16.4:\n<b>Алгоритмы, опирающиеся на несколько предыдущих значений</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t16_4A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t16_4A)
                if call.data == "t16_4R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t16_4A")
                    mi1.add(i1)
                    with open("tmp/Task16/4/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task16/4/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 16.4\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t16_5":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t16_5A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t16_5R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task16/5/task.png", "rb")
                    bot.send_message(idd,
                                     f"Задание16.5:\n<b>Рекурсивные функции с текстовым выводом</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t16_5A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t16_5A)
                if call.data == "t16_5R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t16_5A")
                    mi1.add(i1)
                    with open("tmp/Task16/5/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task16/5/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 16.5\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t16_6":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t16_6A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t16_6R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task16/6/task.png", "rb")
                    bot.send_message(idd,
                                     f"Задание16.6:\n<b>Алгоритмы, опирающиеся на одно предыдущее значение</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t16_6A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t16_6A)
                if call.data == "t16_6R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t16_6A")
                    mi1.add(i1)
                    with open("tmp/Task16/6/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task16/6/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 16.6\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t17_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t17_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t17_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task17/1/task.png", "rb")
                    docc = open("tmp/Task17/1/17_1.txt", 'rb')
                    bot.send_message(idd, f"Задание17.1:\n<b>Задания для подготовки 1</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docc, reply_markup=mi1)
                    phot.close()
                    docc.close()
                if call.data == "t17_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должны быть два целых числа, "
                                          "запишите их через пробел без лишних запятых и знаков. Например: 12312312 3232)")
                    bot.register_next_step_handler(tb, t17_1A)
                if call.data == "t17_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t17_1A")
                    mi1.add(i1)
                    with open("tmp/Task17/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task17/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 17.1\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t17_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t17_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t17_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task17/2/task.png", "rb")
                    docc = open("tmp/Task17/2/17_2.txt", 'rb')
                    bot.send_message(idd, f"Задание17.2:\n<b>Задания для подготовки 2</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docc, reply_markup=mi1)
                    phot.close()
                    docc.close()
                if call.data == "t17_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должны быть два целых числа, "
                                          "запишите их через пробел без лишних запятых и знаков. Например: 12312312 3232)")
                    bot.register_next_step_handler(tb, t17_2A)
                if call.data == "t17_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t17_2A")
                    mi1.add(i1)
                    with open("tmp/Task17/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task17/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 17.2\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t18_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t18_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t18_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task18/1/task.png", "rb")
                    docc = open("tmp/Task18/1/18_1.xlsx", "rb")
                    bot.send_message(idd, f"Задание18.1:\n<b>Задания для подготовки 1</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docc, reply_markup=mi1)
                    phot.close()
                if call.data == "t18_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t18_1A)
                if call.data == "t18_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t18_1A")
                    mi1.add(i1)
                    with open("tmp/Task18/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task18/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 18.1\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t18_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t18_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t18_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task18/2/task.png", "rb")
                    docc = open("tmp/Task18/2/18_2.xlsx", "rb")
                    bot.send_message(idd, f"Задание18.2:\n<b>Задания для подготовки 2</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docc, reply_markup=mi1)
                    phot.close()
                if call.data == "t18_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t18_2A)
                if call.data == "t18_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t18_2A")
                    mi1.add(i1)
                    with open("tmp/Task18/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task18/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 18.2\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t19_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t19_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t19_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task19/1/task.png", "rb")
                    bot.send_message(idd, f"Задание19.1:\n<b>Одна куча</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t19_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t19_1A)
                if call.data == "t19_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t19_1A")
                    mi1.add(i1)
                    with open("tmp/Task19/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task19/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 19.1\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t19_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t19_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t19_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task19/2/task.png", "rb")
                    bot.send_message(idd, f"Задание19.2:\n<b>Две кучи</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t19_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t19_2A)
                if call.data == "t19_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t19_2A")
                    mi1.add(i1)
                    with open("tmp/Task19/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task19/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 19.2\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t20_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t20_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t20_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task20/1/task.png", "rb")
                    bot.send_message(idd, f"Задание20.1:\n<b>Одна куча</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t20_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t20_1A)
                if call.data == "t20_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t20_1A")
                    mi1.add(i1)
                    with open("tmp/Task20/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task20/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 20.1\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t20_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t20_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t20_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task20/2/task.png", "rb")
                    bot.send_message(idd, f"Задание20.2:\n<b>Две кучи</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t20_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t20_2A)
                if call.data == "t20_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t20_2A")
                    mi1.add(i1)
                    with open("tmp/Task20/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task20/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 20.2\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t21_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t21_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t21_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task21/1/task.png", "rb")
                    bot.send_message(idd, f"Задание21.1:\n<b>Одна куча</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t21_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t21_1A)
                if call.data == "t21_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t21_1A")
                    mi1.add(i1)
                    with open("tmp/Task21/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task21/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 21.1\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t21_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t21_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t21_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task21/2/task.png", "rb")
                    bot.send_message(idd, f"Задание21.2:\n<b>Две кучи</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t21_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t21_2A)
                if call.data == "t21_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t21_2A")
                    mi1.add(i1)
                    with open("tmp/Task21/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task21/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 21.2\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t22_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t22_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t22_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task22/1/task.png", "rb")
                    bot.send_message(idd, f"Задание22.1:\n<b>Посимвольная обработка восьмеричных чисел</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t22_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t22_1A)
                if call.data == "t22_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t22_1A")
                    mi1.add(i1)
                    with open("tmp/Task22/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task22/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 22.1\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t22_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t22_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t22_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task22/2/task.png", "rb")
                    bot.send_message(idd, f"Задание22.2:\n<b>Посимвольная обработка чисел в разных СС</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t22_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t22_2A)
                if call.data == "t22_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t22_2A")
                    mi1.add(i1)
                    with open("tmp/Task22/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task22/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 22.2\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t22_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t22_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t22_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task22/3/task.png", "rb")
                    bot.send_message(idd, f"Задание22.3:\n<b>Разное</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t22_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t22_3A)
                if call.data == "t22_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t22_3A")
                    mi1.add(i1)
                    with open("tmp/Task22/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task22/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 22.3\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t22_4":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t22_4A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t22_4R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task22/4/task.png", "rb")
                    bot.send_message(idd, f"Задание22.4:\n<b>Посимвольная обработка десятичных чисел</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t22_4A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t22_4A)
                if call.data == "t22_4R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t22_4A")
                    mi1.add(i1)
                    with open("tmp/Task22/4/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task22/4/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 22.4\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t23_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t23_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t23_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task23/1/task.png", "rb")
                    bot.send_message(idd, f"Задание23.1:\n<b>Количество программ с обязательным этапом</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t23_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t23_1A)
                if call.data == "t23_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t23_1A")
                    mi1.add(i1)
                    with open("tmp/Task23/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task23/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 23.1\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t23_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t23_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t23_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task23/2/task.png", "rb")
                    bot.send_message(idd, f"Задание23.2:\n<b>Количество программ с избегаемым этапом</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t23_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t23_2A)
                if call.data == "t23_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t23_2A")
                    mi1.add(i1)
                    with open("tmp/Task23/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task23/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 23.2\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t23_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t23_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t23_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task23/3/task.png", "rb")
                    bot.send_message(idd,
                                     f"Задание23.3:\n<b>Количество программ с обязательным и избегаемым этапами</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t23_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t23_3A)
                if call.data == "t23_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t23_3A")
                    mi1.add(i1)
                    with open("tmp/Task23/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task23/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 23.3\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t23_4":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t23_4A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t23_4R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task23/4/task.png", "rb")
                    bot.send_message(idd,
                                     f"Задание23.4:\n<b>Поиск количества программ по заданному числу</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t23_4A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t23_4A)
                if call.data == "t23_4R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t23_4A")
                    mi1.add(i1)
                    with open("tmp/Task23/4/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task23/4/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 23.4\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t23_5":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t23_5A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t23_5R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task23/5/task.png", "rb")
                    bot.send_message(idd,
                                     f"Задание23.5:\n<b>Поиск количества чисел по заданному числу команд</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t23_5A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t23_5A)
                if call.data == "t23_5R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t23_5A")
                    mi1.add(i1)
                    with open("tmp/Task23/5/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task23/5/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 23.5\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t24_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t24_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t24_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task24/1/task.png", "rb")
                    docc = open("tmp/Task24/1/24_1.txt", 'rb')
                    bot.send_message(idd, f"Задание24.1:\n<b>Задания для подготовки 1</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docc, reply_markup=mi1)
                    phot.close()
                    docc.close()
                if call.data == "t24_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t24_1A)
                if call.data == "t24_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t24_1A")
                    mi1.add(i1)
                    with open("tmp/Task24/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task24/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 24.1\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t24_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t24_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t24_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task24/2/task.png", "rb")
                    docc = open("tmp/Task24/2/24_2.txt", 'rb')
                    bot.send_message(idd, f"Задание24.2:\n<b>Задания для подготовки 2</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docc, reply_markup=mi1)
                    phot.close()
                    docc.close()
                if call.data == "t24_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t24_2A)
                if call.data == "t24_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t24_2A")
                    mi1.add(i1)
                    with open("tmp/Task24/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task24/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 24.2\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t24_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t24_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t24_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task24/3/task.png", "rb")
                    docc = open("tmp/Task24/3/24_3.txt", 'rb')
                    bot.send_message(idd, f"Задание24.3:\n<b>Задания для подготовки 3</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docc, reply_markup=mi1)
                    phot.close()
                    docc.close()
                if call.data == "t24_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t24_3A)
                if call.data == "t24_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t24_3A")
                    mi1.add(i1)
                    with open("tmp/Task24/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task24/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 24.3\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t24_4":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t24_4A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t24_4R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task24/4/task.png", "rb")
                    docc = open("tmp/Task24/4/24_4.txt", 'rb')
                    bot.send_message(idd, f"Задание24.4:\n<b>Задания для подготовки 4</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docc, reply_markup=mi1)
                    phot.close()
                    docc.close()
                if call.data == "t24_4A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t24_4A)
                if call.data == "t24_4R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t24_4A")
                    mi1.add(i1)
                    with open("tmp/Task24/4/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task24/4/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 24.4\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t25_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t25_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t25_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task25/1/task.png", "rb")
                    bot.send_message(idd, f"Задание25.1:\n<b>Задания для подготовки 1</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t25_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть 8 пар целых чисел, "
                                          "запишите их через точку с запятой без лишних запятых и знаков. Например: 2 133;3 34534; 5 34234;...)")
                    bot.register_next_step_handler(tb, t25_1A)
                if call.data == "t25_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t25_1A")
                    mi1.add(i1)
                    with open("tmp/Task25/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task25/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 25.1\n<b>Ответ:</b> {';'.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t25_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t25_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t25_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task25/2/task.png", "rb")
                    bot.send_message(idd, f"Задание25.2:\n<b>Задания для подготовки 2</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t25_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть 6 пар целых чисел, "
                                          "запишите их через точку с запятой без лишних запятых и знаков. Например: 2 133;3 34534; 5 34234;...)")
                    bot.register_next_step_handler(tb, t25_2A)
                if call.data == "t25_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t25_2A")
                    mi1.add(i1)
                    with open("tmp/Task25/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task25/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 25.2\n<b>Ответ:</b> {';'.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t25_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t25_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t25_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task25/3/task.png", "rb")
                    bot.send_message(idd, f"Задание25.3:\n<b>Задания для подготовки 3</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t25_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть 3 списка по 4 целых чисел, "
                                          "запишите их через точку с запятой без лишних запятых и знаков. Например: 2 5 7 133;3 5 7 345;...)")
                    bot.register_next_step_handler(tb, t25_3A)
                if call.data == "t25_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t25_3A")
                    mi1.add(i1)
                    with open("tmp/Task25/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task25/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 25.3\n<b>Ответ:</b> {';'.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t25_4":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t25_4A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t25_4R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task25/4/task.png", "rb")
                    bot.send_message(idd, f"Задание25.4:\n<b>Задания для подготовки 4</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t25_4A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть 2 списка по 6 целых чисел, "
                                          "запишите их через точку с запятой без лишних запятых и знаков. Например: 2 3 5 7 11 13;3 5 7 11 345 2132)")
                    bot.register_next_step_handler(tb, t25_4A)
                if call.data == "t25_4R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t25_4A")
                    mi1.add(i1)
                    with open("tmp/Task25/4/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task25/4/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 25.4\n<b>Ответ:</b> {';'.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t26_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t26_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t26_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task26/1/task.png", "rb")
                    docc = open("tmp/Task26/1/26_1.txt", 'rb')
                    bot.send_message(idd, f"Задание26.1:\n<b>Задания для подготовки 1</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docc, reply_markup=mi1)
                    phot.close()
                    docc.close()
                if call.data == "t26_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должны быть два целых числа, "
                                          "запишите их через пробел без лишних запятых и знаков. Например: 132 322)")
                    bot.register_next_step_handler(tb, t26_1A)
                if call.data == "t26_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t26_1A")
                    mi1.add(i1)
                    with open("tmp/Task26/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task26/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 26.1\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t26_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t26_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t26_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task26/2/task.png", "rb")
                    docc = open("tmp/Task26/2/26_2.txt", 'rb')
                    bot.send_message(idd, f"Задание26.2:\n<b>Задания для подготовки 2</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docc, reply_markup=mi1)
                    phot.close()
                    docc.close()
                if call.data == "t26_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должны быть два целых числа, "
                                          "запишите их через пробел без лишних запятых и знаков. Например: 132 322)")
                    bot.register_next_step_handler(tb, t26_2A)
                if call.data == "t26_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t26_2A")
                    mi1.add(i1)
                    with open("tmp/Task26/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task26/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 26.2\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t26_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t26_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t26_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task26/3/task.png", "rb")
                    docc = open("tmp/Task26/3/26_3.txt", 'rb')
                    bot.send_message(idd, f"Задание26.3:\n<b>Задания для подготовки 3</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docc, reply_markup=mi1)
                    phot.close()
                    docc.close()
                if call.data == "t26_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должны быть два целых числа, "
                                          "запишите их через пробел без лишних запятых и знаков. Например: 132 322)")
                    bot.register_next_step_handler(tb, t26_3A)
                if call.data == "t26_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t26_3A")
                    mi1.add(i1)
                    with open("tmp/Task26/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task26/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 26.3\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t26_4":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t26_4A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t26_4R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task26/4/task.png", "rb")
                    docc = open("tmp/Task26/4/26_4.txt", 'rb')
                    bot.send_message(idd, f"Задание26.4:\n<b>Задания для подготовки 4</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docc, reply_markup=mi1)
                    phot.close()
                    docc.close()
                if call.data == "t26_4A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должны быть два целых числа, "
                                          "запишите их через пробел без лишних запятых и знаков. Например: 132 322)")
                    bot.register_next_step_handler(tb, t26_4A)
                if call.data == "t26_4R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t26_4A")
                    mi1.add(i1)
                    with open("tmp/Task26/4/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task26/4/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 26.4\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t27_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t27_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t27_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task27/1/task.png", "rb")
                    docA = open("tmp/Task27/1/27-1A.txt", 'rb')
                    docB = open("tmp/Task27/1/27-1B.txt", 'rb')
                    bot.send_message(idd, f"Задание27.1:\n<b>Задания для подготовки 1</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docA)
                    bot.send_document(idd, docB, reply_markup=mi1)
                    phot.close()
                    docA.close()
                    docB.close()
                if call.data == "t27_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должны быть два целых числа, "
                                          "запишите их через пробел без лишних запятых и знаков. Например: 132 322)")
                    bot.register_next_step_handler(tb, t27_1A)
                if call.data == "t27_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t27_1A")
                    mi1.add(i1)
                    with open("tmp/Task27/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task27/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 27.1\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t27_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t27_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t27_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task27/2/task.png", "rb")
                    docA = open("tmp/Task27/2/27-2A.txt", 'rb')
                    docB = open("tmp/Task27/2/27-2B.txt", 'rb')
                    bot.send_message(idd, f"Задание27.2:\n<b>Задания для подготовки 2</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot)
                    bot.send_document(idd, docA)
                    bot.send_document(idd, docB, reply_markup=mi1)
                    phot.close()
                    docA.close()
                    docB.close()
                if call.data == "t27_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должны быть два целых числа, "
                                          "запишите их через пробел без лишних запятых и знаков. Например: 132 322)")
                    bot.register_next_step_handler(tb, t27_2A)
                if call.data == "t27_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t27_2A")
                    mi1.add(i1)
                    with open("tmp/Task27/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task27/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 27.2\n<b>Ответ:</b> {' '.join(d)}",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
            else:
                bot.send_message(idd,
                                 f"<b><u>{call.message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий. /logIn",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(idd, f"Вы не можете приступить к заданиям без регистрации.\n"
                                  f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    # функция для шутки над пользователем
    @bot.message_handler(content_types='sticker')
    def fff(message):
        bot.send_sticker(message.chat.id, message.sticker.file_id)
        bot.send_message(message.chat.id, message.sticker.emoji)

    # функция для обработки неизвестных сообщений
    @bot.message_handler(content_types=['text', 'photo'])
    def tekst(message):
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

    bot.polling(none_stop=True)


if __name__ == '__main__':
    asyncio.run(main())
