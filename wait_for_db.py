import psycopg2
import time
import os


def wait_for_db():
    max_retries = 30
    retry_interval = 2

    db_host = os.environ.get("DB_HOST")
    db_port = os.environ.get("DB_PORT", "5432")

    for i in range(max_retries):
        try:
            conn = psycopg2.connect(
                dbname="mydb",
                user="myuser",
                password="mypassword",
                host=db_host,
                port=db_port,
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
