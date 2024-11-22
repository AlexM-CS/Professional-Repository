# Created: 11-21-2024
# Last updated: 11-21-2024

# IO packages:
from ...IO.Inputs import enter_to_continue

# Graphics packages:
from .Style import Style

# Built-in packages:
from time import time_ns, time

# External packages:
from rich.console import Console

# The Text class is used to display text on the terminal.
class Text:

    # str - the text to write on the terminal
    contents = None

    # Style - the Style used when writing contents
    style = None

    # float - the speed used when displaying this text
    speed = None

    # Initializes the Text object with the given attributes
    def __init__(self, contents = "default", style = Style(), speed = 0):
        self.contents = contents
        self.style = style
        self.speed = speed

    # Displays this Text according to the contents and style
    def display(self, enter_prompt : bool = False):
        if (self.speed > 0):
            startTime = time()
            i = 0
            while (i < len(self.contents)):
                if ((time_ns() - startTime) > self.speed):
                    Console().print(f"{self.style}{self.contents[i]}", end = "")
                    i += 1
        else:
            Console().print(f"{self.style}{self.contents}")

        if (enter_prompt):
            enter_to_continue()
            pass


t = Text("test text", Style("red", "white", ["bold", "underline", "itallic"]))
t.display()