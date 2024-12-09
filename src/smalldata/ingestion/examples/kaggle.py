import os
from pathlib import Path

import duckdb
import kagglehub
import metaflow
from metaflow import FlowSpec
from metaflow.parameters import Parameter


class KaggleFlow(FlowSpec):
    DUCKDB_FILE_IMPORT_FUNCTIONS = {
        "csv": "READ_CSV",
        "json": "READ_JSON_AUTO",
    }

    dataset_handle = Parameter(
        "dataset-handle",
        help="Dataset handle",
        required=True,
        type=str,
    )

    db_name = Parameter(
        "db-name",
        help="Database name",
        default="example",
        type=str,
    )

    db_schema_name = Parameter(
        "db-schema-name",
        help="Database schema name",
        default="kaggle",
        type=str,
    )

    @metaflow.step
    def start(self):
        self.next(self.download_dataset)

    @metaflow.step
    def download_dataset(self):
        dataset_dir_path = kagglehub.dataset_download(self.dataset_handle)

        print(f"Finished downloading dataset: {dataset_dir_path}")

        self.dataset_dir_path = dataset_dir_path
        self.dataset_entries = os.listdir(dataset_dir_path)

        self.next(self.import_dataset)

    @metaflow.step
    def import_dataset(self):
        db = duckdb.connect(Path(os.environ["DUCKDB_DIR"]) / f"{self.db_name}.db")

        db.execute(f"CREATE SCHEMA IF NOT EXISTS {self.db_schema_name};")

        for e in self.dataset_entries:
            print(f"Started to import dataset entry: {e}")

            duckdb_file_import_function_name = self._get_duckdb_file_import_function_name(e)
            if duckdb_file_import_function_name is None:
                print(f"Skpped importing dataset entry that has unsupported data format: {e}")

                continue

            db_table_name = self._get_db_table_name(e)

            dataset_entry_file_path = str(Path(self.dataset_dir_path) / e)

            db.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.db_name}.{self.db_schema_name}.{db_table_name} AS
                    SELECT *
                    FROM {duckdb_file_import_function_name}('{dataset_entry_file_path}')
                ;
            """)

            print(f"Finished importing dataset entry: {e}")

        print("Finished importing dataset")

        self.next(self.end)

    @metaflow.step
    def end(self):
        pass

    def _get_db_table_name(self, dataset_entry):
        segments = [
            self.dataset_handle.lower().replace("/", "__").replace("-", "_"),
            dataset_entry.lower().replace("-", "_").replace(".", "_"),
        ]

        return "__".join(segments)

    def _get_duckdb_file_import_function_name(self, dataset_entry):
        dataset_entry_extension = Path(dataset_entry).suffix[1:]
        if dataset_entry_extension not in self.DUCKDB_FILE_IMPORT_FUNCTIONS:
            return None

        return self.DUCKDB_FILE_IMPORT_FUNCTIONS[dataset_entry_extension]


if __name__ == "__main__":
    KaggleFlow()
