# Smalldata

This project is a boilerplate of a small data platform that can also run on your local machine.


## 🚀 Quickstart


### Prerequisites

Ensure you have the following tools installed:

- [DuckDB](https://duckdb.org/)
- [Docker](https://www.docker.com/)
- [direnv](https://direnv.net/)
- [uv](https://docs.astral.sh/uv/)


### Installation

Run the following commands to set up the platform.

```bash
cp .env.dist .env

direnv allow

mkdir -p ${SD_DATA_DIR}

uv sync

source .venv/bin/activate

lefthook install

docker compose up -d
```


## 🏗️ Architecture

The platform consists of the following layers.

- Ingestion
- Transformation
- Visualization
- Experimentation


### Ingestion

The ingestion layer consists of components that collect data from various sources and store them into databases.

You can run the sample components as follows.

```bash
uv run src/ingestion/jaffle_shop.py
```

The sample components are implemented as simple Python scripts.


### Transformation

The transformation layer consists of components that transform data in databases.

You can run the sample components as follows.

```bash
cd src/transformation/jaffle_shop

dbt deps

dbt run
```

The sample components are implemented as dbt projects.

[dbt](https://www.getdbt.com/) is a tool that makes it effective to transform data. For more information, see the [documentation](https://docs.getdbt.com/).


### Visualization

The visualization layer consists of components that visualize data in databases.

You can run the sample components as follows.

```bash
streamlit run src/visualization/jaffle_shop/main.py
```

The sample components are implemented as Streamlit applications.

[Streamlit](https://streamlit.io/) is a framework that makes it quick to create data applications. For more information, see the [documentation](https://docs.streamlit.io/).


### Experimentation

The experimentation layer consists of components that experiment with data in databases.

You can run the sample components as follows.

```bash
jupyter notebook src/experimentation
```

The sample components are implemented as Jupyter Notebook notebooks.

[Jupyter Notebook](https://jupyter.org/) is a tool that makes it easy to run scripts interactively. For more information, see the [documentation](https://jupyter-notebook.readthedocs.io/).
