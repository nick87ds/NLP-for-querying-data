import json

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


from Class_NLP_Query import BotAI

botAI = BotAI(db_file="data/db_esempio.csv")


with open('config.json') as config_file:
    config = json.load(config_file)

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""

    if botAI.check_model():
        try:        
            risposta = botAI.bot_reply(update.message.text)
            update.message.reply_text(risposta)
        except Exception as err:
            update.message.reply_text(err)
    else:
        update.message.reply_text("Il Bot non si è avviato")

def bot():
    """Start the bot."""

    updater = Updater(config['BOT-TOKEN'], use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    # dp.add_handler(MessageHandler(Filters.text | Filters.caption & ~Filters.command, echo))
    # dp.add_handler(CallbackQueryHandler(button))
    # dp.add_handler(MessageHandler(Filters.regex(r'(https:\/\/www[.A-Za-z0-9]+)'), start))
    # dp.add_handler(StringRegexHandler(r'(https:\/\/www[.A-Za-z0-9]+)', start))
    # dp.add_handler(MessageHandler(Filters.regex(r'^(hp[0-9]+)'), start))
    # dp.add_handler(StringRegexHandler(r'^(hp[0-9]+)', button))
    # dp.add_handler(MessageHandler(Filters.caption & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

# def main():
#     multiThreads = []

#     singleThread = threading.Thread(target=bot)
#     multiThreads.append(singleThread)
#     singleThread.start()

#     # singleThread = threading.Thread(target=scrapy_channel_post.stat_bot)
#     # multiThreads.append(singleThread)
#     # singleThread.start()

if __name__ == '__main__':
    bot()