# Created: 11-22-2024
# Last updated: 11-22-2024

# IO packages:

# Graphics packages:

# Built-in packages:

# External packages:

# Internal packages:
from . import Config
from . import PlayerData

# The TubaKnight class is what actually runs the game, and controls
# all the internal stuff going on.
class TubaKnight:

    # Specifies the version of the game being run
    version = None

    # The name of the selected player-character. Chosen by
    # the player upon launching the game.
    playerName = None

    # The save data of the selected player-character.
    playerData = None

    # Config option that shows additional info while playing
    debug = Config.debug

    # Config option that allows for commands to be used while playing
    commands_on = Config.commands_on

    # Initializes a game on TubaKnight
    def __init__(self, version):
        self.version = version
        self.playerName = None
        self.playerData = None

    # Gets the data for the currently selected character, and creates
    # new pd is the given player name is not recognized.
    # Before doing this, asks the player if they meant to create a new
    # character.
    def getPlayerData(self) -> PlayerData:
        pass

    # Runs the game
    def play(self):
        pass