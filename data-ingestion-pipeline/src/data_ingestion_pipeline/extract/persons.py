import pandas as pd
from sqlalchemy.engine import Engine


def extract_persons_by_country(engine: Engine, country_id: str) -> pd.DataFrame:
    """
    Extracts person data from the database.

    Parameters
    ----------
    engine : Engine
        SQLAlchemy Engine instance connected to the database.

    Returns
    -------
    pd.DataFrame
        DataFrame containing person data.

    Note
    ----
    - This function retrieves all records from the 'Persons' table
        where the 'countryId' matches the specified country.
    - If you want to extract Mexican persons, set country_id='Mexico'.
    """

    query: str = f"""
    SELECT
        *
    FROM
        Persons
    WHERE
        countryId = '{country_id}'
    """

    df: pd.DataFrame = pd.read_sql_query(query, engine)
    return df
