import pandas as pd
from sqlalchemy.engine import Engine


def extract_scrambles_by_persons_of_country(
    engine: Engine, country_id: str
) -> pd.DataFrame:
    """
    Extracts all scrambles for a specific competition.

    Parameters
    ----------
    engine : Engine
        SQLAlchemy Engine instance connected to the database.
    competition_id : str
        The competition identifier to filter results.

    Returns
    -------
    pd.DataFrame
        DataFrame containing scrambles data.

    Note
    ----
    - This function retrieves all records from the 'Scrambles' table
        where the competitionId matches the specified competition_id.
    - If you want to extract scrambles for a competition with ID '2023TEST', set competition_id='2023TEST'.
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
        s.*
    FROM
        wca.Scrambles s
    WHERE
        s.competitionId IN (SELECT competitionId FROM competitions_by_persons_country);
    """

    df: pd.DataFrame = pd.read_sql(query, engine)
    return df
