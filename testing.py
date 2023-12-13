from dotenv import load_dotenv
import os
import openai

load_dotenv()
print(os.environ.get("USER"))


# Configura tu clave de API de OpenAI
if os.getenv("OPENAI_API_KEY") is not None:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    print("OPENAI_API_KEY is ready")
else:
    print("OPENAI_API_KEY environment variable not found")

# Preguntas y respuestas
preguntas_respuestas = {
    "¿Cuál es tu nombre?": "Mi nombre es Panchita.",
    "¿Cuántos años tienes?": "Tengo 12 años.",
}

# Entrenar el modelo con las preguntas y respuestas
for pregunta, respuesta in preguntas_respuestas.items():
    prompt = f"Pregunta: {pregunta}\nRespuesta: {respuesta}\n"
    openai.Completion.create(
        model="text-embedding-ada-002", prompt=prompt, temperature=0, max_tokens=150
    )


# Consulta el modelo con una pregunta
def obtener_respuesta(pregunta):
    prompt = f"Pregunta: {pregunta}\nRespuesta:"
    response = openai.completions.create(
        model="text-embedding-ada-002", prompt=prompt, temperature=0, max_tokens=150
    )
    print(response)
    return response.choices[0].text.strip()


response = openai.embeddings.create(
    input="Your text string goes here", model="text-embedding-ada-002"
)
