import os

from sqlalchemy.engine import Engine
from dotenv import load_dotenv

from data_ingestion_pipeline.db import get_db_engine
from data_ingestion_pipeline.db import create_db
from .competitions import run_competitions_by_persons_of_country_pipeline
from .continents import run_continents_pipeline
from .countries import run_countries_pipeline
from .events import run_events_pipeline
from .formats import run_formats_pipeline
from .ranks_average import run_ranks_average_by_country_pipeline
from .ranks_single import run_ranks_single_by_country_pipeline
from .persons import run_persons_by_country_pipeline
from .results import run_results_by_country_pipeline
from .round_types import run_round_types_pipeline

load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST", "localhost")
PORT = int(os.getenv("DB_PORT", 3306))


def run_mexico_pipeline() -> None:
    """
    Run the data ingestion pipeline for Mexico.
    """

    print("Starting Mexico data ingestion pipeline...")

    DB_RAW: str = "wca"
    DB_MX: str = "wca_mexico"
    COUNTRY_ID: str = "Mexico"

    engine: Engine = get_db_engine(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        database=DB_RAW,
    )

    # --------- DB Creation for Mexico ----------
    create_db(database_name=DB_MX, engine=engine)

    # ---------- Competitions by Country Pipeline ----------
    run_competitions_by_persons_of_country_pipeline(
        engine=engine,
        country_id=COUNTRY_ID,
        target_db=DB_MX,
    )

    # ---------- Continents Pipeline ----------
    run_continents_pipeline(
        engine=engine,
        target_db=DB_MX,
    )

    # ---------- Countries Pipeline ----------
    run_countries_pipeline(
        engine=engine,
        target_db=DB_MX,
    )

    # ---------- Events Pipeline ----------
    run_events_pipeline(
        engine=engine,
        target_db=DB_MX,
    )

    # ---------- Formats Pipeline ----------
    run_formats_pipeline(
        engine=engine,
        target_db=DB_MX,
    )

    # ---------- Persons by Country Pipeline ----------
    run_persons_by_country_pipeline(
        engine=engine,
        country_id=COUNTRY_ID,
        target_db=DB_MX,
    )

    # ---------- Ranks Average by Country Pipeline ----------
    run_ranks_average_by_country_pipeline(
        engine=engine,
        country_id=COUNTRY_ID,
        target_db=DB_MX,
    )

    # ---------- Ranks Single by Country Pipeline ----------
    run_ranks_single_by_country_pipeline(
        engine=engine,
        country_id=COUNTRY_ID,
        target_db=DB_MX,
    )

    # ---------- Results by Country Pipeline ---------
    run_results_by_country_pipeline(
        engine=engine,
        country_id=COUNTRY_ID,
        target_db=DB_MX,
    )

    # ---------- Round Types Pipeline ----------
    run_round_types_pipeline(
        engine=engine,
        target_db=DB_MX,
    )

    # ---------- End of Pipeline ----------
    print("Mexico data ingestion pipeline completed!")
