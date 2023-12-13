import openai
from dotenv import load_dotenv
import os
from utils.embedding import Embedding
from utils.read_files import question_data
from questions import questions

# def main():
#     load_dotenv()
#     openai.api_key = os.environ.get("OPENAI_API_KEY")


def embed_and_write(input):
    load_dotenv()
    embedding = Embedding(
        os.environ.get("OPENAI_API_KEY"), os.environ.get("EMBEDDING_MODEL")
    )
    question_collection = embedding.create_collections("questions")
    embedding.populate_collection(question_collection, input)
    # questions = embedding.add_questions(input)
    # embedding.write(questions)


# main()
# embed_and_write("embed_example")
# embed_testing(embedded_example)

embed_and_write(question_data())
