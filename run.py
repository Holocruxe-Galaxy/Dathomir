import openai
from dotenv import load_dotenv
import os
from utils.embedding import add_questions


def main():
    load_dotenv()
    openai.api_key = os.environ.get("OPENAI_API_KEY")


questions = [
    "¿Cuál es el costo de asegurar mi envío?",
    "¿Cómo puedo verificar mi envío?",
    "¿Cómo puedo hacer el seguimiento de mi envío?",
]

main()
print(add_questions(questions))
