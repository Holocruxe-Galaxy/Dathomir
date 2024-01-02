import telebot
import os
from dotenv import load_dotenv
from utils.main import main


load_dotenv()

def load_envs():
    return [os.environ.get("API_KEY_TELEGRAM")]

envs = load_envs()
TOKEN = envs[0]

def setup_telegram_bot(collection, questions_dataframe ):
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def handle_start(message):
        bot.send_message(message.chat.id, "¡Hola! Soy R2D2, el chatbot de Holocruxe. ¡Bienvenido estoy aquí para ayudarte!")

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        response = main.query(collection, message.text, questions_dataframe)
        bot.reply_to(message, response[0])

    def run_telegram_bot():
        bot.polling()

    run_telegram_bot()
