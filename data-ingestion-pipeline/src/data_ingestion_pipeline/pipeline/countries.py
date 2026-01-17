import pandas as pd
from sqlalchemy.engine import Engine

from data_ingestion_pipeline.extract import extract_countries
from data_ingestion_pipeline.load import load_df_to_db


def run_countries_pipeline(engine: Engine, target_db: str) -> None:
    """
    Run the data ingestion pipeline for WCA countries data.
    """

    print("Starting Countries data ingestion pipeline...")

    countries: pd.DataFrame = extract_countries(
        engine=engine,
    )

    load_df_to_db(
        df=countries,
        engine=engine,
        target_db=target_db,
        target_table="Countries",
        method="replace",
    )
