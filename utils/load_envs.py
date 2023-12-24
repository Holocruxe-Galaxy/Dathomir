import os
from dotenv import load_dotenv


def load_envs():
    load_dotenv()
    return [os.environ.get("OPENAI_API_KEY"), os.environ.get("EMBEDDING_MODEL")]
