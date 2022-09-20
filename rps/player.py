from dataclasses import astuple, dataclass


from enforce_typing import enforce_types
from random import choice
from typing import Iterator


class Player:
    '''
        class that represents a Player
    '''
    def __init__(self) -> None:
        pass
    def beats(card1:str,card2:str) -> bool:
        """
        :param card1 str: Players card\n
        :param card2 str: Opponents  card\n
        :returns bool: True if card1 beats card2
        :raises KeyError: KeyError is raised when one of the cards are invalid 
        """
        card1,card2 = card1.lower(),card2.lower() 
        validCards = ["rock", "paper", "scissors"]
        if card1 not in validCards or card2 not in validCards:
            raise KeyError(f"card1 or card2 is not a valid card!")
        match (card1,card2):
            case ("rock","scissors"):
                return True
            case ("paper","rock"):
                return True
            case ("scissors","paper"):
                return True
            case _:
                return False

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
        
    

def Cards() -> list[str,str,str]:
    """
    :returns list: the list contains 3 cards of type str"
    """
    return [
            choice(["rock", "paper", "scissors"]),
            choice(["rock", "paper", "scissors"]),
            choice(["rock", "paper", "scissors"])
            ]