"""
Tests for data_loader.py
"""
import os

from data_loader import load_csv_data


def test_load_csv_data() -> None:
    """
    Test loading of CSV data.
    """
    file_path = os.path.join(os.path.dirname(__file__), '..', 'datasets', 'test_presidents.csv')
    df = load_csv_data(file_path)

    assert not df.empty, "Loaded DataFrame should not be empty"
