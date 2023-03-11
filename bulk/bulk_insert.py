from src.main.app.bulk.bulk_insert_mysql import bulk_insert_mysql


class BulkInsert:

    def __init__(self, table, row, is_unique):
        self.table = table
        self.row = row
        self.is_unique = is_unique

    def mysql(self):
        bulk_insert_mysql(self.table, self.row, self.is_unique)
