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

- Storage
- Ingestion
- Transformation
- Visualization
- Experimentation
- Orchestration


### 📌 Storage

- Persistes data
- Consists of multiple [DuckDB](https://duckdb.org/) databases.


#### Samples

```bash
duckdb ${SD_DATA_DIR}/jaffle_shop.db
```


### 📌 Ingestion

- Collects data from various sources and stores them into the storages
- Consists of simple Python scripts


#### Samples

```bash
uv run src/ingestion/jaffle_shop.py
```


### 📌 Transformation

- Transforms data in storages
- Consists of multiple [dbt](https://www.getdbt.com/) projects


#### Samples

```bash
cd src/transformation/jaffle_shop

dbt deps

dbt run
```


### 📌 Visualization

- Visualizes data in the storages
- Consists of [Streamlit](https://streamlit.io/) applications


#### Samples

```bash
streamlit run src/visualization/jaffle_shop/Welcome.py
```


### 📌 Experimentation

- Experiments with data in the storages
- Consists of [Jupyter Notebook](https://jupyter.org/) notebooks


#### Notes

```bash
jupyter notebook src/experimentation
```


### 📌 Orchestration

- Orchestrates the processes
- Consists of [Invoke](http://www.pyinvoke.org/) tasks


#### Samples

```bash
invoke jaffle-shop
```
