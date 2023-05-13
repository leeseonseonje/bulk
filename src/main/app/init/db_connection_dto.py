class DBConnectionDto:

    def __init__(self, dbms, host, port, user, password, db):
        self.dbms = dbms
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db

