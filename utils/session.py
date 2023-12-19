from cryptography.fernet import Fernet


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
