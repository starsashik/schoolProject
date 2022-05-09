import asyncio
import hashlib
import sqlite3

import telebot

TOKEN = '1633681368:AAEHBoqBKhg26ai_tPsw16qZJrgn-2tqFyU'
db_name = "tmp/TeleDB.db"

start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
start_markup.row("/login")
start_markup.row('/registration')
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
    dd = {i[0]: False for i in result}

    @bot.message_handler(commands=["start"])
    def start(message):
        mess = f"Привет, <b><u>{message.from_user.username}</u></b>, Я бот помощник для ЕГЭ по информатике.\nДля удобной работы со мной, лучше всего зарегистрироваться\n" \
               f"Если у вас уже есть аккаунт, то можете войти в него.\n" \
               f"Для лучшего понимания работы робота используйте функцию /help"
        bot.send_message(message.chat.id, mess, reply_markup=start_markup, parse_mode='html')

    @bot.message_handler(commands=['help'])
    def help(messagge):
        doc = open("tmp/info.txt", mode="rb")
        bot.send_document(messagge.chat.id, doc)
        doc.close()

    @bot.message_handler(commands=["registration"])
    def reg1(message):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""SELECT id FROM User"""
        result = cur.execute(command).fetchall()
        result = [i[0] for i in result]
        if int(message.from_user.id) in result:
            bot.send_message(message.chat.id, "Пользователь с вашем id уже зарегистрирован")
        else:
            tb = bot.send_message(message.chat.id, "Придумайте и отправьте пароль")
            bot.register_next_step_handler(tb, reg2)

    def reg2(message):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        passwords = "b" + message.text
        password = hashlib.md5(passwords.encode("utf8"))
        bot.delete_message(message.chat.id, message.message_id)
        command = f"""INSERT INTO User  VALUES(?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), message.from_user.username, password.hexdigest()))
        con.commit()
        bot.send_message(message.chat.id, f"Добро пожаловать, <b>{message.from_user.username}</b>!", parse_mode='html',
                         reply_markup=login_markup)
        dd[int(message.from_user.id)] = True

    @bot.message_handler(commands=["login"])
    def login(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                bot.send_message(message.chat.id, f"{message.from_user.username}, вы уже вошли в аккаунт",
                                 reply_markup=login_markup)
            else:
                dd[int(message.from_user.id)] = True
                bot.send_message(message.chat.id, f"{message.from_user.username}, вы успешно вошли в аккаунт",
                                 reply_markup=login_markup)
        except ValueError:
            bot.send_message(message.chat.id, f"Аккаунта с вашем логином не существуют.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=login_markup)

    @bot.message_handler(content_types=['text'])
    def info(message):
        bot.send_message(message.chat.id, message, parse_mode='html')

    bot.polling(none_stop=True)


if __name__ == '__main__':
    asyncio.run(main())
