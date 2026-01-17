import pandas as pd
from sqlalchemy.engine import Engine

from data_ingestion_pipeline.extract import extract_events
from data_ingestion_pipeline.load import load_df_to_db

def run_events_pipeline(engine: Engine, target_db: str) -> None:
    """
    Run the data ingestion pipeline for WCA events data.
    """

    print(f"Starting Events data ingestion pipeline to {target_db}...")

    events: pd.DataFrame = extract_events(
        engine=engine,
    )

    load_df_to_db(
        df=events,
        engine=engine,
        target_db=target_db,
        target_table="Events",
        method="replace",
    )
