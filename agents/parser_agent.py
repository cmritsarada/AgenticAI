import pandas as pd

def parse_statement(file):

    df = pd.read_csv(file)

    return df