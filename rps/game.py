from player import Player
from player import Cards 
from rich import print as rprint
from random import choice 

class Game: 
    def __init__(self) -> None:
        pass
    player   = Player
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
    def opponentCard(self):
        return choice(Game.opponentStats.cards) 
    def newPlayerCard(self):
        return 
    def draw(self) -> tuple[bool,str]:
        print("in draw()")
        print(f"Your Cards: {self.playerStats.cards}")
        drawCard = str(input("Draw A Card: ")).lower()
        if drawCard not in self.playerStats.cards:
            print(f"{drawCard} is not in your deck!")
        return (Player.beats(drawCard, self.opponentCard()), drawCard)
    
def gameLoop(running=True):
    print("in gameLoop()")
    game = Game()
    while running:
        cardDownBeat,cardDrawn = game.draw()
        if cardDownBeat:
            game.playerStats.score += 1
            game.opponentStats.score -= 1
            print(f"{cardDrawn} beats {game.opponentCard()}")
            print("you win this round!")
        elif not cardDownBeat:
            game.playerStats.score -= 1
            game.opponentStats.score += 1
        print(f"Your Score: {game.playerStats.score}")
        game.playerStats.cards = Cards()
        

while True:
    gameLoop()