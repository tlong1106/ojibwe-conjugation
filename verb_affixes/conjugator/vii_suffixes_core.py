# This file contains the core functionality of the program: the VII (Verb Inanimate Intransitive) conjugation logic.
# Implements all logic rules (suffixes, vowel handling, pronoun mapping).
# Takes in data (via models.py), applies logic, and returns results.
# Should be pure and testable — no printing, user interaction, or I/O.

from .models import ConjugationInput
from .utils import styled_text

SHORT_VOWELS = ("a", "i", "o")
LONG_VOWELS = ("aa", "ii", "oo", "e")
CONSONANTS = ("d", "n")
DUMMY_N = {
    "verbs": ["zoogipon", "dagwaagin", "onaagoshin"],
    "roots": ("aagami",)
}

PRONOUN_SUFFIX_MAP = {
    "independent": {
        False: {
            "d_n": {
                "0s": "",
                "0's": "ini",
                "0p": "oon",
                "0'p": "iniwan"
            },
            "long_vowel": {
                "0s": "",
                "0's": "ni",
                "0p": "wan",
                "0'p": "niwan"
            },
            "short_vowel": {
                "0s": "",
                "0's": "ini",
                "0p": "oon",
                "0'p": "iniwan"
            }
        },
        True: {
            "n": {
                "0s": "zinoon",
                "0's": "zinini",
                "0p": "zinoon",
                "0'p": "zininiwan"
            },
            "d_long_vowel_short_vowel": {
                "0s": "sinoon",
                "0's": "sinini",
                "0p": "sinoon",
                "0'p": "sininiwan"
            }
        }
    },
    "dependent": {
        False: {
            "d_n": {
                "d": {
                    "0s": "k",
                    "0p": "k"
                },
                "n": {
                    "0s": "g",
                    "0p": "g",
                    "0's": "inig",
                    "0'p": "inig"
                }
            },
            "vowel": {
                "0s": "g",
                "0p": "g",
                "0's": "nig",
                "0'p": "nig"
            }
        },
        True: {
            "d_vowel": {
                "0s": "sinog",
                "0p": "sinog",
                "0's": "sininig",
                "0'p": "sininig"
            },
            "n": {
                "0s": "zinog",
                "0p": "zinog",
                "0's": "zininig",
                "0'p": "zininig"
            }
        }
    }
}

def get_vii_suffix(input_data: ConjugationInput) -> str:
    """
    Pure function that returns conjugated form of a verb
    """
    
    verb = input_data.verb
    form = input_data.form
    neg = input_data.negation
    pronoun = input_data.pronoun

    suffix = ""
    base = verb

    if form == "independent":
        if not neg:
            if verb.endswith(("d", "n")):
                suffix = PRONOUN_SUFFIX_MAP[form][neg]["d_n"].get(pronoun, "")
            elif verb.endswith(LONG_VOWELS):
                suffix = PRONOUN_SUFFIX_MAP[form][neg]["long_vowel"].get(pronoun, "")
            elif verb[-1] in SHORT_VOWELS:
                suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_vowel"].get(pronoun, "")
        else:
            if verb.endswith("n"):
                if verb in DUMMY_N["verbs"] or verb.endswith(DUMMY_N["roots"]):
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["d_long_vowel_short_vowel"].get(pronoun, "")
                else:
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n"].get(pronoun, "")
            elif verb.endswith("d") or verb.endswith(LONG_VOWELS) or verb[-1] in SHORT_VOWELS:
                if verb.endswith("d"):
                    base = verb[:-1]
                suffix = PRONOUN_SUFFIX_MAP[form][neg]["d_long_vowel_short_vowel"].get(pronoun, "")

    elif form == "dependent":
        if not neg:
            if verb.endswith("d"):
                if pronoun in ("0s", "0p"):
                    base = verb[:-1]
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["d_n"]["d"][pronoun]
            elif verb.endswith("n"):
                suffix = PRONOUN_SUFFIX_MAP[form][neg]["d_n"]["n"].get(pronoun, "")
            elif verb.endswith(LONG_VOWELS) or verb[-1] in SHORT_VOWELS:
                suffix = PRONOUN_SUFFIX_MAP[form][neg]["vowel"].get(pronoun, "")
        else:
            if verb.endswith("d"):
                base = verb[:-1]
                suffix = PRONOUN_SUFFIX_MAP[form][neg]["d_vowel"].get(pronoun, "")
            elif verb.endswith("n"):
                if verb in DUMMY_N["verbs"] or verb.endswith(DUMMY_N["roots"]):
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["d_vowel"].get(pronoun, "")
                else:
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n"].get(pronoun, "")
            elif verb.endswith(LONG_VOWELS) or verb[-1] in SHORT_VOWELS:
                suffix = PRONOUN_SUFFIX_MAP[form][neg]["d_vowel"].get(pronoun, "")

    if form == "independent" and neg == False:
        return base + styled_text(suffix, "green_normal")
    elif form == "independent" and neg == True:
        return base + styled_text(suffix, "red_normal")
    
    if form == "dependent" and neg == False:
        return base + styled_text(suffix, "green_italic")
    if form == "dependent" and neg == True:
        return base + styled_text(suffix, "red_italic")