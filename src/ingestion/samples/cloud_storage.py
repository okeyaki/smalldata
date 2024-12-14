import os
from pathlib import Path

import duckdb

DB_NAME = "sample.db"

DB_SCHEMA_NAME = "source__aws_s3"


def run():
    with duckdb.connect(
        database=Path(os.environ["SD_DATA_DIR"]) / DB_NAME,
        read_only=False,
    ) as db:
        create_secret(db)

        s = """
            CREATE SCHEMA IF NOT EXISTS %(db_schema_name)s;

            CREATE OR REPLACE TABLE %(db_schema_name)s.first AS
                FROM 's3://default/samples/first.jsonl'
            ;
            CREATE OR REPLACE TABLE %(db_schema_name)s.second AS
                FROM 's3://default/samples/second.jsonl'
            ;
            CREATE OR REPLACE TABLE %(db_schema_name)s.third AS
                FROM 's3://default/samples/third.jsonl'
            ;
        """ % {
            "db_schema_name": DB_SCHEMA_NAME,
        }
        db.execute(s)


def create_secret(db):
    s = """
        CREATE OR REPLACE SECRET sample (
            TYPE S3,
            REGION 'us-east-1',
            KEY_ID '%(s3_access_key_id)s',
            SECRET  '%(s3_secret_access_key)s',
            ENDPOINT 'localhost:%(s3_port)s',
            URL_STYLE 'path',
            USE_SSL FALSE
        );
    """ % {
        "s3_access_key_id": os.environ["MINIO_ROOT_USER"],
        "s3_secret_access_key": os.environ["MINIO_ROOT_PASSWORD"],
        "s3_port": os.environ["MINIO_PORT"],
    }
    _ = db.execute(s)


if __name__ == "__main__":
    run()
