import invoke
from dbt.cli.main import dbtRunner
from dbt.cli.main import dbtRunnerResult
from invoke import Collection

import ingestion.jaffle_shop

DBT_PROJECT_DIR = "src/transformation/jaffle_shop"


@invoke.task()
def ingest(c):
    ingestion.jaffle_shop.run()


@invoke.task(
    default=True,
    pre=[ingest],
)
def transform(c):
    dbt_runner = dbtRunner()

    _: dbtRunnerResult = dbt_runner.invoke([
        "run",
        "--project-dir",
        DBT_PROJECT_DIR,
        "--profiles-dir",
        DBT_PROJECT_DIR,
    ])


ns = Collection(__name__)
ns.add_task(ingest)
ns.add_task(transform)
