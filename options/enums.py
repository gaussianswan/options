from enum import Enum

class OptionExerciseType(Enum):

    AMERICAN = 1
    EUROPEAN = 2
    BERMUDAN = 3
    ASIAN = 4

class OptionClass(Enum):

    CALL = 1
    PUT = 2

class TradeSide(Enum):

    LONG = 1
    SHORT = -1