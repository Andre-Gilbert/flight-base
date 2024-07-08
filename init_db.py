"""Fill DB on start."""

import os

import psycopg2


def run_sql_file(filename, db_params):
    # Read SQL file
    with open(filename, "r", encoding="utf-8") as file:
        sql_script = file.read()

    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            dbname=db_params["dbname"],
            user=db_params["user"],
            password=db_params["password"],
            host=db_params["host"],
            port=db_params["port"],
        )
        cursor = connection.cursor()

        # Execute SQL script
        cursor.execute(sql_script)

        # Commit changes
        connection.commit()

        print("SQL script executed successfully")

    except Exception as error:
        print(f"Error executing SQL script: {error}")

    finally:
        # Close the database connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    sql_file = "database_init.sql"

    # Run the SQL file
    run_sql_file(
        sql_file,
        {
            "dbname": os.environ.get("POSTGRES_NAME"),
            "user": os.environ.get("POSTGRES_USER"),
            "password": os.environ.get("POSTGRES_PASSWORD"),
            "host": os.environ.get("POSTGRES_HOST"),
            "port": os.environ.get("POSTGRES_PORT"),
        },
    )
