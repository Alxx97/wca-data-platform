import pandas as pd
from sqlalchemy.engine import Engine


def extract_championships_by_persons_of_country(
    engine: Engine, country_id: str
) -> pd.DataFrame:
    """
    Extracts all championships where persons from a specific country have participated.

    Parameters
    ----------
    engine : Engine
        SQLAlchemy Engine instance connected to the database.
    country_id : str
        The country identifier to filter results.

    Returns
    -------
    pd.DataFrame
        DataFrame containing results data.

    Note
    ----
    - This function retrieves all records from the 'Championships' table
        where the championship includes persons from the specified country.
    - If you want to extract championships involving Mexican persons, set country_id='Mexico'.
    """

    query: str = f"""
    WITH
    persons_by_country AS (
        SELECT
            id
        FROM
            wca.Persons p
        WHERE
            p.countryId = '{country_id}'
    ),
    competitions_by_persons_country AS (
        SELECT
            DISTINCT r.competitionId AS competitionId
        FROM
            wca.Results r
            JOIN persons_by_country pc
            ON r.personId = pc.id
    )

    SELECT
        ch.*
    FROM
        wca.Championships ch
    WHERE
        ch.competition_id IN (SELECT competitionId FROM competitions_by_persons_country);
    """

    df: pd.DataFrame = pd.read_sql_query(query, engine)
    return df
