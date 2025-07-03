from dagster import asset, AssetIn
import pandas as pd
from ..constants import POSTGRES_CONN_STRING
import psycopg2
@asset(
    group_name="custom",
    key_prefix=["custom"]
)
def rental_analytics():
    """Analyse avancée des locations (exemple custom)"""
    conn = psycopg2.connect(POSTGRES_CONN_STRING)
    query = """
        SELECT r.customer_id, 
               COUNT(*) as rental_count,
               SUM(p.amount) as total_spent
        FROM rental r
        JOIN payment p ON r.rental_id = p.rental_id
        GROUP BY 1
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df