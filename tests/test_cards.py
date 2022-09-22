from rps.player import CardClass

def test_colorCards_valid():
    assert CardClass.ColorCards("rock, paper, scissors") == ["[grey37]rock[/grey37]", "[bright_white]paper[/bright_white]","[bright_magenta]scissors[/bright_magenta]"]