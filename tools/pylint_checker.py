from pylint.lint import Run
from pylint.reporters.text import TextReporter

with open("tools/reports/pylintReport.txt", "w") as f:
    reporter = TextReporter(f)
    tracked_files = [
        "rps/game.py",
        "rps/player.py",
        "tests/manual_testing.py",
        "tests/test_beats.py",
        "tests/test_cards.py",
        "tests/test_stats.py",
        "tools/check_reqs.py",
        "tools/pylintChecker.py",
    ]

    Run(tracked_files, reporter=reporter, exit=False)
with open("tools/reports/pylintReport.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.replace("\n", ""))
