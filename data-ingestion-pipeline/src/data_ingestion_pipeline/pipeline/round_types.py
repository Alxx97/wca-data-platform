import pandas as pd
from sqlalchemy.engine import Engine

from data_ingestion_pipeline.extract import extract_round_types
from data_ingestion_pipeline.load import load_df_to_db


def run_round_types_pipeline(engine: Engine, target_db: str) -> None:
    """
    Run the data ingestion pipeline for WCA round types data.
    """

    print(f"Starting Round Types data ingestion pipeline to {target_db}...")

    round_types: pd.DataFrame = extract_round_types(
        engine=engine,
    )

    load_df_to_db(
        df=round_types,
        engine=engine,
        target_db=target_db,
        target_table="RoundTypes",
        method="replace",
    )
