import pandas as pd
from sqlalchemy.engine import Engine

from data_ingestion_pipeline.extract import extract_championships_by_persons_of_country
from data_ingestion_pipeline.load import load_df_to_db


def run_championships_by_persons_of_country_pipeline(
    engine: Engine, country_id: str, target_db: str
) -> None:
    """
    Run the data ingestion pipeline for WCA-Country championships data.
    """

    print(f"Starting Championships data ingestion pipeline for {country_id} to {target_db}...")

    championships: pd.DataFrame = extract_championships_by_persons_of_country(
        engine=engine,
        country_id=country_id,
    )

    load_df_to_db(
        df=championships,
        engine=engine,
        target_db=target_db,
        target_table="championships",
        method="replace",
    )
