import os
from pathlib import Path

import duckdb
import streamlit
from plotly import express


def main():
    streamlit.set_page_config(
        page_title="Supply Costs | Jaffle Shop",
    )

    streamlit.title("Supply Costs")

    with duckdb.connect(
        database=Path(os.environ["SD_DATA_DIR"]) / "jaffle_shop.db",
        read_only=True,
    ) as db:
        df_supply_costs = db.sql("SELECT * FROM mart__default.supply_costs").to_df()

    tabs = streamlit.tabs([
        "Charts",
        "Data",
    ])

    with tabs[0]:
        figure = express.histogram(
            data_frame=df_supply_costs,
            x="supply_cost",
        )
        figure.update_layout(
            bargap=0.1,
            xaxis_title="Supply Cost",
            yaxis_title="Supplies",
        )

        streamlit.plotly_chart(figure)

    with tabs[1]:
        streamlit.dataframe(
            data=df_supply_costs,
            use_container_width=True,
        )


main()
