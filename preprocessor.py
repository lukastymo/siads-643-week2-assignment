import pandas as pd


def preprocess_president_column(df):
    """
    Preprocess 'President' column by splitting it into 'First' and 'Last' names,

    :param df: The DataFrame with 'President' column.
    :return: DataFrame with processed 'First' and 'Last' column, but without 'President' column.
    """

    def split_name(row):
        row['First'] = row['President'].split(' ')[0]
        row['Last'] = row['President'].split(' ')[-1]
        return row

    df = df.apply(split_name, axis='columns')
    del df['President']
    return df


def preprocess_born_column(df):
    """
    Extract and clean 'Born' column.

    :param df: The DataFrame with 'Born' column.
    :return: DataFrame with processed 'Born' column.
    """
    df['Born'] = df['Born'].str.extract(r'([\w]{3} [\w]{1,2}, [\w]{4})')
    return df


def select_first_last_born_columns(df):
    """
    Selects only first, last and born date columns
    :param df: Dataframe with 'First', 'Last', 'Born' columns
    :return: DAtaFrame with just these three columns
    """
    return df[['First', 'Last', 'Born']]

