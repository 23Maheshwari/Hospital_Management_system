import pymysql

class DBConnUtil:
    @staticmethod
    def get_connection():
        return pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='hospital_db',
            port=3306
        )
