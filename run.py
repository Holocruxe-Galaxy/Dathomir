import openai
from dotenv import load_dotenv
import os
from utils.embedding import Embedding
from utils.read_files import question_data
from questions import questions


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
        return self.embedding.query_collection(collection, query, 1, dataframe)


def load_envs():
    load_dotenv()
    return [os.environ.get("OPENAI_API_KEY"), os.environ.get("EMBEDDING_MODEL")]


envs = load_envs()
questions_dataframe = question_data()
main = Main(envs[0], envs[1])
# main.embed_and_write(questions)
collection = main.create_and_populate_collections(questions_dataframe)
response = main.query(collection, "hasta donde llegan", questions_dataframe)
print(response)
