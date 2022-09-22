from rps.player import CardClass
import pytest

def test_colorCards_valid_elements():
    assert CardClass.ColorCards("rock, paper, scissors") == ["[grey37]rock[/grey37]", "[bright_white]paper[/bright_white]","[bright_magenta]scissors[/bright_magenta]"]

def test_colorCards_invalid_elements():
    expected_exception = KeyError
    with pytest.raises(expected_exception=expected_exception) as excInfo:
        CardClass.ColorCards("rock, notPaper, scissors")
    excInfo.value == expected_exception

def test_colorCards_empty_elements():
    expected_exception = KeyError
    with pytest.raises(expected_exception=expected_exception) as excInfo:
        CardClass.ColorCards("")
    excInfo.value == expected_exception
def test_colorCards_no_elements():
    expected_exception = TypeError
    with pytest.raises(expected_exception=expected_exception) as excInfo:
        CardClass.ColorCards()
    excInfo.value == expected_exception