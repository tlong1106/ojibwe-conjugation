from conjugator.utils import styled_text
from .enum import Form, Pronoun, WordEndingVowel

PRONOUN_POSSESSIVE_PREFIX_MAP = {
    Pronoun.FIRST_SINGULAR_ANIMATE: {
        "b": ["im", "ni", "nim"],
        "d": ["in", "ni", "nin"],
        "g": ["in", "ni", "nin"],
        "j": ["in", "ni", "nin"],
        "z": ["in", "ni", "nin"],
        "m": "ni",
        "n": "ni",
        "w": "ni",
        "a": ["ind", "nid", "nind"],
        "i": ["ind", "nid", "nind"],
        "o": ["indo", "nido", "nindo"],
        "aa": ["ind", "nid", "nind"],
        "ii": ["ind", "nid", "nind"],
        "oo": ["ind", "nid", "nind"],
        "e": ["ind", "nid", "nind"]
    },
    Pronoun.FIRST_PLURAL_EXC_ANIMATE: {
        "b": ["im", "ni", "nim"],
        "d": ["in", "ni", "nin"],
        "g": ["in", "ni", "nin"],
        "j": ["in", "ni", "nin"],
        "z": ["in", "ni", "nin"],
        "m": "ni",
        "n": "ni",
        "w": "ni",
        "a": ["ind", "nid", "nind"],
        "i": ["ind", "nid", "nind"],
        "o": ["indo", "nido", "nindo"],
        "aa": ["ind", "nid", "nind"],
        "ii": ["ind", "nid", "nind"],
        "oo": ["ind", "nid", "nind"],
        "e": ["ind", "nid", "nind"]
    },
    Pronoun.SECOND_SINGULAR_ANIMATE: {
        "b": "gi",
        "d": "gi",
        "g": "gi",
        "j": "gi",
        "z": "gi",
        "m": "gi",
        "n": "gi",
        "w": "gi",
        "a": "gid",
        "i": "gid",
        "o": "gido",
        "aa": "gid",
        "ii": "gid",
        "oo": "gid",
        "e": "gid",
    },
    Pronoun.FIRST_PLURAL_INC_ANIMATE: {
        "b": "gi",
        "d": "gi",
        "g": "gi",
        "j": "gi",
        "z": "gi",
        "m": "gi",
        "n": "gi",
        "w": "gi",
        "a": "gid",
        "i": "gid",
        "o": "gido",
        "aa": "gid",
        "ii": "gid",
        "oo": "gid",
        "e": "gid",
    },
    Pronoun.SECOND_PLURAL_ANIMATE: {
        "b": "gi",
        "d": "gi",
        "g": "gi",
        "j": "gi",
        "z": "gi",
        "m": "gi",
        "n": "gi",
        "w": "gi",
        "a": "gid",
        "i": "gid",
        "o": "gido",
        "aa": "gid",
        "ii": "gid",
        "oo": "gid",
        "e": "gid",
    },
    Pronoun.THIRD_SINGULAR_ANIMATE: {
        "b": "o",
        "d": "o",
        "g": "o",
        "j": "o",
        "z": "o",
        "m": "o",
        "n": "o",
        "w": "o",
        "a": "od",
        "i": "od",
        "o": "odo",
        "aa": "od",
        "ii": "od",
        "oo": "od",
        "e": "od",
    },
    Pronoun.THIRD_PLURAL_ANIMATE: {
        "b": "o",
        "d": "o",
        "g": "o",
        "j": "o",
        "z": "o",
        "m": "o",
        "n": "o",
        "w": "o",
        "a": "od",
        "i": "od",
        "o": "odo",
        "aa": "od",
        "ii": "od",
        "oo": "od",
        "e": "od",
    }
}

def get_initial_letter(verb: str) -> str:
    pass

def handle_first_prefix():
    pass

def handle_second_prefix():
    pass

def handle_third_prefix():
    pass

def get_pronoun_prefix(verb_type: str, verb: str, form: str, neg: bool, pronoun: str, tense: str) -> str:
    if form in (Form.DEPENDENT_CLAUSE, Form.IMPERATIVE) or verb_type == "vii": return verb

    pronoun_prefix_map = PRONOUN_POSSESSIVE_PREFIX_MAP.get(pronoun, {})
    if tense == "present":
        initial = verb[:2] if verb[:2] in WordEndingVowel.LONG_VOWEL else verb[0]
    else:
        initial = verb[7]
    prefix = pronoun_prefix_map.get(initial)

    if pronoun in (Pronoun.FIRST_SINGULAR_ANIMATE, Pronoun.FIRST_PLURAL_EXC_ANIMATE) and isinstance(prefix, list):
        if form == Form.INDEPENDENT_CLAUSE and neg == False:
            multi_pronoun_prefix = [styled_text(p, "green_normal") + verb for p in prefix]
        elif form == Form.INDEPENDENT_CLAUSE and neg == True:
            multi_pronoun_prefix = [styled_text(p, "red_normal") + verb for p in prefix]
        return multi_pronoun_prefix
    elif pronoun in (Pronoun.FIRST_SINGULAR_ANIMATE, Pronoun.FIRST_PLURAL_EXC_ANIMATE):
        if form == Form.INDEPENDENT_CLAUSE and neg == False:
            return styled_text(prefix, "green_normal") + verb
        elif form == Form.INDEPENDENT_CLAUSE and neg == True:
            return styled_text(prefix, "red_normal") + verb
    
    if pronoun in (Pronoun.SECOND_SINGULAR_ANIMATE, Pronoun.SECOND_PLURAL_ANIMATE, Pronoun.FIRST_PLURAL_INC_ANIMATE):
        if form == Form.INDEPENDENT_CLAUSE and neg == False:
            return styled_text(prefix, "green_normal") + verb
        if form == Form.INDEPENDENT_CLAUSE and neg == True:
            return styled_text(prefix, "red_normal") + verb

    if pronoun in (Pronoun.THIRD_SINGULAR_ANIMATE, Pronoun.THIRD_PLURAL_ANIMATE) and verb_type == "vai":
        return verb
    elif pronoun in (Pronoun.THIRD_SINGULAR_ANIMATE, Pronoun.THIRD_PLURAL_ANIMATE) and verb_type in ("vti", "vta"):
        if form == Form.INDEPENDENT_CLAUSE and neg == False:
            return styled_text(prefix, "green_normal") + verb
        elif form == Form.INDEPENDENT_CLAUSE and neg == True:
            return styled_text(prefix, "red_normal") + verb

    raise ValueError(f"No valid prefix found for pronoun '{pronoun}' and verb '{verb}'")