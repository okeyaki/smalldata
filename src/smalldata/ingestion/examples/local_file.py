import os
from pathlib import Path

import duckdb
import metaflow
from metaflow import FlowSpec
from metaflow.parameters import Parameter


class LocalFileExampleFlow(FlowSpec):
    db_name = Parameter(
        "db-name",
        help="Database name",
        default="example",
        type=str,
    )

    db_schema_name = Parameter(
        "db-schema-name",
        help="Database schema name",
        default="source__local_file",
        type=str,
    )

    @metaflow.step
    def start(self):
        self.next(self.ingest)

    @metaflow.step
    def ingest(self):
        with duckdb.connect(
            database=Path(os.environ["DUCKDB_DIR"]) / "example.db",
            read_only=False,
        ) as db:
            s = """
                CREATE SCHEMA IF NOT EXISTS %(db_schema_name)s;

                CREATE OR REPLACE TABLE %(db_schema_name)s.first AS
                    SELECT *
                    FROM
                        READ_JSON('etc/metaflow/examples/local_files/first.jsonl')
                ;
                CREATE OR REPLACE TABLE %(db_schema_name)s.second AS
                    SELECT *
                    FROM
                        READ_JSON('etc/metaflow/examples/local_files/second.jsonl')
                ;
                CREATE OR REPLACE TABLE %(db_schema_name)s.third AS
                    SELECT *
                    FROM
                        READ_JSON('etc/metaflow/examples/local_files/third.jsonl')
                ;
            """ % {
                "db_schema_name": self.db_schema_name,
            }
            db.execute(s)

        self.next(self.end)

    @metaflow.step
    def end(self):
        pass


if __name__ == "__main__":
    LocalFileExampleFlow()
