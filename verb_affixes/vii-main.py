# This is the entry point of your program — where it all comes together and runs.
# Imports models and logic from other modules.
# Constructs input data and calls the conjugation logic.
# Handles output: prints to terminal or logs results.
# Good place for CLI or a future GUI to start from.

from conjugator.models import ConjugationInput
from conjugator.vii_suffixes_core import get_vii_suffix
import logging

logging.basicConfig(level=logging.INFO)

VERBS = ["onaagoshin", "zoogipon", "gimiwan", "noodin", "aabawaa", "maajibiisaa", "dagwaagin", "ishkwaabiisaa", "niiskadad"]
FORMS = ["independent", "dependent"]
NEGATIONS = {False: "positive", True: "negative"}
PRONOUNS = ["0s", "0p"]

def main():
    for verb in VERBS:
        print(f"\n--- {verb.capitalize()} ---")
        for form in FORMS:
            for neg in NEGATIONS:
                print(f"{form.capitalize()} ({NEGATIONS[neg].capitalize()}):")
                for pronoun in PRONOUNS:
                    input_data = ConjugationInput(
                        type="vii",
                        form=form,
                        verb=verb,
                        pronoun=pronoun,
                        negation=neg,
                        direct_object=None
                    )
                    try:
                        result = get_vii_suffix(input_data)
                        print(f"{pronoun}: {result}")
                    except Exception as e:
                        logging.error(f"error processing {verb}/{form}/{neg}/{pronoun}: {e}")
                print()

if __name__ == "__main__":
    """Iterates over verbs, forms, negations, and pronouns to add conjugation suffixes and print the result."""
    main()