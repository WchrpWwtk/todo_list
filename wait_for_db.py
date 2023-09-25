import psycopg2
import time
import os


def wait_for_db():
    max_retries = 30
    retry_interval = 2

    for _ in range(max_retries):
        try:
            conn = psycopg2.connect(
                dbname=os.environ.get("POSTGRES_NAME"),
                user=os.environ.get("POSTGRES_USER"),
                password=os.environ.get("POSTGRES_PASSWORD"),
                host="db",
                port="5432",
            )
            conn.close()
            print("Database is available.")
            return
        except psycopg2.OperationalError:
            print("Database is not yet available. Retrying...")
            time.sleep(retry_interval)

    print("Database is not available after waiting.")
    exit(1)


if __name__ == "__main__":
    wait_for_db()
