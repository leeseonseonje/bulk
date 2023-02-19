from src.main.app.db.bulk_insert_mysql import bulk_insert_mysql


class BulkInsert:

    def __init__(self, table, row):
        self.table = table
        self.row = row

    def mysql(self):
        bulk_insert_mysql(self.table, self.row)
