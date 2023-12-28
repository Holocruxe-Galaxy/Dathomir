from flask import abort
import cryptography


class Error:
    def __init__(self, code, name, description) -> None:
        self.code = code
        self.name = name
        self.description = description


def handleErrors(error):
    if type(error) == cryptography.fernet.InvalidToken:
        return Error(400, "Bad Request", description="El token es inválido")
    return error
