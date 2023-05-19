from src.app.bulk.mysql.bulk_insert_mysql import bulk_insert_mysql


class BulkInsert:

    def __init__(self, table, row, is_random):
        self.table = table
        self.row = row
        self.is_random = is_random

    def mysql(self):
        bulk_insert_mysql(self.table, self.row, self.is_random)
