from dotenv import load_dotenv
import os
import openai

load_dotenv()
print(os.environ.get('USER'))


# Configura tu clave de API de OpenAI
openai.api_key = os.environ.get('API_KEY')

# Preguntas y respuestas
preguntas_respuestas = {
    "¿Cuál es tu nombre?": "Mi nombre es [TuNombre].",
    "¿Cuántos años tienes?": "Tengo [TuEdad] años."
}

# Entrenar el modelo con las preguntas y respuestas
for pregunta, respuesta in preguntas_respuestas.items():
    prompt = f"Pregunta: {pregunta}\nRespuesta: {respuesta}\n"
    openai.completions.create(
        model="text-embedding-ada-002",
        prompt=prompt,
        temperature=0,
        max_tokens=150
    )

# Consulta el modelo con una pregunta
def obtener_respuesta(pregunta):
    prompt = f"Pregunta: {pregunta}\nRespuesta:"
    response = openai.completions.create(
        model="text-embedding-ada-002",
        prompt=prompt,
        temperature=0,
        max_tokens=150
    )
    print(response)
    return response.choices[0].text.strip()

# Ejemplo de uso
nombre = obtener_respuesta("¿Cuál es tu nombre?")
edad = obtener_respuesta("¿Cuántos años tienes?")
