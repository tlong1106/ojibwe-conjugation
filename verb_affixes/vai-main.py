# This is the entry point of your program — where it all comes together and runs.
# Imports models and logic from other modules.
# Constructs input data and calls the conjugation logic.
# Handles output: prints to terminal or logs results.
# Good place for CLI or a future GUI to start from.

from conjugator.enum import Tense
from conjugator.models import ConjugationInput
from conjugator.vai_suffixes_core import get_vai_suffix
from conjugator.tense_prefix_core import get_tense_prefix
from conjugator.pronoun_prefix_core import get_pronoun_prefix
import logging

logging.basicConfig(level=logging.INFO)

VERBS = ["debisinii","giishkaabaagwe","jiibaakwe","ziikawidoon","zhoomiingweni","minikwe","nibaa","wiisini","bakade","ashange","ikido","aagade","ojibwemo","jiikendam"]
FORMS = ["independent", "dependent", "imperative"]
NEGATIONS = {False: "positive", True: "negative"}
PRONOUNS = ["1s","2s", "3s", "1p", "21", "2p", "3p"]
TENSES = ["past", "present", "definitive", "desiderative", "conditional"]

def main():
    for verb in VERBS:
        print(f"\n--- {verb.capitalize()} ---")
        for form in FORMS:
            for neg in NEGATIONS:
                for tense in TENSES:
                    print(f"{form.capitalize()} ({NEGATIONS[neg].capitalize()}, {tense.capitalize()}):")
                    for pronoun in PRONOUNS:
                        if form == "imperative" and pronoun in ("1s", "3s", "1p", "3p"):
                            continue
                        input_data = ConjugationInput(
                            type="vai",
                            form=form,
                            verb=verb,
                            pronoun=pronoun,
                            tense=tense,
                            negation=neg,
                            direct_object=None
                        )
                        try:
                            added_suffix = get_vai_suffix(input_data)
                            added_tense_prefix = get_tense_prefix(added_suffix, pronoun, tense)
                            added_pronoun_prefix = get_pronoun_prefix("vai", added_tense_prefix, form, neg, pronoun, tense)
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