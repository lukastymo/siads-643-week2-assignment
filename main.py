from data_loader import load_csv_data


def run():
    """
    Run the workflow to find a list of presidents data of birth
    """
    file_path = 'datasets/presidents.csv'
    df = load_csv_data(file_path)
    print(df.head())


if __name__ == '__main__':
    run()
