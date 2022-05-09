# Импортируем необходимые классы.
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import CommandHandler
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler

TOKEN = '1633681368:AAEHBoqBKhg26ai_tPsw16qZJrgn-2tqFyU'

reply_keyboard = [['/address', '/phone'],
                  ['/site'],
                  ['/set', '/unset']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def help(update, context):
    update.message.reply_text(
        "Я пока не умею помогать... Я только ваше эхо.")


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def start(update, context):
    update.message.reply_text(
        "Привет. Пройдите небольшой опрос, пожалуйста!\n"
        "Вы можете прервать опрос, послав команду /stop.\n"
        "В каком городе вы живёте?")

    # Число-ключ в словаре states —
    # втором параметре ConversationHandler'а.
    return 1
    # Оно указывает, что дальше на сообщения от этого пользователя
    # должен отвечать обработчик states[1].
    # До этого момента обработчиков текстовых сообщений
    # для этого пользователя не существовало,
    # поэтому текстовые сообщения игнорировались.


def first_response(update, context):
    # Сохраняем ответ в словаре.
    context.user_data['locality'] = update.message.text
    update.message.reply_text(
        "Какая погода в городе {0}?".format(context.user_data['locality']))
    return 2


# Добавили словарь user_data в параметры.
def second_response(update, context):
    weather = update.message.text
    # Используем user_data в ответе.
    update.message.reply_text("Спасибо за участие в опросе! Привет, {0}!".
                              format(context.user_data['locality']))
    return ConversationHandler.END


def stop(update, context):
    update.message.reply_text("Спасибо за участие в опросе! Всего доброго!")
    return ConversationHandler.END


def set_timer(update, context, delay):
    chat_id = update.message.chat_id
    """if 'job' in context.chat_data:
        old_job = context.chat_data['job']
        old_job.schedule_removal()"""
    new_job = context.job_queue.run_once(task30, delay, context=chat_id)
    context.chat_data['job'] = new_job
    update.message.reply_text(f'Засек {delay} секунд', reply_markup=close_markup)


def timer30(update, context):
    set_timer(update, context, 30)


def task30(context):
    job = context.job
    context.bot.send_message(job.context, text=f'30 секунд истекло', reply_markup=timer_markup)

def unset_timer(update, context):
    job = context.chat_data['job']
    job.schedule_removal()
    del context.chat_data['job']
    update.message.reply_text('Таймер сброшен', reply_markup=timer_markup)



def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("close", close_keyboard))




    dp.add_handler(CommandHandler("30c", timer30))
    dp.add_handler(CommandHandler("1m", timer60))
    dp.add_handler(CommandHandler("5m", timer300))

    dp.add_handler(CommandHandler("set", set_timer,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("close", unset_timer,
                                  pass_chat_data=True))


    conv_handler = ConversationHandler(
        # Без изменений
        entry_points=[CommandHandler('start', start)],

        states={
            # Добавили user_data для сохранения ответа.
            1: [MessageHandler(Filters.text, first_response, pass_user_data=True)],
            # ...и для его использования.
            2: [MessageHandler(Filters.text, second_response, pass_user_data=True)]
        },

        # Без изменений
        fallbacks=[CommandHandler('stop', stop)]
    )
    dp.add_handler(conv_handler)

    updater.start_polling()

    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
