# Created: 11-21-2024
# Last updated: 11-21-2024

# Built-in packages:

# External packages:
import maskpass

# Internal packages:
from . import Window

# This file keeps track of various inputs the user can perform while playing.

# Loops until an integer is input, then returns the parsed integer
def nextInt(text : str = "default", pre : int = None):
    while True:
        try:
            if (pre is None):
                num = int(input(text) + "\n")
            else:
                num = pre
            Window.clear()
            return num

        except ValueError:
            Window.clear()

# Returns a parsed string
def nextStr(text : str = "default", pre : str = None):
    if (pre is None):
        string = input(text + "\n")
    else:
        string = pre
    Window.clear()
    return string

# Allows the user to enter a string that gets masked
def password(ask : str):
    return maskpass.askpass(ask, mask="*")

# Waits until enter is pressed by the user
def enter_to_continue():
    input("Press Enter to continue...")
    Window.clear()