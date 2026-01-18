import pandas as pd
from sqlalchemy.engine import Engine

from data_ingestion_pipeline.extract import extract_scrambles_by_persons_of_country
from data_ingestion_pipeline.load import load_df_to_db


def run_scrambles_by_persons_of_country_pipeline(
    engine: Engine, country_id: str, target_db: str
) -> None:
    """
    Run the data ingestion pipeline for WCA-Country scrambles data.
    """

    print(f"Starting Scrambles data ingestion pipeline for {country_id} to {target_db}...")

    scrambles: pd.DataFrame = extract_scrambles_by_persons_of_country(
        engine=engine,
        country_id=country_id,
    )

    load_df_to_db(
        df=scrambles,
        engine=engine,
        target_db=target_db,
        target_table="Scrambles",
        method="replace",
    )
    