# Created: 11-22-2024
# Last updated: 11-22-2024

# IO packages:

# Graphics packages:

# Built-in packages:

# External packages:

# Internal packages:

# The Stats class represents the Stats of a Character object.
# Stats are mainly used during damage calculations for Characters.
class Stats:

    # The HPS stat.
    hitpoints = None
    magicpoints = None
    strength = None
    dexterity = None
    magic = None
    defense = None
    speed = None
    critchance = None

    # Initializes a Stats object
    def __init__(self, hitpoints : int = 0x0000, magicpoints : int = 0x0000, strength : int = 0x0000, dexterity : int = 0x0000,
                 magic : int = 0x0000, defense : int = 0x0000, speed : int = 0x0000, critchance : int = 0x0000):
        self.hitpoints = hitpoints
        self.magicpoints = magicpoints
        self.strength = strength
        self.dexterity = dexterity
        self.magic = magic
        self.defense = defense
        self.speed = speed
        self.critchance = critchance

    # Used to re-create this Stats object
    def __repr__(self):
        HPS = "0x%04x" % self.hitpoints
        MPS = "0x%04x" % self.magicpoints
        STR = "0x%04x" % self.strength
        DEX = "0x%04x" % self.dexterity
        MGC = "0x%04x" % self.magic
        DFN = "0x%04x" % self.defense
        SPE = "0x%04x" % self.speed
        CRT = "0x%04x" % self.critchance

        return f"Stats_HPS:{HPS},MPS:{MPS},STR:{STR},DEX:{DEX},MGC:{MGC},DFN:{DFN},SPE:{SPE},CRT:{CRT}"