from dagster import Definitions
from dagster_dbt import load_assets_from_dbt_project, DbtCliResource

# Define the paths
DBT_PROJECT_DIR = "C:/Users/HA/Desktop/dbt-trial1/dbt_dagster_project/pagila_dbt"
DBT_PROFILES_DIR = "C:/Users/HA/.dbt"

# Define the dbt resource
dbt_resource = DbtCliResource(
    project_dir=DBT_PROJECT_DIR,
    profiles_dir=DBT_PROFILES_DIR
)

# Load dbt models as Dagster assets
dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_DIR,
    profiles_dir=DBT_PROFILES_DIR
)

# Define everything Dagster needs
defs = Definitions(
    assets=[dbt_assets],
    resources={"dbt": dbt_resource},
)
