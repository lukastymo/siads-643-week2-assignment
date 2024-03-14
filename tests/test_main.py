"""
Test for main.py
"""
import sys
from unittest.mock import patch
from main import get_input_parameters


def test_get_input_parameters() -> None:
    """
    Test get input parameters
    """
    test_args = [
        "program_name",
        "path/to/dataset.csv",
        "--president_column", "President",
        "--born_column", "Born",
        "--target_first_column", "First",
        "--target_last_column", "Last",
        "--title", "Test Title"
    ]

    with patch.object(sys, 'argv', test_args):
        (file_path, president_col, born_col, target_first,
         target_last, title) = get_input_parameters()

    assert file_path == "path/to/dataset.csv"
    assert president_col == "President"
    assert born_col == "Born"
    assert target_first == "First"
    assert target_last == "Last"
    assert title == "Test Title"
