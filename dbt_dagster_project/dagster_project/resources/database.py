from dagster import resource
import psycopg2
from contextlib import contextmanager

class PostgresResource:
    def __init__(self, conn_string):
        self.conn_string = conn_string

    @contextmanager
    def get_connection(self):
        conn = psycopg2.connect(self.conn_string)
        try:
            yield conn
        finally:
            conn.close()

@resource
def postgres_resource(init_context):
    return PostgresResource(init_context.resource_config["conn_string"])