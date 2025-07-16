# This file contains the core functionality of the program: the VAI (Verb Animate Intransitive) conjugation logic.
# Implements all logic rules (suffixes, vowel handling, pronoun mapping).
# Takes in data (via models.py), applies logic, and returns results.
# Should be pure and testable — no printing, user interaction, or I/O.

from enum import Enum
from .enum import Form, Negation, Pronoun, WordEndingVowel, WordEndingVAI
from .models import ConjugationInput
from .utils import styled_text, get_style

# --- 1. Constants ---
VAI_SUFFIX_MAP = {
    Form.INDEPENDENT_CLAUSE: {
        Negation.AFFIRMATIVE: {
            WordEndingVAI.SHORT_LONG_VOWEL: {
                Pronoun.FIRST_SINGULAR_ANIMATE: "",
                Pronoun.SECOND_SINGULAR_ANIMATE: "",
                Pronoun.THIRD_SINGULAR_ANIMATE: "",
                Pronoun.FIRST_PLURAL_EXC_ANIMATE: "min",
                Pronoun.FIRST_PLURAL_INC_ANIMATE: "min",
                Pronoun.SECOND_PLURAL_ANIMATE: "m",
                Pronoun.THIRD_PLURAL_ANIMATE: "wag"
            },
           WordEndingVAI.N_AM: {
                Pronoun.FIRST_SINGULAR_ANIMATE: "",
                Pronoun.SECOND_SINGULAR_ANIMATE: "",
                Pronoun.THIRD_SINGULAR_ANIMATE: "",
                Pronoun.FIRST_PLURAL_EXC_ANIMATE: "min",
                Pronoun.FIRST_PLURAL_INC_ANIMATE: "min",
                Pronoun.SECOND_PLURAL_ANIMATE: "m",
                Pronoun.THIRD_PLURAL_ANIMATE: "oog"
            }
        },
        Negation.NEGATIVE: {
            WordEndingVAI.SHORT_LONG_VOWEL: {
                Pronoun.FIRST_SINGULAR_ANIMATE: "siin",
                Pronoun.SECOND_SINGULAR_ANIMATE: "siin",
                Pronoun.THIRD_SINGULAR_ANIMATE: "siin",
                Pronoun.FIRST_PLURAL_EXC_ANIMATE: "siimin",
                Pronoun.FIRST_PLURAL_INC_ANIMATE: "siimin",
                Pronoun.SECOND_PLURAL_ANIMATE: "siim",
                Pronoun.THIRD_PLURAL_ANIMATE: "siiwag"
            },
           WordEndingVAI.N_AM: {
                Pronoun.FIRST_SINGULAR_ANIMATE: "ziin",
                Pronoun.SECOND_SINGULAR_ANIMATE: "ziin",
                Pronoun.THIRD_SINGULAR_ANIMATE: "ziin",
                Pronoun.FIRST_PLURAL_EXC_ANIMATE: "ziimin",
                Pronoun.FIRST_PLURAL_INC_ANIMATE: "ziimin",
                Pronoun.SECOND_PLURAL_ANIMATE: "ziim",
                Pronoun.THIRD_PLURAL_ANIMATE: "ziiwag"
            }
        }
    },
    Form.DEPENDENT_CLAUSE: {
        Negation.AFFIRMATIVE: {
            WordEndingVAI.SHORT_LONG_VOWEL: {
                Pronoun.FIRST_SINGULAR_ANIMATE: "yaan",
                Pronoun.SECOND_SINGULAR_ANIMATE: "yan",
                Pronoun.THIRD_SINGULAR_ANIMATE: "d",
                Pronoun.FIRST_PLURAL_EXC_ANIMATE: "yaang",
                Pronoun.FIRST_PLURAL_INC_ANIMATE: "yang",
                Pronoun.SECOND_PLURAL_ANIMATE: "yeg",
                Pronoun.THIRD_PLURAL_ANIMATE: "waad"
            },
           WordEndingVAI.N_AM: {
                Pronoun.FIRST_SINGULAR_ANIMATE: "aan",
                Pronoun.SECOND_SINGULAR_ANIMATE: "an",
                Pronoun.THIRD_SINGULAR_ANIMATE: "g",
                Pronoun.FIRST_PLURAL_EXC_ANIMATE: "aang",
                Pronoun.FIRST_PLURAL_INC_ANIMATE: "ang",
                Pronoun.SECOND_PLURAL_ANIMATE: "eg",
                Pronoun.THIRD_PLURAL_ANIMATE: "owaad"
            }
        },
        Negation.NEGATIVE: {
            WordEndingVAI.SHORT_LONG_VOWEL: {
                Pronoun.FIRST_SINGULAR_ANIMATE: "siwaan",
                Pronoun.SECOND_SINGULAR_ANIMATE: "siwan",
                Pronoun.THIRD_SINGULAR_ANIMATE: "sig",
                Pronoun.FIRST_PLURAL_EXC_ANIMATE: "siwaang",
                Pronoun.FIRST_PLURAL_INC_ANIMATE: "siwang",
                Pronoun.SECOND_PLURAL_ANIMATE: "siweg",
                Pronoun.THIRD_PLURAL_ANIMATE: "sigwaa"
            },
           WordEndingVAI.N_AM: {
                Pronoun.FIRST_SINGULAR_ANIMATE: "ziwaan",
                Pronoun.SECOND_SINGULAR_ANIMATE: "ziwan",
                Pronoun.THIRD_SINGULAR_ANIMATE: "zig",
                Pronoun.FIRST_PLURAL_EXC_ANIMATE: "ziwaang",
                Pronoun.FIRST_PLURAL_INC_ANIMATE: "ziwang",
                Pronoun.SECOND_PLURAL_ANIMATE: "ziweg",
                Pronoun.THIRD_PLURAL_ANIMATE: "zigwaa"
            }
        }
    },
    Form.IMPERATIVE: {
        Negation.AFFIRMATIVE: {
            WordEndingVAI.SHORT_LONG_VOWEL: {
                Pronoun.SECOND_SINGULAR_ANIMATE: "n",
                Pronoun.FIRST_PLURAL_INC_ANIMATE: "daa",
                Pronoun.SECOND_PLURAL_ANIMATE: "k"
            },
           WordEndingVAI.N_AM: {
                Pronoun.SECOND_SINGULAR_ANIMATE: "in",
                Pronoun.FIRST_PLURAL_INC_ANIMATE: "daa",
                Pronoun.SECOND_PLURAL_ANIMATE: "ok"
            }
        },
        Negation.NEGATIVE: {
            WordEndingVAI.SHORT_LONG_VOWEL: {
                Pronoun.SECOND_SINGULAR_ANIMATE: "ken",
                Pronoun.FIRST_PLURAL_INC_ANIMATE: "siidaa",
                Pronoun.SECOND_PLURAL_ANIMATE: "kegon"
            },
           WordEndingVAI.N_AM: {
                Pronoun.SECOND_SINGULAR_ANIMATE: "gen",
                Pronoun.FIRST_PLURAL_INC_ANIMATE: "ziidaa",
                Pronoun.SECOND_PLURAL_ANIMATE: "gegon"
            }
        }
    }
}

# --- 2. Helpers ---
def get_suffix(form: str | Enum, neg: bool | Enum, category: str | Enum, pronoun: str, key = None) -> str:
    return VAI_SUFFIX_MAP[form][neg][category].get(pronoun, "")

def ends_with_long_vowel(verb: str) -> bool:
    return verb.endswith(WordEndingVowel.LONG_VOWEL)

def ends_with_short_vowel(verb: str) -> bool:
    return verb.endswith(WordEndingVowel.SHORT_VOWEL)

def ends_with_vowel(verb: str) -> bool:
    return verb.endswith(WordEndingVowel.SHORT_VOWEL) or verb.endswith(WordEndingVowel.LONG_VOWEL)

def ends_with_am(verb: str) -> bool:
    return verb.endswith(WordEndingVAI.AM)

def ends_with_n(verb: str) -> bool:
    return verb.endswith(WordEndingVAI.N)

def add_a(verb: str) -> str:
    return verb + "a"

def add_i(verb: str) -> str:
    return verb + "i"

def add_n(verb: str) -> str:
    return verb + "n"

def remove_final_letter(verb: str) -> str:
    return verb[:-1]

# --- 3. Rule Interface and Implementation ---
class IndependentAffirmativeRule:
    def matches(self, verb: str, pronoun: str) -> bool:
        raise NotImplementedError

    def apply(self, verb: str, pronoun: str) -> tuple[str, str]:
        raise NotImplementedError
    
class DropShortVowel(IndependentAffirmativeRule):
    def matches(self, verb: str, pronoun: str):
        return ends_with_short_vowel(verb) and not ends_with_long_vowel(verb) and pronoun in (Pronoun.FIRST_SINGULAR_ANIMATE, Pronoun.SECOND_SINGULAR_ANIMATE)
    
    def apply(self, verb: str, pronoun: str):
        return remove_final_letter(verb), get_suffix(Form.INDEPENDENT_CLAUSE, Negation.AFFIRMATIVE, WordEndingVAI.SHORT_LONG_VOWEL, pronoun)
    
class VowelEndIndPos(IndependentAffirmativeRule):
    def matches(self, verb: str, pronoun: str):
        return ends_with_vowel(verb)
    
    def apply(self, verb: str, pronoun: str):
        return verb, get_suffix(Form.INDEPENDENT_CLAUSE, Negation.AFFIRMATIVE, WordEndingVAI.SHORT_LONG_VOWEL, pronoun)

class AddAIndPos(IndependentAffirmativeRule):
    def matches(self, verb: str, pronoun: str):
        return ends_with_n(verb) and pronoun in (Pronoun.FIRST_PLURAL_EXC_ANIMATE, Pronoun.FIRST_PLURAL_INC_ANIMATE, Pronoun.SECOND_PLURAL_ANIMATE)
    
    def apply(self, verb: str, pronoun: str):
        return add_i(verb), get_suffix(Form.INDEPENDENT_CLAUSE, Negation.AFFIRMATIVE, WordEndingVAI.N_AM, pronoun)

class AddIIndPos(IndependentAffirmativeRule):
    def matches(self, verb: str, pronoun: str):
        return ends_with_n(verb) and pronoun in (Pronoun.FIRST_PLURAL_EXC_ANIMATE, Pronoun.FIRST_PLURAL_INC_ANIMATE, Pronoun.SECOND_PLURAL_ANIMATE)
    
    def apply(self, verb: str, pronoun: str):
        return add_i(verb), get_suffix(Form.INDEPENDENT_CLAUSE, Negation.AFFIRMATIVE, WordEndingVAI.N_AM, pronoun)

class EndNorAMIndPos(IndependentAffirmativeRule):
    def matches(self, verb: str, pronoun: str):
        return ends_with_am(verb) or ends_with_n(verb)
    
    def apply(self, verb: str, pronoun: str):
        if pronoun in (Pronoun.FIRST_PLURAL_EXC_ANIMATE, Pronoun.FIRST_PLURAL_INC_ANIMATE, Pronoun.SECOND_PLURAL_ANIMATE):
            return add_a(remove_final_letter(verb)), get_suffix(Form.INDEPENDENT_CLAUSE, Negation.AFFIRMATIVE, WordEndingVAI.N_AM, pronoun)
        return verb, get_suffix(Form.INDEPENDENT_CLAUSE, Negation.AFFIRMATIVE, WordEndingVAI.N_AM, pronoun)

class IndependentNegativeRule:
    def matches(self, verb: str, pronoun: str) -> bool:
        raise NotImplementedError

    def apply(self, verb: str, pronoun: str) -> tuple[str, str]:
        raise NotImplementedError
    
class EndVowelIndNeg(IndependentNegativeRule):
    def matches(self, verb: str, pronoun: str):
        return ends_with_vowel(verb)
    
    def apply(self, verb: str, pronoun: str):
        return verb, get_suffix(Form.INDEPENDENT_CLAUSE, Negation.NEGATIVE, WordEndingVAI.SHORT_LONG_VOWEL, pronoun)

class EndAMIndNeg(IndependentNegativeRule):
    def matches(self, verb: str, pronoun: str):
        return ends_with_am(verb)
    
    def apply(self, verb: str, pronoun: str):
        return add_n(remove_final_letter(verb)), get_suffix(Form.INDEPENDENT_CLAUSE, Negation.NEGATIVE, WordEndingVAI.N_AM, pronoun)
    
class EndNIndNeg(IndependentNegativeRule):
    def matches(self, verb: str, pronoun: str):
        return ends_with_n(verb)
    
    def apply(self, verb: str, pronoun: str):
        return verb, get_suffix(Form.INDEPENDENT_CLAUSE, Negation.NEGATIVE, WordEndingVAI.N_AM, pronoun)

class DependentAffirmativeRule:
    def matches(self, verb: str, pronoun: str) -> bool:
        raise NotImplementedError

    def apply(self, verb: str, pronoun: str) -> tuple[str, str]:
        raise NotImplementedError

class EndVowelDepPos(DependentAffirmativeRule):
    def matches(self, verb: str, pronoun: str):
        return ends_with_vowel(verb)
    
    def apply(self, verb: str, pronoun: str):
        return verb, get_suffix(Form.DEPENDENT_CLAUSE, Negation.AFFIRMATIVE, WordEndingVAI.SHORT_LONG_VOWEL, pronoun)

class EndNorAMDepPos(DependentAffirmativeRule):
    def matches(self, verb: str, pronoun: str):
        return ends_with_am(verb) or ends_with_n(verb)
    
    def apply(self, verb: str, pronoun: str):
        return verb, get_suffix(Form.DEPENDENT_CLAUSE, Negation.AFFIRMATIVE, WordEndingVAI.N_AM, pronoun)

class DependentNegativeRule:
    def matches(self, verb: str, pronoun: str) -> bool:
        raise NotImplementedError

    def apply(self, verb: str, pronoun: str) -> tuple[str, str]:
        raise NotImplementedError

class EndVowelDepNeg(DependentNegativeRule):
    def matches(self, verb: str, pronoun: str):
        return ends_with_vowel(verb)
    
    def apply(self, verb: str, pronoun: str):
        return verb, get_suffix(Form.DEPENDENT_CLAUSE, Negation.NEGATIVE, WordEndingVAI.SHORT_LONG_VOWEL, pronoun)

class EndNorAMDepNeg(DependentNegativeRule):
    def matches(self, verb: str, pronoun: str):
        return ends_with_am(verb) or ends_with_n(verb)
    
    def apply(self, verb: str, pronoun: str):
        return verb, get_suffix(Form.DEPENDENT_CLAUSE, Negation.NEGATIVE, WordEndingVAI.N_AM, pronoun)

class ImperativeAffirmativeRule:
    def matches(self, verb: str, pronoun: str) -> bool:
        raise NotImplementedError

    def apply(self, verb: str, pronoun: str) -> tuple[str, str]:
        raise NotImplementedError
    
class EndVowelImpPos(ImperativeAffirmativeRule):
    def matches(self, verb: str, pronoun: str):
        return ends_with_vowel(verb)
    
    def apply(self, verb: str, pronoun: str):
        return verb, get_suffix(Form.IMPERATIVE, Negation.AFFIRMATIVE, WordEndingVAI.SHORT_LONG_VOWEL, pronoun)

class EndNorAMImpPos(ImperativeAffirmativeRule):
    def matches(self, verb: str, pronoun: str):
        return ends_with_am(verb) or ends_with_n(verb)
    
    def apply(self, verb: str, pronoun: str):
        return verb, get_suffix(Form.IMPERATIVE, Negation.AFFIRMATIVE, WordEndingVAI.N_AM, pronoun)
    
class ImperativeNegativeRule:
    def matches(self, verb: str, pronoun: str) -> bool:
        raise NotImplementedError

    def apply(self, verb: str, pronoun: str) -> tuple[str, str]:
        raise NotImplementedError

class EndVowelImpNeg(ImperativeNegativeRule):
    def matches(self, verb: str, pronoun: str):
        return ends_with_vowel(verb)
    
    def apply(self, verb: str, pronoun: str):
        return verb, get_suffix(Form.IMPERATIVE, Negation.NEGATIVE, WordEndingVAI.SHORT_LONG_VOWEL, pronoun)

class EndNorAMImpNeg(ImperativeNegativeRule):
    def matches(self, verb: str, pronoun: str):
        return ends_with_am(verb) or ends_with_n(verb)
    
    def apply(self, verb: str, pronoun: str):
        return verb, get_suffix(Form.IMPERATIVE, Negation.NEGATIVE, WordEndingVAI.N_AM, pronoun)

# --- 4. Rule Registry ---
INDEPENDENT_AFFIRMATIVE_RULES = [
DropShortVowel(),
VowelEndIndPos(),
AddAIndPos(),
AddIIndPos(),
EndNorAMIndPos()
]

INDEPENDENT_NEGATIVE_RULES = [
EndVowelIndNeg(),
EndAMIndNeg(),
EndNIndNeg()
]

DEPENDENT_AFFIRMATIVE_RULES = [
EndVowelDepPos(),
EndNorAMDepPos()
]

DEPENDENT_NEGATIVE_RULES = [
EndVowelDepNeg(),
EndNorAMDepNeg()
]

IMPERATIVE_AFFIRMATIVE_RULES = [
EndVowelImpPos(),
EndNorAMImpPos()
]

IMPERATIVE_NEGATIVE_RULES = [
EndVowelImpNeg(),
EndNorAMImpNeg()
]

# --- 5. Main Logic Functions ---
def handle_independent(verb: str, neg: bool, pronoun: str) -> tuple[str, str]:
    if not neg:
        return handle_independent_affirmative(verb, pronoun)
    else:
        return handle_independent_negative(verb, pronoun)
    
def handle_independent_affirmative(verb: str, pronoun: str) -> tuple[str, str]:
    for rule in INDEPENDENT_AFFIRMATIVE_RULES:
        if rule.matches(verb, pronoun):
            return rule.apply(verb, pronoun)
    return verb, ""

def handle_independent_negative(verb: str, pronoun: str) -> tuple[str, str]:
    for rule in INDEPENDENT_NEGATIVE_RULES:
        if rule.matches(verb, pronoun):
            return rule.apply(verb, pronoun)
    return verb, ""

def handle_dependent(verb: str, neg: bool, pronoun: str) -> tuple[str, str]:
    if not neg:
        return handle_dependent_affirmative(verb, pronoun)
    else:
        return handle_dependent_negative(verb, pronoun)
    
def handle_dependent_affirmative(verb: str, pronoun: str) -> tuple[str, str]:
    for rule in DEPENDENT_AFFIRMATIVE_RULES:
        if rule.matches(verb, pronoun):
            return rule.apply(verb, pronoun)
    return verb, ""

def handle_dependent_negative(verb: str, pronoun: str) -> tuple[str, str]:
    for rule in DEPENDENT_NEGATIVE_RULES:
        if rule.matches(verb, pronoun):
            return rule.apply(verb, pronoun)
    return verb, ""

def handle_imperative(verb: str, neg: bool, pronoun: str) -> tuple[str, str]:
    if not neg:
        return handle_imperative_affirmative(verb, pronoun)
    else:
        return handle_imperative_negative(verb, pronoun)
    
def handle_imperative_affirmative(verb: str, pronoun: str) -> tuple[str, str]:
    for rule in IMPERATIVE_AFFIRMATIVE_RULES:
        if rule.matches(verb, pronoun):
            return rule.apply(verb, pronoun)
    return verb, ""

def handle_imperative_negative(verb: str, pronoun: str) -> tuple[str, str]:
    for rule in IMPERATIVE_NEGATIVE_RULES:
        if rule.matches(verb, pronoun):
            return rule.apply(verb, pronoun)
    return verb, ""

def get_vai_suffix(input_data: ConjugationInput) -> str:

    type = "vai"
    verb = input_data.verb
    form = input_data.form
    neg = input_data.negation
    pronoun = input_data.pronoun

    if type != "vai":
        return verb
    
    if form == Form.INDEPENDENT_CLAUSE:
        verb, suffix = handle_independent(verb, neg, pronoun)
    elif form == Form.DEPENDENT_CLAUSE:
        verb, suffix = handle_dependent(verb, neg, pronoun)
    elif form == Form.IMPERATIVE:
        verb, suffix = handle_imperative(verb, neg, pronoun)

    # green = affirmative, red = negative
    # regular = independent, italic = dependent, bold = imperative, underline = direct object
    style = get_style(form, neg)

    return verb + styled_text(suffix, style)