"""
Database connection and interaction module.
"""

import os

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


# Example usage
if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()

    db_engine = get_db_engine(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 3306)),
        database=os.getenv("DB_NAME"),
        echo=True,
    )
    print("Database engine created successfully:", db_engine)
