"""
Module for data ingestion pipelines.
"""

from .continents import run_continents_pipeline
from .competitions import run_competitions_by_persons_of_country_pipeline
from .mexico import run_mexico_pipeline
from .persons import run_persons_by_country_pipeline
from .results import run_results_by_country_pipeline

__all__ = [
    "run_continents_pipeline",
    "run_competitions_by_persons_of_country_pipeline",
    "run_mexico_pipeline",
    "run_persons_by_country_pipeline",
    "run_results_by_country_pipeline",
]
