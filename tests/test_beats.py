import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from rps.player import Player

import pytest


def test_beats_valid_card_rock():
    assert Player.beats("rock", "scissors") == True


def test_beats_valid_card_scissors():
    assert Player.beats("scissors", "paper") == True


def test_beats_valid_card_paper():
    assert Player.beats("paper", "rock") == True


def test_beats_valid_card_draw():
    assert Player.beats("paper", "paper") == False


def test_beats_invalid():
    expected_exception = KeyError
    with pytest.raises(expected_exception=expected_exception) as excInfo:
        Player.beats("not a rock", "rock")
    excInfo.value == expected_exception
