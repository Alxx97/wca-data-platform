import pandas as pd
from sqlalchemy.engine import Engine

from data_ingestion_pipeline.extract import extract_persons_by_country
from data_ingestion_pipeline.load import load_df_to_db


def run_persons_by_country_pipeline(
    engine: Engine, country_id: str, target_db: str
) -> None:
    """
    Run the data ingestion pipeline for WCA-Country persons data.
    """

    print(f"Starting {country_id} Persons data ingestion pipeline...")

    persons: pd.DataFrame = extract_persons_by_country(
        engine=engine,
        country_id=country_id,
    )

    load_df_to_db(
        df=persons,
        engine=engine,
        target_db=target_db,
        target_table="Persons",
        method="replace",
    )
