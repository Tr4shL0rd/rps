"""
    checks the project for new imports and inserts them in the requirements.txt file
"""
import os
import sys
from rich import print as rprint

try:
    # checks if file exists
    with open("requirements.txt", "r", encoding="utf-8") as req:
        # runs pipreqs with --force flag and redirects to /dev/null
        old_lines = []
        lines = req.readlines()
        for line in lines:
            old_lines.append(line.replace("\n", ""))
        COMMAND = "pipreqs --force > /dev/null 2>&1"
        CREATION_STATUS = "Updated"
# if does not exist
except FileNotFoundError:
    # runs pipreqs and redirects to /dev/null
    COMMAND = "pipreqs > /dev/null 2>&1"
    CREATION_STATUS = "Created"
print(f"{CREATION_STATUS.replace('ed', 'ing')} requirements.txt...")
os.system(COMMAND)
# checks if file is empty
if os.path.getsize("requirements.txt") <= 1:
    print("\nNot using any third party libraries\nDeleting requirements.txt...")
    # deletes if empty
    os.system("rm requirements.txt")
    sys.exit()
print(f"{CREATION_STATUS} requirements.txt")
with open("requirements.txt", "r", encoding="utf-8") as req:
    new_lines = []
    lines = req.readlines()
    for line in lines:
        new_lines.append(line.replace("\n", ""))
    OLD_LINES_LENGTH = len(old_lines)
    NEW_LINE_LENGTH = len(new_lines)
    new_imports = new_lines[OLD_LINES_LENGTH:]
    PRETTY_IMPORTS = ""
    for new_import in new_imports:
        if new_imports.index(new_import) - 1 != new_imports[len(new_imports) - 1]:
            PRETTY_IMPORTS += f"{new_import}, "
    PRETTY_IMPORTS = PRETTY_IMPORTS.removesuffix(", ")
    if len(PRETTY_IMPORTS) <= 0:
        rprint("[red][underline]No New Imports[/underline][/red]")
        sys.exit()
    rprint(f"new requirements: [underline]{PRETTY_IMPORTS}[/underline]")
    CHOICE = str(input("push to repo? [Y/n]: ").lower() or "y")
    if CHOICE == "y":
        rprint("[green]running command: git add requirements.txt[/green]")
        os.system("git add requirements.txt")
        commit_message = f"added {PRETTY_IMPORTS} to requirements.txt"
        rprint(f"Your Commit: [green]{commit_message}[/green]")
        CHOICE = str(
            input("Do you want to change the commit message? [y/N]: ").lower() or "n"
        )
        if CHOICE == "y":
            print("Write Your Message")
            commit_message = input("")
        rprint(f"[green]running command: git commit -m '{commit_message}'[/green]")
        os.system(f"git commit -m '{commit_message}'")
        rprint("[green]running command: git push[/green]")
        os.system("git push")
    else:
        sys.exit()
