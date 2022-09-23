"""
    player module keeps track of game stats and player stats
"""
from random import choice
import sys
from player import Player
from player import CardClass
from rich import print as rprint


class Game:
    """
    tracks player, game and opponent.
    """

    def __init__(self) -> None:
        pass

    player = Player
    opponent = Player
    playerStats = player.Stats(name="Hero", score=0, cards=CardClass.cards())
    opponentStats = opponent.Stats(name="Opponent", score=0, cards=CardClass.cards())
    gameDraws = Player.Stats(name="TIE", score=0, cards=CardClass.cards())
    gameRounds = Player.Stats(name="ROUNDS", score=1, cards=CardClass.cards())


    """
        :return str: a string containing the card the opponent uses
    """
    def opponent_card(self) -> str:
        """
        Game.OpponentStats.cards is a list
        """
        return choice(Game.opponentStats.cards)

    def draw(self) -> tuple[bool, str]:
        """
        :return tuple[bool,str]:
        :bool: boolean if the player card beats the opponent card
        :str:  the card the player drew
        """
        Cards = CardClass
        card_stack = self.playerStats.cards
        pretty_cards = ", ".join(card_stack)
        rprint(f"Your Cards: {', '.join(Cards.color_cards(pretty_cards))}")
        draw_card = str(input("Draw A Card: ")).lower()
        if draw_card not in self.playerStats.cards:
            print(f"{draw_card} is not in your deck!")
            self.draw()
        return (Player.beats(card1=draw_card, card2=self.opponent_card()), draw_card)


def game_loop(running=True):
    """
    :param running bool: a boolean value dictation if the game is runnig
    :returns:
    """
    game = Game()
    while running:
        if game.gameRounds.score == 1:
            rprint(
                f"""
                    [blue]{Game.playerStats.name}[/blue] VS [red]{Game.opponentStats.name}[/red]
                    """
            )
        if game.gameRounds.score >= 10:
            rprint(
                f"""
                    [blue underline]{game.playerStats.name}'s[/blue underline]"
                    Score: {game.playerStats.score}
                    """
            )
            rprint(
                f"""
                [red underline]
                    {game.opponentStats.name}'s
                [/red underline] Score: {game.opponentStats.score}
                """
            )
            rprint(
                f"""
                    {game.gameDraws.score}
                    [yellow underline]{game.gameDraws.name}(S)[/yellow underline]
                """
            )
            if game.playerStats.score == 10:
                print("YOU WIN THE GAME!")
            elif game.opponentStats.score == 10:
                print("YOU LOSE THE GAME!")
            sys.exit()
        else:
            print(game.gameRounds.score)
            rprint(f"Your Score: {game.playerStats.score}")
        cpu_card = game.opponent_card()
        card_down_beat, card_drawn = game.draw()
        if card_drawn == cpu_card:
            rprint("[yellow underline]TIE[/yellow underline]")
            game.gameDraws.score += 1

        if card_down_beat:
            game.playerStats.score += 1
            rprint("[green]WIN[/green]")
            rprint(f"[blue]{card_drawn}[/blue] beats [red]{cpu_card}[/red]")
            print("You Win This Round!")
        elif not card_down_beat and not card_drawn == cpu_card:
            game.opponentStats.score += 1
            rprint("[red]LOSS[/red]")
            rprint(f"[red]{cpu_card}[/red] beats [blue]{card_drawn}[/blue]")
            print("You Lost This Round!")
        if card_down_beat or not card_down_beat:
            game.gameRounds.score += 1

        print("")
        game.playerStats.cards = CardClass.cards()


try:
    while True:
        game_loop()
except KeyboardInterrupt:
    print("\nExiting...")
