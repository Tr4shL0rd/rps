import os
import sys
import subprocess
command = ["python", "-m", "pylint", "$(git", "ls-files", "'*.py'", ")"]
if os.name == "nt":
    command.insert(0,"powershell.exe")
subprocess.call(command)