import pandas as pd
from sqlalchemy.engine import Engine


def extract_ranks_average_by_country(engine: Engine, country_id: str) -> pd.DataFrame:
    """
    Extracts average rank data from the database.

    Parameters
    ----------
    engine : Engine
        SQLAlchemy Engine instance connected to the database.
    country_id : str
        The country identifier to filter the ranks.

    Returns
    -------
    pd.DataFrame
        DataFrame containing average rank data.

    Note
    ----
    - This function retrieves average ranks from the 'RanksAverage' table
        where the 'countryId' matches the specified country.
    - If you want to extract average ranks for Mexican persons, set country_id='Mexico'.
    """

    query: str = f"""
    SELECT
        ra.*
    FROM
        RanksAverage ra
    WHERE
        ra.personId IN (SELECT id FROM Persons WHERE countryId = '{country_id}');
    """

    df: pd.DataFrame = pd.read_sql_query(query, engine)
    return df
