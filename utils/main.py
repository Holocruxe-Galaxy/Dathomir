from utils.session import Session
from utils.embedding import Embedding


class Main:
    def __init__(self, api_key, embedding_model) -> None:
        self.embedding = Embedding(api_key, embedding_model)
        self.session = Session()

    def embed_and_write(self, inputs):
        questions = self.embedding.add_questions(inputs)
        self.embedding.write(questions)

    def create_and_populate_collections(self, dataframe):
        question_collection = self.embedding.create_collections("questions")
        self.embedding.populate_collection(question_collection, dataframe)
        return question_collection

    def query(self, collection, query, dataframe):
        df = self.embedding.query_collection(collection, query, 1, dataframe)
        json_response = self.embedding.format_json(df)
        if json_response["score"] > 0.355:
            return [self.embedding.give_response()]
        return json_response["response"]

    def response_manager(self, req, res):
        token = self.session.generate_token(res[0])
        response = self.session.give_response(res)
        if not req["token"]:
            return {"response": response, "repeated": 0, "token": token}
        repeated = self.session.compare_tokens(req, token)
        if repeated <= 2:
            return {"response": response, "repeated": repeated, "token": token}
        response = self.session.give_response()
        return {"response": response, "repeated": repeated, "token": token}
