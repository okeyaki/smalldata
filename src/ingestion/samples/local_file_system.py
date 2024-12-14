import os
from pathlib import Path

import duckdb

DB_NAME = "sample.db"

DB_SCHEMA_NAME = "source__local_file"


def run():
    with duckdb.connect(
        database=Path(os.environ["SD_DATA_DIR"]) / DB_NAME,
        read_only=False,
    ) as db:
        s = """
            CREATE SCHEMA IF NOT EXISTS %(db_schema_name)s;

            CREATE OR REPLACE TABLE %(db_schema_name)s.first AS
                FROM 'etc/smalldata/samples/local_files/first.jsonl'
            ;
            CREATE OR REPLACE TABLE %(db_schema_name)s.second AS
                FROM 'etc/smalldata/samples/local_files/second.jsonl'
            ;
            CREATE OR REPLACE TABLE %(db_schema_name)s.third AS
                FROM 'etc/smalldata/samples/local_files/third.jsonl'
            ;
        """ % {
            "db_schema_name": DB_SCHEMA_NAME,
        }
        db.execute(s)


if __name__ == "__main__":
    run()
