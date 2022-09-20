from player import Player
from player import Cards 

player = Player
opponent = Player

playerStats = Player.Stats(
            name="Hero", 
            score=0,
            cards=Cards()
            )
opponentStats = Player.Stats(
                name="Opponent",
                score=0,
                cards=Cards()
                )

print(f"Your Cards: {playerStats.cards}")

