import os
from pathlib import Path

import duckdb
import metaflow
from metaflow import FlowSpec
from metaflow.parameters import Parameter


class MysqlExampleFlow(FlowSpec):
    db_name = Parameter(
        "db-name",
        help="Database name",
        default="example",
        type=str,
    )

    db_schema_name = Parameter(
        "db-schema-name",
        help="Database schema name",
        default="source__mysql",
        type=str,
    )

    @metaflow.step
    def start(self):
        self.next(self.ingest)

    @metaflow.step
    def ingest(self):
        with duckdb.connect(
            database=Path(os.environ["DUCKDB_DIR"]) / f"{self.db_name}.db",
            read_only=False,
        ) as db:
            db.install_extension("mysql")
            db.load_extension("mysql")

            s = """
                CREATE OR REPLACE SECRET (
                    TYPE MYSQL,
                    HOST 'localhost',
                    PORT %(mysql_port)d,
                    DATABASE 'example',
                    USER 'root',
                    PASSWORD 'password'
                );

                ATTACH '' AS source (TYPE MYSQL);

                CREATE SCHEMA IF NOT EXISTS %(db_schema_name)s;

                CREATE OR REPLACE TABLE %(db_schema_name)s.user_roles AS
                    FROM source.user_roles;
                CREATE OR REPLACE TABLE %(db_schema_name)s.users AS
                    FROM source.users;
            """ % {
                "mysql_port": int(os.environ["MYSQL_PORT"]),
                "db_schema_name": self.db_schema_name,
            }
            db.execute(s)

        self.next(self.end)

    @metaflow.step
    def end(self):
        pass


if __name__ == "__main__":
    MysqlExampleFlow()
