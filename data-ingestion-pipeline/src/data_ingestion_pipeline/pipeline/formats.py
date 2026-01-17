import pandas as pd
from sqlalchemy.engine import Engine

from data_ingestion_pipeline.extract import extract_formats
from data_ingestion_pipeline.load import load_df_to_db


def run_formats_pipeline(engine: Engine, target_db: str) -> None:
    """
    Run the data ingestion pipeline for WCA formats data.
    """

    print(f"Starting Formats data ingestion pipeline to {target_db}...")

    formats: pd.DataFrame = extract_formats(
        engine=engine,
    )

    load_df_to_db(
        df=formats,
        engine=engine,
        target_db=target_db,
        target_table="Formats",
        method="replace",
    )
