from dotenv import load_dotenv
import os
import openai

load_dotenv()
# Configura tu clave de API de OpenAI
openai.api_key = os.environ.get('API_KEY')


print(openai.models.list())