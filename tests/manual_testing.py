import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from rps.player import Player
from rps.player import Cards

def check_player_type():
    player = Player.Stats("hero", 0, Cards())
    print(type(player))
def check_player_garbage_name_error():
    p = Player.Stats(name=42, score=0, cards=Cards())
    print(p.name)
check_player_garbage_name_error()