import os
from pathlib import Path

import duckdb
import kagglehub

DB_NAME = "kaggle.db"

DB_SCHEMA_NAME = "main"

KAGGLE_DATASET_HANDLE = "michau96/internet-search-engine-worldwide"

KAGGLE_DATASET_ENTRIES = {
    "search_engine_data.csv": {
        "db_table_name": "search_engine_popularity_reports",
    }
}


def run():
    with duckdb.connect(
        database=Path(os.environ["SD_DATA_DIR"]) / DB_NAME,
        read_only=False,
    ) as db:
        kaggle_dataset_dir_path = kagglehub.dataset_download(KAGGLE_DATASET_HANDLE)

        for e in KAGGLE_DATASET_ENTRIES.keys():
            s = """
                CREATE SCHEMA IF NOT EXISTS %(db_schema_name)s;

                CREATE OR REPLACE TABLE %(db_schema_name)s.%(db_table_name)s AS
                    FROM '%(dataset_entry_path)s'
                ;
            """ % {
                "db_schema_name": DB_SCHEMA_NAME,
                "db_table_name": KAGGLE_DATASET_ENTRIES[e]["db_table_name"],
                "dataset_entry_path": Path(kaggle_dataset_dir_path) / e,
            }
            db.execute(s)


if __name__ == "__main__":
    run()
