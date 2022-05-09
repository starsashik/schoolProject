import asyncio
import hashlib
import sqlite3

import telebot

TOKEN = '1633681368:AAEHBoqBKhg26ai_tPsw16qZJrgn-2tqFyU'
db_name = "tmp/TeleDB.db"

start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
start_markup.row("/logIn")
start_markup.row('/registration')
start_markup.row('/logOut')
start_markup.row("/help")

login_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
login_markup.add("/1-5", "/6-10", "/11-15")
login_markup.add("/16-20", "/21-25", "/26-27")


async def main():
    bot = telebot.TeleBot(TOKEN)
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    command = f"""SELECT id FROM User"""
    result = cur.execute(command).fetchall()
    cur.close()
    dd = {i[0]: False for i in result}
    print(dd)

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
                con.commit()
                cur.close()
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

    @bot.message_handler(content_types=['text', 'photo', 'audio', 'voice', 'document', 'sticker', 'video', 'vidonote'])
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
            pass

    bot.polling(none_stop=True)


if __name__ == '__main__':
    asyncio.run(main())
