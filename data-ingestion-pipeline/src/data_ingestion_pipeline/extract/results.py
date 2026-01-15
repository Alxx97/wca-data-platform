import pandas as pd
from sqlalchemy.engine import Engine

def extract_results_by_country(engine: Engine, country_id: str) -> pd.DataFrame:
    """
    Extracts results data from the database.

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
    - This function retrieves all records from the 'Results' table
        where the 'countryId' matches the specified country.
    - If you want to extract Mexican results, set country_id='Mexico'.
    """

    query: str = f"""
    SELECT
        r.*
    FROM Results r
    WHERE r.personCountryId = '{country_id}'
    """

    df: pd.DataFrame = pd.read_sql_query(query, engine)
    return df
