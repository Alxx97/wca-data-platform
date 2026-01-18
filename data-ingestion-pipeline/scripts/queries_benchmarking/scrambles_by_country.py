import os
import time

import pandas as pd
from data_ingestion_pipeline.db import get_db_engine
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
    WITH persons_by_country AS (
        SELECT id FROM wca.Persons p
        WHERE p.countryId = 'Mexico'
    ),
    competitions_by_persons_country AS (
    SELECT DISTINCT r.competitionId AS competitionId
    FROM wca.Results r
    JOIN persons_by_country pc
    ON r.personId = pc.id
    )

    SELECT 
    s.*
    FROM
    wca.Scrambles s
    JOIN competitions_by_persons_country cc
    ON s.competitionId = cc.competitionId;
    """

    # Second query: Using CTE + IN Subquery
    query_2 = """
    WITH persons_by_country AS (
        SELECT id FROM wca.Persons p
        WHERE p.countryId = 'Mexico'
    ),
    competitions_by_persons_country AS (
    SELECT DISTINCT r.competitionId AS competitionId
    FROM wca.Results r
    JOIN persons_by_country pc
    ON r.personId = pc.id
    )

    SELECT
    s.*
    FROM
    wca.Scrambles s
    WHERE s.competitionId IN (
        SELECT competitionId FROM competitions_by_persons_country
    );
    """

    # Third query: Direct IN Subquery
    query_3 = """
    SELECT
    s.*
    FROM
    wca.Scrambles s
    WHERE s.competitionId IN (
        SELECT DISTINCT r.competitionId AS competitionId
        FROM wca.Results r
        WHERE r.personId IN (
            SELECT p.id
            FROM wca.Persons p
            WHERE p.countryId = 'Mexico'
        )
    );
    """
    times = {}

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
        print(
            f"Query {i} ({query_name}) returned {len(df)} rows in {elapsed_time:.4f} seconds."
        )

    print("\nSummary of execution times:")
    for query_name, elapsed_time in times.items():
        print(f"{query_name}: {elapsed_time:.4f} seconds")

    # You can confirm that all queries return the same number of rows,
    # but the second and third query is expected to be the fastest.
    # We use the second query in the main pipeline for clarity.

if __name__ == "__main__":
    main()
