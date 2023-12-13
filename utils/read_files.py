import pandas as pd


def question_data():
    questions_df = pd.read_excel("./files/vectors.xlsx")
    print(questions_df)
