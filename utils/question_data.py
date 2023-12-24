import pandas as pd
from ast import literal_eval


def question_data():
    # questions_df = pd.read_excel("./files/vectors.xlsx")
    questions_df = pd.read_csv("./files/vectors.csv", encoding="latin1")

    # Read vectors from strings back into a list
    questions_df["embed"] = questions_df.embed.apply(literal_eval)

    # # Set vector_id to be a string
    questions_df["vector_id"] = questions_df["vector_id"].apply(str)

    return questions_df
