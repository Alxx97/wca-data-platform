"""
Module for data extraction.
"""

from .persons import extract_persons_by_country
from .results import extract_results_by_country


__all__ = [
    "extract_persons_by_country",
    "extract_results_by_country",
]