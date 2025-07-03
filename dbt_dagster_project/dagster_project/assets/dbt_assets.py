import dagster as dg
from dagster_dbt import DbtCliResource, dbt_assets
from ..constants import DBT_PROJECT_DIR, DBT_PROFILES_DIR
from pathlib import Path

manifest_path = Path(DBT_PROJECT_DIR) / "target" / "manifest.json"

@dbt_assets(manifest=manifest_path)
def dbt_assets_fn(context: dg.AssetExecutionContext, dbt: DbtCliResource):
    # You can change 'run' to 'build' or other dbt commands you prefer
    yield from dbt.cli(["build"], context=context).stream()
