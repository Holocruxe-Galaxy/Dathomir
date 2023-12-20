from cryptography.fernet import Fernet
import random


class Session:
    def __init__(self) -> None:
        key = Fernet.generate_key()
        self.f = Fernet(key)

    def generate_token(self, response) -> str:
        encoded = response.encode()
        return self.f.encrypt(encoded).decode()

    def compare_tokens(self, req, res):
        if self.f.decrypt(req["token"]) == self.f.decrypt(res):
            return req["repeated"] + 1

    @staticmethod
    def give_response(responses=None):
        if responses:
            return responses[random.randint(0, len(responses) - 1)]
        return "Parece que no estoy pudiendo ayudarlo. Por favor comuníquese con atención al cliente"
