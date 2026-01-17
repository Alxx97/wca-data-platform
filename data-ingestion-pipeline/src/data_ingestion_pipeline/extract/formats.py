import pandas as pd
from sqlalchemy.engine import Engine


def extract_formats(engine: Engine) -> pd.DataFrame:
    """
    Extracts all formats from the database.

    Parameters
    ----------
    engine : Engine
        SQLAlchemy Engine instance connected to the database.

    Returns
    -------
    pd.DataFrame
        DataFrame containing formats data.

    Note
    ----
    - This function retrieves all records from the 'Formats' table.
    """

    query: str = "SELECT * FROM wca.Formats"

    df: pd.DataFrame = pd.read_sql_query(query, engine)
    return df
