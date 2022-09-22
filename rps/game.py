from player import Player
from player import CardClass
from rich import print as rprint
from random import choice 

class Game: 
    def __init__(self) -> None:
        pass
    player   = Player
    opponent = Player

    playerStats = player.Stats(
                name="Hero", 
                score=0,
                cards=CardClass.Cards()
                )
    opponentStats = opponent.Stats(
                    name="Opponent",
                    score=0,
                    cards=CardClass.Cards()
                    )
    gameStats = Player.Stats(
                name="DRAWS",
                score=0,
                cards=CardClass.Cards()
                )
    def opponentCard(self):
        return choice(Game.opponentStats.cards) 
    def newPlayerCard(self):
        return 
    def draw(self) -> tuple[bool,str]:
        Cards = CardClass
        cardStack = self.playerStats.cards
        prettyCards = ", ".join(cardStack)
        rprint(f"Your Cards: {', '.join(Cards.ColorCards(prettyCards))}")
        drawCard = str(input("Draw A Card: ")).lower()
        if drawCard not in self.playerStats.cards:
            print(f"{drawCard} is not in your deck!")
            self.draw()
        return (Player.beats(drawCard, self.opponentCard()), drawCard)
    
def gameLoop(running=True):
    game = Game()
    while running:
        if game.playerStats.score < 1 and game.opponentStats.score < 1 and game.gameStats.score < 1: rprint(f"[blue]{Game.playerStats.name}[/blue] VS [red]{Game.opponentStats.name}[/red]")
        cpuCard = game.opponentCard()
        cardDownBeat,cardDrawn = game.draw()
        if cardDrawn == cpuCard:
            rprint("[yellow][underline]DRAW[/underline][/yellow]")
            game.gameStats.score += 1
            
        if cardDownBeat:
            game.playerStats.score += 1
            rprint(f"[blue]{cardDrawn}[/blue] beats [red]{cpuCard}[/red]")
            print("You Win This Round!")
        elif not cardDownBeat:
            game.opponentStats.score += 1
            rprint(f"[red]{cpuCard}[/red] beats [blue]{cardDrawn}[/blue]")
            print("You Lost This Round!")
        print("")
        print(f"Your Score: {game.playerStats.score}")
        game.playerStats.cards = CardClass.Cards()
try:
    while True:
        gameLoop()
except KeyboardInterrupt:
    print("\nExiting...")