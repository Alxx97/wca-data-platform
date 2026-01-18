"""
Database connection and interaction module.
"""

from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def get_db_engine(
    user: str,
    password: str,
    host: str,
    port: int,
    database: str,
    echo: bool = False,
):
    """
    Create a SQLAlchemy engine for a MariaDB database.

    Parameters
    --------
    user : str
        Database username.
    password: str
        Database password.
    host : str
        Database host address.
    port : int
        Database port number.
    database : str
        Database name.
    echo : bool, optional
        If True, SQLAlchemy will log all SQL statements.

    Returns
    -------
    Engine
        SQLAlchemy engine instance.
    """
    if not all([user, password, host, port, database]):
        raise ValueError("All database connection parameters must be provided.")

    connection_string: str = (
        f"mysql+pymysql://{user}:{password}" f"@{host}:{port}/{database}"
    )

    engine: Engine = create_engine(
        connection_string,
        echo=echo,
        pool_pre_ping=True,
    )

    return engine

def create_db(database_name: str, engine: Engine) -> None:
    """
    Create a new database if it does not exist.

    Parameters
    ----------
    database_name : str
        Name of the database to create.
    engine : Engine
        SQLAlchemy engine instance.
    """

    query = text(f"CREATE DATABASE IF NOT EXISTS {database_name};")

    # We use begin() instead of connect() to ensure the command
    # is executed in a transaction
    with engine.begin() as connection:
        connection.execute(query)
