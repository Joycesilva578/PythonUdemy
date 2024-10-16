import mysql.connector
from mysql.connector import errorcode

def conexao_mysql ():
    try:
        conexao = mysql.connector.connect(
            host= 'av31dbp.mysql.database.azure.com',
            user = 'joyce.hora@av31dbp',
            password = 'b3i$B@U8d14K-:*!',
            database = 'governanca'
    )
        return conexao

    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("User name or password is wrong")
        else:
            print(error)




