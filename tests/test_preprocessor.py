"""
Tests for preprocessor.py
"""
import pandas as pd

from preprocessor import (preprocess_president_column, preprocess_born_column,
                          select_first_last_born_columns)


def test_preprocess_president_column() -> None:
    """
    Test loading CSV data
    """
    df = pd.DataFrame({
        'Dummy': [1, 2],  # Dummy column to test preservation of other data
        'President': ['George Washington', 'John Adams']
    })
    processed_df = preprocess_president_column(df, 'President', 'First', 'Last')

    expected_df = pd.DataFrame({
        'Dummy': [1, 2],
        'First': ['George', 'John'],
        'Last': ['Washington', 'Adams'],
    })

    pd.testing.assert_frame_equal(processed_df, expected_df)


def test_preprocess_born_column() -> None:
    """
    Test preprocessing
    """
    df = pd.DataFrame({
        'Born': ['Feb 22, 1732', 'Oct 30, 1735', 'Invalid Date']
    })
    processed_df = preprocess_born_column(df, 'Born')

    expected_df = pd.DataFrame({
        'Born': ['Feb 22, 1732', 'Oct 30, 1735', None]
    })

    pd.testing.assert_frame_equal(processed_df, expected_df)


def test_select_first_last_born_columns() -> None:
    """
    Test select first last born columns
    """
    df = pd.DataFrame({
        'First': ['George', 'John'],
        'Last': ['Washington', 'Adams'],
        'Born': ['Feb 22, 1732', 'Oct 30, 1735'],
        'Dummy': [1, 2]  # Dummy column to test it's removed
    })
    selected_df = select_first_last_born_columns(df, 'First', 'Last', 'Born')

    expected_df = pd.DataFrame({
        'First': ['George', 'John'],
        'Last': ['Washington', 'Adams'],
        'Born': ['Feb 22, 1732', 'Oct 30, 1735']
    })

    pd.testing.assert_frame_equal(selected_df, expected_df)
