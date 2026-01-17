"""
Module for data extraction.
"""

from .competitions import extract_competitions_by_persons_of_country
from .continents import extract_continents
from .persons import extract_persons_by_country
from .results import extract_results_by_country

__all__ = [
    "extract_competitions_by_persons_of_country",
    "extract_continents",
    "extract_persons_by_country",
    "extract_results_by_country",
]