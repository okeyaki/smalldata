import os
from pathlib import Path

import duckdb


def run():
    """
    This function ingests the Jaffle Shop dataset into the DuckDB database.
    """

    with duckdb.connect(
        database=Path(os.environ["SD_DATA_DIR"]) / "jaffle_shop.db",
        read_only=False,
    ) as db:
        db.execute("""
            CREATE SCHEMA IF NOT EXISTS source;

            CREATE OR REPLACE TABLE source.customers AS
                FROM 'https://raw.githubusercontent.com/dbt-labs/jaffle-shop-data/refs/heads/main/jaffle-data/raw_customers.csv';
            CREATE OR REPLACE TABLE source.items AS
                FROM 'https://raw.githubusercontent.com/dbt-labs/jaffle-shop-data/refs/heads/main/jaffle-data/raw_items.csv';
            CREATE OR REPLACE TABLE source.products AS
                FROM 'https://raw.githubusercontent.com/dbt-labs/jaffle-shop-data/refs/heads/main/jaffle-data/raw_products.csv';
            CREATE OR REPLACE TABLE source.orders AS
                FROM 'https://raw.githubusercontent.com/dbt-labs/jaffle-shop-data/refs/heads/main/jaffle-data/raw_orders.csv';
            CREATE OR REPLACE TABLE source.stores AS
                FROM 'https://raw.githubusercontent.com/dbt-labs/jaffle-shop-data/refs/heads/main/jaffle-data/raw_stores.csv';
            CREATE OR REPLACE TABLE source.supplies AS
                FROM 'https://raw.githubusercontent.com/dbt-labs/jaffle-shop-data/refs/heads/main/jaffle-data/raw_supplies.csv';
        """)


if __name__ == "__main__":
    run()
