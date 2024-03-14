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
    parser.add_argument('--president_column', type=str, default='President', nargs='?',
                        help='Column with president name')
    parser.add_argument('--born_column', type=str, default='Born', nargs='?', help='Column with president born date')
    parser.add_argument('--target_first_column', type=str, default='First', nargs='?',
                        help='Column with the target first name of a President')
    parser.add_argument('--target_last_column', type=str, default='Last', nargs='?',
                        help='Column with the target last name of a President')
    args = parser.parse_args()
    return args.file_path, args.president_column, args.born_column, args.target_first_column, args.target_last_column


def run():
    """
    Run the workflow to find a list of presidents data of birth
    """
    (file_path, president_col, born_col, target_first, target_last) = get_file_path()
    df = load_csv_data(file_path)
    df = preprocess_president_column(df, president_col, target_first, target_last)
    df = preprocess_born_column(df, born_col)
    df = select_first_last_born_columns(df, target_first, target_last, born_col)
    display_data(df, "List of Presidents by Date")


if __name__ == '__main__':
    run()
