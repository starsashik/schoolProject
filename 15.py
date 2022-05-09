import asyncio
import hashlib
import sqlite3

import telebot

TOKEN = '1633681368:AAEHBoqBKhg26ai_tPsw16qZJrgn-2tqFyU'
db_name = "tmp/TeleDB.db"

start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
start_markup.row("/logIn")
start_markup.row('/registration')
start_markup.row("/help")

login_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
login_markup.add("/1-5", "/6-10", "/11-15")
login_markup.add("/16-20", "/21-25", "/26-27")
login_markup.row('/profile', '/logOut')


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
        doc = open("tmp/info.txt", mode="rb")
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
                                 f"Всего выполнено: {str(round(sum(result[1:]) / 27 * 100))}%",
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

    @bot.message_handler(content_types='sticker')
    def fff(message):
        bot.send_sticker(message.chat.id, message.sticker.file_id)
        bot.send_message(message.chat.id, message.sticker.emoji)

    @bot.message_handler(content_types='photo')
    def ff(message):
        bot.send_message(message.chat.id, message)

    bot.polling(none_stop=True)


if __name__ == '__main__':
    asyncio.run(main())
