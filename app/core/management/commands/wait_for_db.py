"""
simple Django command to handle wait for DB 
to be available in the cluster.
"""
import time

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

from psycopg2 import OperationalError as Psycopg2Error


class Command(BaseCommand):
    """command to wait for DB"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for DB...')
        db_up = False
        # wait max 20 seconds for a connection
        for _ in range(20):
            if db_up is True:
                break
            try:
                self.check(databases=['default'])
                db_up = True
                self.stdout.write(self.style.SUCCESS('DB is ready!'))

            except (Psycopg2Error, OperationalError):
                self.stdout.write('DB not ready yet, waiting 1 second.')
                time.sleep(1)
