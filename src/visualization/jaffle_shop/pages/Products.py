import os
from pathlib import Path

import duckdb
import streamlit
from plotly import express


def main():
    streamlit.set_page_config(
        page_title="Products | Jaffle Shop",
    )

    streamlit.title("Products")

    with duckdb.connect(
        database=Path(os.environ["SD_DATA_DIR"]) / "jaffle_shop.db",
        read_only=True,
    ) as db:
        df_products = db.sql("SELECT * FROM mart__default.products").to_df()

    tabs = streamlit.tabs([
        "Charts",
        "Data",
    ])

    with tabs[0]:
        f = express.pie(
            title="The number of products per product type",
            data_frame=df_products,
            names="product_type",
        )
        f.update_traces(
            textinfo="value+label",
            textposition="inside",
        )
        streamlit.plotly_chart(f)

        f = express.histogram(
            title="The number of products per product price range",
            data_frame=df_products,
            x="product_price",
        )
        f.update_layout(
            bargap=0.1,
            xaxis_title="Product price",
            yaxis_title="Products",
        )

        streamlit.plotly_chart(f)

    with tabs[1]:
        streamlit.dataframe(
            data=df_products,
            use_container_width=True,
        )


main()
