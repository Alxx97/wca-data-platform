import pandas as pd
from sqlalchemy.engine import Engine

from data_ingestion_pipeline.extract import extract_continents
from data_ingestion_pipeline.load import load_df_to_db


def run_continents_pipeline(engine: Engine, target_db: str) -> None:
    """
    Run the data ingestion pipeline for WCA continents data.
    """

    print(f"Starting Continents data ingestion pipeline to {target_db}...")

    continents: pd.DataFrame = extract_continents(
        engine=engine,
    )

    load_df_to_db(
        df=continents,
        engine=engine,
        target_db=target_db,
        target_table="Continents",
        method="replace",
    )
