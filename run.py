from flask import request, jsonify, abort
from flask_cors import CORS
from app import app
from utils.main import main
from utils.exceptions import handleErrors
from utils.question_data import question_data
from questions import questions
import threading
import time
import telebot
import os
from dotenv import load_dotenv

# main.embed_and_write(questions)
questions_dataframe = question_data()
collection = main.create_and_populate_collections(questions_dataframe)

def load_envs():
    load_dotenv()
    return [os.environ.get("API_KEY_TELEGRAM")]


envs = load_envs()

@app.errorhandler(Exception)
def handle_generic_error(exception):
    error = handleErrors(exception)
    error_response = {
        "code": error.code,
        "name": error.name,
        "description": error.description,
    }
    return jsonify(error_response), error.code


@app.route("/questions", methods=["POST"])
def answerQuestion():
    try:
        question = request.args.get("question")
        req_json = request.get_json()

        if not question:
            abort(400, description="La pregunta es obligatoria")
        else:
            queried = main.query(collection, question, questions_dataframe)
            response = main.response_manager(req_json, queried)
            return jsonify(response)
    except ValueError as e:
        print(e)


CORS(app, origins="*")
 
TOKEN = envs[0]
bot = telebot.TeleBot(TOKEN)

# Manejador para el comando /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "¡Hola! Soy R2D2, el chatbot de Holocruxe. ¡Bienvenido estoy aquí para ayudarte!")

# Manejador para mensajes de texto
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # user_name = message.from_user.first_name
    # print(user_name)
    response = main.query(collection, message.text, questions_dataframe)
    bot.reply_to(message, response[0])


def is_any_thread_alive(threads):
    return True in [t.is_alive() for t in threads]


#Función para ejecutar el bot de Telegram en un hilo
def run_telegram_bot():
    bot.polling()
    

# Función para ejecutar el servidor Flask en un hilo
def run_flask_server():
    app.run(host="0.0.0.0", port=8080, threaded=True)


#ésta funcion hace que flask y el bot se ejecuten el hilos separados xd
if __name__ == "__main__":
    telegram_thread = threading.Thread(target=run_telegram_bot,daemon=True)
    flask_thread = threading.Thread(target=run_flask_server,daemon=True)

    telegram_thread.start()
    flask_thread.start()
    while is_any_thread_alive([telegram_thread,flask_thread]):
        time.sleep(0)