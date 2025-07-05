# This file contains the core functionality of the program: the VII (Verb Inanimate Intransitive) conjugation logic.
# Implements all logic rules (suffixes, vowel handling, pronoun mapping).
# Takes in data (via models.py), applies logic, and returns results.
# Should be pure and testable — no printing, user interaction, or I/O.

from .models import ConjugationInput
from .utils import styled_text, get_style

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
            "d_vowel": {
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

def get_suffix(form: str, neg: bool, category: str, pronoun: str, key = None) -> str:
    if key:
        return PRONOUN_SUFFIX_MAP[form][neg][category].get(key, {}).get(pronoun, "")
    return PRONOUN_SUFFIX_MAP[form][neg][category].get(pronoun, "")

def ends_with_d_or_n(verb: str) -> bool:
    return verb.endswith(("d", "n"))

def ends_with_long_vowel(verb: str) -> bool:
    return verb.endswith(LONG_VOWELS)

def ends_with_short_vowel(verb: str) -> bool:
    return verb[:-1] in SHORT_VOWELS

def ends_with_vowel(verb: str) -> bool:
    return ends_with_long_vowel(verb) or ends_with_short_vowel(verb)

def ends_with_d_vowel(verb: str) -> bool:
    return verb.endswith("d") or ends_with_vowel(verb)

def ends_with_dummy_n(verb: str) -> bool:
    return verb in DUMMY_N["verbs"] or verb.endswith(tuple(DUMMY_N["roots"]))

def handle_independent(verb: str, neg: bool, pronoun: str) -> tuple[str, str]:
    
    base = verb
    suffix = ""
    
    if not neg:
        if ends_with_d_or_n(verb):
            suffix = get_suffix("independent", False, "d_n", pronoun)
        elif ends_with_long_vowel(verb):
            suffix = get_suffix("independent", False, "long_vowel", pronoun)
        elif ends_with_short_vowel(verb):
            suffix = get_suffix("independent", False, "short_vowel", pronoun)
        
    else:
        if ends_with_d_vowel(verb):
            if verb.endswith("d"):
                base = verb[:-1]
            suffix = get_suffix("independent", True, "d_vowel", pronoun)
        elif verb.endswith("n"):
            if ends_with_dummy_n(verb):
                base = verb[:-1]
                suffix = get_suffix("independent", True, "d_vowel", pronoun)
            else:
                suffix = get_suffix("independent", True, "n", pronoun)

    return base, suffix

def handle_dependent(verb: str, neg: str, pronoun: str) -> tuple[str, str]:
    
    base = verb
    suffix = ""

    if not neg:
        if verb.endswith("d") and pronoun in ("0s", "0p"):
            base = verb[:-1]
            suffix = get_suffix("dependent", False, "d_n", pronoun, key = "d")
        elif verb.endswith("n"):
            suffix = get_suffix("dependent", False, "d_n", pronoun, key = "n")
        elif ends_with_vowel(verb):
            suffix = get_suffix("dependent", False, "vowel", pronoun)
    else:
        if verb.endswith("d"):
            base = verb[:-1]
            suffix = get_suffix("dependent", True, "d_vowel", pronoun)
        elif verb.endswith("n"):
            if ends_with_dummy_n(verb):
                base = verb[:-1]
                suffix = get_suffix("dependent", True, "d_vowel", pronoun)
            else:
                suffix = get_suffix("dependent", True, "n", pronoun)
        elif ends_with_vowel(verb):
            suffix = get_suffix("dependent", True, "d_vowel", pronoun)

    return base, suffix

def get_vii_suffix(input_data: ConjugationInput) -> str:
    """
    Pure function that returns vii conjugation:
      form: independent, dependent
      negation: true, false
    """
    
    verb = input_data.verb
    form = input_data.form
    neg = input_data.negation
    pronoun = input_data.pronoun

    if form not in ("independent", "dependent"):
        return verb
    
    if form == "independent":
        base, suffix = handle_independent(verb, neg, pronoun)
    else:
        base, suffix = handle_dependent(verb, neg, pronoun)

    style = get_style(form, neg)

    return base + styled_text(suffix, style)