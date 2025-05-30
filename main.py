from flask import Flask
from threading import Thread
from telegram.ext import Updater, CommandHandler

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

TOKEN = "7983991903:AAFojMxjcDiAKGtJyG1qlegLyCUv37m5zDQ"

def start(update, context):
    update.message.reply_text("✅ Bot chal raha hai!")

def main():
    keep_alive()
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if _name_ == '_main_':
    main()
