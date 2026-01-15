from sqlalchemy import text
from sqlalchemy.engine import Engine
from data_ingestion_pipeline.db import get_db_engine
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST", "localhost")
PORT = int(os.getenv("DB_PORT", 3306))


def main() -> None:
    """
    Basic script for checking database connection.
    """

    database_name: str = "wca"
    engine: Engine = get_db_engine(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        database=database_name,
    )

    with engine.connect() as connection:
        print("Connected to the database successfully.")

        result = connection.execute(text("SHOW TABLES;"))
        tables = [row[0] for row in result]

        print(f"Tables in the '{database_name}' database:")
        for table in tables:
            print(f"- {table}")

if __name__ == "__main__":
    main()
