import pandas as pd

def load_data(filepath="datasets/computers.csv"):
    """Loads the dataset and returns a DataFrame"""
    return pd.read_csv(filepath)
