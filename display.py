"""
Module for displaying dataframe
"""
import pandas as pd


def display_data(df: pd.DataFrame, title: str) -> None:
    """
    Display the dataframe in a formatted way.

    :param df: DataFrame small enough to fit on the screen.
    :param title: Title of the dataframe to be presented.
    """
    print("+===========================+")
    print(title)
    print("+===========================+")
    print(df)
