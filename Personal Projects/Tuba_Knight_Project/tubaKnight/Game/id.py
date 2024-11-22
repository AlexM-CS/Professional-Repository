# Created: 11-21-2024
# Last updated: 11-21-2024
# Credits: Alexander Myska - Developer

# The ID class is the bedrock of this project. Using binary, we can
# universally use 16-bit values as IDs for everything from items to
# players.

# From left to right:
# Bit 4: isArea
# Bit 5: isAction
# Bit 6: isCharacter
# Bits 7-16: "Real ID"

# The "Real ID" is a 10-Bit number that represents the "real" ID-
# the previous bits are mostly meant to distinguish between different
# types of objects that will all use IDs.

class ID:

    # Instance variables:
    # int _ID - the ID of this object

    def __init__(self, _ID : int):
        self._ID = _ID