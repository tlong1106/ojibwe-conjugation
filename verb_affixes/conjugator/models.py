# This file defines the data structure used to hold information about conjugation inputs (form, verb, pronoun, negation, tense).
# Defines structured data using a dataclass.
# Makes input passing cleaner, consistent, and self-documenting.
# May later grow to include validation or more model types.

from dataclasses import dataclass

@dataclass
class ConjugationInput:
    # Required when creating an instance.
    type: str
    form: str
    verb: str
    # Optional when creating an instance. If not passed, will default automatically.
    pronoun: str = None
    direct_object: str = None
    negation: bool = False
    plural: bool = False
    suffix: str = None
    tense: str = None