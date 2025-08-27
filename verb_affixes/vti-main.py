# This is the entry point of your program — where it all comes together and runs.
# Imports models and logic from other modules.
# Constructs input data and calls the conjugation logic.
# Handles output: prints to terminal or logs results.
# Good place for CLI or a future GUI to start from.

from conjugator.models import ConjugationInput
from conjugator.vti_suffixes_core import get_vti_suffix
from conjugator.tense_prefix_core import get_tense_prefix
from conjugator.pronoun_prefix_core import get_pronoun_prefix
import logging

logging.basicConfig(level=logging.INFO)

VERBS = ["mamoon", "miijin", "giziibiiginan", "biitwaabaawidoon", "na'inan", "ayaan", "miijin"]
FORMS = ["independent", "dependent", "imperative"]
NEGATIONS = {False: "positive", True: "negative"}
PRONOUNS = ["1s","2s", "3s", "1p", "21", "2p", "3p"]
TENSES = ["past", "present", "definitive", "desiderative", "conditional"]
DIRECT_OBJECTS = {"singular": "0s", "plural": "0p"}

def main():
    for verb in VERBS:
        print(f"\n--- {verb.capitalize()} ---")
        for form in FORMS:
            for neg in NEGATIONS:
                for tense in TENSES:
                    for pronoun in PRONOUNS:
                        if form == "imperative" and pronoun in ("1s", "3s", "1p", "3p"):
                            continue
                        for obj in DIRECT_OBJECTS:
                            print(f"{form.capitalize()} ({DIRECT_OBJECTS[obj].capitalize()} {NEGATIONS[neg].capitalize()}, {tense.capitalize()}):")
                            input_data = ConjugationInput(
                                type="vti",
                                form=form,
                                negation=neg,
                                verb=verb,
                                pronoun=pronoun,
                                tense=tense,
                                direct_object=obj
                            )
                            try:
                                added_suffix = get_vti_suffix(input_data)
                                added_tense_prefix = get_tense_prefix(added_suffix, pronoun, tense)
                                added_pronoun_prefix = get_pronoun_prefix("vti", added_tense_prefix, form, neg, pronoun, tense)
                                if isinstance(added_pronoun_prefix, list):
                                    print(f"{pronoun}:", *added_pronoun_prefix)
                                else:
                                    print(f"{pronoun}: {added_pronoun_prefix}")
                            except Exception as e:
                                logging.error(f"error processing {verb}/{form}/{neg}/{pronoun}: {e}")
                        print()

if __name__ == "__main__":
    """Iterates over verbs, forms, negations, and pronouns to add conjugation suffixes and print the result."""
    main()