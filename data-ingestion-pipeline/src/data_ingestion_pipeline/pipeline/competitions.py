import pandas as pd
from sqlalchemy.engine import Engine

from data_ingestion_pipeline.extract import extract_competitions_by_persons_of_country
from data_ingestion_pipeline.load import load_df_to_db


def run_competitions_by_persons_of_country_pipeline(
    engine: Engine, country_id: str, target_db: str
) -> None:
    """
    Run the data ingestion pipeline for WCA-Country competitions data.
    """

    print(f"Starting {country_id} Competitions data ingestion pipeline...")

    competitions: pd.DataFrame = extract_competitions_by_persons_of_country(
        engine=engine,
        country_id=country_id,
    )

    load_df_to_db(
        df=competitions,
        engine=engine,
        target_db=target_db,
        target_table="Competitions",
        method="replace",
    )
