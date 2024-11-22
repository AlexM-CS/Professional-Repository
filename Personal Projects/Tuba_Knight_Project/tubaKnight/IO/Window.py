# Created: 11-21-2024
# Last updated: 11-21-2024

# Built-in packages:
import sys
from time import sleep

# External packages:
from rich.console import Console

# Internal packages:

# This file is used to create a Window to play the game on.

# Creates a console to be used to display the game
console = Console()

# Clears the display
def clear():
    console.clear()