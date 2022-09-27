"""
module for testing cards
"""
import pytest
from rps.player import CardClass


def test_color_cards_valid_elements():
    """
    control test
    """
    assert CardClass.color_cards("rock, paper, scissors") == [
        "[grey37]rock[/grey37]",
        "[bright_white]paper[/bright_white]",
        "[bright_magenta]scissors[/bright_magenta]",
    ]


def test_color_cards_invalid_elements():
    """
    KeyError test for invalid card input
    """
    expected_exception = KeyError
    with pytest.raises(expected_exception=expected_exception) as exc_info:
        CardClass.color_cards("rock, notPaper, scissors")
    exc_info.value == expected_exception  # pylint: disable=pointless-statement


def test_color_cards_empty_elements():
    """
    KeyError test for invalid function arg
    """
    expected_exception = KeyError
    with pytest.raises(expected_exception=expected_exception) as exc_info:
        CardClass.color_cards("")
    exc_info.value == expected_exception  # pylint: disable=pointless-statement


def test_color_cards_no_elements():
    """
    KeyError test for not function arg
    """
    expected_exception = TypeError
    with pytest.raises(expected_exception=expected_exception) as exc_info:
        CardClass.color_cards()  # pylint: disable=no-value-for-parameter
    exc_info.value == expected_exception  # pylint: disable=pointless-statement
