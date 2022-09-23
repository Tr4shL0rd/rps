import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
import unittest
from rps.player import Player
from rps.player import CardClass
import pytest


class stats_testing(unittest.TestCase):
    def test_stats_valid_player(self):
        """
        control test for player class
        excepted str, int, list, int
        """
        p = Player.Stats(name="Hero", score=0, cards=CardClass.cards())
        self.assertEqual(
            (type(p.name), p.score, type(p.cards), len(p.cards)), (str, 0, list, 3)
        )

    def test_stats_invalid_name_type(self):
        """
        test for invalid name type
        expected str
             got int
        """
        expected_exception = TypeError
        with pytest.raises(expected_exception) as excInfo:
            Player.Stats(name=42, score=0, cards=CardClass.cards())
        excInfo == expected_exception

    def test_stats_invalid_score_type(self):
        """
        test for invalid score type
        expected int
             got str

        """
        expected_exception = TypeError
        with pytest.raises(expected_exception) as excInfo:
            Player.Stats(name="hero", score="hej", cards=CardClass.cards())
        excInfo == expected_exception

    def test_stats_invalid_cards_type(self):
        """
        test for invalid score type
        expected function
             got str

        """
        expected_exception = TypeError
        with pytest.raises(expected_exception) as excInfo:
            Player.Stats(name="Hero", score=0, cards="CardClass.Cards()")
        excInfo == expected_exception

    def test_stats_invalid_cards_function(self):
        """
        test for invalid function
        expected defined function
             got undefined str

        """
        expected_exception = NameError
        with pytest.raises(expected_exception) as excInfo:
            Player.Stats(name=42, score=0, cards=aCardClass.Cards())  # type: ignore (pyLance complains about undefind function name)
        excInfo == expected_exception

    def test_stats_invalid_cards_function_return(self):
        expected_exception = TypeError

        def wrong_cards():
            return "i swear i'm a stack of cards!"

        with pytest.raises(expected_exception) as excInfo:
            Player.Stats(name=42, score=0, cards=wrong_cards())
        excInfo == expected_exception
