import pickle
import unittest

from src.main.app.init.db_connection import ConnectDB, get_connection


class DBConnectTest(unittest.TestCase):
    def get_connection_for_db_name(self):
        with open('../../resource/db.pickle', 'wb') as save:
            pickle.dump(['localhost', 3306, 'root', 'root', 'cli_test'], save)
        
        get_connection()
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
