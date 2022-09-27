"""
module for testing beats
"""
import pytest
from rps.player import Player


def test_beats_valid_card_rock():
    """
    test for rock
    """
    assert Player.beats("rock", "scissors") is True


def test_beats_valid_card_scissors():
    """
    test for scissors
    """
    assert Player.beats("scissors", "paper") is True


def test_beats_valid_card_paper():
    """
    test for paper
    """
    assert Player.beats("paper", "rock") is True


def test_beats_valid_card_draw():
    """
    test for same draw
    """
    assert Player.beats("paper", "paper") is False


def test_beats_invalid():
    """
    test for invalid card
    """

    expected_exception = KeyError
    with pytest.raises(expected_exception=expected_exception) as exc_info:
        Player.beats("not a rock", "rock")
    exc_info.value == expected_exception  # pylint: disable=pointless-statement
