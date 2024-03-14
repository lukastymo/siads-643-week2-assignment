from data_loader import load_csv_data
from preprocessor import preprocess_born_column, preprocess_president_column, select_first_last_born_columns
from display import display_data

def run():
    """
    Run the workflow to find a list of presidents data of birth
    """
    file_path = 'datasets/presidents.csv'
    df = load_csv_data(file_path)
    df = preprocess_president_column(df)
    df = preprocess_born_column(df)
    df = select_first_last_born_columns(df)
    display_data(df, "List of Presidents by Date")


if __name__ == '__main__':
    run()
