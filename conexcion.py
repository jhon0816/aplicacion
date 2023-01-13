import mysql.connector


def conectar():
     db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1111659493',
        database = 'proyecto'
 )

     cursor = db.cursor(buffered=True)

     return [db, cursor]

