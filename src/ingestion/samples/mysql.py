import os
from pathlib import Path

import duckdb

DB_NAME = "sample.db"

DB_SCHEMA_NAME = "source__mysql"


def run():
    with duckdb.connect(
        database=Path(os.environ["SD_DATA_DIR"]) / DB_NAME,
        read_only=False,
    ) as db:
        db.install_extension("mysql")
        db.load_extension("mysql")

        create_secret(db)

        s = """
            ATTACH '' AS source (TYPE MYSQL);

            CREATE SCHEMA IF NOT EXISTS %(db_schema_name)s;

            CREATE OR REPLACE TABLE %(db_schema_name)s.user_roles AS
                FROM source.user_roles;
            CREATE OR REPLACE TABLE %(db_schema_name)s.users AS
                FROM source.users;
        """ % {
            "db_schema_name": DB_SCHEMA_NAME,
        }
        db.execute(s)


def create_secret(db):
    s = """
        CREATE OR REPLACE SECRET (
            TYPE MYSQL,
            HOST 'localhost',
            PORT %(mysql_port)d,
            DATABASE 'sample',
            USER 'root',
            PASSWORD 'password'
        );
    """ % {
        "mysql_port": int(os.environ["MYSQL_PORT"]),
    }
    db.execute(s)


if __name__ == "__main__":
    run()
