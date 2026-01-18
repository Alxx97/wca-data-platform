import pandas as pd
from sqlalchemy.engine import Engine


def extract_ranks_single_by_country(engine: Engine, country_id: str) -> pd.DataFrame:
    """
    Extracts single rank data from the database.

    Parameters
    ----------
    engine : Engine
        SQLAlchemy Engine instance connected to the database.
    country_id : str
        The country identifier to filter the ranks.

    Returns
    -------
    pd.DataFrame
        DataFrame containing single rank data.

    Note
    ----
    - This function retrieves single ranks from the 'RanksSingle' table
        where the 'countryId' matches the specified country.
    - If you want to extract single ranks for Mexican persons, set country_id='Mexico'.
    """

    query: str = f"""
    SELECT
        rs.*
    FROM
        RanksSingle rs
    WHERE
        rs.personId IN (SELECT id FROM Persons WHERE countryId = '{country_id}');
    """

    df: pd.DataFrame = pd.read_sql_query(query, engine)
    return df
