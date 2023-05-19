import psycopg2

class Connection1:
    def __init__(self):
        self.connection = None
    def openConnection1(self):
        try:
            self.connection = psycopg2.connect(user = "postgres",
                                               password = "Isabela147",
                                               database = "postgres",
                                               host = "localhost",
                                               port = "5431")
        except Exception as e:
            print(e)
    def closeConnection1(self):
        self.connection.close()
