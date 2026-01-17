import pandas as pd
from sqlalchemy.engine import Engine


def extract_countries(engine: Engine) -> pd.DataFrame:
    """
    Extracts all countries from the database.

    Parameters
    ----------
    engine : Engine
        SQLAlchemy Engine instance connected to the database.

    Returns
    -------
    pd.DataFrame
        DataFrame containing countries data.

    Note
    ----
    - This function retrieves all records from the 'Countries' table.
    """

    query: str = "SELECT * FROM wca.Countries"

    df: pd.DataFrame = pd.read_sql_query(query, engine)
    return df
