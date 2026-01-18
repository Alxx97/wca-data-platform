import pandas as pd
from sqlalchemy.engine import Engine


def extract_round_types(engine: Engine) -> pd.DataFrame:
    """
    Extracts all round types from the database.

    Parameters
    ----------
    engine : Engine
        SQLAlchemy Engine instance connected to the database.

    Returns
    -------
    pd.DataFrame
        DataFrame containing round types data.

    Note
    ----
    - This function retrieves all records from the 'RoundTypes' table.
    """

    query: str = "SELECT * FROM wca.RoundTypes"

    df: pd.DataFrame = pd.read_sql_query(query, engine)
    return df
