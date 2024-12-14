import os
from pathlib import Path

import duckdb
import streamlit
from plotly import express


def main():
    streamlit.set_page_config(
        page_title="Orders | Jaffle Shop",
    )

    streamlit.title("Orders")

    with duckdb.connect(
        database=Path(os.environ["SD_DATA_DIR"]) / "jaffle_shop.db",
        read_only=True,
    ) as db:
        df_orders = db.sql("SELECT * FROM mart__default.orders").to_df()

    tabs = streamlit.tabs([
        "Charts",
        "Data",
    ])

    with tabs[0]:
        render_chart(df_orders)

    with tabs[1]:
        streamlit.dataframe(
            data=df_orders,
            use_container_width=True,
        )


def render_chart(df_orders):
    figure = express.histogram(
        data_frame=df_orders,
        x="num_order_items",
    )
    figure.update_layout(
        bargap=0.1,
        xaxis_title="Order Items",
        yaxis_title="Orders",
    )

    streamlit.plotly_chart(figure)


main()
