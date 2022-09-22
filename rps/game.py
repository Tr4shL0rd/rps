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
    gameDraws = Player.Stats(
                name="DRAWS",
                score=0,
                cards=CardClass.Cards()
                )
    gameRounds = Player.Stats(
                name="ROUNDS",
                score=1,
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
        if game.playerStats.score < 1 and game.opponentStats.score < 1 and game.gameDraws.score < 1: rprint(f"[blue]{Game.playerStats.name}[/blue] VS [red]{Game.opponentStats.name}[/red]")
        if game.gameRounds.score >= 10:
            rprint(f"[blue underline]{game.playerStats.name}'s[/blue underline] Score: {game.playerStats.score}")
            rprint(f"[red underline]{game.opponentStats.name}'s[/red underline] Score: {game.opponentStats.score}")
            rprint(f"{game.gameDraws.score} [yellow underline]{game.gameDraws.name}[/yellow underline]")
            if game.playerStats.score == 10:
                print("YOU WIN THE GAME!")
            elif game.opponentStats.score == 10:
                print("YOU LOSE THE GAME!")
            exit()
        else:
            print(game.gameRounds.score)
            rprint(f"Your Score: {game.playerStats.score}")
        cpuCard = game.opponentCard()
        cardDownBeat,cardDrawn = game.draw()
        if cardDrawn == cpuCard:
            rprint("[yellow][underline]DRAW[/underline][/yellow]")
            game.gameDraws.score += 1
            
        if cardDownBeat:
            game.playerStats.score += 1
            rprint("[green]WIN[/green]")
            rprint(f"[blue]{cardDrawn}[/blue] beats [red]{cpuCard}[/red]")
            print("You Win This Round!")
        elif not cardDownBeat and not cardDrawn == cpuCard :
            game.opponentStats.score += 1
            rprint("[red]LOSS[/red]")
            rprint(f"[red]{cpuCard}[/red] beats [blue]{cardDrawn}[/blue]")
            print("You Lost This Round!")
        if cardDownBeat or not cardDownBeat:
            game.gameRounds.score += 1

        print("")
        game.playerStats.cards = CardClass.Cards()
try:
    while True:
        gameLoop()
except KeyboardInterrupt:
    print("\nExiting...")