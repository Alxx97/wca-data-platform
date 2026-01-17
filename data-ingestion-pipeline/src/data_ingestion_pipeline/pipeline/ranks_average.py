import pandas as pd
from sqlalchemy.engine import Engine

from data_ingestion_pipeline.extract import extract_ranks_average_by_country
from data_ingestion_pipeline.load import load_df_to_db


def run_ranks_average_by_country_pipeline(
    engine: Engine, country_id: str, target_db: str
) -> None:
    """
    Run the data ingestion pipeline for WCA-Country ranks average data.
    """

    print(f"Starting Ranks Average data ingestion pipeline for {country_id} to {target_db}...")

    ranks_average: pd.DataFrame = extract_ranks_average_by_country(
        engine=engine,
        country_id=country_id,
    )

    load_df_to_db(
        df=ranks_average,
        engine=engine,
        target_db=target_db,
        target_table="RanksAverage",
        method="replace",
    )
