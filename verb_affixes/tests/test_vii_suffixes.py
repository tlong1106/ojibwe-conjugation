import pytest
from conjugator.vii_suffixes_core import handle_independent, handle_dependent

# Test data format:
# (func, verb, neg, pronoun, expected_verb, expected_suffix)

test_cases = [
    # ad ending tests
    (handle_independent, "bakaanad", False, "0s", "bakaanad", ""),
    (handle_independent, "bakaanad", False, "0p", "bakaanad", "oon"),
    (handle_independent, "bakaanad", True,  "0s", "bakaana",  "sinoon"),
    (handle_independent, "bakaanad", True,  "0p", "bakaana",  "sinoon"),
    (handle_dependent,   "bakaanad", False, "0s", "bakaana",  "k"),
    (handle_dependent,   "bakaanad", False, "0p", "bakaana",  "k"),
    (handle_dependent,   "bakaanad", True,  "0s", "bakaana",  "sinog"),
    (handle_dependent,   "bakaanad", True,  "0p", "bakaana",  "sinog"),

    # vowel ending tests
    (handle_independent, "gisinaa", False, "0s", "gisinaa", ""),
    (handle_independent, "gisinaa", False, "0p", "gisinaa", "wan"),
    (handle_independent, "gisinaa", True,  "0s", "gisinaa", "sinoon"),
    (handle_independent, "gisinaa", True,  "0p", "gisinaa", "sinoon"),
    (handle_dependent,   "gisinaa", False, "0s", "gisinaa", "g"),
    (handle_dependent,   "gisinaa", False, "0p", "gisinaa", "g"),
    (handle_dependent,   "gisinaa", True,  "0s", "gisinaa", "sinog"),
    (handle_dependent,   "gisinaa", True,  "0p", "gisinaa", "sinog"),

    # true n ending tests
    (handle_independent, "wanisin", False, "0s", "wanisin", ""),
    (handle_independent, "wanisin", False, "0p", "wanisin", "oon"),
    (handle_independent, "wanisin", True,  "0s", "wanisin", "zinoon"),
    (handle_independent, "wanisin", True,  "0p", "wanisin", "zinoon"),
    (handle_dependent,   "wanisin", False, "0s", "wanisin", "g"),
    (handle_dependent,   "wanisin", False, "0p", "wanisin", "g"),
    (handle_dependent,   "wanisin", True,  "0s", "wanisin", "zinog"),
    (handle_dependent,   "wanisin", True,  "0p", "wanisin", "zinog"),

    # dummy n ending tests
    (handle_independent, "dakaagamin", False, "0s", "dakaagamin", ""),
    (handle_independent, "dakaagamin", False, "0p", "dakaagami",  "wan"),
    (handle_independent, "dakaagamin", True,  "0s", "dakaagami",  "sinoon"),
    (handle_independent, "dakaagamin", True,  "0p", "dakaagami",  "sinoon"),
    (handle_dependent,   "dakaagamin", False, "0s", "dakaagami",  "g"),
    (handle_dependent,   "dakaagamin", False, "0p", "dakaagami",  "g"),
    (handle_dependent,   "dakaagamin", True,  "0s", "dakaagami",  "sinog"),
    (handle_dependent,   "dakaagamin", True,  "0p", "dakaagami",  "sinog"),
]

@pytest.mark.parametrize("func, verb, neg, pronoun, expected_verb, expected_suffix", test_cases)
def test_vii_suffixes(func, verb, neg, pronoun, expected_verb, expected_suffix):
    verb, suffix = func(verb, neg, pronoun)
    assert verb == expected_verb, f"Expected verb '{expected_verb}', got '{verb}'"
    assert suffix == expected_suffix, f"Expected suffix '{expected_suffix}', got '{suffix}'"