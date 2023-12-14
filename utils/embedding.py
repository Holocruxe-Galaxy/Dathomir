from ast import arguments
import openai
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
import pandas as pd
import json
# import xlsxwriter


class Embedding:
    def __init__(self, api_key, embedding_model) -> None:
        openai.api_key = api_key
        self.api_key = api_key
        self.embedding_model = embedding_model
        self.chroma_client = chromadb.EphemeralClient()

    def create_collections(self, name):
        embedding_function = OpenAIEmbeddingFunction(
            api_key=self.api_key, model_name=self.embedding_model
        )

        return self.chroma_client.create_collection(
            name=name, embedding_function=embedding_function
        )

    @staticmethod
    def populate_collection(collection, question_df):
        collection.add(
            ids=question_df.vector_id.values.tolist(),
            embeddings=question_df.embed.values.tolist(),
        )

    def __embed(self, input):
        return (
            openai.embeddings.create(
                model=self.embedding_model, input=input, encoding_format="float"
            )
            .data[0]
            .embedding
        )

    def add_questions(self, questions: list[str]):
        for q in questions:
            embedded_question = self.__embed(q["question"])
            q["embed"] = embedded_question
        return questions

    @staticmethod
    def __add_id_and_vector_id(questions):
        for index, q in enumerate(questions):
            q["id"] = index + 1
            q["vector_id"] = index
        return questions

    def write(self, questions):
        formatted_questions = self.__add_id_and_vector_id(questions)

        df = pd.DataFrame(formatted_questions)
        df.to_csv("files/vectors.csv", encoding="latin1", index=False)

    @staticmethod
    def query_collection(collection, query, max_results, dataframe):
        
        results = collection.query(
            query_texts=query, n_results=max_results, include=["distances"]
        )
        df = pd.DataFrame(
            {
                "response": dataframe[dataframe.vector_id.isin(results["ids"][0])][
                    "response"
                ],
            }
        )
 
        return df
    
    @staticmethod
    def format_json(df):
        json_dict = json.loads(df.to_json(force_ascii=False, orient='split'))
        return json_dict["data"][0][0]
  
        
        
    
        