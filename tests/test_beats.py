import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from rps.player import Player

import pytest

def test_beats_valid():
    assert Player.beats("rock", "scissors") == True