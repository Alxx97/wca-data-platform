import pandas as pd
from sqlalchemy.engine import Engine


def extract_continents(engine: Engine) -> pd.DataFrame:
    """
    Extracts all continents from the database.

    Parameters
    ----------
    engine : Engine
        SQLAlchemy Engine instance connected to the database.

    Returns
    -------
    pd.DataFrame
        DataFrame containing continents data.

    Note
    ----
    - This function retrieves all records from the 'Continents' table.
    """

    query: str = "SELECT * FROM wca.Continents"

    df: pd.DataFrame = pd.read_sql_query(query, engine)
    return df
