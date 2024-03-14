"""
Tests for display.py
"""
from _pytest.capture import CaptureFixture
import pandas as pd
from display import display_data


def test_display_data(capsys: CaptureFixture) -> None:
    """
    Test the display_data function's ability to correctly format and print a DataFrame.

    Parameters:
    capsys: CaptureFixture - pytest fixture to capture print outputs

    Returns:
    None
    """
    data = {'Name': ['John Doe', 'Jane Doe'], 'Age': [30, 32]}
    df = pd.DataFrame(data)

    display_data(df, "Test DataFrame")
    captured = capsys.readouterr()

    assert "Test DataFrame" in captured.out
    assert "Name" in captured.out
    assert "Age" in captured.out
    assert "John Doe" in captured.out
    assert "Jane Doe" in captured.out
    assert "30" in captured.out
    assert "32" in captured.out
