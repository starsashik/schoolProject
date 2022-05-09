# print(max(list(filter(lambda x: str(x)[-1] == "3", [int(input()) for x in range(int(input()))]))))
from random import randint

from telegram import ReplyKeyboardMarkup, replykeyboardremove
from telegram.ext import CommandHandler, ConversationHandler
from telegram.ext import Updater, MessageHandler, Filters


TOKEN = '1633681368:AAEHBoqBKhg26ai_tPsw16qZJrgn-2tqFyU'

start_keyboard = [['/dice', '/timer']]
start_markup = ReplyKeyboardMarkup(start_keyboard, one_time_keyboard=False)


def start(update, context):
    update.message.reply_text(
        "Я бот помощник для ЕГЭ по информатике.\nДля удобной работы со мной, лучше всего зарегистрироваться\n"
        "Если у вас уже есть аккаунт, то можете войти в него",
        reply_markup=start_markup
    )


def help(update, context):
    update.message.reply_text(
        "Я помогу тебе убить время",
        reply_markup=start_markup
    )

def proverka(update, context):
    update.message.reply_text(update.chat_id)



def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))




    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
