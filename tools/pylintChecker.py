from pylint.lint import Run
from pylint.reporters.text import TextReporter

with open("tools/reports/pylintReport.txt", "w") as f:
    reporter = TextReporter(f)
    Run(["rps"], reporter=reporter, exit=False)
with open("tools/reports/pylintReport.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.replace("\n", ""))