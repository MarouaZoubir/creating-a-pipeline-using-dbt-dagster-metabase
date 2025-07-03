from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets.dbt_assets import dbt_assets_fn
from .assets.pagila_assets import rental_analytics

from .resources import postgres_resource
from .constants import DBT_PROJECT_DIR, DBT_PROFILES_DIR, POSTGRES_CONN_STRING

defs = Definitions(
    assets=[dbt_assets_fn, rental_analytics],
    resources={
        "dbt": DbtCliResource(
            project_dir=DBT_PROJECT_DIR,
            profiles_dir=DBT_PROFILES_DIR,
        ),
        "postgres": postgres_resource.configured(
            {"conn_string": POSTGRES_CONN_STRING}
        ),
    },
)
