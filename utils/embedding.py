import openai


class Embedding:
    def __init__(self, api_key) -> None:
        openai.api_key = api_key

    @staticmethod
    def __embed(input):
        return (
            openai.embeddings.create(
                model="text-embedding-ada-002", input=input, encoding_format="float"
            )
            .data[0]
            .embedding
        )

    def add_questions(self, questions: list[str]):
        embedded_questions = []
        for q in questions:
            embedded_question = self.__embed(q)
            embedded_questions.append({"embed": embedded_question, "question": q})
        return embedded_questions
