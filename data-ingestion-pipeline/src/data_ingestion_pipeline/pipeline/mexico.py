import os

import pandas as pd
from dotenv import load_dotenv

from data_ingestion_pipeline.db import create_db, get_db_engine
from data_ingestion_pipeline.extract import extract_persons_by_country
from data_ingestion_pipeline.load import load_df_to_db

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

    engine = get_db_engine(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        database=DB_RAW,
    )

    create_db(database_name=DB_MX, engine=engine)

    persons: pd.DataFrame = extract_persons_by_country(
        engine=engine,
        country_id="Mexico",
    )

    load_df_to_db(
        df=persons,
        engine=engine,
        target_db=DB_MX,
        target_table="persons",
        method="replace",
    )

    print("Mexico data ingestion pipeline completed successfully.")
