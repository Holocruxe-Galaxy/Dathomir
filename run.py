from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.main import main
from utils.question_data import question_data
from questions import questions

app = Flask(__name__)

# main.embed_and_write(questions)
questions_dataframe = question_data()
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
