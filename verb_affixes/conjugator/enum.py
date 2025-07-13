from enum import Enum

class Form(str, Enum):
    INDEPENDENT_CLAUSE = "independent"
    DEPENDENT_CLAUSE = "dependent"

class Negation(str, Enum):
    AFFIRMATIVE = False
    NEGATIVE = True

class WordEndingVowel(tuple, Enum):
    VOWEL = ("a", "aa", "e", "i", "ii", "o", "oo")
    LONG_VOWEL = ("aa", "e", "ii", "oo")
    SHORT_VOWEL = ("a", "i", "o")

class WordEndingVII(str, Enum):
    D = "d"
    N = "n"
    D_N = "d_n"
    D_VOWEL = "d_vowel"

class Pronoun(str, Enum):
    THIRD_SINGULAR_INANIMATE = "0s"
    THIRD_PLURAL_INANIMATE = "0p"
    THIRD_SINGULAR_INANIMATE_OBVIATE = "0's"
    THIRD_PLURAL_INANIMATE_OBVIATE = "0'p"
