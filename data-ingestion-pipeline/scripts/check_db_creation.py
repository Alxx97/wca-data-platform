from sqlalchemy.engine import Engine
from sqlalchemy import text
from data_ingestion_pipeline.db import get_db_engine
from data_ingestion_pipeline.db import create_db
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

    create_db(database_name="wca_mexico", engine=engine)

    with engine.connect() as connection:
        print("Connected to the database successfully.")

        result = connection.execute(text("SHOW DATABASES;"))
        dbs = [row[0] for row in result]

        print(f"Databases in the server:")
        for db in dbs:
            print(f"- {db}")
    
if __name__ == "__main__":
    main()
