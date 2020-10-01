from dotenv import find_dotenv, load_dotenv
from sqlalchemy import create_engine
import os

def get_db_engine():
    load_dotenv(find_dotenv())
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    connection_str = "postgresql+psycopg2://{0}:{1}@postgresdb/case_db".format(username, password)

    db_engine = create_engine(connection_str)

    return db_engine


def db_display():
    db_engine = get_db_engine()
    sql_qry = "SELECT * FROM PROD.test_table ORDER BY username;"
    result = db_engine.execute(sql_qry)
    print(result)


if __name__ == "__main__":
    db_display()