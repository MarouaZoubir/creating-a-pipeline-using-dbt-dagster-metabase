from dagster import job
from dagster_dbt import DbtCliResource, dbt_cli_command_op

# Define your dbt resource
dbt_resource = DbtCliResource(
    project_dir="C:/Users/HA/Desktop/dbt-trial1/dbt_dagster_project/pagila_dbt",
    profiles_dir="C:/Users/HA/.dbt"
)

# Create the dbt run and test operations
dbt_run_op = dbt_cli_command_op.configured({"command": "run"})
dbt_test_op = dbt_cli_command_op.configured({"command": "test"})

# Define Dagster jobs
@job(resource_defs={"dbt": dbt_resource})
def dbt_run_job():
    dbt_run_op()

@job(resource_defs={"dbt": dbt_resource})
def dbt_test_job():
    dbt_test_op()
