from enum import Enum

class Form(str, Enum):
    INDEPENDENT_CLAUSE = "independent"
    DEPENDENT_CLAUSE = "dependent"
    IMPERATIVE = "imperative"

class Negation(str, Enum):
    AFFIRMATIVE = False
    NEGATIVE = True

class WordEndingVowel(tuple, Enum):
    VOWEL = ("a", "aa", "e", "i", "ii", "o", "oo")
    LONG_VOWEL = ("aa", "e", "ii", "oo")
    SHORT_VOWEL = ("a", "i", "o")

class WordEndingVII(str, Enum):
    D = "d"
    N = "n" ###
    D_N = "d_n"
    D_VOWEL = "d_vowel"

class WordEndingVAI(str, Enum):
    SHORT_LONG_VOWEL = "short_long_vowel" ### VOWEL
    AM = "am"
    N = "n" ###
    N_AM = "n_am"

class Pronoun(str, Enum):
    THIRD_SINGULAR_INANIMATE = "0s"
    THIRD_PLURAL_INANIMATE = "0p"
    THIRD_SINGULAR_INANIMATE_OBVIATE = "0's"
    THIRD_PLURAL_INANIMATE_OBVIATE = "0'p"
    FIRST_SINGULAR_ANIMATE = "1s"
    SECOND_SINGULAR_ANIMATE = "2s"
    THIRD_SINGULAR_ANIMATE = "3s"
    FIRST_PLURAL_EXC_ANIMATE = "1p"
    FIRST_PLURAL_INC_ANIMATE = "21"
    SECOND_PLURAL_ANIMATE = "2p"
    THIRD_PLURAL_ANIMATE = "3p"
