"""
Preprocessing data, so they could be used by the further part of the program
"""
import pandas as pd
from pandas import Series


def preprocess_president_column(df: pd.DataFrame, president_col: str, target_first: str,
                                target_last: str) -> pd.DataFrame:
    """
    Preprocess a column by splitting it into <target_first> and <target_last> names,

    :param df: The DataFrame with <president_col> column.
    :param president_col: The column with the full name.
    :param target_first: The name of the column to store the first name.
    :param target_last: The name of the column to store the last name.
    :return: DataFrame with processed 'First' and 'Last' column, but without <president_col> column.
    """

    def split_name(row: Series) -> Series:
        row[target_first] = row[president_col].split(' ')[0]
        row[target_last] = row[president_col].split(' ')[-1]
        return row

    df = df.apply(split_name, axis='columns')
    del df[president_col]
    return df


def preprocess_born_column(df: pd.DataFrame, born_col: str) -> pd.DataFrame:
    """
    Extract and clean <born_col> column.

    :param df: The DataFrame with <born_col> column.
    :param born_col: column with date of birth
    :return: DataFrame with processed <born_col> column.
    """
    df[born_col] = df[born_col].str.extract(r'([\w]{3} [\w]{1,2}, [\w]{4})')
    return df


def select_first_last_born_columns(df: pd.DataFrame, target_first: str, target_last: str,
                                   born_col: str) -> pd.DataFrame:
    """
    Selects only first, last and born date columns

    :param df: Dataframe with first, last, and born
    :param target_first: target column where first name will be set
    :param target_last: target column where last name will be set
    :param born_col: column with date of birth
    :return: DataFrame with just these three columns
    """
    return df[[target_first, target_last, born_col]]
