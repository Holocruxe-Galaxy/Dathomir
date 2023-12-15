import asyncio
from http.client import responses
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from utils.embedding import Embedding
from utils.read_files import question_data
from questions import questions
from flask_cors import CORS

app = Flask(__name__)


class Main:
    def __init__(self, api_key, embedding_model) -> None:
        self.embedding = Embedding(api_key, embedding_model)

    def embed_and_write(self, inputs):
        questions = self.embedding.add_questions(inputs)
        self.embedding.write(questions)

    def create_and_populate_collections(self, dataframe):
        question_collection = self.embedding.create_collections("questions")
        self.embedding.populate_collection(question_collection, dataframe)
        return question_collection

    def query(self, collection, query, dataframe):
        df = self.embedding.query_collection(collection, query, 1, dataframe)
        json_response = self.embedding.format_json(df)
        if json_response["data"][0][0] > 0.425:
            return "Disculpa, no entendí la pregunta. Prueba reformularla."
        return json_response["data"][0][1]


def load_envs():
    load_dotenv()
    return [os.environ.get("OPENAI_API_KEY"), os.environ.get("EMBEDDING_MODEL")]


envs = load_envs()
questions_dataframe = question_data()
main = Main(envs[0], envs[1])
# main.embed_and_write(questions)
collection = main.create_and_populate_collections(questions_dataframe)


@app.route("/questions")
def answerQuestion():
    question = request.args.get("question")
    if not question:
        return jsonify({"Error": "La pregunta es obligatoria"}), 400
    else:
        response = main.query(collection, question, questions_dataframe)
        return jsonify({"response": response})


CORS(app, origins="*")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, threaded=True)
