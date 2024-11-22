# Created: 11-21-2024
# Last updated: 11-21-2024

# Built-in packages:

# External packages:

# Internal packages:

# The Style class affects how something gets displayed.
class Style:

    # str - the color of the background
    bg_color = None

    # str - the color of the text
    color = None

    # list[str] - styles for this text
    styles = None

    # Initializes the Style object with the given attributes
    def __init__(self, bg_color = "black", color = "white", styles = []):
        self.bg_color = bg_color
        self.color = color
        self.styles = styles

    # Returns a stylized version of the string
    def __repr__(self):
        thisStyle = ""
        for style in self.styles:
            thisStyle += f"{style}"
        return f"[{self.color} on {self.bg_color} {thisStyle}]"