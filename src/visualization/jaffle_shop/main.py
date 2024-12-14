import os
from pathlib import Path

import duckdb
import streamlit

streamlit.set_page_config(
    page_title="Jaffle Shop",
)

streamlit.title("Jaffle Shop")

with duckdb.connect(
    database=Path(os.environ["SD_DATA_DIR"]) / "jaffle_shop.db",
    read_only=True,
) as db:
    columns = streamlit.columns(2)
    with columns[0]:
        streamlit.header("Customers")

        df_customers = db.sql("SELECT * FROM mart.customers").to_df()

        streamlit.dataframe(df_customers)

    with columns[1]:
        streamlit.header("Products")

        df_orders = db.sql("SELECT * FROM mart.products").to_df()

        streamlit.dataframe(df_orders)
