import os

from data_ingestion_pipeline.db import get_db_engine
import pandas as pd
import time
from dotenv import load_dotenv
from sqlalchemy.engine import Engine


load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST", "localhost")
PORT = int(os.getenv("DB_PORT", 3306))

def main() -> None:

    database_name: str = "wca"
    engine: Engine = get_db_engine(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        database=database_name,
    )

    # First query: Using CTE + JOIN
    query_1 = """
    WITH persons_from_mexico AS (
    SELECT id FROM wca.Persons p
    WHERE p.countryId = 'Mexico'
    )

    SELECT ra.*
    FROM wca.RanksAverage ra
    JOIN persons_from_mexico pm
    ON ra.personId = pm.id;
    """

    # Second query: Using CTE + IN Subquery
    query_2 = """
    WITH persons_from_mexico AS (
    SELECT id FROM wca.Persons p
    WHERE p.countryId = 'Mexico'
    )

    SELECT ra.*
    FROM wca.RanksAverage ra
    WHERE ra.personId IN (SELECT id FROM persons_from_mexico);
    """

    # Third query: Direct IN Subquery
    query_3 = """
    SELECT ra.*
    FROM wca.RanksAverage ra
    WHERE ra.personId IN (
        SELECT p.id
        FROM wca.Persons p
        WHERE p.countryId = 'Mexico'
    );
    """

    times: dict[str, float] = {}

    for i, (query, query_name) in enumerate(
        [
            (query_1, "CTE + JOIN"),
            (query_2, "CTE + IN Subquery"),
            (query_3, "Direct IN Subquery"),
        ],
        start=1,
    ):
        start_time = time.time()
        df: pd.DataFrame = pd.read_sql_query(query, con=engine)
        end_time = time.time()
        elapsed_time = end_time - start_time
        times[query_name] = elapsed_time
        print(f"Query {i} ({query_name}) returned {len(df)} rows in {elapsed_time:.4f} seconds.")
    
    print("\nSummary of execution times:")
    for query_name, elapsed_time in times.items():
        print(f"{query_name}: {elapsed_time:.4f} seconds")

    # You can find that typically the "Direct IN Subquery" performs the best.

if __name__ == "__main__":
    main()