import openai
from dotenv import load_dotenv
import os
from utils.embedding import Embedding
from utils.read_files import question_data


def main():
    load_dotenv()
    openai.api_key = os.environ.get("OPENAI_API_KEY")


def embed(input):
    load_dotenv()
    embedding = Embedding(os.environ.get("OPENAI_API_KEY"))
    return embedding.add_questions(input)


questions = [
    "¿Cuál es el costo de asegurar mi envío?",
    "¿Cómo puedo verificar mi envío?",
    "¿Cómo puedo hacer el seguimiento de mi envío?",
]

main()
# print(embed(questions))
# question_data()
