from flask import request, jsonify, abort
from flask_cors import CORS
from app import app
from utils.main import main
from utils.exceptions import handleErrors
from utils.question_data import question_data
import threading
import time
from utils.telegram_bot import setup_telegram_bot

# main.embed_and_write(questions)
questions_dataframe = question_data()
collection = main.create_and_populate_collections(questions_dataframe)


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
 

def is_any_thread_alive(threads):
    return True in [t.is_alive() for t in threads]


# Función para ejecutar el servidor Flask en un hilo
def run_flask_server():
    app.run(host="0.0.0.0", port=8080, threaded=True)


#ésta funcion hace que flask y el bot se ejecuten el hilos separados xd
if __name__ == "__main__":
    telegram_thread = threading.Thread(target=lambda: setup_telegram_bot(collection, questions_dataframe), daemon=True)
    flask_thread = threading.Thread(target=run_flask_server, daemon=True)

    flask_thread.start()
    telegram_thread.start()
    while is_any_thread_alive([telegram_thread, flask_thread]):
        time.sleep(0)
