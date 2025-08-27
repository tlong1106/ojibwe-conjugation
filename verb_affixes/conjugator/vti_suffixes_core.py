# This file contains the core functionality of the program: the VAI (Verb Animate Intransitive) conjugation logic.
# Implements all logic rules (suffixes, vowel handling, pronoun mapping).
# Takes in data (via models.py), applies logic, and returns results.
# Should be pure and testable — no printing, user interaction, or I/O.

from .models import ConjugationInput
from .utils import styled_text

PRONOUN_SUFFIX_MAP = {
    "independent": {
        "singular": {
            False: {
                "an_aan_oon_in": {
                    "1s": "",
                    "2s": "",
                    "3s": "",
                    "1p": "min",
                    "21": "min",
                    "2p": "aawaa",
                    "3p": "aawaa"
                }
            },
            True: {
                "an_aan": {
                    "1s": "ziin",
                    "2s": "ziin",
                    "3s": "ziin",
                    "1p": "ziimin",
                    "21": "ziimin",
                    "2p": "ziinaawaa",
                    "3p": "ziinaawaa"
                },
                "oon_in": {
                    "1s": "siin",
                    "2s": "siin",
                    "3s": "siin",
                    "1p": "siimin",
                    "21": "siimin",
                    "2p": "siinaawaa",
                    "3p": "siinaawaa"
                },   
            }
        },
        "plural": {
           False: {
                "an_aan_oon_in": {
                    "1s": "an",
                    "2s": "an",
                    "3s": "an",
                    "1p": "min",
                    "21": "min",
                    "2p": "aawaan",
                    "3p": "aawaan"
                }
            },
            True: {
                "an_aan": {
                    "1s": "ziinan",
                    "2s": "ziinan",
                    "3s": "ziinan",
                    "1p": "ziimin",
                    "21": "ziimin",
                    "2p": "ziinaawaan",
                    "3p": "ziinaawaan"
                },
                "oon_in": {
                    "1s": "siinan",
                    "2s": "siinan",
                    "3s": "siinan",
                    "1p": "siimin",
                    "21": "siimin",
                    "2p": "siinaawaan",
                    "3p": "siinaawaan"
                },   
            } 
        }
    },
    "dependent": {
        "singular_plural": {
            False: {
                "an_aan": {
                    "1s": "aan",
                    "2s": "an",
                    "3s": "g",
                    "1p": "aang",
                    "21": "ang",
                    "2p": "eg",
                    "3p": "owaad"
                },
                "oon_in": {
                    "1s": "yaan",
                    "2s": "yan",
                    "3s": "d",
                    "1p": "yaang",
                    "21": "yang",
                    "2p": "yeg",
                    "3p": "waad"
                }
            },
            True: {
                "an_aan": {
                    "1s": "ziwaan",
                    "2s": "ziwan",
                    "3s": "zig",
                    "1p": "ziwaang",
                    "21": "ziwang",
                    "2p": "ziweg",
                    "3p": "zigwaa"
                },
                "oon_in": {
                    "1s": "siwaan",
                    "2s": "siwan",
                    "3s": "sig",
                    "1p": "siwaang",
                    "21": "siwang",
                    "2p": "siweg",
                    "3p": "sigwaa"
                }
            }
        }
    },
    "imperative": {
        "singular_plural": {
            False: {
                "an_aan": { # mikan, gidaan
                    "2s": "",
                    "21": ["daa", "daanin"],
                    "2p": "ok"
                },
                "oon_in": { # mamoon, miijin
                    "2s": "",
                    "21": ["daa", "daanin"],
                    "2p": "g"
                }
            },
            True: {
                "an_aan": { # mikan, gidaan
                    "2s": "gen",
                    "21": ["ziidaa", "ziidaanin"],
                    "2p": "gegon"
                },
                "oon_in": { # mamoon, miijin
                    "2s": "ken",
                    "21": ["siidaa", "siidaanin"],
                    "2p": "kegon"
                }
            }
        },
    }
}

def get_vti_suffix(input_data: ConjugationInput) -> str:

    verb = input_data.verb
    form = input_data.form
    neg = input_data.negation
    pronoun = input_data.pronoun
    obj = input_data.direct_object

    suffix = ""
    base = verb

    if form == "independent":
        if obj == "singular":
            if not neg:
                if verb.endswith("aan"):
                    if pronoun in ("1s", "2s", "3s", "2p", "3p"):
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan_oon_in"].get(pronoun, "")
                    elif pronoun in ("1p", "21"):
                        base = verb[:-1]
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan_oon_in"].get(pronoun, "")
                elif verb.endswith("an"):
                    if pronoun in ("1s", "2s", "3s", "2p", "3p"):
                        base = verb[:-1] + "an"
                        if pronoun in ("1s", "2s", "3s"):
                            suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan_oon_in"].get(pronoun, "")
                        elif pronoun in ("2p", "3p"):
                            suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan_oon_in"].get(pronoun, "")
                    elif pronoun in ("1p", "21"):
                        base = verb[:-1]
                        suffix = suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan_oon_in"].get(pronoun, "")
                elif verb.endswith(("oon", "in")):
                    if pronoun in ("1s", "2s", "3s", "2p", "3p"):
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan_oon_in"].get(pronoun, "")
                    elif pronoun in ("1p", "21"):
                        base = verb[:-1]
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan_oon_in"].get(pronoun, "")
            else:
                if verb.endswith("an"):
                    if pronoun in ("1s", "2s", "3s"):
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan"].get(pronoun, "")
                    elif pronoun in ("1p", "21"):
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan"].get(pronoun, "")
                    elif pronoun in ("2p", "3p"):
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan"].get(pronoun, "")
                elif verb.endswith(("oon", "in")):
                    base = verb[:-1]
                    if pronoun in ("1s", "2s", "3s"):
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["oon_in"].get(pronoun, "")
                    elif pronoun in ("1p", "21"):
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["oon_in"].get(pronoun, "")
                    elif pronoun in ("2p", "3p"):
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["oon_in"].get(pronoun, "")
        else:
            if not neg:
                if verb.endswith("aan"):
                    if pronoun in ("1s", "2s", "3s", "2p", "3p"):
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan_oon_in"].get(pronoun, "")
                    elif pronoun in ("1p", "21"):
                        base = verb[:-1]
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan_oon_in"].get(pronoun, "")
                elif verb.endswith("an"):
                    if pronoun in ("1s", "2s", "3s", "2p", "3p"):
                        base = verb[:-1] + "an"
                        if pronoun in ("1s", "2s", "3s"):
                            suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan_oon_in"].get(pronoun, "")
                        elif pronoun in ("2p", "3p"):
                            suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan_oon_in"].get(pronoun, "")
                    elif pronoun in ("1p", "21"):
                        base = verb[:-1]
                        suffix = suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan_oon_in"].get(pronoun, "")
                elif verb.endswith(("oon", "in")):
                    if pronoun in ("1s", "2s", "3s", "2p", "3p"):
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan_oon_in"].get(pronoun, "")
                    elif pronoun in ("1p", "21"):
                        base = verb[:-1]
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan_oon_in"].get(pronoun, "")
            else:
                if verb.endswith("an"):
                    if pronoun in ("1s", "2s", "3s"):
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan"].get(pronoun, "")
                    elif pronoun in ("1p", "21"):
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan"].get(pronoun, "")
                    elif pronoun in ("2p", "3p"):
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["an_aan"].get(pronoun, "")
                elif verb.endswith(("oon", "in")):
                    base = verb[:-1]
                    if pronoun in ("1s", "2s", "3s"):
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["oon_in"].get(pronoun, "")
                    elif pronoun in ("1p", "21"):
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["oon_in"].get(pronoun, "")
                    elif pronoun in ("2p", "3p"):
                        suffix = PRONOUN_SUFFIX_MAP[form][obj][neg]["oon_in"].get(pronoun, "")
    
    elif form == "dependent":
        if obj in ("singular", "plural"):
            if not neg:
                if verb.endswith(("an", "aan")):
                    if pronoun in ("1s", "2s", "1p", "21", "2p", "3p"):
                        base = verb[:-1] + styled_text("m", "underline")
                        if pronoun == "1s":
                            suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["an_aan"].get(pronoun, "")
                        elif pronoun == "2s":
                            suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["an_aan"].get(pronoun, "")
                        elif pronoun == "1p":
                            suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["an_aan"].get(pronoun, "")
                        elif pronoun == "21":
                            suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["an_aan"].get(pronoun, "")
                        elif pronoun == "2p":
                            suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["an_aan"].get(pronoun, "")
                        elif pronoun == "3p":
                            suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["an_aan"].get(pronoun, "")
                    elif pronoun == "3s":
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["an_aan"].get(pronoun, "")
                elif verb.endswith("oon"):
                    base = verb[:-1]
                    if pronoun in ("1s"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                    elif pronoun in ("2s"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                    elif pronoun in ("3s"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                    elif pronoun in ("1p"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                    elif pronoun in ("21"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                    elif pronoun in ("2p"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                    elif pronoun in ("3p"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                elif verb.endswith("in"):
                    if pronoun != "3s":
                        base = verb[:-1] + styled_text("m", "underline")
                        if pronoun in ("1s"):
                            suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                        elif pronoun in ("2s"):
                            suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                        elif pronoun in ("1p"):
                            suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                        elif pronoun in ("21"):
                            suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                        elif pronoun in ("2p"):
                            suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                        elif pronoun in ("3p"):
                            suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                    elif pronoun == "3s":
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
            else:
                if verb.endswith(("an", "aan")):
                    if pronoun in ("1s"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["an_aan"].get(pronoun, "")
                    elif pronoun in ("2s"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["an_aan"].get(pronoun, "")
                    elif pronoun in ("3s"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["an_aan"].get(pronoun, "")
                    elif pronoun in ("1p"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["an_aan"].get(pronoun, "")
                    elif pronoun in ("21"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["an_aan"].get(pronoun, "")
                    elif pronoun in ("2p"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["an_aan"].get(pronoun, "")
                    elif pronoun in ("3p"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["an_aan"].get(pronoun, "")
                elif verb.endswith(("oon", "in")):
                    base = verb[:-1]
                    if pronoun in ("1s"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                    elif pronoun in ("2s"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                    elif pronoun in ("3s"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                    elif pronoun in ("1p"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                    elif pronoun in ("21"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                    elif pronoun in ("2p"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                    elif pronoun in ("3p"):
                        suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
    
    elif form == "imperative":
        if obj in ("singular", "plural"):
            if not neg:
                if verb.endswith(("an", "aan")) and pronoun in ("2s", "2p"):
                    if pronoun == "2p":
                        base = verb[:-1] + styled_text("m", "underline")
                    suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["an_aan"].get(pronoun, "")
                elif verb.endswith(("an", "aan")) and pronoun == "21":
                    suffix_list = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["an_aan"].get(pronoun, [])
                    if isinstance(suffix_list, list):
                        suffix = suffix_list[0] if obj == "singular" else suffix_list[1]
                    else:
                        suffix = suffix_list
                if verb.endswith(("oon", "in")) and pronoun in ("2s", "2p"):
                    if pronoun == "2p":
                        base = verb[:-1]
                    suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                elif verb.endswith(("oon", "in")) and pronoun == "21":
                    base = verb[:-1]
                    suffix_list = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["an_aan"].get(pronoun, [])
                    if isinstance(suffix_list, list):
                        suffix = suffix_list[0] if obj == "singular" else suffix_list[1]
                    else:
                        suffix = suffix_list
            else:
                if verb.endswith(("an", "aan")) and pronoun in ("2s", "2p"):
                    if pronoun == "2p":
                        base = verb[:-1] + styled_text("m", "underline")
                    suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["an_aan"].get(pronoun, "")
                elif verb.endswith(("an", "aan")) and pronoun == "21":
                    suffix_list = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["an_aan"].get(pronoun, [])
                    if isinstance(suffix_list, list):
                        suffix = suffix_list[0] if obj == "singular" else suffix_list[1]
                    else:
                        suffix = suffix_list
                if verb.endswith(("oon", "in")) and pronoun in ("2s", "2p"):
                    base = verb[:-1]
                    suffix = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, "")
                elif verb.endswith(("oon", "in")) and pronoun == "21":
                    base = verb[:-1]
                    suffix_list = PRONOUN_SUFFIX_MAP[form]["singular_plural"][neg]["oon_in"].get(pronoun, [])
                    if isinstance(suffix_list, list):
                        suffix = suffix_list[0] if obj == "singular" else suffix_list[1]
                    else:
                        suffix = suffix_list

    if form == "independent" and neg == False:
        return base + styled_text(suffix, "green_normal")
    elif form == "independent" and neg == True:
        return base + styled_text(suffix, "red_normal")
    
    if form == "dependent" and neg == False:
        return base + styled_text(suffix, "green_italic")
    if form == "dependent" and neg == True:
        return base + styled_text(suffix, "red_italic")
    
    if form == "imperative" and neg == False:
        return base + styled_text(suffix, "green_bold")
    if form == "imperative" and neg == True:
        return base + styled_text(suffix, "red_bold")