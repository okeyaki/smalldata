import os
from pathlib import Path

import duckdb

DATASET_BASE_URL = "https://raw.githubusercontent.com/dbt-labs/jaffle-shop-data/refs/heads/main/jaffle-data"


def run():
    """
    This function ingests the Jaffle Shop dataset.
    """

    with duckdb.connect(
        database=Path(os.environ["SD_DATA_DIR"]) / "jaffle_shop.db",
        read_only=False,
    ) as db:
        s = """
            CREATE SCHEMA IF NOT EXISTS source;

            CREATE OR REPLACE TABLE source.customers AS
                FROM '%(dataset_base_url)s/raw_customers.csv';
            CREATE OR REPLACE TABLE source.items AS
                FROM '%(dataset_base_url)s/raw_items.csv';
            CREATE OR REPLACE TABLE source.products AS
                FROM '%(dataset_base_url)s/raw_products.csv';
            CREATE OR REPLACE TABLE source.orders AS
                FROM '%(dataset_base_url)s/raw_orders.csv';
            CREATE OR REPLACE TABLE source.stores AS
                FROM '%(dataset_base_url)s/raw_stores.csv';
            CREATE OR REPLACE TABLE source.supplies AS
                FROM '%(dataset_base_url)s/raw_supplies.csv';
        """ % {
            "dataset_base_url": DATASET_BASE_URL,
        }
        db.execute(s)


if __name__ == "__main__":
    run()
