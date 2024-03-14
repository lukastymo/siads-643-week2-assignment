# SIADS-643 - Week 2 Assignment - Presents Presidents data

This project display list of presidents with their first name, last name, and born date columns.

## Set up

To set up the script install necessary requirements:

```bash
pip install -r requirments.txt
```

## Running

Run the script:

```bash
python main.py datasets/presidents.csv
```

To use non-standard columns or customize title see help:

```bash
python main.py -h
```

## Script functionality:

- Load a presidents file (we only support CSV file)
- We can provide custom location for the csv
- We can provide custom column with full name, target first name, target last name, born column
- Lastly, the script support customization for the title for the report presented on the console
- The successfully script will produce a report on the script with columns: First, Last and Born for presidents.
