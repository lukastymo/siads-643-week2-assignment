def preprocess_president_column(df, president_col, target_first, target_last):
    """
    Preprocess a column by splitting it into <target_first> and <target_last> names,

    :param df: The DataFrame with <president_col> column.
    :param president_col: The column with full name
    :return: DataFrame with processed 'First' and 'Last' column, but without 'President' column.
    """

    def split_name(row):
        row[target_first] = row[president_col].split(' ')[0]
        row[target_last] = row[president_col].split(' ')[-1]
        return row

    df = df.apply(split_name, axis='columns')
    del df[president_col]
    return df


def preprocess_born_column(df, born_col):
    """
    Extract and clean <born_col> column.

    :param df: The DataFrame with <born_col> column.
    :param born_col: column with date of birth
    :return: DataFrame with processed <born_col> column.
    """
    df[born_col] = df[born_col].str.extract(r'([\w]{3} [\w]{1,2}, [\w]{4})')
    return df


def select_first_last_born_columns(df, target_first, target_last, born_col):
    """
    Selects only first, last and born date columns
    :param df: Dataframe with first, last, and born
    :return: DAtaFrame with just these three columns
    """
    return df[[target_first, target_last, born_col]]
