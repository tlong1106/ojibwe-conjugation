# This file contains the core functionality of the program: the VII (Verb Inanimate Intransitive) conjugation logic.
# Implements all logic rules (suffixes, vowel handling, pronoun mapping).
# Takes in data (via models.py), applies logic, and returns results.
# Should be pure and testable — no printing, user interaction, or I/O.

from .models import ConjugationInput
from .utils import styled_text, get_style

SHORT_VOWELS = ("a", "i", "o")
LONG_VOWELS = ("aa", "ii", "oo", "e")
DUMMY_N = (
"agaasademon",
"akwamon",
"animamon",
"animipon",
"azhashkiiwaagamin",
"aazhawamon",
"aazhawaandawemon",
"aazhoomon",
"babaamipon",
"babigwaagamin",
"babiikwadamon",
"bagakaagamin",
"bagamipon",
"bakemon",
"bakobiimon",
"bakobiiyaabiigamon",
"bakwebiigamin",
"bangishimon",
"bazagwaagamin",
"baapaagadamon",
"baashkadaawangamon",
"bengopon",
"bimamon",
"bimaabiigamon",
"bimidewaagamin",
"bimipon",
"biijipon",
"biinaagamin",
"biindigepon",
"biinisaagamin",
"biisipon",
"biitewaagamin",
"biiwipon",
"boonipon",
"boozaagamin",
"dagon",
"dagwaagin",
"dakaagamin",
"dakigamin",
"dakipon",
"dakwamon",
"gibaakwadin",
"gibichipon",
"ginoomon",
"gizhaagamin",
"giiwitaamon",
"giizhowaagamin",
"giizhoogamin",
"gopamon",
"inamon",
"inaabiigamon",
"inaagamin",
"inigokwademon",
"ishkwaapon",
"ishpi-dagwaagin",
"izhipon",
"jiigeweyaazhagaamemon",
"jiikaagamin",
"madaabiimon",
"madaagamin",
"makadewaagamin",
"mamaangadepon",
"mamaangipon",
"mangademon",
"mashkawaagamin",
"maajipon",
"maanadamon",
"maanamon",
"maanaagamin",
"maazhimaagwaagamin",
"minwamon",
"minwaagamin",
"miskwaagamin",
"miskwiiwaagamin",
"mishkawaagamin",
"naazibiimon",
"nibiiwaagamin",
"ningwaagonemon",
"niingidoomon",
"niiskaajipon",
"nookaagamin",
"ogidaakiiwemon",
"onaagoshin",
"ondadamon",
"ondamon",
"onjipon",
"ozhaashadamon",
"ozhaashamon",
"ozhaawashkwaagamin",
"ozaawaagamin",
"washkadamon",
"waabishkaagamin",
"waakamin",
"wekwaamon",
"wiinaagamin",
"wiisagaagamin",
"wiishkobaagamin",
"zanagamon",
"ziiwiskaagamin",
"zoogipon",
"zhakipon",
"zhaagwaagamin",
"zhiiwaagamin",
"zhiiwitaaganaagamin"
)

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
    return verb.endswith(SHORT_VOWELS)

def ends_with_vowel(verb: str) -> bool:
    return ends_with_long_vowel(verb) or ends_with_short_vowel(verb)

def ends_with_d_vowel(verb: str) -> bool:
    return verb.endswith("d") or ends_with_vowel(verb)

def remove_final_letter(verb: str) -> str:
    return verb[:-1]

def handle_independent(verb: str, neg: bool, pronoun: str) -> tuple[str, str]:
    if not neg:
        return handle_independent_affirmative(verb, pronoun)
    else:
        return handle_independent_negative(verb, pronoun)

def handle_independent_affirmative(verb: str, pronoun: str) -> tuple[str, str]:
    if verb in DUMMY_N and pronoun == "0p":
        return remove_final_letter(verb), get_suffix("independent", False, "long_vowel", pronoun)
    elif ends_with_d_or_n(verb):
        return verb, get_suffix("independent", False, "d_n", pronoun)
    elif ends_with_long_vowel(verb):
        return verb, get_suffix("independent", False, "long_vowel", pronoun)
    elif ends_with_short_vowel(verb):
        return remove_final_letter(verb), get_suffix("independent", False, "short_vowel", pronoun)
    return verb, ""
    
def handle_independent_negative(verb: str, pronoun: str) -> tuple[str, str]:
    if verb.endswith("d") or verb in DUMMY_N:
        return remove_final_letter(verb), get_suffix("independent", True, "d_vowel", pronoun)
    elif verb.endswith("n"):
        return verb, get_suffix("independent", True, "n", pronoun)
    if ends_with_vowel(verb):
        return verb, get_suffix("independent", True, "d_vowel", pronoun)
    return verb, ""

def handle_dependent(verb: str, neg: str, pronoun: str) -> tuple[str, str]:
    if not neg:
        return handle_dependent_affirmative(verb, pronoun)
    else:
        return handle_dependent_negative(verb, pronoun)
    
def handle_dependent_affirmative(verb: str, pronoun: str) -> tuple[str, str]:
    if verb.endswith("d") and pronoun in ("0s", "0p"):
        return remove_final_letter(verb), get_suffix("dependent", False, "d_n", pronoun, key = "d")
    elif verb in DUMMY_N:
        return remove_final_letter(verb), get_suffix("dependent", False, "d_n", pronoun, key = "n")
    elif verb.endswith("n"):
        return verb, get_suffix("dependent", False, "d_n", pronoun, key = "n")
    elif ends_with_vowel(verb):
        return verb, get_suffix("dependent", False, "vowel", pronoun)
    return verb, ""
    
def handle_dependent_negative(verb: str, pronoun: str) -> tuple[str, str]:
    if verb.endswith("d") or verb in DUMMY_N:
        return remove_final_letter(verb), get_suffix("dependent", True, "d_vowel", pronoun)
    elif verb.endswith("n"):
        return verb, get_suffix("dependent", True, "n", pronoun)
    elif ends_with_vowel(verb):
        return verb, get_suffix("dependent", True, "d_vowel", pronoun)
    return verb, ""

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
        verb, suffix = handle_independent(verb, neg, pronoun)
    else:
        verb, suffix = handle_dependent(verb, neg, pronoun)

    style = get_style(form, neg)

    return verb + styled_text(suffix, style)