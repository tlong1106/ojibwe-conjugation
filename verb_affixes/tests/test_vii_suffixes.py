import pytest
from conjugator.vii_suffixes_core import handle_independent, handle_dependent

# ojibwe-conjugation/verb_affixes run: python -m pytest

# ad ending tests:

def test_ad_ending_ind_pos_sing(): # independent positive singular
    base, suffix = handle_independent("bakaanad", False, "0s")
    assert base == "bakaanad", f"Expected base 'bakaanad', got '{base}'"
    assert suffix == "", f"Expected suffix '', got '{suffix}'"

def test_ad_ending_ind_pos_pl(): # independent positive plural
    base, suffix = handle_independent("bakaanad", False, "0p")
    assert base == "bakaanad", f"Expected base 'bakaanad', got '{base}'"
    assert suffix == "oon", f"Expected suffix 'oon', got '{suffix}'"

def test_ad_ending_ind_neg_sing(): # independent negative singular
    base, suffix = handle_independent("bakaanad", True, "0s")
    assert base == "bakaana", f"Expected base 'bakaana', got '{base}'"
    assert suffix == "sinoon", f"Expected suffix 'sinoon', got '{suffix}'"

def test_ad_ending_ind_neg_pl(): # independent negative plural
    base, suffix = handle_independent("bakaanad", True, "0p")
    assert base == "bakaana", f"Expected base 'bakaana', got '{base}'"
    assert suffix == "sinoon", f"Expected suffix 'sinoon', got '{suffix}'"

def test_ad_ending_dep_pos_sing(): # dependent positive singular
    base, suffix = handle_dependent("bakaanad", False, "0s")
    assert base == "bakaana", f"Expected base 'bakaana', got '{base}'"
    assert suffix == "k", f"Expected suffix 'k', got '{suffix}'"

def test_ad_ending_dep_pos_pl(): # dependent positive plural
    base, suffix = handle_dependent("bakaanad", False, "0p")
    assert base == "bakaana", f"Expected base 'bakaana', got '{base}'"
    assert suffix == "k", f"Expected suffix 'k', got '{suffix}'"

def test_ad_ending_dep_neg_sing(): # dependent negative singular
    base, suffix = handle_dependent("bakaanad", True, "0s")
    assert base == "bakaana", f"Expected base 'bakaana', got '{base}'"
    assert suffix == "sinog", f"Expected suffix 'sinog', got '{suffix}'"

def test_ad_ending_dep_neg_pl(): # dependent negative plural
    base, suffix = handle_dependent("bakaanad", True, "0p")
    assert base == "bakaana", f"Expected base 'bakaana', got '{base}'"
    assert suffix == "sinog", f"Expected suffix 'sinog', got '{suffix}'"


# vowel ending tests:

def test_vowel_ending_ind_pos_sing(): # independent positive singular
    base, suffix = handle_independent("gisinaa", False, "0s")
    assert base == "gisinaa", f"Expected base 'gisinaa', got '{base}'"
    assert suffix == "", f"Expected suffix '', got '{suffix}'"

def test_vowel_ending_ind_pos_pl(): # independent positive plural
    base, suffix = handle_independent("gisinaa", False, "0p")
    assert base == "gisinaa", f"Expected base 'gisinaa', got '{base}'"
    assert suffix == "wan", f"Expected suffix 'wan', got '{suffix}'"

def test_vowel_ending_ind_neg_sing(): # independent negative singular
    base, suffix = handle_independent("gisinaa", True, "0s")
    assert base == "gisinaa", f"Expected base 'gisinaa', got '{base}'"
    assert suffix == "sinoon", f"Expected suffix 'sinoon', got '{suffix}'"

def test_vowel_ending_ind_neg_pl(): # independent negative plural
    base, suffix = handle_independent("gisinaa", True, "0p")
    assert base == "gisinaa", f"Expected base 'gisinaa', got '{base}'"
    assert suffix == "sinoon", f"Expected suffix 'sinoon', got '{suffix}'"

def test_vowel_ending_dep_pos_sing(): # dependent positive singular
    base, suffix = handle_dependent("gisinaa", False, "0s")
    assert base == "gisinaa", f"Expected base 'gisinaa', got '{base}'"
    assert suffix == "g", f"Expected suffix 'g', got '{suffix}'"

def test_vowel_ending_dep_pos_pl(): # dependent positive plural
    base, suffix = handle_dependent("gisinaa", False, "0p")
    assert base == "gisinaa", f"Expected base 'gisinaa', got '{base}'"
    assert suffix == "g", f"Expected suffix 'g', got '{suffix}'"

def test_vowel_ending_dep_neg_sing(): # dependent negative singular
    base, suffix = handle_dependent("gisinaa", True, "0s")
    assert base == "gisinaa", f"Expected base 'gisinaa', got '{base}'"
    assert suffix == "sinog", f"Expected suffix 'sinog', got '{suffix}'"

def test_vowel_ending_dep_neg_pl(): # dependent negative plural
    base, suffix = handle_dependent("gisinaa", True, "0p")
    assert base == "gisinaa", f"Expected base 'gisinaa', got '{base}'"
    assert suffix == "sinog", f"Expected suffix 'sinog', got '{suffix}'"


# true n ending tests:

def test_true_n_ending_ind_pos_sing(): # independent positive singular
    base, suffix = handle_independent("wanisin", False, "0s")
    assert base == "wanisin", f"Expected base 'wanisin', got '{base}'"
    assert suffix == "", f"Expected suffix '', got '{suffix}'"

def test_true_n_ending_ind_pos_pl(): # independent positive plural
    base, suffix = handle_independent("wanisin", False, "0p")
    assert base == "wanisin", f"Expected base 'wanisin', got '{base}'"
    assert suffix == "oon", f"Expected suffix 'oon', got '{suffix}'"

def test_true_n_ending_ind_neg_sing(): # independent negative singular
    base, suffix = handle_independent("wanisin", True, "0s")
    assert base == "wanisin", f"Expected base 'wanisin', got '{base}'"
    assert suffix == "zinoon", f"Expected suffix 'zinoon', got '{suffix}'"

def test_true_n_ending_ind_neg_pl(): # independent negative plural
    base, suffix = handle_independent("wanisin", True, "0p")
    assert base == "wanisin", f"Expected base 'wanisin', got '{base}'"
    assert suffix == "zinoon", f"Expected suffix 'zinoon', got '{suffix}'"

def test_true_n_ending_dep_pos_sing(): # dependent positive singular
    base, suffix = handle_dependent("wanisin", False, "0s")
    assert base == "wanisin", f"Expected base 'wanisin', got '{base}'"
    assert suffix == "g", f"Expected suffix 'g', got '{suffix}'"

def test_true_n_ending_dep_pos_pl(): # dependent positive plural
    base, suffix = handle_dependent("wanisin", False, "0p")
    assert base == "wanisin", f"Expected base 'wanisin', got '{base}'"
    assert suffix == "g", f"Expected suffix 'g', got '{suffix}'"

def test_true_n_ending_dep_neg_sing(): # dependent negative singular
    base, suffix = handle_dependent("wanisin", True, "0s")
    assert base == "wanisin", f"Expected base 'wanisin', got '{base}'"
    assert suffix == "zinog", f"Expected suffix 'zinog', got '{suffix}'"

def test_true_n_ending_dep_neg_pl(): # dependent negative plural
    base, suffix = handle_dependent("wanisin", True, "0p")
    assert base == "wanisin", f"Expected base 'wanisin', got '{base}'"
    assert suffix == "zinog", f"Expected suffix 'zinog', got '{suffix}'"


# dummy n ending tests:

