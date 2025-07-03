from pathlib import Path

# Chemins dbt
DBT_PROJECT_DIR = Path(__file__).parent.parent / "pagila_dbt"
DBT_PROFILES_DIR = Path(r"C:/Users/HA/.dbt")


# Configuration PostgreSQL
POSTGRES_CONN_STRING = "postgresql://hruser:hrpass@localhost:5432/pagila"
