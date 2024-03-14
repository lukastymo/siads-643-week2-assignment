# SIADS-643 - Week 2 Assignment - Display Presidents Data

This project displays a list of presidents with their first names, last names, and birth dates.

## Setup

To set up the script, place the dataset inside the `datasets` folder and install the necessary requirements:

```bash
pip install -r requirements.txt
```

You can use the default CSV already there: `presidents.csv`.

## Running

Run the script with default parameters:

```bash
python main.py datasets/presidents.csv
```

To use non-standard columns or customize the title, see help:

```bash
python main.py -h
```

For example:

```bash
python main.py datasets/presidents.csv --title "My custom title"
```

## Script Functionality

- Loads a presidents file (currently, only CSV files are supported).
- Allows for a custom location for the CSV file.
- Enables specifying custom columns for the full name, target first name, target last name, and birth date.
- Supports customization of the title for the report presented in the console.
- The successful execution of the script will produce a report on the console with columns: First, Last, and Born for the presidents.
