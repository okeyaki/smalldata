# Smalldata

Smalldata is a boilerplate of a small data platform that can also run on your local machine.


## Quickstart


### Prerequisites

- [DuckDB](https://duckdb.org/)
- [Docker](https://www.docker.com/)
- [direnv](https://direnv.net/)
- [uv](https://docs.astral.sh/uv/)


### Installation

```bash
cp .env.dist .env

direnv allow

mkdir -p ${DUCKDB_DIR}

uv sync

source .venv/bin/activate

lefthook install

docker compose up -d
```


### [Ingestion](/src/smalldata/ingestion)

```bash
uv run src/smalldata/ingestion/examples/local_file.py run

uv run src/smalldata/ingestion/examples/mysql.py run

uv run src/smalldata/ingestion/examples/kaggle.py run \
    --dataset-handle koki25ando/japanese-whisky-review
```


### [Transformation](/src/smalldata/transformation)

```bash
export DBT_PROJECT_DIR=src/smalldata/transformation/example

dbt deps

dbt run
```


### [Experimentation](/src/smalldata/experimentation)

- [DuckDB UDF Example](/src/smalldata/experimentation/examples/duckdb_udf.ipynb)
- [DuckDB with AWS S3 Example](/src/smalldata/experimentation/examples/duckdb_with_aws_s3.ipynb)


### [Visualization](/src/smalldata/visualization)

```bash
streamlit run src/smalldata/visualization/examples/pygwalker/main.py
```
