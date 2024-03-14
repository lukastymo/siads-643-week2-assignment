from data_loader import load_csv_data
from preprocessor import preprocess_born_column, preprocess_president_column, select_first_last_born_columns
from display import display_data
import argparse


def get_file_path():
    """
    Parse the command line parameters to get the file path to the Presidents Data
    :return: Parsed `file_path` to the Presidents Data file
    """
    parser = argparse.ArgumentParser(description="Process Presidents Data")
    parser.add_argument('file_path', type=str, help='Path to the presidents.csv file')
    args = parser.parse_args()
    return args.file_path


def run():
    """
    Run the workflow to find a list of presidents data of birth
    """
    file_path = get_file_path()
    df = load_csv_data(file_path)
    df = preprocess_president_column(df)
    df = preprocess_born_column(df)
    df = select_first_last_born_columns(df)
    display_data(df, "List of Presidents by Date")


if __name__ == '__main__':
    run()
