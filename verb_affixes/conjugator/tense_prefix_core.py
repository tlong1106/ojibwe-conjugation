from conjugator.utils import styled_text
from .enum import Pronoun, Tense

CONSONANT_SHIFT_MAP = {
    "zh": "sh",
    "b": "p",
    "d": "t",
    "g": "k",
    "j": "ch",
    "z": "s"
}

TENSE_PREFIX_MAP = {
    Tense.CONDITIONAL: "daa-",
    Tense.FUTURE_DEFINITIVE: ("da-", "ga-"),
    Tense.FUTURE_DESIDERATIVE: "wii-",
    Tense.PAST: "gii-"
}

def consonant_shift(verb: str, tense: str) -> str:
    if tense in (Tense.FUTURE_DESIDERATIVE, Tense.PAST):
        for tense_prefix in CONSONANT_SHIFT_MAP:
            if verb.startswith(tense_prefix):
                replacement = CONSONANT_SHIFT_MAP[tense_prefix]
                return replacement + verb[len(tense_prefix):]
    return verb

def handle_conditional(verb: str, pronoun: str, tense: str) -> str:
    return styled_text(TENSE_PREFIX_MAP[Tense.CONDITIONAL], "gray_normal") + consonant_shift(verb, tense)

def handle_future_definitive(verb: str, pronoun: str, tense: str) -> str:
    if pronoun in (Pronoun.THIRD_SINGULAR_ANIMATE, Pronoun.THIRD_PLURAL_ANIMATE):
        return styled_text(TENSE_PREFIX_MAP[Tense.FUTURE_DEFINITIVE][0], "gray_normal") + consonant_shift(verb, tense)
    else:
        return styled_text(TENSE_PREFIX_MAP[Tense.FUTURE_DEFINITIVE][1], "gray_normal") + consonant_shift(verb, tense)

def handle_future_desiderative(verb: str, pronoun: str, tense: str) -> str:
    return styled_text(TENSE_PREFIX_MAP[Tense.FUTURE_DESIDERATIVE], "gray_normal") + consonant_shift(verb, tense)

def handle_past(verb: str, pronoun: str, tense: str) -> str:
    return styled_text(TENSE_PREFIX_MAP[Tense.PAST], "gray_normal") + consonant_shift(verb, tense)

def get_tense_prefix(verb: str, pronoun: str, tense: str) -> str:
    if tense == Tense.PRESENT:
        return verb
    elif tense == Tense.CONDITIONAL:
        verb = handle_conditional(verb, pronoun, tense)
    elif tense == Tense.FUTURE_DEFINITIVE:
        verb = handle_future_definitive(verb, pronoun, tense)
    elif tense == Tense.FUTURE_DESIDERATIVE:
        verb = handle_future_desiderative(verb, pronoun, tense)
    elif tense == Tense.PAST:
        verb = handle_past(verb, pronoun, tense)

    return verb