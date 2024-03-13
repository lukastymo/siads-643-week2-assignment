import pandas as pd


def load_csv_data(file_path):
    """
    Load data from a CSV file.

    :param file_path: The path to the CSV file
    :return: The loaded DataFrame
    """
    return pd.read_csv(file_path)