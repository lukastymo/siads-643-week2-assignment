"""
Data Loader responsible for loading data from CSV files
"""
import pandas as pd


def load_csv_data(file_path: str) -> pd.DataFrame:
    """
    Load data from a CSV file.

    :param file_path: The path to the CSV file.
    :return: The loaded DataFrame.
    """
    return pd.read_csv(file_path)  # We only support CSV right now
