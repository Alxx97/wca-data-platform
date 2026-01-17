import pandas as pd

from sqlalchemy.engine import Engine
from data_ingestion_pipeline.db import create_db
from data_ingestion_pipeline.extract import extract_results_by_country
from data_ingestion_pipeline.load import load_df_to_db

def run_results_by_country_pipeline(engine: Engine, country_id: str, db_country: str) -> None:
    """
    Run the data ingestion pipeline for WCA-Country results data.
    """

    print(f"Starting {country_id} Results data ingestion pipeline...")

    create_db(database_name=db_country, engine=engine)

    results: pd.DataFrame = extract_results_by_country(
        engine=engine,
        country_id=country_id,
    )

    load_df_to_db(
        df=results,
        engine=engine,
        target_db=db_country,
        target_table="Results",
        method="replace",
    )