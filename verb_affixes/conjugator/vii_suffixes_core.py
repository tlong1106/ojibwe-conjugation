# This file contains the core functionality of the program: the VII (Verb Inanimate Intransitive) conjugation logic.
# Implements all logic rules (suffixes, vowel handling, pronoun mapping).
# Takes in data (via models.py), applies logic, and returns results.
# Should be pure and testable — no printing, user interaction, or I/O.

from enum import Enum
from .enum import Form, Negation, Pronoun, WordEndingVowel, WordEndingVII
from .models import ConjugationInput
from .utils import styled_text, get_style

# --- 1. Constants ---
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

VII_SUFFIX_MAP = {
    Form.INDEPENDENT_CLAUSE: {
        Negation.AFFIRMATIVE: {
            WordEndingVII.D_N: {
                Pronoun.THIRD_SINGULAR_INANIMATE: "",
                Pronoun.THIRD_PLURAL_INANIMATE: "oon",
                Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "ini",
                Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "iniwan"
            },
            WordEndingVowel.LONG_VOWEL: {
                Pronoun.THIRD_SINGULAR_INANIMATE: "",
                Pronoun.THIRD_PLURAL_INANIMATE: "wan",
                Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "ni",
                Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "niwan"
            },
            WordEndingVowel.SHORT_VOWEL: {
                Pronoun.THIRD_SINGULAR_INANIMATE: "",
                Pronoun.THIRD_PLURAL_INANIMATE: "oon",
                Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "ini",
                Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "iniwan"
            }
        },
        Negation.NEGATIVE: {
            WordEndingVII.N: {
                Pronoun.THIRD_SINGULAR_INANIMATE: "zinoon",
                Pronoun.THIRD_PLURAL_INANIMATE: "zinoon",
                Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "zinini",
                Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "zininiwan"
            },
            WordEndingVII.D_VOWEL: {
                Pronoun.THIRD_SINGULAR_INANIMATE: "sinoon",
                Pronoun.THIRD_PLURAL_INANIMATE: "sinoon",
                Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "sinini",
                Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "sininiwan"
            }
        }
    },
    Form.DEPENDENT_CLAUSE: {
        Negation.AFFIRMATIVE: {
            WordEndingVII.D_N: {
                WordEndingVII.D: {
                    Pronoun.THIRD_SINGULAR_INANIMATE: "k",
                    Pronoun.THIRD_PLURAL_INANIMATE: "k"
                },
                WordEndingVII.N: {
                    Pronoun.THIRD_SINGULAR_INANIMATE: "g",
                    Pronoun.THIRD_PLURAL_INANIMATE: "g",
                    Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "inig",
                    Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "inig"
                }
            },
            WordEndingVowel.VOWEL: {
                Pronoun.THIRD_SINGULAR_INANIMATE: "g",
                Pronoun.THIRD_PLURAL_INANIMATE: "g",
                Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "nig",
                Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "nig"
            }
        },
        Negation.NEGATIVE: {
            WordEndingVII.D_VOWEL: {
                Pronoun.THIRD_SINGULAR_INANIMATE: "sinog",
                Pronoun.THIRD_PLURAL_INANIMATE: "sinog",
                Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "sininig",
                Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "sininig"
            },
            WordEndingVII.N: {
                Pronoun.THIRD_SINGULAR_INANIMATE: "zinog",
                Pronoun.THIRD_PLURAL_INANIMATE: "zinog",
                Pronoun.THIRD_SINGULAR_INANIMATE_OBVIATE: "zininig",
                Pronoun.THIRD_PLURAL_INANIMATE_OBVIATE: "zininig"
            }
        }
    }
}

# --- 2. Helpers ---
def get_suffix(form: str | Enum, neg: bool | Enum, category: str | Enum, pronoun: str, key = None) -> str:
    if key:
        return VII_SUFFIX_MAP[form][neg][category].get(key, {}).get(pronoun, "")
    return VII_SUFFIX_MAP[form][neg][category].get(pronoun, "")

def ends_with_d_or_n(verb: str) -> bool:
    return verb.endswith((WordEndingVII.D, WordEndingVII.N))

def ends_with_long_vowel(verb: str) -> bool:
    return verb.endswith(WordEndingVowel.LONG_VOWEL)

def ends_with_short_vowel(verb: str) -> bool:
    return verb.endswith(WordEndingVowel.SHORT_VOWEL)

def ends_with_vowel(verb: str) -> bool:
    return ends_with_long_vowel(verb) or ends_with_short_vowel(verb)

def ends_with_d_vowel(verb: str) -> bool:
    return verb.endswith(WordEndingVII.D) or ends_with_vowel(verb)

def remove_final_letter(verb: str) -> str:
    return verb[:-1]

# --- 3. Rule Interface and Implementation ---
class IndependentAffirmativeRule:
    def matches(self, verb: str, pronoun: str) -> bool:
        raise NotImplementedError

    def apply(self, verb: str, pronoun: str) -> tuple[str, str]:
        raise NotImplementedError
    
class EndDummyNPluralIndPos(IndependentAffirmativeRule):
    def matches(self, verb, pronoun):
        return verb in DUMMY_N and pronoun == Pronoun.THIRD_PLURAL_INANIMATE
    
    def apply(self, verb, pronoun):
        return remove_final_letter(verb), get_suffix(Form.INDEPENDENT_CLAUSE, Negation.AFFIRMATIVE, WordEndingVowel.LONG_VOWEL, pronoun)
    
class EndDorNIndPos(IndependentAffirmativeRule):
    def matches(self, verb, pronoun):
        return ends_with_d_or_n(verb)

    def apply(self, verb, pronoun):
        return verb, get_suffix(Form.INDEPENDENT_CLAUSE, Negation.AFFIRMATIVE, WordEndingVII.D_N, pronoun)
    
class EndLongVowelIndPos(IndependentAffirmativeRule):
    def matches(self, verb, pronoun):
        return ends_with_long_vowel(verb)
        
    def apply(self, verb, pronoun):
        return verb, get_suffix(Form.INDEPENDENT_CLAUSE, Negation.AFFIRMATIVE, WordEndingVowel.LONG_VOWEL, pronoun)
    
class EndShortVowelIndPos(IndependentAffirmativeRule):
    def matches(self, verb, pronoun):
        return ends_with_short_vowel(verb)
    
    def apply(self, verb, pronoun):
        return remove_final_letter(verb), get_suffix(Form.INDEPENDENT_CLAUSE, Negation.AFFIRMATIVE, WordEndingVowel.SHORT_VOWEL, pronoun)
    
class IndependentNegativeRule:
    def matches(self, verb: str, pronoun: str) -> bool:
        raise NotImplementedError
    
    def apply(self, verb: str, pronoun: str) -> tuple[str, str]:
        raise NotImplementedError
    
class EndDorDummyNIndNeg(IndependentNegativeRule):
    def matches(self, verb, pronoun):
        return verb.endswith(WordEndingVII.D) or verb in DUMMY_N
    
    def apply(self, verb, pronoun):
        return remove_final_letter(verb), get_suffix(Form.INDEPENDENT_CLAUSE, Negation.NEGATIVE, WordEndingVII.D_VOWEL, pronoun)

class EndNIndNeg(IndependentNegativeRule):
    def matches(self, verb, pronoun):
        return verb.endswith(WordEndingVII.N)
    
    def apply(self, verb, pronoun):
        category = WordEndingVII.N
        return verb, get_suffix(Form.INDEPENDENT_CLAUSE, Negation.NEGATIVE, category, pronoun)
    
class EndVowelIndNeg(IndependentNegativeRule):
    def matches(self, verb, pronoun):
        return ends_with_vowel(verb)
    
    def apply(self, verb, pronoun):
        return verb, get_suffix(Form.INDEPENDENT_CLAUSE,  Negation.NEGATIVE, WordEndingVII.D_VOWEL, pronoun)
    
class DependentAffirmativeRule:
    def matches(self, verb: str, pronoun: str) -> bool:
        raise NotImplementedError
    
    def apply(self, verb: str, pronoun: str) -> tuple[str, str]:
        raise NotImplementedError
    
class ENdDDepPos(DependentAffirmativeRule):
    def matches(self, verb, pronoun):
        return verb.endswith(WordEndingVII.D) and pronoun in (Pronoun.THIRD_SINGULAR_INANIMATE, Pronoun.THIRD_PLURAL_INANIMATE)
    
    def apply(self, verb, pronoun):
        return remove_final_letter(verb), get_suffix(Form.DEPENDENT_CLAUSE, Negation.AFFIRMATIVE, WordEndingVII.D_N, pronoun, key = WordEndingVII.D)
    
class EndDummyNDepPos(DependentAffirmativeRule):
    def matches(self, verb, pronoun):
        return verb in DUMMY_N
    
    def apply(self, verb, pronoun):
        return remove_final_letter(verb), get_suffix(Form.DEPENDENT_CLAUSE, Negation.AFFIRMATIVE, WordEndingVII.D_N, pronoun, key = WordEndingVII.N)
    
class EndNDepPos(DependentAffirmativeRule):
    def matches(self, verb, pronoun):
        return verb.endswith(WordEndingVII.N)
    
    def apply(self, verb, pronoun):
        return verb, get_suffix(Form.DEPENDENT_CLAUSE, Negation.AFFIRMATIVE, WordEndingVII.D_N, pronoun, key = WordEndingVII.N)
    
class ENdVowelDepPos(DependentAffirmativeRule):
    def matches(self, verb, pronoun):
        return ends_with_vowel(verb)
    
    def apply(self, verb, pronoun):
        return verb, get_suffix(Form.DEPENDENT_CLAUSE, Negation.AFFIRMATIVE, WordEndingVowel.VOWEL, pronoun)
    
class DependentNegativeRule:
    def matches(self, verb: str, pronoun: str) -> bool:
        raise NotImplementedError
    
    def apply(self, verb: str, pronoun: str) -> tuple[str, str]:
        raise NotImplementedError
    
class EndDorDummyNDepNeg(DependentNegativeRule):
    def matches(self, verb, pronoun):
        return verb.endswith(WordEndingVII.D) or verb in DUMMY_N
    
    def apply(self, verb, pronoun):
        return remove_final_letter(verb), get_suffix(Form.DEPENDENT_CLAUSE, Negation.NEGATIVE, WordEndingVII.D_VOWEL, pronoun)
    
class EndNDepNeg(DependentNegativeRule):
    def matches(self, verb, pronoun):
        return verb.endswith(WordEndingVII.N)
    
    def apply(self, verb, pronoun):
        category = WordEndingVII.N
        return verb, get_suffix(Form.DEPENDENT_CLAUSE, Negation.NEGATIVE, category, pronoun)
    
class EndVowelDepNeg(DependentNegativeRule):
    def matches(self, verb, pronoun):
        return ends_with_vowel(verb)
    
    def apply(self, verb, pronoun):
        return verb, get_suffix(Form.DEPENDENT_CLAUSE, Negation.NEGATIVE, WordEndingVII.D_VOWEL, pronoun)

# --- 4. Rule Registry --- 
INDEPENDENT_AFFIRMATIVE_RULES = [
    EndDummyNPluralIndPos(),
    EndDorNIndPos(),
    EndLongVowelIndPos(),
    EndShortVowelIndPos()
]

INDEPENDENT_NEGATIVE_RULES = [
    EndDorDummyNIndNeg(),
    EndNIndNeg(),
    EndVowelIndNeg()
]

DEPENDENT_AFFIRMATIVE_RULES = [
    ENdDDepPos(),
    EndDummyNDepPos(),
    EndNDepPos(),
    ENdVowelDepPos()
]

DEPENDENT_NEGATIVE_RULES = [
    EndDorDummyNDepNeg(),
    EndNDepNeg(),
    EndVowelDepNeg()
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

def handle_dependent(verb: str, neg: str, pronoun: str) -> tuple[str, str]:
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

def get_vii_suffix(input_data: ConjugationInput) -> str:
    """
    Pure function that returns vii conjugation:
      form: independent, dependent
      negation: true, false
    """
    
    type = "vii"
    verb = input_data.verb
    form = input_data.form
    neg = input_data.negation
    pronoun = input_data.pronoun

    if type != "vii":
        return verb
    
    if form == Form.INDEPENDENT_CLAUSE:
        verb, suffix = handle_independent(verb, neg, pronoun)
    else:
        verb, suffix = handle_dependent(verb, neg, pronoun)

    # green = affirmative, red = negative
    # regular = independent, italic = dependent, bold = imperative, underline = direct object
    style = get_style(form, neg)

    return verb + styled_text(suffix, style)