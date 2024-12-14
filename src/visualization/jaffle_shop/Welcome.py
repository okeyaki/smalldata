import streamlit


def main():
    streamlit.set_page_config(
        page_title="Jaffle Shop",
    )

    streamlit.title("Jaffle Shop")

    streamlit.header("Welcome!")

    streamlit.markdown("""
        This is a sample Streamlit application.
    """)


main()
