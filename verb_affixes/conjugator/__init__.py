# conjugator/__init__.py

from .vii_suffixes_core import get_vii_suffix
from .vai_suffixes_core import get_vai_suffix
from .vti_suffixes_core import get_vti_suffix
from .models import ConjugationInput
from .utils import styled_text

__all__ = ["get_vii_suffix",
           "get_vai_suffix",
           "get_vti_suffix",
           "ConjugationInput",
           "styled_text"]