"""
    This module keeps track of player stats and card decks
"""
from dataclasses import astuple, dataclass
from random import choice
from typing import Iterator
from enforce_typing import enforce_types




class Player:
    '''
        class that represents a Player
    '''
    def __init__(self) -> None:
        pass
    @classmethod
    def beats(cls,card1:str,card2:str) -> bool:
        """
        :param card1 str: Players card\n
        :param card2 str: Opponents  card\n
        :returns bool: True if card1 beats card2
        :raises KeyError: KeyError is raised when one of the cards are invalid
        """
        card1,card2 = card1.lower(),card2.lower()
        valid_cards = ["rock", "paper", "scissors"]
        if card1 not in valid_cards or card2 not in valid_cards:
            raise KeyError("card1 or card2 is not a valid card!")
        match (card1,card2):
            case ("rock","scissors"):
                return True
            case ("paper","rock"):
                return True
            case ("scissors","paper"):
                return True
            case _:
                return False
    def check_player_card(self,player_card:str) -> bool:
        """
            checks if player_card is a string
        """
        return isinstance(player_card,str)

    @enforce_types
    @dataclass
    class Stats:
        '''
            class that represents Player stats
        '''
        name:str
        cards:list[str,str,str]
        score:int = 0
        def __iter__(self) -> Iterator:
            '''
                enables iteration over each stat in the Player class
            '''
            return iter(astuple(self))


class CardClass:
    """
        class the represents a stack of cards
    """
    def __init__(self) -> None:
        pass
    @classmethod
    def cards(cls) -> list[str,str,str]:
        """
        :returns list: the list contains 3 cards of type str"
        """
        return [
                choice(["rock", "paper", "scissors"]),
                choice(["rock", "paper", "scissors"]),
                choice(["rock", "paper", "scissors"])
                ]
    @classmethod
    def color_cards(cls,cards:str) -> list:
        """
            :returns list: containing pretty displayable cards
        """
        colors = {
            "rock":     "[grey37]rock[/grey37]",
            "paper":    "[bright_white]paper[/bright_white]",
            "scissors": "[bright_magenta]scissors[/bright_magenta]"
        }
        pretty_cards = []
        for card in cards.split(", "):
            pretty_cards.append(colors[card])
        return pretty_cards
