import os
from pathlib import Path

import duckdb
import streamlit
from plotly import express


def main():
    streamlit.set_page_config(
        page_title="Customers | Jaffle Shop",
    )

    streamlit.title("Customers")

    with duckdb.connect(
        database=Path(os.environ["SD_DATA_DIR"]) / "jaffle_shop.db",
        read_only=True,
    ) as db:
        df_customers = db.sql("SELECT * FROM mart__default.customers").to_df()

    tabs = streamlit.tabs([
        "Charts",
        "Data",
    ])

    with tabs[0]:
        figure = express.histogram(
            data_frame=df_customers,
            x="num_customer_lifetime_orders",
        )
        figure.update_layout(
            bargap=0.1,
            xaxis_title="Customer Lifetime Orders",
            yaxis_title="Customers",
        )

        streamlit.plotly_chart(figure)

    with tabs[1]:
        streamlit.dataframe(
            data=df_customers,
            use_container_width=True,
        )


main()
