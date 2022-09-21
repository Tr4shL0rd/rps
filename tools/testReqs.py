import os
from rich import print as rprint
try:
    # checks if file exists
    with open("requirements.txt", "r") as req:
        # runs pipreqs with --force flag and redirects to /dev/null
        oldLines = []
        lines = req.readlines()
        for line in lines:
            oldLines.append(line.replace("\n", ""))
        command = "pipreqs --force > /dev/null 2>&1"
        creationStatus = "Updated"
# if does not exist
except FileNotFoundError:
    # runs pipreqs and redirects to /dev/null
    command = "pipreqs > /dev/null 2>&1"
    creationStatus = "Created"
print(f"{creationStatus.replace('ed', 'ing')} requirements.txt...")
os.system(command)
# checks if file is empty 
if os.path.getsize("requirements.txt") <= 1:
    print("\nNot using any third party libraries\nDeleting requirements.txt...")
    # deletes if empty
    os.system("rm requirements.txt")
    exit()
print(f"{creationStatus} requirements.txt")
with open("requirements.txt", "r") as req:
    newLines = []
    lines = req.readlines()
    for line in lines:
        newLines.append(line.replace("\n", ""))
    olL = len(oldLines)
    nlL = len(newLines)
    newImports = newLines[olL:]
    prettyImports = ""
    for nI in newImports:
        if newImports.index(nI)-1 != newImports[len(newImports)-1]:
            prettyImports += f"{nI}, "
    prettyImports = prettyImports.removesuffix(", ")
    if len(prettyImports) <= 0:
        rprint("[red][underline]No New Imports[/underline][/red]")
        exit()
    rprint(f"new requirements: [underline]{prettyImports}[/underline]")
    choice = str(input("push to repo? [Y/n]: ").lower() or "y")
    if choice == "y":
        rprint("[green]running command: git add requirements.txt[/green]")
        os.system("git add requirements.txt")
        commitMessage = f"added {prettyImports} to requirements.txt"
        rprint(f"Your Commit: [green]{commitMessage}[/green]")
        choice = str(input("Do you want to change the commit message? [y/N]: ").lower() or "n")
        if choice == "y":
            print("Write Your Message")
            commitMessage = input("")
        rprint(f"[green]running command: git commit -m '{commitMessage}'[/green]")
        os.system(f"git commit -m '{commitMessage}'")
        rprint("[green]running command: git push[/green]")
        os.system("git push")
    else:
        exit()
