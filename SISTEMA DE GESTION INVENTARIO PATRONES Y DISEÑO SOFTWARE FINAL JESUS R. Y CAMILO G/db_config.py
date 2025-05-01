import mysql.connector
from mysql.connector import Error
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Jesu1701',
                database='inventario_ropa'
            )
            return self.connection
        except Error as e:
            print(f"Error conectando a MySQL: {e}")
            return None

    def get_connection(self):
        if not self.connection or not self.connection.is_connected():
            self.connect()
        return self.connection