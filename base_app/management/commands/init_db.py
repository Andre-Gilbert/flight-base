from django.core.management.base import BaseCommand
from django.db import connection, transaction


class Command(BaseCommand):
    help = "Fills the database with initial data"

    def handle(self, *args, **kwargs):
        try:
            with connection.cursor() as cursor:
                with open("init_db.sql", "r") as file:
                    sql_script = file.read()
                    cursor.execute(sql_script)
                    transaction.commit()

                self.stdout.write(self.style.SUCCESS("Database filled successfully"))

        except Exception as error:
            self.stdout.write(self.style.ERROR(f"Error filling database: {error}"))

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
