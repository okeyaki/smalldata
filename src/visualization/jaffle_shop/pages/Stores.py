import os
from pathlib import Path

import duckdb
import streamlit


def main():
    streamlit.set_page_config(
        page_title="Stores | Jaffle Shop",
    )

    streamlit.title("Stores")

    with duckdb.connect(
        database=Path(os.environ["SD_DATA_DIR"]) / "jaffle_shop.db",
        read_only=True,
    ) as db:
        df_stores = db.sql("SELECT * FROM mart__default.stores").to_df()

    tabs = streamlit.tabs([
        "Charts",
        "Data",
    ])

    with tabs[0]:
        streamlit.warning("WIP")

    with tabs[1]:
        streamlit.dataframe(
            data=df_stores,
            use_container_width=True,
        )


main()
