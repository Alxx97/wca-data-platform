import pandas as pd
from sqlalchemy.engine import Engine


def extract_events(engine: Engine) -> pd.DataFrame:
    """
    Extracts all events from the database.

    Parameters
    ----------
    engine : Engine
        SQLAlchemy Engine instance connected to the database.

    Returns
    -------
    pd.DataFrame
        DataFrame containing events data.

    Note
    ----
    - This function retrieves all records from the 'Events' table.
    """

    query: str = "SELECT * FROM wca.Events"

    df: pd.DataFrame = pd.read_sql_query(query, engine)
    return df