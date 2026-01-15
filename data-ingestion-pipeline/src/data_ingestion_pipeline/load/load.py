import pandas as pd
from sqlalchemy.engine import Engine


def load_df_to_db(
    df: pd.DataFrame,
    engine: Engine,
    target_db: str,
    target_table: str,
    method: str = "replace",
) -> None:
    """
    Load data from a DataFrame into a specified database table.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the data to be loaded.
    engine : Engine
        The SQLAlchemy engine connected to the target database.
    target_db : str
        The name of the target database.
    target_table : str
        The name of the target table within the database.
    method : str, optional
        The method to use when inserting data ('replace', 'append', etc.), by default 'replace'.

    Returns
    -------
    None

    Notes
    -----
    - This function uses pandas' to_sql method to load data into the database.
    - If table does not exist, it will be created.
    """

    df.to_sql(
        name=target_table,
        con=engine,
        schema=target_db,
        if_exists=method,
        index=False,
        chunksize=1000,
        method="multi",
    )
