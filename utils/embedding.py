import openai


def embed(input):
    return (
        openai.embeddings.create(
            model="text-embedding-ada-002", input=input, encoding_format="float"
        )
        .data[0]
        .embedding
    )


def add_questions(questions):
    embedded_questions = []
    for q in questions:
        embedded_question = embed(q)
        embedded_questions.append({"embed": embedded_question, "question": q})
    return embedded_questions
