import mysql.connector


class DataBase:
    dbconfig1 = {'host': '',
            'user': '',
            'password': '',#пароль передан в открытом виде. это опасно. лучше все, что в фигурых скобках считывать с файла. файл скрыть
            'database': ''}
    dbconfig2 = {'host': '',
                'user': '',
                'password': '',#пароль передан в открытом виде. это опасно. лучше все, что в фигурых скобках считывать с файла. файл скрыть
                'database': ''}
    def __init__(self):
        try:
            self.connect()
        except mysql.connector.Error as error:
            print( f"Error", error )
            
    def connect(self):
        self.connection = mysql.connector.connect(**self.dbconfig1)
        self.cursor = self.connection.cursor()

        self.my_connection = mysql.connector.connect(**self.dbconfig2)
        self.cursor_right = self.my_connection.cursor()
    def disconnect(self):
        self.cursor.close()
        self.cursor_right.close()
        self.connection.close()
        self.my_connection.close()