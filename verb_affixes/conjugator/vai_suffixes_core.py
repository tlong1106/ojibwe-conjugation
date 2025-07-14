# This file contains the core functionality of the program: the VAI (Verb Animate Intransitive) conjugation logic.
# Implements all logic rules (suffixes, vowel handling, pronoun mapping).
# Takes in data (via models.py), applies logic, and returns results.
# Should be pure and testable — no printing, user interaction, or I/O.

from .models import ConjugationInput
from .utils import styled_text

SHORT_VOWELS = ("a", "i", "o")
LONG_VOWELS = ("aa", "ii", "oo", "e")
SINGLE_CONSONANTS = ("b", "d", "g", "h", "'", "j", "k", "m", "n", "p", "s", "t", "w", "y", "z")
DOUBLE_CONSONANTS = ("ch", "sh", "zh")

PRONOUN_SUFFIX_MAP = {
    "independent": {
        False: {
            "short_long_vowel": {
                "1s": "",
                "2s": "",
                "3s": "",
                "1p": "min",
                "21": "min",
                "2p": "m",
                "3p": "wag"
            },
            "n_am": {
                "1s": "",
                "2s": "",
                "3s": "",
                "1p": "min",
                "21": "min",
                "2p": "m",
                "3p": "oog"
            }
        },
        True: {
            "short_long_vowel": {
                "1s": "siin",
                "2s": "siin",
                "3s": "siin",
                "1p": "siimin",
                "21": "siimin",
                "2p": "siim",
                "3p": "siiwag"
            },
            "n_am": {
                "1s": "ziin",
                "2s": "ziin",
                "3s": "ziin",
                "1p": "ziimin",
                "21": "ziimin",
                "2p": "ziim",
                "3p": "ziiwag"
            }
        }
    },
    "dependent": {
        False: {
            "short_long_vowel": {
                "1s": "yaan",
                "2s": "yan",
                "3s": "d",
                "1p": "yaang",
                "21": "yang",
                "2p": "yeg",
                "3p": "waad"
            },
            "n_am": {
                "1s": "aan",
                "2s": "an",
                "3s": "g",
                "1p": "aang",
                "21": "ang",
                "2p": "eg",
                "3p": "owaad"
            }
        },
        True: {
            "short_long_vowel": {
                "1s": "siwaan",
                "2s": "siwan",
                "3s": "sig",
                "1p": "siwaang",
                "21": "siwang",
                "2p": "siweg",
                "3p": "sigwaa"
            },
            "n_am": {
                "1s": "ziwaan",
                "2s": "ziwan",
                "3s": "zig",
                "1p": "ziwaang",
                "21": "ziwang",
                "2p": "ziweg",
                "3p": "zigwaa"
            }
        }
    },
    "imperative": {
        False: {
            "short_long_vowel": {
                "2s": "n",
                "21": "daa",
                "2p": "k"
            },
            "n_am": {
                "2s": "in",
                "21": "daa",
                "2p": "ok"
            }
        },
        True: {
            "short_long_vowel": {
                "2s": "ken",
                "21": "siidaa",
                "2p": "kegon"
            },
            "n_am": {
                "2s": "gen",
                "21": "ziidaa",
                "2p": "gegon"
            }
        }
    }
}

def get_vai_suffix(input_data: ConjugationInput) -> str:

    verb = input_data.verb
    form = input_data.form
    neg = input_data.negation
    pronoun = input_data.pronoun

    suffix = ""
    base = verb

    # follow vii_suffixes_core.py and edit content below above this line

    if form == "independent":
        if not neg:
            if verb.endswith(SHORT_VOWELS) or verb.endswith(LONG_VOWELS):
                if pronoun in ("1s", "2s"):
                    if verb.endswith(SHORT_VOWELS) and not verb.endswith(LONG_VOWELS):
                        base = verb[:-1]
                        suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                    else:
                        suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "3s":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun in ("1p", "21"):
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "2p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "3p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
            elif verb.endswith(("n", "am")):
                if pronoun in ("1s", "2s", "3s"):
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun in ("1p", "21"):
                    if verb.endswith("n"):
                        base = verb + styled_text("i", "underline")
                        suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                    elif verb.endswith("am"):
                        base = verb[:-1] + styled_text("a", "underline")
                        suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun in ("2p"):
                    if verb.endswith("n"):
                        base = verb + styled_text("i", "underline")
                        suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                    elif verb.endswith("am"):
                        base = verb[:-1] + styled_text("a", "underline")
                        suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun in ("3p"):
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
        else:
            if verb.endswith(SHORT_VOWELS) or verb.endswith(LONG_VOWELS):
                if pronoun in ("1s", "2s", "3s"):
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun in ("1p", "21"):
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "2p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "3p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
            elif verb.endswith(("n", "am")):
                if verb.endswith("am"):
                    base = verb[:-1] + styled_text("n", "underline")
                if pronoun in ("1s", "2s", "3s"):
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun in ("1p", "21"):
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun == "2p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun == "3p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
    
    elif form == "dependent":
        if not neg:
            if verb.endswith(SHORT_VOWELS) or verb.endswith(LONG_VOWELS):
                if pronoun == "1s":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "2s":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "3s":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "1p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "21":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "2p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "3p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
            elif verb.endswith(("n","am")):
                if pronoun == "1s":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun == "2s":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun == "3s":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun == "1p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun == "21":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun == "2p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun == "3p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
        else:
            if verb.endswith(SHORT_VOWELS) or verb.endswith(LONG_VOWELS):
                if pronoun == "1s":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "2s":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "3s":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "1p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "21":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "2p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "3p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
            elif verb.endswith(("n","am")):
                if pronoun == "1s":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun == "2s":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun == "3s":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun == "1p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun == "21":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun == "2p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun == "3p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
    
    elif form == "imperative":
        if pronoun in ("1s", "3s", "1p", "3p"):
            base = ""
        if not neg:
            if verb.endswith(SHORT_VOWELS) or verb.endswith(LONG_VOWELS):
                if pronoun == "2s":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "21":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "2p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
            elif verb.endswith(("n","am")):
                if pronoun == "2s":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun == "21":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun == "2p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
        else:
            if verb.endswith(SHORT_VOWELS) or verb.endswith(LONG_VOWELS):
                if pronoun == "2s":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "21":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
                elif pronoun == "2p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["short_long_vowel"].get(pronoun, "")
            elif verb.endswith(("n","am")):
                if pronoun == "2s":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun == "21":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")
                elif pronoun == "2p":
                    suffix = PRONOUN_SUFFIX_MAP[form][neg]["n_am"].get(pronoun, "")

    if form == "independent" and neg == False:
        return base + styled_text(suffix, "green_normal")
    elif form == "independent" and neg == True:
        return base + styled_text(suffix, "red_normal")
    
    if form == "dependent" and neg == False:
        return base + styled_text(suffix, "green_italic")
    if form == "dependent" and neg == True:
        return base + styled_text(suffix, "red_italic")
    
    if form == "imperative" and neg == False:
        return base + styled_text(suffix, "green_bold")
    if form == "imperative" and neg == True:
        return base + styled_text(suffix, "red_bold")