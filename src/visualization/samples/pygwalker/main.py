import os
from pathlib import Path

import duckdb
import streamlit
from pygwalker.api.streamlit import StreamlitRenderer


@streamlit.cache_resource
def get_pygwalker_renderer(
    db_name: str,
    db_query: str,
) -> StreamlitRenderer:
    db = duckdb.connect(
        database=Path(os.environ["SD_DATA_DIR"]) / db_name,
        read_only=True,
    )

    records = db.sql(db_query)

    return StreamlitRenderer(records.to_df())


streamlit.set_page_config(
    page_title="PyGWalker Sample",
    layout="wide",
)

streamlit.title("PyGWalker Sample")

streamlit.markdown("""
    This is an sample Streamlit application that visualizes data using PyGWalker.
""")

with streamlit.form("Select data"):
    db_name = streamlit.text_input("Database", "sample.db")
    db_query = streamlit.text_area("Query", "SELECT * FROM source__mysql.users;")

    if streamlit.form_submit_button("Visualize"):
        pygwalker_renderer = get_pygwalker_renderer(
            db_name=db_name,
            db_query=db_query,
        )

        pygwalker_renderer.explorer()
