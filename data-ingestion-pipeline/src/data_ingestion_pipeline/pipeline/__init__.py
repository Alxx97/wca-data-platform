"""
Module for data ingestion pipelines.
"""

from .continents import run_continents_pipeline
from .competitions import run_competitions_by_persons_of_country_pipeline
from .countries import run_countries_pipeline
from .events import run_events_pipeline
from .formats import run_formats_pipeline
from .mexico import run_mexico_pipeline
from .persons import run_persons_by_country_pipeline
from .results import run_results_by_country_pipeline

__all__ = [
    "run_continents_pipeline",
    "run_competitions_by_persons_of_country_pipeline",
    "run_countries_pipeline",
    "run_events_pipeline",
    "run_formats_pipeline",
    "run_mexico_pipeline",
    "run_persons_by_country_pipeline",
    "run_results_by_country_pipeline",
]
