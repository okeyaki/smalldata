import os
from pathlib import Path

import duckdb
import streamlit


def main():
    streamlit.set_page_config(
        page_title="Order Items | Jaffle Shop",
    )

    streamlit.title("Order Items")

    with duckdb.connect(
        database=Path(os.environ["SD_DATA_DIR"]) / "jaffle_shop.db",
        read_only=True,
    ) as db:
        df_order_items = db.sql("SELECT * FROM mart__default.order_items").to_df()

    tabs = streamlit.tabs([
        "Charts",
        "Data",
    ])

    with tabs[0]:
        streamlit.warning("WIP")

    with tabs[1]:
        streamlit.dataframe(
            data=df_order_items,
            use_container_width=True,
        )


main()
