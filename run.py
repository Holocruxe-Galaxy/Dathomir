import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from utils.main import Main
from utils.read_files import question_data
from questions import questions
from flask_cors import CORS

app = Flask(__name__)


def load_envs():
    load_dotenv()
    return [os.environ.get("OPENAI_API_KEY"), os.environ.get("EMBEDDING_MODEL")]


envs = load_envs()
questions_dataframe = question_data()
main = Main(envs[0], envs[1])
# main.embed_and_write(questions)
collection = main.create_and_populate_collections(questions_dataframe)


@app.route("/questions", methods=["POST"])
def answerQuestion():
    question = request.args.get("question")
    req_json = request.get_json()
    if not question:
        return jsonify({"Error": "La pregunta es obligatoria"}), 400
    else:
        queried = main.query(collection, question, questions_dataframe)
        response = main.response_manager(req_json, queried)
        return jsonify(response)


CORS(app, origins="*")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, threaded=True)
